
# 🛡️ Kick.com Kasada (KPSDK) Solver - Free API Automation

This project is designed to bypass the Kasada (KPSDK) protection system used by [kick.com](https://kick.com) by using a free API via RapidAPI. It automatically generates usernames and passwords, handles email verification with temp mail, and registers new accounts.

---

## 🚀 Features

- ✅ KPSDK (Kasada) Solver via RapidAPI
- 📩 Automatic email verification using temp mail
- 🔐 Random username and strong password generator
- 🔁 Continuous account creation loop

---

## 🧪 Quick Start

### Requirements

- Python 3.8+
- Install the required packages:

```bash
pip install aiohttp 
```

### How to Use

1. Replace `"YOUR_API_KEY"` inside the `kasadasolv()` function with your own [RapidAPI](https://rapidapi.com/ttur5678/api/kick-kasada-kpsdk-solver-api/playground) key:

```python
headers = {
  "x-rapidapi-key": "YOUR_API_KEY",
  "x-rapidapi-host": "kick-kasada-kpsdk-solver-api.p.rapidapi.com"
}
```

2. Run the script:

```bash
python accgen.py
```

---

## 🌐 Free Kasada Solver API

This script uses a free API via RapidAPI to solve Kick’s KPSDK protection.

🔗 **Free API URL**:  
https://rapidapi.com/ttur5678/api/kick-kasada-kpsdk-solver-api/playground

You can send 1 request/second in the free tier.

---

## 💎 Premium KPSDK Solver 

Need higher speed or stability? A private and faster version is available for purchase.

https://rapidapi.com/ttur5678/api/kick-kasada-kpsdk-solver-api/playground

---

## 📁 Output

All created accounts will be saved to a local `kicks.json` file in this format:

```json
[
  {
    "auth": "TOKEN_HERE",
    "mail": "example@dataarchive.site",
    "password": "securePassword"
  }
]
```

---

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Any misuse is strictly the user's responsibility.

---

## 📞 Contact

Need help or have questions?  

Reach out via Telegram: [@wezaxy](https://t.me/wezassy)
discord: wezaxyy
