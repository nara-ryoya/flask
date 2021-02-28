from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    flg = True
    return render_template('index.html',
    title = "Flask Introduction!",
    message = "start Jinja",
    flg = flg)

@app.route('/', methods=['POST'])
def form():
    flg = False
    name = request.form.get('name')
    message = request.form.get('message')
    sex = request.form.get('sex')
    return render_template('index.html',
    title = "Form Sample",
    name = name,
    message = message,
    sex = sex,
    flg = flg)


if __name__ =='__main__':
    app.debug = True
    app.run(host='localhost')