from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def bot():
    return render_template('main-sample.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
