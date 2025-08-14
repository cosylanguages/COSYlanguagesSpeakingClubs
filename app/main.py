from flask import Flask, render_template
from app.scraper import get_random_quote

app = Flask(__name__)

@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
