# 🛡️ Kick.com Kasada (KPSDK) Solver – Free API Automation

This project automates the process of bypassing the Kasada (KPSDK) protection system used by **Kick.com**. It integrates with a free API on **RapidAPI** to solve Kasada challenges, automatically generates usernames and passwords, verifies emails via IMAP, and continuously registers new accounts.

---

## 🚀 Features

* ✅ KPSDK (Kasada) solver via **RapidAPI**
* 📩 Automatic email verification using **IMAP**
* 🔐 Random username and strong password generator
* 🔁 Continuous account creation loop

---

## 🧪 Quick Start

### Requirements

* **Python 3.8+**
* Install required dependencies:

```bash
pip install aiohttp aiocurl
```

### API Setup

Open `sa.py` and replace `YOUR_API_KEY` with your RapidAPI key:

```python
headers = {
    "x-rapidapi-key": "YOUR_API_KEY",
    "x-rapidapi-host": "kick-kasada-kpsdk-solver-api.p.rapidapi.com"
}
```

---

### Hotmail Source (Required)

* Obtain Hotmail addresses from: **[https://hotmail.dataarchive.site](https://hotmail.dataarchive.site)**
* Save them in `livelive.txt` with the following format (one entry per line):

```
email@hotmail.com:password
```

The script uses these accounts via IMAP to read Kick.com's verification emails.

---

### Usage

1. Add your RapidAPI key into `sa.py`.
2. Prepare `livelive.txt` with Hotmail accounts (`email:password`).
3. (Optional) Add proxies into `babaproxy.txt` (one per line).
4. Run the generator:

```bash
python accgen.py
```

> The Kasada solver logic is already implemented in `sa.py`. You only need a valid RapidAPI key.

---

## 🌐 Free Kasada Solver API

This script uses the **Kick Kasada KPSDK Solver** API available on RapidAPI.

* Playground: [https://rapidapi.com/ttur5678/api/kick-kasada-kpsdk-solver-api/playground](https://rapidapi.com/ttur5678/api/kick-kasada-kpsdk-solver-api/playground)
* Free tier: **1 request/second**

---

## 💎 Premium KPSDK Solver

Need higher performance or stability? A **private premium version** is available for purchase on RapidAPI.

* Premium API: [https://rapidapi.com/ttur5678/api/kick-kasada-kpsdk-solver-api/playground](https://rapidapi.com/ttur5678/api/kick-kasada-kpsdk-solver-api/playground)

---

## 📁 Output

All successfully created accounts are stored in `kicks.json` in the following format:

```json
[
  {
    "auth": "TOKEN_HERE",
    "mail": "example@hotmail.com",
    "password": "securePassword"
  }
]
```

---

## ⚠️ Disclaimer

This tool is provided strictly for **educational and research purposes only**.
The author assumes no responsibility for any misuse.

---

## 📞 Contact

Need assistance or have questions?

* **Telegram:** [@wezaxy](https://t.me/wezaxy)
* **Discord:** wezaxy
* **Community Server:** [Join Here](https://discord.gg/c44FB4PFcW)

---

### License

Use this project responsibly. No license specified — add one if you plan to publish publicly.
