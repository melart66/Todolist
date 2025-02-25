from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
#loginpage
@app.route('/')
def home():
    # Передача переменных в шаблон
    return render_template(
        'index.html',
        name="loginpage",
        date=datetime.now().strftime("%d.%m.%Y")
    )
# main page for standart user
@app.route('/mainpage')
def mainpage():
    # Передача переменных в шаблон
    return render_template(
        'mainpage.html',
        name="mainpage",
        date=datetime.now().strftime("%d.%m.%Y")
    )
#lk for standart user
@app.route('/lkstandartuser')
def lk():
    # Передача переменных в шаблон
    return render_template(
        'lkstandartuser.html',
        name="lksu",
        date=datetime.now().strftime("%d.%m.%Y")
    )
#mainpage for admin user
@app.route('/mainpageadmin')
def manepageadmin():
    # Передача переменных в шаблон
    return render_template(
        'mainpageadmin.html',
        name="manepageadmin",
        date=datetime.now().strftime("%d.%m.%Y")
    )
#lk for amdin user
@app.route('/lkadmin')
def lkadmin():
    # Передача переменных в шаблон
    return render_template(
        'lkadmin.html',
        name="lkadmin",
        date=datetime.now().strftime("%d.%m.%Y")
    )
if __name__ == '__main__':
    app.run(debug=True)