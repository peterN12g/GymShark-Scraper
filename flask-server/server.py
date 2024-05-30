from flask import Flask
from flask_cors import CORS
from main import product_scrape

app = Flask(__name__)
CORS(app, resources={r"/members": {"origins": ["http://localhost:3000",'https://gymshark-scraper.pages.dev/']}})

# Members API Route
@app.route("/members")
def members():
    products = product_scrape()
    
    response = {
        'product': products,
    }
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True, ssl_context='adhoc')