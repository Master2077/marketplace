"""Курсовое задание: веб-приложение «Контакты» с приёмом GET и POST.

GET  — на любой запрос возвращается страница contacts.html.
POST — данные формы читаются из тела запроса, печатаются в консоль,
       в ответ отправляется страница-подтверждение.

Запуск:
    python app.py

После запуска откройте http://127.0.0.1:8000/ — или любой другой адрес
на этом порту, например http://127.0.0.1:8000/anything.
"""

from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

HOST = "127.0.0.1"
PORT = 8000

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "contacts.html"

# Русские подписи для полей формы (в консоли печатаются исходные имена полей).
FIELD_LABELS = {
    "name": "Имя",
    "email": "Почта",
    "message": "Сообщение",
}

RESULT_PAGE = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Сообщение получено — MarketPlace</title>
  <link href="https://cdn.jsdelivr.net/gh/Master2077/marketplace@main/css/common.css" rel="stylesheet">
  <style>
    body {
      margin: 0;
      background: #121212;
      color: #f5f5f5;
      font-family: Arial, sans-serif;
    }

    .result {
      max-width: 620px;
      margin: 70px auto;
      padding: 26px;
      border: 1px solid #2b2b2b;
      border-radius: 16px;
      background: #181818;
    }

    .result h1 {
      margin: 0 0 8px;
      font-size: 24px;
    }

    .result p {
      margin: 0 0 18px;
      color: #a7a7a7;
      font-size: 14px;
    }

    .result dl {
      display: grid;
      grid-template-columns: 150px 1fr;
      gap: 8px 16px;
      margin: 0 0 22px;
    }

    .result dt {
      color: #a7a7a7;
      font-size: 13px;
    }

    .result dd {
      margin: 0;
      font-size: 14px;
      overflow-wrap: anywhere;
    }

    .result a {
      color: #e53935;
      font-size: 14px;
      text-decoration: none;
    }

    .result a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <main class="result">
    <h1>Сообщение получено</h1>
    <p>Данные отправлены на сервер и выведены в консоли.</p>
    <dl>{rows}</dl>
    <a href="/">← Вернуться на страницу «Контакты»</a>
  </main>
</body>
</html>
"""


class ContactsHandler(BaseHTTPRequestHandler):
    """GET отдаёт страницу «Контакты», POST печатает данные формы в консоль."""

    def do_GET(self):
        # Читаем HTML-файл целиком через with open(), как требует задание.
        with open(HTML_FILE, "r", encoding="utf-8") as file:
            page = file.read()

        self.send_page(page)

    def do_HEAD(self):
        with open(HTML_FILE, "r", encoding="utf-8") as file:
            page = file.read()

        body = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

    def do_POST(self):
        # 1. Читаем тело запроса: длина указана в заголовке Content-Length.
        length = int(self.headers.get("Content-Length") or 0)
        raw_body = self.rfile.read(length)

        # 2. Декодируем с учётом кодировки из заголовка Content-Type.
        content_type = self.headers.get("Content-Type", "")
        charset = "utf-8"
        if "charset=" in content_type:
            charset = content_type.split("charset=")[-1].strip()
        body = raw_body.decode(charset, errors="replace")

        # 3. Печатаем в консоль всё, что пришло от пользователя.
        print("\n" + "=" * 60)
        print(f"POST {self.path}")
        print(f"Content-Type: {content_type}")
        print(f"Content-Length: {length}")
        print("-" * 60)

        fields = []
        parsed = parse_qs(body, keep_blank_values=True)
        if parsed:
            for key, values in parsed.items():
                for value in values:
                    fields.append((key, value))
                    print(f"{key}: {value}")
        else:
            fields.append(("тело запроса", body))
            print(body)

        print("-" * 60)
        print(f"Сырое тело запроса: {body}")
        print("=" * 60)

        # 4. Отправляем страницу-подтверждение с принятыми данными.
        rows = "".join(
            f"<dt>{escape(FIELD_LABELS.get(key, key))}</dt><dd>{escape(value)}</dd>"
            for key, value in fields
        )
        self.send_page(RESULT_PAGE.replace("{rows}", rows))

    def send_page(self, page):
        body = page.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Аккуратный лог запросов в консоли.
        print(f"{self.address_string()} — {fmt % args}")


def main():
    server = HTTPServer((HOST, PORT), ContactsHandler)
    print(f"Сервер запущен: http://{HOST}:{PORT}/")
    print("GET — страница «Контакты», POST — данные формы в консоли. Ctrl+C — остановить.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
