from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inndex():
    return render_template('base.html', username='Володя', title='Ок')

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, title=f'{prof}ам, не рады')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
