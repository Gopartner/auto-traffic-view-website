
## Prasyarat

Pastikan Anda telah menginstal Python 3.x dan pip. Anda juga memerlukan ChromeDriver untuk Selenium.

### Instalasi ChromeDriver

1. Unduh ChromeDriver dari [sini](https://sites.google.com/a/chromium.org/chromedriver/downloads) sesuai dengan versi Chrome Anda.
2. Ekstrak file yang diunduh dan letakkan di direktori yang sesuai.
3. Perbarui jalur ke ChromeDriver di skrip `scripts/bot.py` pada bagian `Service("/path/to/chromedriver")`.

## Instalasi

1. Clone repository ini:

    ```sh
    git clone https://github.com/username/my-traffic-bot.git
    cd my-traffic-bot
    ```

2. Instal dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Konfigurasi

Perbarui file `config/config.json` sesuai kebutuhan Anda. Contoh konfigurasi:

```json
{
  "proxies": [    "http://192.168.1.100:8080",    "http://192.168.1.101:8080",    "http://192.168.1.102:8080"  ],
  "website": "http://www.togelon.com"
}

