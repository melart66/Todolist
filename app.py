from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Передача переменных в шаблон
    return render_template(
        'index.html',
        name="Алексей",
        date=datetime.now().strftime("%d.%m.%Y")
    )

if __name__ == '__main__':
    app.run(debug=True)