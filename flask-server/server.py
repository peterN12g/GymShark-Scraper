from flask import Flask
from main import scrape_and_notify

app = Flask(__name__)

# Members API Route
@app.route("/members")
def members():
    name, price = scrape_and_notify()
    
    response = {
        'item-name': name,
        'item-price':price
    }
    return response

if __name__ == "__main__":
    app.run(debug=True)