import asyncio
import json
import os
import tempfile
import uuid
from urllib.parse import urljoin

class Response:
    def __init__(self, status, headers, body, url, history, content):
        self.status = status
        self.headers = headers
        self.body = body
        self.url = url
        self.history = history
        self.content = content

    def __repr__(self):
        return f"<Response [status={self.status}, url={self.url}]>"


class Session:
    def __init__(self, proxy=None, notrust=None,path=None, max_data_size=4000):  
        self.cookies = {}
        self.proxy = proxy
        self.max_data_size = max_data_size 
        self.notrust = notrust
        self.path = path

    async def request(self, method, url, headers=None, data=None, follow_redirects=True, history=None, proxy=None,notrust=None, timeout=None):
        if history is None:
            history = []

        if method.upper() not in ["GET", "POST", "PUT", "DELETE"]:
            raise ValueError("Invalid HTTP method.")
            
        exex = self.path if self.path else "curl-8.9.1_1-win64-mingw/bin/curl.exe"
        

        commands = [exex, "--compressed", "-s", "-i", "-X", method.upper()]

        
        if proxy:
            commands.append("-x")
            commands.append(proxy)
        elif self.proxy:
            commands.append("-x")
            commands.append(self.proxy)

        
        if notrust:
            commands.append("-k")
        elif self.notrust:
            commands.append("-k")
        



        commands.append(url)

        
        if headers:
            for key, value in headers.items():
                if key.lower() == "cookie":
                    for cookie in value.split("; "):
                        k, v = cookie.split("=", 1)
                        self.cookies[k] = v
                else:
                    commands.append("-H")
                    commands.append(f"{key}: {value}")

        
        if self.cookies:
            cookie_string = "; ".join(f"{k}={v}" for k, v in self.cookies.items())
            commands.append("-H")
            commands.append(f"Cookie: {cookie_string}")

        
        tmpfile_path = None  
        if data is not None:
            
            if isinstance(data, (dict, list)):
                data_str = json.dumps(data)
            else:
                data_str = str(data)

            if len(data_str) > self.max_data_size:
                
                tmpfile_path = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4().hex}.txt")

                
                with open(tmpfile_path, 'w', encoding='utf-8') as tmpfile:
                    tmpfile.write(data_str)
                commands.append("-d")
                commands.append(f"@{tmpfile_path}")  
            else:
                
                commands.append("-d")
                commands.append(data_str)

        process = await asyncio.create_subprocess_exec(
            *commands,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            if timeout is not None:
                stdout, stderr = await asyncio.wait_for(process.communicate(), timeout)
            else:
                stdout, stderr = await process.communicate()
        finally:
            if tmpfile_path:
                await self._cleanup_temp_file(tmpfile_path)  

        if process.returncode != 0:
            raise RuntimeError(f"Error: {stderr.decode().strip()}")
        lines = stdout.decode('utf-8', errors='ignore').strip().split('\n')

        if not lines:
            return Response(status=None, headers={}, body="", url=url, history=history, content=b"")
        
        status_line = lines[0] if lines[0].startswith('HTTP/') else None
        if not status_line:
             return Response(status=None, headers={}, body="", url=url, history=history, content=b"")
        if lines[2].startswith('HTTP/'):
            status_line = lines[2]
        else:
          status_line = lines[0]
        rheaders = {}
        body_started = False
        body = []
        rheaders["Set-cookie"] = {}
        location = None
 
        empty_line_indexes = [index for index, line in enumerate(lines[1:], start=1) if line.strip() == ""]
        for index, line in enumerate(lines[1:], start=1): 
            if line.strip() == "":
                empty_line_indexes.append(index)
       
        try:
            eind = empty_line_indexes[1]
        except:
            eind = empty_line_indexes[0] if empty_line_indexes else len(lines)


        for index, line in enumerate(lines[1:], start=1):
            line = line.replace('\r', '')

            if index > eind:  
                body.append(line)
            else:
                if ':' in line:  
                    try:
                        key, value = line.split(': ', 1)
                        if key.lower().startswith("set-cookie"):
                            parts = value.split("; ")
                            for part in parts:
                                key_value = part.split("=", 1)
                                if len(key_value) == 2:
                                    cookie_key = key_value[0].strip()
                                    cookie_value = key_value[1].strip()
                                    rheaders["Set-cookie"][cookie_key] = cookie_value
                                    self.cookies[cookie_key] = cookie_value
                        else:
                            if key.lower() == "location":
                                location = value

                            rheaders[key] = value
                    except ValueError:
                        print(f"Geçersiz başlık satırı: {line}")
                elif line.strip() == "":  
                    continue
                else:
                    
                    print(f"Geçersiz başlık satırı: {line}")

        
        body = '\n'.join(body)
        content = b"".join(bytes(x, encoding='utf-8') for x in body if isinstance(x, str))

        
        current_response = Response(
            status=status_line.split(" ")[1],
            headers=rheaders,
            body=body,
            url=url,
            history=history,
            content=content
        )

        
        if not location is None:
                history.append(current_response)
                location_url = urljoin(url, location)
                await asyncio.sleep(0.1)  
                return await self.request(method, location_url, headers, data, follow_redirects, history, proxy, timeout)

        
        history.append(current_response)
        return current_response

    async def _cleanup_temp_file(self, file_path):
        """Remove temporary file after request is done."""
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error cleaning up temporary file {file_path}: {e}")