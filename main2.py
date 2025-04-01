from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def inndex():
    return render_template('base.html', username='Володя', title='Ок')

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower(), title=f'{prof}ам, не рады')


@app.route('/list_prof/<list>')
def list_prof(list):
    with open("news.json", "rt", encoding="utf8") as f:
        prof_list = json.loads(f.read())
    return render_template('list_prof.html', prof_list=prof_list, list_type=list.lower())


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')
