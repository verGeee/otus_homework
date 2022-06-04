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

pages_dict = {1: "Smth_else", 2: "About"}


@app.route("/")
def get_pages():
    return render_template(
        "index.html",
        pages=list(pages_dict.items()),
    )


@app.get("/<int:page_id>/")
def get_page_id(page_id: int):
    page_name = pages_dict[page_id]
    return render_template("details.html", page_name=page_name)


# @app.route("/about/")
# def about():
#     return render_template("about.html")
#
#
# @app.route("/smth_else/")
# def smth_else():
#     return render_template("smth_else.html")


app.run(debug=True)
