
## Prasyarat

Pastikan Anda telah menginstal Python 3.x dan pip. Anda juga memerlukan ChromeDriver untuk Selenium.

### Instalasi ChromeDriver

1. Unduh ChromeDriver dari [sini](https://developer.chrome.com/docs/chromedriver/downloads?hl=id) sesuai dengan versi Chrome Anda.
2. Ekstrak file yang diunduh dan letakkan di direktori yang sesuai.
3. Perbarui jalur ke ChromeDriver di skrip `scripts/bot.py` pada bagian `Service("/path/to/chromedriver")`.

## Instalasi

1. Clone repository ini:

    ```sh
    https://github.com/Gopartner/auto-traffic-view-website.git
    ```

2. Instal dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Konfigurasi

Perbarui file `config/config.json` sesuai kebutuhan Anda. Contoh konfigurasi:

```json
{
  "proxies": [
  "http://192.168.1.100:8080",
  "http://192.168.1.101:8080",
  "http://192.168.1.102:8080"],
  "website": "http://www.yudibilly.blogspot.com"
}
```

## fake data
```json
{
  "cookies": {
    "session_id": "abc123def456ghi789jkl",
    "userSegment": "tech_enthusiast",
    "visitCount": 5,
    "lastVisit": "2024-07-28T10:20:30Z",
    "preferences": {
      "theme": "dark",
      "language": "en-US"
    }
  },
  "pixelTracking": {
    "pageViews": [
      {
        "url": "http://www.togelon.com/home",
        "timestamp": "2024-07-28T10:15:00Z"
      },
      {
        "url": "http://www.togelon.com/games",
        "timestamp": "2024-07-28T10:16:30Z"
      },
      {
        "url": "http://www.togelon.com/contact",
        "timestamp": "2024-07-28T10:18:10Z"
      }
    ],
    "clicks": [
      {
        "url": "http://www.togelon.com/games",
        "elementId": "gameBanner1",
        "timestamp": "2024-07-28T10:16:35Z"
      },
      {
        "url": "http://www.togelon.com/contact",
        "elementId": "contactButton",
        "timestamp": "2024-07-28T10:18:15Z"
      }
    ],
    "scrollDepth": {
      "url": "http://www.togelon.com/games",
      "depth": "75%",
      "timestamp": "2024-07-28T10:17:00Z"
    }
  },
  "formRegistration": {
    "username": "techUser123",
    "email": "techuser123@example.com",
    "password": "hashedpassword123",
    "dob": "1990-01-01",
    "gender": "male",
    "interests": ["technology", "gaming", "programming"]
  }
}
```
## jalankan
```sh
python scripts/bot.py
```
## struktur projects:
```lua
my-traffic-bot/
├── README.md
├── requirements.txt
├── config/
│   └── config.json
├── data/
│   ├── fake_data.json
│   └── user_agents.txt
├── logs/
│   └── bot.log
├── scripts/
│   ├── __init__.py
│   ├── bot.py
│   ├── menu.py
│   ├── proxy.py
│   ├── user_agent.py
│   └── utils.py
└── tests/
    └── test_bot.py
```

## Lokasi

Proyek ini dibuat di Bali

[Klik di sini untuk melihat lokasi di Google Maps](https://maps.app.goo.gl/42dhk7qCd1F6JWH4A)

