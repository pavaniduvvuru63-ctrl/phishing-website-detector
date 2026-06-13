import whois
from datetime import datetime
from urllib.parse import urlparse
from flask import Flask, render_template, request
import joblib
import re

def get_domain_age(url):
    try:
        domain = urlparse(url).netloc

        if domain.startswith("www."):
            domain = domain[4:]

        print("Domain:", domain)

        info = whois.whois(domain)

        print("WHOIS Data:", info)

        creation_date = info.creation_date

        print("Creation Date:", creation_date)

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        current_time = datetime.now(creation_date.tzinfo)    

        age_days = (current_time - creation_date).days

        return age_days

    except Exception as e:
        print("WHOIS ERROR:", e)
        return -1



app = Flask(__name__)

model = joblib.load("phishing_model.pkl")

def extract_features(url):

    # URL length
    url_length = len(url)

    # HTTPS check
    has_https = 1 if url.startswith("https") else 0

    # IP address check
    domain = urlparse(url).netloc

    ip_pattern = r"^\d+\.\d+\.\d+\.\d+$"

    has_ip = 1 if re.match(ip_pattern, domain) else 0

    features = [url_length, has_https, has_ip]
    return features, url_length, has_https, has_ip

@app.route("/")
def home():
    return render_template("index.html")    
    

@app.route("/predict", methods=["POST"])
def predict():

    url = request.form["url"]

    domain_age = get_domain_age(url)

    print("Domain Age:", domain_age)

    features, url_length, has_https, has_ip = extract_features(url)

    prediction = model.predict([features])

    if prediction[0] == 1:
        result = "⚠️ Phishing Website Detected"
    else:
        result = "✅ Safe Website"

    return render_template(
        "index.html",
        result=result,
        domain_age=domain_age,
        url_length=url_length,
        has_https=has_https,
        has_ip=has_ip
    )

if __name__ == "__main__":
    app.run(debug=True)