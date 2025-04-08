from flask import Flask, render_template, request, url_for
from loginform import LoginForm
from data import db_session
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "YES"


@app.route("/")
def inndex():
    return render_template("base.html", username="Володя", title="Ок")


@app.route("/form_sample", methods=["POST", "GET"])
def form_sample():
    if request.method == "GET":
        return render_template("form_sample.html")

    elif request.method == "POST":
        print(request.form["email"])
        print(request.form["password"])
        print(request.form["class"])
        print(request.form["file"])
        print(request.form["about"])
        print(request.form["accept"])
        print(request.form["sex"])
        return "Форма отправлена"


@app.route("/training/<prof>")
def training(prof):
    return render_template(
        "training.html", prof=prof.lower(), title=f"{prof}ам, не рады"
    )


@app.route("/list_prof/<list>")
def list_prof(list):
    with open("news.json", "rt", encoding="utf8") as f:
        prof_list = json.loads(f.read())
    return render_template(
        "list_prof.html", prof_list=prof_list, list_type=list.lower()
    )


@app.route("/news")
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template("news.html", news=news_list)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="логин", form=form)

def main():
    db_session.global_init("db/test.sqlite3")
    app.run(host="127.0.0.1", port="8080", debug=True)


if __name__ == "__main__":
    main()
