

import threading
import time
import string
import random
import asyncio
import json
import aiohttp
from random import randint, choice, choices
import aiocurl
async def kasadasolv():
    print("ok")
    headers={
	"x-rapidapi-key": "YOUR_API_KEY",
	"x-rapidapi-host": "kick-kasada-kpsdk-solver-api.p.rapidapi.com"
}
    async with aiohttp.ClientSession() as session:
        
        rep = await session.post("https://kick-kasada-kpsdk-solver-api.p.rapidapi.com/kasada",headers=headers,data=json.dumps({"method": "POST","fetch": "https://kick.com/api/v1/signup/send/email"}))
        js = await rep.json()
        print(js)
        task_id = js["task_id"]
        for _ in range(3):  
            await asyncio.sleep(1)
            res = await session.get(f"https://kick-kasada-kpsdk-solver-api.p.rapidapi.com/kasada-headers?task_id={task_id}",headers=headers)
            res_text = await res.text()
            print(res_text)
            result = json.loads(res_text)
            print(result)
            if result.get("pending"):
                await asyncio.sleep(0.5)
                continue
            elif result.get("error") == "not solution created":
                return result
            elif result.get("user-agent"):
                return result
            else:
                await asyncio.sleep(0.5)
        return {"error": "Timeout, header gelmedi", "task_id": task_id}
def generate_random_username():
    nick = list()
    prefix = str()
    under_score = str()
    under_score2 = str()
    rnd_number = str()
    rnd_vowels = choices(('a', 'e', 'i', 'o', 'u', 'y'), k=randint(3, 5))
    rnd_consonant = choices(('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'), k=randint(4, 6))

    nick = [f"{x}{y}" for x, y in zip(rnd_vowels, rnd_consonant)]
    if choice((True, False)):
        if choice((True, False)):
            under_score = "_"

        prefix = choice(('Shadow', 'Fireball', 'Storm', 'Dragon', 'Phoenix', 'Thunder', 'Wolf', 'Eagle', 'Tiger', 'Lion','Falcon', 'Blaze', 'Ghost', 'Raven', 'Cobra', 'Viper', 'Sphinx', 'Griffin', 'Knight', 'Samurai','Ninja', 'Pirate', 'Hunter', 'Rogue', 'Wizard', 'Mystic', 'Ace', 'Fox', 'Blade', 'Ranger','Zephyr', 'Titan', 'Maverick', 'Legend', 'Sniper', 'Panda', 'Brawler', 'Phantom', 'Jester', 'Frost','Sparrow', 'Hawk', 'Specter', 'Assassin', 'Drifter', 'Hurricane', 'Grizzly', 'Vortex', 'Crusher', 'Oracle','Savage', 'Viking', 'Crimson', 'Golem', 'Spartan', 'Elemental', 'Valkyrie', 'Nebula', 'Warrior', 'Banshee','Thunderbolt', 'Saber', 'Chaser', 'Wraith', 'Cyborg', 'Banshee', 'Fury', 'Hunter', 'Cheetah', 'Blizzard','Lynx', 'Chimera', 'Reaper', 'Tornado', 'Iceblade', 'Rift', 'Prowler', 'Sorcerer', 'Oblivion', 'Mystique','Steel', 'Icefire', 'Firefly', 'Blitz', 'Inferno', 'Shifter', 'Nomad', 'Fallen', 'Dusk', 'Demon','Gladiator', 'Wanderer', 'Stalker', 'Sphinx', 'Ranger', 'Crimson', 'Talon', 'Shockwave', 'Shadowfax', 'Tempest','Nighthawk', 'Wildfire', 'Thorn', 'Jaguar', 'Falconer', 'Berserker', 'Rogue', 'Grim', 'Drake', 'Void','Abyss', 'Seeker', 'Firestorm', 'Ravager', 'Shade', 'Challenger', 'Windrider', 'Soulreaver', 'Whisper', 'Brawler','Dread', 'Phantom', 'Infernal', 'Frostbite', 'Fable', 'Nimbus', 'Astral', 'Vengeance', 'Wraith', 'Havoc','Riftwalker', 'Fury', 'Hollow', 'Mythic', 'Eclipse', 'Volt', 'Shade', 'Echo', 'Frostfire', 'Thunderstorm','Ragnarok', 'Ironclad', 'Doombringer', 'Bloodhound', 'Harbinger', 'Nightmare', 'Cinder', 'Titanfall', 'Magnetar','Astral', 'Galactic', 'Meteor', 'Elysium', 'Spectral', 'Aether', 'Radiance', 'Vortex', 'Celestial', 'Karma','Chronos', 'Reverie', 'Sunder', 'Tempest', 'Omen', 'Shroud', 'Abysswalker', 'Lightbringer', 'Voidwalker', 'Shadowblade','Sunfire', 'Nightstalker', 'Scorpion', 'Dreadnought', 'Armageddon', 'Duskbringer', 'Soulbinder', 'Mist', 'Ember', 'Harbinger', 'Raider', 'Zealot', 'Stormbringer', 'Fate', 'Shatter', 'Aegis', 'Bolt', 'Whirlwind', 'Spectre','Thunderstrike', 'Demonhunter', 'Wrath', 'Chaos', 'Gale', 'Shade', 'Phantom', 'Trickster', 'Oracle', 'Frostfire','Valiant', 'Scourge', 'Glint', 'Glacier', 'Frostbite', 'Thalor', 'Nether', 'Icarus', 'Dusk', 'Fable', 'Horizon', 'Valiant', 'Wanderlust', 'Fallen', 'Ebon', 'Sable', 'Warden', 'Skywalker', 'Illusion', 'Harrier','Frost', 'Flare', 'Lancer', 'Vanguard', 'Duskweaver', 'Frostfire', 'Aetherblade', 'Serpent', 'Coral', 'Cinder','Stormrider', 'Twilight', 'Phantomblade', 'Windwalker', 'Cinderstorm', 'Phoenixfire', 'Nebulon', 'Elysium', 'Spectral','Obsidian', 'Flamekeeper', 'Emberstorm', 'Starfire', 'Nightrider', 'Flameborn', 'Cosmic', 'Thunderfury', 'Starlight','Windrider', 'Galewind', 'Ironheart', 'Celestial', 'Glimmer', 'Brimstone', 'Wisp', 'Nightwing', 'Emberheart', 'Frostwind', 'Blight', 'Phantomfire', 'Glint', 'Hellscream', 'Solaris', 'Shadowdancer', 'Radiant', 'Havoc', 'Wraithlord', 'Windshear', 'Specterblade', 'Ruin', 'Flamewaker', 'Emberblade', 'Celestial', 'Nightshade', 'Echo','Eclipse', 'Frostmoon', 'Tempest', 'Galeforce', 'Duskfall', 'Chaosbringer', 'Nightstalker', 'Nightfall', 'Voidblade','Shade', 'Bane', 'Mystic', 'Oathkeeper', 'Shadeweaver', 'Frostfire', 'Emberstorm', 'Shadowhunter', 'Windswept', 'Stormcaller', 'Flameheart', 'Darkflame', 'Ember', 'Valiant', 'Riptide', 'Steelwind', 'Ebonheart', 'Emberstorm', 'Stormrider', 'Emberblade', 'Mistwalker', 'Duskblade', 'Galewind', 'Netherblade', 'Stargazer', 'Gloom', 'Shard','Illusionist', 'Firewhisper', 'Frostwhisper', 'Dreamweaver', 'Aetherstorm', 'Nightwhisper', 'Blizzard', 'Shadowsong', 'Gale', 'Nightshade', 'Tempest', 'Emberglow', 'Dawnbringer', 'Twilight', 'Frostsoul', 'Emberveil', 'Dread', 'Dusk','Mysticwind', 'Windwhisper', 'Starfire', 'Void', 'Frostflame', 'Phoenixfeather', 'Spiritwalker', 'Skyfire', 'Emberdancer','Glacier', 'Duskreaver', 'Dawnstalker', 'Shadowfeather', 'Nightflare', 'Embermist', 'Voidveil', 'Flamewisp', 'Galeflare','Horizon', 'Frostlance', 'Emberstrike', 'Firethorn', 'Flameweaver', 'Netherwing', 'Ebonflame', 'Starshard', 'Glint','Shadeweaver', 'Nebulon', 'Aetherflare', 'Starfall', 'Hollowsong', 'Embershadow', 'Frostshard', 'Chaoswalker', 'Windhowl','Windshear', 'Emberclaw', 'Flameveil', 'Ironthorn', 'Riftwalker', 'Galewind', 'Shadowveil', 'Hurricane', 'Ebonthorn', 'Stormwatcher', 'Nightgale', 'Radiant', 'Soulflame', 'Duskfire', 'Firestorm', 'Havoc', 'Gale', 'Phantomveil', 'Twilight','Frostfire', 'Nightshade', 'Demonhunter', 'Flamebringer', 'Shadowstrike', 'Spectral', 'Starbloom', 'Vortex', 'Windwhisper','Celestial', 'Darkstar', 'Stormrage', 'Embermist', 'Horizon', 'Emberstorm', 'Hollowsong', 'Starlight', 'Voidcaller','Horizon', 'Skyblade', 'Ethereal', 'Frostwhisper', 'Emberflame', 'Hallowed', 'Phoenixborn', 'Frostshroud', 'Twilightfall','Stardust', 'Galewind', 'Duskweaver', 'Mistweaver', 'Shadowreaver', 'Chaoswind', 'Flamebreaker', 'Nightsong', 'Radiance','Embershadow', 'Fireweaver', 'Nightbringer', 'Voidwalker', 'Frostclaw', 'Emberflame', 'Abysswalker', 'Thundercall', 'Galesinger', 'Ebonclaw', 'Sunstalker', 'Hallowed', 'Nebulaflame', 'Phantomwing', 'Frostcall', 'Shadowmancer', 'Twilightwisp', 'Mistwalker', 'Nightstalker', 'Emberguard', 'Thunderstrike', 'Gloom', 'Starblade', 'Frostveil', 'Frostflare', 'Hurricane', 'Galewind', 'Ebonveil', 'Stormsong', 'Windfire', 'Mysticspark', 'Duskflame', 'Chaosstorm', 'Nightflame', 'Twilightblade', 'Embersong', 'Radiant', 'Frostflare', 'Phantom', 'Ebon', 'Windscream', 'Shadowspark', 'Emberwhisper', 'Froststorm', 'Duskweaver', 'Nebulon', 'Sundancer', 'Voidgale', 'Mysticflare', 'Frostlight', 'Gale', 'Stormblade', 'Thorn', 'Skyfire', 'Hurricane', 'Abyss', 'Blight', 'Hollow', 'Emberstrike', 'Cinder', 'Lunar', 'Voidreaver', 'Starshard', 'Frostmist', 'Dread', 'Emberwind','Wraith', 'Gale', 'Emberstorm', 'Frostfire', 'Celestial', 'Emberthorn', 'Frostflame', 'Hallowed', 'Shadowveil','Windshear', 'Mysticwind', 'Starflare', 'Dawn', 'Emberlance', 'Starlight', 'Frostmoon', 'Phantomfire', 'Gale', 'Shade', 'Firethorn', 'Twilight', 'Ebonheart', 'Shadowgale', 'Emberwhirl', 'Frostflame', 'Mistweaver','Embershadow', 'Phoenixfeather', 'Frostflare', 'Nightsong', 'Twilightfall', 'Voidfire', 'Celestial', 'Galewind', 'Duskblade', 'Windshear', 'Stormgale', 'Hurricane', 'Frostthorn', 'Starbloom', 'Emberveil', 'Shade', 'Emberflame', 'Duskweaver', 'Frostbite', 'Phoenixborn', 'Mistwalker', 'Shadowveil', 'Emberwind', 'Galesinger', 'Twilightflame', 'Firethorn', 'Nebulaflame', 'Frostshroud', 'Shade', 'Starlight', 'Galewind','Twilight', 'Gloom', 'Nightstalker', 'Frostflare', 'Shadowreaver', 'Embershadow', 'Celestial', 'Duskfire','Embersong', 'Phantom', 'Chaos', 'Emberguard', 'Frostlance', 'Shadeweaver', 'Hallowed', 'Cinder', 'Gloom', 'Flame', 'Spiritwalker', 'Hollow', 'Gale', 'Frostfire', 'Twilight', 'Starfire', 'Emberglow','Dawn', 'Ebonthorn', 'Frostfire', 'Mistwalker', 'Shadowveil', 'Galewind', 'Frostshard', 'Phantom', 'Emberdancer', 'Wraith', 'Frostfire', 'Cinder', 'Windshear', 'Nebula', 'Duskweaver', 'Embershadow','Nightstalker', 'Galewind', 'Firestorm', 'Embershadow', 'Frostflare', 'Dawnbringer', 'Radiant', 'Emberstrike', 'Shade', 'Emberclaw', 'Galewind', 'Nightsong', 'Windrider', 'Twilight', 'Voidfire', 'Firewhisper', 'Emberflare', 'Frostgale', 'Nightfall', 'Starbloom', 'Ebonfire', 'Hallowed', 'Shade', 'Phoenix', 'Frostfire', 'Shadeweaver', 'Nebulaflame', 'Chaos', 'Emberveil', 'Nightsong', 'Dawn', 'Emberstorm', 'Cinder', 'Frostwhisper', 'Spiritwalker', 'Windshear', 'Gale', 'Twilight', 'Nightshade','Froststorm', 'Firethorn', 'Ethereal', 'Duskfire', 'Nightwing', 'Ebon', 'Shade', 'Emberveil', 'Embershadow', 'Flame', 'Emberstrike', 'Voidwalker', 'Galewind', 'Froststorm', 'Wraith', 'Phantomfire', 'Windfire', 'Nebulon', 'Dawnblade', 'Firestorm', 'Mystic', 'Twilightflame', 'Hallowed', 'Wraithlord','Embershadow', 'Gale', 'Frostveil', 'Emberheart', 'Shade', 'Cinder', 'Hallowed', 'Twilightfall', 'Flamekeeper', 'Windrider', 'Dawnstalker', 'Galewind', 'Windshear', 'Emberguard', 'Duskblade', 'Wraith', 'Nightshade', 'Cinder', 'Emberstorm', 'Voidcaller', 'Frostbite', 'Galewind', 'Emberflame','Shade', 'Shadowblade', 'Frostwind', 'Embersong', 'Twilight', 'Nightfire', 'Duskfall', 'Cinder','Hallowed', 'Galewind', 'Frostfire', 'Emberveil', 'Embershadow', 'Void', 'Ebon', 'Emberclaw', 'Hallowed', 'Frostfire', 'Shade', 'Emberguard', 'Wraith', 'Firethorn', 'Shade', 'Hallowed', 'Twilight', 'Galewind', 'Frostflame', 'Dawn', 'Dusk', 'Frostfire', 'Void', 'Emberwind', 'Nightshade', 'Frostwhisper', 'Gale', 'Emberdancer', 'Embershadow', 'Voidcaller', 'Hallowed', 'Shade', 'Ethereal', 'Emberveil', 'Dusk', 'Nightsong', 'Froststorm', 'Gale', 'Dawnbringer', 'Cinder', 'Nebulaflame', 'Shadowveil', 'Wraith', 'Emberwind', 'Galewind', 'Twilight', 'Cinder', 'Ebon', 'Nightfall', 'Shade', 'Twilightfall', 'Hallowed', 'Nebulon', 'Cinder', 'Firewhisper', 'Galewind', 'Duskfall', 'Flame', 'Frostgale', 'Emberstorm', 'Voidwalker', 'Spiritwalker', 'Twilight'))

    if choice((True, False)):
        if choice((True, False)):
            under_score2 = "_"
        rnd_number = f'{under_score2}{randint(1, 99)}'

    nick = prefix + under_score + "".join(nick).capitalize() + rnd_number
    return nick
def generate_password():
    chars = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "dot": "."
    }

    password_length = random.randint(8, 15)
    
    
    password_chars = [random.choice(chars[key]) for key in chars]
    
    
    remaining_chars = random.choices("".join(chars.values()), k=password_length - len(password_chars))
    
    password_chars.extend(remaining_chars)
    random.shuffle(password_chars)  
    
    return ''.join(password_chars)

def generate_random_string(length):
    chars = string.ascii_letters + string.digits + "."
    return ''.join(random.choices(chars, k=length))






# removed unused urllib.parse
import traceback
import imaplib, email, re



def getcode(mail, password, server="imap.zmailservice.com", folder="INBOX", sender="noreply@email.kick.com", timeout=90, poll_interval=5):

    try:
        M = imaplib.IMAP4_SSL(server, 993)
        M.login(mail, password)
    except Exception as e:
        print(f"IMAP login hatası: {e}")
        return None

    end_at = time.time() + timeout
    code_found = None
    try:
        while time.time() < end_at and not code_found:
            try:
                M.select(folder)
                typ, data = M.search(None, 'FROM', f'"{sender}"')
                if typ == 'OK' and data and data[0]:
                    ids = data[0].split()
                    if ids:
                        latest_id = ids[-1]
                        typ2, msg_data = M.fetch(latest_id, '(RFC822)')
                        if typ2 == 'OK' and msg_data and msg_data[0]:
                            msg = email.message_from_bytes(msg_data[0][1])
                            
                            raw_subj = msg.get('Subject', '')
                            try:
                                from email.header import decode_header
                                parts = decode_header(raw_subj)
                                subject = ''.join(
                                    [(t.decode(c or 'utf-8', errors='ignore') if isinstance(t, bytes) else t) for t, c in parts]
                                )
                            except Exception:
                                subject = raw_subj or ''

                            
                            m = re.search(r"\b(\d{4,8})\b", subject)
                            if m:
                                code_found = m.group(1)
                                print(f"IMAP: Subject code: {code_found}")
                            else:
                                
                                body_text = ''
                                if msg.is_multipart():
                                    for part in msg.walk():
                                        if part.get_content_type() == 'text/plain':
                                            cs = part.get_content_charset() or 'utf-8'
                                            try:
                                                body_text += part.get_payload(decode=True).decode(cs, errors='ignore')
                                            except Exception:
                                                pass
                                            
                                            
                                else:
                                    cs = msg.get_content_charset() or 'utf-8'
                                    try:
                                        body_text = msg.get_payload(decode=True).decode(cs, errors='ignore')
                                    except Exception:
                                        body_text = ''
                                m2 = re.search(r"\b(\d{4,8})\b", body_text)
                                if m2:
                                    code_found = m2.group(1)

                if code_found:
                    try:
                        M.logout()
                    except Exception:
                        pass
                    try:
                        return int(code_found)
                    except Exception:
                        return code_found
            except Exception as ie:
                print(f"IMAP okuma hatası: {ie}")
            time.sleep(poll_interval)
    finally:
        try:
            M.logout()
        except Exception:
            pass
    return None

async def process_kpsdk_item():
    try:
        retry_count = 0
        while retry_count < 15:
            with open("livelive.txt", "r", encoding="utf-8") as f:
                raw_lines = [ln.strip() for ln in f.read().splitlines() if ln.strip()]
            lines = [ln for ln in raw_lines if ":" in ln]

            if not lines:
                print("Hata: livelive.txt boş veya 'email:password' formatında kayıt yok!")
                return

            selected_line = random.choice(lines)
            parts = selected_line.split(':', 1)
            if len(parts) < 2:
                print(f"Hatalı format (skip): {selected_line}")
                continue
            mail, pas = parts[0], parts[1]

            print(f"Seçilen mail: {mail}")
            print("[STAGE] Kasada solve başlıyor")
            kasada = await kasadasolv()
            print("[STAGE] Kasada solve bitti")

            headers = {
                "Host": "kick.com",
                "Accept": "application/json, text/plain, */*",
                "X-App-Version": "39.7.19",
                "Content-Type": "application/json",
                "X-Kpsdk-V": "j-0.0.0",
                "X-App-Platform": "Android",
                "Origin": "https://localhost",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://localhost/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                "User-Agent": kasada.get('user-agent'),
                "x-requested-with": "XMLHttpRequest",
                "x-kpsdk-ct": kasada.get('x-kpsdk-ct'),
                "x-kpsdk-cd": kasada.get('x-kpsdk-cd'),
            }

            with open('babaproxy.txt', 'r', encoding="utf-8") as f:
                proxies = f.read().splitlines()
            if not proxies:
                print("Hata: babaproxy.txt boş!")
                return

            session = aiocurl.Session()

            print("[STAGE] Doğrulama maili isteniyor")
            try:
                mailat = await session.request(method="POST", url='https://kick.com/api/v1/signup/send/email', headers=headers, data={"email": mail.strip()})
            except Exception as send_err:
                print("[ERROR] Mail gönderme isteğinde hata (session.request)")
                print(repr(send_err))
                traceback.print_exc()
                raise
            print(f"Mail gönderme durumu: {mailat.status}")

            status_val = str(mailat.status)
            if status_val in ("429", "403"):
                retry_count += 1
                print(mailat.body)
                print(f"Mail gönderme denemesi {retry_count}/15 başarısız, tekrar deniyorum...")
                continue
            break

        
        if str(mailat.status) == "429":
            print(f"Mail 3 deneme sonunda da 429 verdi, listeden siliyorum: {mail}")
            if selected_line in lines:
                lines.remove(selected_line)
                with open("livelive.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
            return

        username = generate_random_username()
        passw = generate_password()

        print("[STAGE] IMAP ile kod okunuyor")
        log = getcode(mail, pas)
        print(f"[STAGE] IMAP sonuç: {log}")

        if selected_line in lines:
            lines.remove(selected_line)
            with open("livelive.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(lines) + "\n")
        print("logalti")

        if log:
            code = log
            onaylaa = await session.request(method="POST", url='https://kick.com/api/v1/signup/verify/code', headers=headers, data={"email": mail.strip(), "code": str(code).strip()})
            print(onaylaa.body)
            print(onaylaa.status)

            if str(onaylaa.status) == "204":
                jsn = {
                    "agreed_to_terms": True,
                    "isMobileRequest": True,
                    "birthdate": "04/04/2005",
                    "email": mail.strip(),
                    "cf_captcha_token": "",
                    "password": passw,
                    "password_confirmation": passw,
                    "username": username
                }

                res = await session.request(method="POST", url='https://kick.com/register', headers=headers, data=jsn)
                print(res.body)

                if str(res.status) == "200":
                    try:
                        with open("kicks.json", "r") as fs:
                            data = json.load(fs)
                    except (FileNotFoundError, json.JSONDecodeError):
                        data = []

                    ress = json.loads(res.body)
                    data.append({"auth": ress.get("token"), "mail": mail.strip(), "password": passw})

                    with open("kicks.json", "w") as fs:
                        json.dump(data, fs, indent=4)
    except Exception as e:
        print("kicksinalti ")
        print(e)
        try:
            with open("livelive.txt", "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            if 'selected_line' in locals() and selected_line in lines:
                lines.remove(selected_line)
                with open("livelive.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
        except Exception:
            pass

def worker():
    asyncio.run(process_kpsdk_item())

async def ol():
    try:
        
        items = []
        
        
        threads = []
        for i in range(1):
            t = threading.Thread(target=worker, args=())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        



    except Exception as e:
        print("olun alti")
        print(f"Error occurred: {e}")

while True:
 asyncio.run(ol())
async def kasadasolv():
    print("ok")
    headers={
	"x-rapidapi-key": "YOUR_API_KEY",
	"x-rapidapi-host": "kick-kasada-kpsdk-solver-api.p.rapidapi.com"
}
    async with aiohttp.ClientSession() as session:
        
        rep = await session.post("https://kick-kasada-kpsdk-solver-api.p.rapidapi.com/kasada",headers=headers,data=json.dumps({"method": "POST","fetch": "https://kick.com/api/v1/signup/send/email"}))
        js = await rep.json()
        print(js)
        task_id = js["task_id"]
        for _ in range(3):  
            await asyncio.sleep(1)
            res = await session.get(f"https://kick-kasada-kpsdk-solver-api.p.rapidapi.com/kasada-headers?task_id={task_id}",headers=headers)
            res_text = await res.text()
            print(res_text)
            result = json.loads(res_text)
            print(result)
            if result.get("pending"):
                await asyncio.sleep(0.5)
                continue
            elif result.get("error") == "not solution created":
                return result
            elif result.get("user-agent"):
                return result
            else:
                await asyncio.sleep(0.5)
        return {"error": "Timeout, header gelmedi", "task_id": task_id}
def generate_random_username():
    nick = list()
    prefix = str()
    under_score = str()
    under_score2 = str()
    rnd_number = str()
    rnd_vowels = choices(('a', 'e', 'i', 'o', 'u', 'y'), k=randint(3, 5))
    rnd_consonant = choices(('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'), k=randint(4, 6))

    nick = [f"{x}{y}" for x, y in zip(rnd_vowels, rnd_consonant)]
    if choice((True, False)):
        if choice((True, False)):
            under_score = "_"

        prefix = choice(('Shadow', 'Fireball', 'Storm', 'Dragon', 'Phoenix', 'Thunder', 'Wolf', 'Eagle', 'Tiger', 'Lion','Falcon', 'Blaze', 'Ghost', 'Raven', 'Cobra', 'Viper', 'Sphinx', 'Griffin', 'Knight', 'Samurai','Ninja', 'Pirate', 'Hunter', 'Rogue', 'Wizard', 'Mystic', 'Ace', 'Fox', 'Blade', 'Ranger','Zephyr', 'Titan', 'Maverick', 'Legend', 'Sniper', 'Panda', 'Brawler', 'Phantom', 'Jester', 'Frost','Sparrow', 'Hawk', 'Specter', 'Assassin', 'Drifter', 'Hurricane', 'Grizzly', 'Vortex', 'Crusher', 'Oracle','Savage', 'Viking', 'Crimson', 'Golem', 'Spartan', 'Elemental', 'Valkyrie', 'Nebula', 'Warrior', 'Banshee','Thunderbolt', 'Saber', 'Chaser', 'Wraith', 'Cyborg', 'Banshee', 'Fury', 'Hunter', 'Cheetah', 'Blizzard','Lynx', 'Chimera', 'Reaper', 'Tornado', 'Iceblade', 'Rift', 'Prowler', 'Sorcerer', 'Oblivion', 'Mystique','Steel', 'Icefire', 'Firefly', 'Blitz', 'Inferno', 'Shifter', 'Nomad', 'Fallen', 'Dusk', 'Demon','Gladiator', 'Wanderer', 'Stalker', 'Sphinx', 'Ranger', 'Crimson', 'Talon', 'Shockwave', 'Shadowfax', 'Tempest','Nighthawk', 'Wildfire', 'Thorn', 'Jaguar', 'Falconer', 'Berserker', 'Rogue', 'Grim', 'Drake', 'Void','Abyss', 'Seeker', 'Firestorm', 'Ravager', 'Shade', 'Challenger', 'Windrider', 'Soulreaver', 'Whisper', 'Brawler','Dread', 'Phantom', 'Infernal', 'Frostbite', 'Fable', 'Nimbus', 'Astral', 'Vengeance', 'Wraith', 'Havoc','Riftwalker', 'Fury', 'Hollow', 'Mythic', 'Eclipse', 'Volt', 'Shade', 'Echo', 'Frostfire', 'Thunderstorm','Ragnarok', 'Ironclad', 'Doombringer', 'Bloodhound', 'Harbinger', 'Nightmare', 'Cinder', 'Titanfall', 'Magnetar','Astral', 'Galactic', 'Meteor', 'Elysium', 'Spectral', 'Aether', 'Radiance', 'Vortex', 'Celestial', 'Karma','Chronos', 'Reverie', 'Sunder', 'Tempest', 'Omen', 'Shroud', 'Abysswalker', 'Lightbringer', 'Voidwalker', 'Shadowblade','Sunfire', 'Nightstalker', 'Scorpion', 'Dreadnought', 'Armageddon', 'Duskbringer', 'Soulbinder', 'Mist', 'Ember', 'Harbinger', 'Raider', 'Zealot', 'Stormbringer', 'Fate', 'Shatter', 'Aegis', 'Bolt', 'Whirlwind', 'Spectre','Thunderstrike', 'Demonhunter', 'Wrath', 'Chaos', 'Gale', 'Shade', 'Phantom', 'Trickster', 'Oracle', 'Frostfire','Valiant', 'Scourge', 'Glint', 'Glacier', 'Frostbite', 'Thalor', 'Nether', 'Icarus', 'Dusk', 'Fable', 'Horizon', 'Valiant', 'Wanderlust', 'Fallen', 'Ebon', 'Sable', 'Warden', 'Skywalker', 'Illusion', 'Harrier','Frost', 'Flare', 'Lancer', 'Vanguard', 'Duskweaver', 'Frostfire', 'Aetherblade', 'Serpent', 'Coral', 'Cinder','Stormrider', 'Twilight', 'Phantomblade', 'Windwalker', 'Cinderstorm', 'Phoenixfire', 'Nebulon', 'Elysium', 'Spectral','Obsidian', 'Flamekeeper', 'Emberstorm', 'Starfire', 'Nightrider', 'Flameborn', 'Cosmic', 'Thunderfury', 'Starlight','Windrider', 'Galewind', 'Ironheart', 'Celestial', 'Glimmer', 'Brimstone', 'Wisp', 'Nightwing', 'Emberheart', 'Frostwind', 'Blight', 'Phantomfire', 'Glint', 'Hellscream', 'Solaris', 'Shadowdancer', 'Radiant', 'Havoc', 'Wraithlord', 'Windshear', 'Specterblade', 'Ruin', 'Flamewaker', 'Emberblade', 'Celestial', 'Nightshade', 'Echo','Eclipse', 'Frostmoon', 'Tempest', 'Galeforce', 'Duskfall', 'Chaosbringer', 'Nightstalker', 'Nightfall', 'Voidblade','Shade', 'Bane', 'Mystic', 'Oathkeeper', 'Shadeweaver', 'Frostfire', 'Emberstorm', 'Shadowhunter', 'Windswept', 'Stormcaller', 'Flameheart', 'Darkflame', 'Ember', 'Valiant', 'Riptide', 'Steelwind', 'Ebonheart', 'Emberstorm', 'Stormrider', 'Emberblade', 'Mistwalker', 'Duskblade', 'Galewind', 'Netherblade', 'Stargazer', 'Gloom', 'Shard','Illusionist', 'Firewhisper', 'Frostwhisper', 'Dreamweaver', 'Aetherstorm', 'Nightwhisper', 'Blizzard', 'Shadowsong', 'Gale', 'Nightshade', 'Tempest', 'Emberglow', 'Dawnbringer', 'Twilight', 'Frostsoul', 'Emberveil', 'Dread', 'Dusk','Mysticwind', 'Windwhisper', 'Starfire', 'Void', 'Frostflame', 'Phoenixfeather', 'Spiritwalker', 'Skyfire', 'Emberdancer','Glacier', 'Duskreaver', 'Dawnstalker', 'Shadowfeather', 'Nightflare', 'Embermist', 'Voidveil', 'Flamewisp', 'Galeflare','Horizon', 'Frostlance', 'Emberstrike', 'Firethorn', 'Flameweaver', 'Netherwing', 'Ebonflame', 'Starshard', 'Glint','Shadeweaver', 'Nebulon', 'Aetherflare', 'Starfall', 'Hollowsong', 'Embershadow', 'Frostshard', 'Chaoswalker', 'Windhowl','Windshear', 'Emberclaw', 'Flameveil', 'Ironthorn', 'Riftwalker', 'Galewind', 'Shadowveil', 'Hurricane', 'Ebonthorn', 'Stormwatcher', 'Nightgale', 'Radiant', 'Soulflame', 'Duskfire', 'Firestorm', 'Havoc', 'Gale', 'Phantomveil', 'Twilight','Frostfire', 'Nightshade', 'Demonhunter', 'Flamebringer', 'Shadowstrike', 'Spectral', 'Starbloom', 'Vortex', 'Windwhisper','Celestial', 'Darkstar', 'Stormrage', 'Embermist', 'Horizon', 'Emberstorm', 'Hollowsong', 'Starlight', 'Voidcaller','Horizon', 'Skyblade', 'Ethereal', 'Frostwhisper', 'Emberflame', 'Hallowed', 'Phoenixborn', 'Frostshroud', 'Twilightfall','Stardust', 'Galewind', 'Duskweaver', 'Mistweaver', 'Shadowreaver', 'Chaoswind', 'Flamebreaker', 'Nightsong', 'Radiance','Embershadow', 'Fireweaver', 'Nightbringer', 'Voidwalker', 'Frostclaw', 'Emberflame', 'Abysswalker', 'Thundercall', 'Galesinger', 'Ebonclaw', 'Sunstalker', 'Hallowed', 'Nebulaflame', 'Phantomwing', 'Frostcall', 'Shadowmancer', 'Twilightwisp', 'Mistwalker', 'Nightstalker', 'Emberguard', 'Thunderstrike', 'Gloom', 'Starblade', 'Frostveil', 'Frostflare', 'Hurricane', 'Galewind', 'Ebonveil', 'Stormsong', 'Windfire', 'Mysticspark', 'Duskflame', 'Chaosstorm', 'Nightflame', 'Twilightblade', 'Embersong', 'Radiant', 'Frostflare', 'Phantom', 'Ebon', 'Windscream', 'Shadowspark', 'Emberwhisper', 'Froststorm', 'Duskweaver', 'Nebulon', 'Sundancer', 'Voidgale', 'Mysticflare', 'Frostlight', 'Gale', 'Stormblade', 'Thorn', 'Skyfire', 'Hurricane', 'Abyss', 'Blight', 'Hollow', 'Emberstrike', 'Cinder', 'Lunar', 'Voidreaver', 'Starshard', 'Frostmist', 'Dread', 'Emberwind','Wraith', 'Gale', 'Emberstorm', 'Frostfire', 'Celestial', 'Emberthorn', 'Frostflame', 'Hallowed', 'Shadowveil','Windshear', 'Mysticwind', 'Starflare', 'Dawn', 'Emberlance', 'Starlight', 'Frostmoon', 'Phantomfire', 'Gale', 'Shade', 'Firethorn', 'Twilight', 'Ebonheart', 'Shadowgale', 'Emberwhirl', 'Frostflame', 'Mistweaver','Embershadow', 'Phoenixfeather', 'Frostflare', 'Nightsong', 'Twilightfall', 'Voidfire', 'Celestial', 'Galewind', 'Duskblade', 'Windshear', 'Stormgale', 'Hurricane', 'Frostthorn', 'Starbloom', 'Emberveil', 'Shade', 'Emberflame', 'Duskweaver', 'Frostbite', 'Phoenixborn', 'Mistwalker', 'Shadowveil', 'Emberwind', 'Galesinger', 'Twilightflame', 'Firethorn', 'Nebulaflame', 'Frostshroud', 'Shade', 'Starlight', 'Galewind','Twilight', 'Gloom', 'Nightstalker', 'Frostflare', 'Shadowreaver', 'Embershadow', 'Celestial', 'Duskfire','Embersong', 'Phantom', 'Chaos', 'Emberguard', 'Frostlance', 'Shadeweaver', 'Hallowed', 'Cinder', 'Gloom', 'Flame', 'Spiritwalker', 'Hollow', 'Gale', 'Frostfire', 'Twilight', 'Starfire', 'Emberglow','Dawn', 'Ebonthorn', 'Frostfire', 'Mistwalker', 'Shadowveil', 'Galewind', 'Frostshard', 'Phantom', 'Emberdancer', 'Wraith', 'Frostfire', 'Cinder', 'Windshear', 'Nebula', 'Duskweaver', 'Embershadow','Nightstalker', 'Galewind', 'Firestorm', 'Embershadow', 'Frostflare', 'Dawnbringer', 'Radiant', 'Emberstrike', 'Shade', 'Emberclaw', 'Galewind', 'Nightsong', 'Windrider', 'Twilight', 'Voidfire', 'Firewhisper', 'Emberflare', 'Frostgale', 'Nightfall', 'Starbloom', 'Ebonfire', 'Hallowed', 'Shade', 'Phoenix', 'Frostfire', 'Shadeweaver', 'Nebulaflame', 'Chaos', 'Emberveil', 'Nightsong', 'Dawn', 'Emberstorm', 'Cinder', 'Frostwhisper', 'Spiritwalker', 'Windshear', 'Gale', 'Twilight', 'Nightshade','Froststorm', 'Firethorn', 'Ethereal', 'Duskfire', 'Nightwing', 'Ebon', 'Shade', 'Emberveil', 'Embershadow', 'Flame', 'Emberstrike', 'Voidwalker', 'Galewind', 'Froststorm', 'Wraith', 'Phantomfire', 'Windfire', 'Nebulon', 'Dawnblade', 'Firestorm', 'Mystic', 'Twilightflame', 'Hallowed', 'Wraithlord','Embershadow', 'Gale', 'Frostveil', 'Emberheart', 'Shade', 'Cinder', 'Hallowed', 'Twilightfall', 'Flamekeeper', 'Windrider', 'Dawnstalker', 'Galewind', 'Windshear', 'Emberguard', 'Duskblade', 'Wraith', 'Nightshade', 'Cinder', 'Emberstorm', 'Voidcaller', 'Frostbite', 'Galewind', 'Emberflame','Shade', 'Shadowblade', 'Frostwind', 'Embersong', 'Twilight', 'Nightfire', 'Duskfall', 'Cinder','Hallowed', 'Galewind', 'Frostfire', 'Emberveil', 'Embershadow', 'Void', 'Ebon', 'Emberclaw', 'Hallowed', 'Frostfire', 'Shade', 'Emberguard', 'Wraith', 'Firethorn', 'Shade', 'Hallowed', 'Twilight', 'Galewind', 'Frostflame', 'Dawn', 'Dusk', 'Frostfire', 'Void', 'Emberwind', 'Nightshade', 'Frostwhisper', 'Gale', 'Emberdancer', 'Embershadow', 'Voidcaller', 'Hallowed', 'Shade', 'Ethereal', 'Emberveil', 'Dusk', 'Nightsong', 'Froststorm', 'Gale', 'Dawnbringer', 'Cinder', 'Nebulaflame', 'Shadowveil', 'Wraith', 'Emberwind', 'Galewind', 'Twilight', 'Cinder', 'Ebon', 'Nightfall', 'Shade', 'Twilightfall', 'Hallowed', 'Nebulon', 'Cinder', 'Firewhisper', 'Galewind', 'Duskfall', 'Flame', 'Frostgale', 'Emberstorm', 'Voidwalker', 'Spiritwalker', 'Twilight'))

    if choice((True, False)):
        if choice((True, False)):
            under_score2 = "_"
        rnd_number = f'{under_score2}{randint(1, 99)}'

    nick = prefix + under_score + "".join(nick).capitalize() + rnd_number
    return nick
def generate_password():
    chars = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "dot": "."
    }

    password_length = random.randint(8, 15)
    
    
    password_chars = [random.choice(chars[key]) for key in chars]
    
    
    remaining_chars = random.choices("".join(chars.values()), k=password_length - len(password_chars))
    
    password_chars.extend(remaining_chars)
    random.shuffle(password_chars)  
    
    return ''.join(password_chars)

def generate_random_string(length):
    chars = string.ascii_letters + string.digits + "."
    return ''.join(random.choices(chars, k=length))






import urllib.parse
import traceback
import imaplib, email, re



def getcode(mail, password, server="imap.zmailservice.com", folder="INBOX", sender="noreply@email.kick.com", timeout=90, poll_interval=5):

    try:
        M = imaplib.IMAP4_SSL(server, 993)
        M.login(mail, password)
    except Exception as e:
        print(f"IMAP login hatası: {e}")
        return None

    end_at = time.time() + timeout
    code_found = None
    try:
        while time.time() < end_at and not code_found:
            try:
                M.select(folder)
                typ, data = M.search(None, 'FROM', f'"{sender}"')
                if typ == 'OK' and data and data[0]:
                    ids = data[0].split()
                    if ids:
                        latest_id = ids[-1]
                        typ2, msg_data = M.fetch(latest_id, '(RFC822)')
                        if typ2 == 'OK' and msg_data and msg_data[0]:
                            msg = email.message_from_bytes(msg_data[0][1])
                            
                            raw_subj = msg.get('Subject', '')
                            try:
                                from email.header import decode_header
                                parts = decode_header(raw_subj)
                                subject = ''.join(
                                    [(t.decode(c or 'utf-8', errors='ignore') if isinstance(t, bytes) else t) for t, c in parts]
                                )
                            except Exception:
                                subject = raw_subj or ''

                            
                            m = re.search(r"\b(\d{4,8})\b", subject)
                            if m:
                                code_found = m.group(1)
                                print(f"IMAP: Subject code: {code_found}")
                            else:
                                
                                body_text = ''
                                if msg.is_multipart():
                                    for part in msg.walk():
                                        if part.get_content_type() == 'text/plain':
                                            cs = part.get_content_charset() or 'utf-8'
                                            try:
                                                body_text += part.get_payload(decode=True).decode(cs, errors='ignore')
                                            except Exception:
                                                pass
                                            
                                            
                                else:
                                    cs = msg.get_content_charset() or 'utf-8'
                                    try:
                                        body_text = msg.get_payload(decode=True).decode(cs, errors='ignore')
                                    except Exception:
                                        body_text = ''
                                m2 = re.search(r"\b(\d{4,8})\b", body_text)
                                if m2:
                                    code_found = m2.group(1)

                if code_found:
                    try:
                        M.logout()
                    except Exception:
                        pass
                    try:
                        return int(code_found)
                    except Exception:
                        return code_found
            except Exception as ie:
                print(f"IMAP okuma hatası: {ie}")
            time.sleep(poll_interval)
    finally:
        try:
            M.logout()
        except Exception:
            pass
    return None

async def process_kpsdk_item():
    try:
        retry_count = 0
        while retry_count < 15:
            with open("livelive.txt", "r", encoding="utf-8") as f:
                raw_lines = [ln.strip() for ln in f.read().splitlines() if ln.strip()]
            lines = [ln for ln in raw_lines if ":" in ln]

            if not lines:
                print("Hata: livelive.txt boş veya 'email:password' formatında kayıt yok!")
                return

            selected_line = random.choice(lines)
            parts = selected_line.split(':', 1)
            if len(parts) < 2:
                print(f"Hatalı format (skip): {selected_line}")
                continue
            mail, pas = parts[0], parts[1]

            print(f"Seçilen mail: {mail}")
            print("[STAGE] Kasada solve başlıyor")
            kasada = await kasadasolv()
            print("[STAGE] Kasada solve bitti")

            headers = {
                "Host": "kick.com",
                "Accept": "application/json, text/plain, */*",
                "X-App-Version": "39.7.19",
                "Content-Type": "application/json",
                "X-Kpsdk-V": "j-0.0.0",
                "X-App-Platform": "Android",
                "Origin": "https://localhost",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://localhost/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                "User-Agent": kasada.get('user-agent'),
                "x-requested-with": "XMLHttpRequest",
                "x-kpsdk-ct": kasada.get('x-kpsdk-ct'),
                "x-kpsdk-cd": kasada.get('x-kpsdk-cd'),
            }

            with open('babaproxy.txt', 'r', encoding="utf-8") as f:
                proxies = f.read().splitlines()
            if not proxies:
                print("Hata: babaproxy.txt boş!")
                return

            session = aiocurl.Session()

            print("[STAGE] Doğrulama maili isteniyor")
            try:
                mailat = await session.request(method="POST", url='https://kick.com/api/v1/signup/send/email', headers=headers, data={"email": mail.strip()})
            except Exception as send_err:
                print("[ERROR] Mail gönderme isteğinde hata (session.request)")
                print(repr(send_err))
                traceback.print_exc()
                raise
            print(f"Mail gönderme durumu: {mailat.status}")

            status_val = str(mailat.status)
            if status_val in ("429", "403"):
                retry_count += 1
                print(mailat.body)
                print(f"Mail gönderme denemesi {retry_count}/15 başarısız, tekrar deniyorum...")
                continue
            break

        
        if str(mailat.status) == "429":
            print(f"Mail 3 deneme sonunda da 429 verdi, listeden siliyorum: {mail}")
            if selected_line in lines:
                lines.remove(selected_line)
                with open("livelive.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
            return

        username = generate_random_username()
        passw = generate_password()

        print("[STAGE] IMAP ile kod okunuyor")
        log = getcode(mail, pas)
        print(f"[STAGE] IMAP sonuç: {log}")

        if selected_line in lines:
            lines.remove(selected_line)
            with open("livelive.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(lines) + "\n")
        print("logalti")

        if log:
            code = log
            onaylaa = await session.request(method="POST", url='https://kick.com/api/v1/signup/verify/code', headers=headers, data={"email": mail.strip(), "code": str(code).strip()})
            print(onaylaa.body)
            print(onaylaa.status)

            if str(onaylaa.status) == "204":
                jsn = {
                    "agreed_to_terms": True,
                    "isMobileRequest": True,
                    "birthdate": "04/04/2005",
                    "email": mail.strip(),
                    "cf_captcha_token": "",
                    "password": passw,
                    "password_confirmation": passw,
                    "username": username
                }

                res = await session.request(method="POST", url='https://kick.com/register', headers=headers, data=jsn)
                print(res.body)

                if str(res.status) == "200":
                    try:
                        with open("kicks.json", "r") as fs:
                            data = json.load(fs)
                    except (FileNotFoundError, json.JSONDecodeError):
                        data = []

                    ress = json.loads(res.body)
                    data.append({"auth": ress.get("token"), "mail": mail.strip(), "password": passw})

                    with open("kicks.json", "w") as fs:
                        json.dump(data, fs, indent=4)
    except Exception as e:
        print("kicksinalti ")
        print(e)
        try:
            with open("livelive.txt", "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            if 'selected_line' in locals() and selected_line in lines:
                lines.remove(selected_line)
                with open("livelive.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
        except Exception:
            pass

def worker():
    asyncio.run(process_kpsdk_item())

async def ol():
    try:
        
        items = []
        
        
        threads = []
        for i in range(1):
            t = threading.Thread(target=worker, args=())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        



    except Exception as e:
        print("olun alti")
        print(f"Error occurred: {e}")

while True:
 asyncio.run(ol())
