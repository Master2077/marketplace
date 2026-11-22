"""Курсовое задание: простое веб-приложение «Контакты».

Сервер отвечает на любой GET-запрос одной и той же страницей contacts.html.
Содержимое страницы читается из файла через with open(), а в ответе
указывается Content-Type: text/html (вместо application/json из прошлого урока).

Запуск:
    python app.py

После запуска откройте в браузере http://127.0.0.1:8000/ — или любой другой
адрес на этом порту, например http://127.0.0.1:8000/anything.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8000

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "contacts.html"


class ContactsHandler(BaseHTTPRequestHandler):
    """На любой GET-запрос отдаёт страницу «Контакты»."""

    def do_GET(self):
        # Читаем HTML-файл целиком через with open(), как требует задание.
        with open(HTML_FILE, "r", encoding="utf-8") as file:
            page = file.read()

        body = page.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_HEAD(self):
        # Тот же ответ, но без тела — чтобы корректно работали проверки ссылок.
        with open(HTML_FILE, "r", encoding="utf-8") as file:
            page = file.read()

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page.encode("utf-8"))))
        self.end_headers()

    def log_message(self, fmt, *args):
        # Аккуратный лог запросов в консоли.
        print(f"{self.address_string()} — {fmt % args}")


def main():
    server = HTTPServer((HOST, PORT), ContactsHandler)
    print(f"Сервер запущен: http://{HOST}:{PORT}/")
    print("Любой GET-запрос возвращает страницу «Контакты». Ctrl+C — остановить.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
