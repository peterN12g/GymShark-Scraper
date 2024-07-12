from flask import Flask
from main import product_scrape
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/members": {"origins": ["https://gymshark-scraper.peternguyen.tech"]}})

# Members API Route
@app.route("/members")
def members():
    products = product_scrape()
    
    response = {
        'product': products,
    }
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8085,debug=True)