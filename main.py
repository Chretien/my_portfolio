from flask import Flask, render_template
import os
from datetime import date

app = Flask(__name__)
@app.context_processor
def year():
    year = str(date.today().year)
    return dict(year=year)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))