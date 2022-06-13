"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)
app.config.update(ENV="development")

pages_list = ["about"]


@app.route("/", endpoint="index")
def get_pages():
    return render_template(
        "index.html",
        pages=pages_list,
    )


# @app.get("/<string:page_name>/", endpoint="details")
# def get_page_name(page_name: str):
#     return render_template("details.html", page_name=page_name)
@app.route("/about/", endpoint="about")
def get_page_name():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
