# Phishing Website Detection System

## Introduction

The Phishing Website Detection System is a cybersecurity project developed using Machine Learning and URL analysis techniques. This system helps users identify whether a website is safe or a phishing website by analyzing various URL-based features and domain information.

The user enters a website URL, and the system automatically extracts features, performs domain analysis, and predicts whether the website is legitimate or malicious.

---

## Objectives

* Detect phishing websites using Machine Learning.
* Analyze URLs automatically.
* Check HTTPS security status.
* Detect IP address-based URLs.
* Perform WHOIS domain age analysis.
* Provide Safe or Phishing predictions.

---

## Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Web Framework

* Flask

### Libraries

* Pandas
* NumPy
* Joblib
* Requests
* BeautifulSoup
* Python-WHOIS

### Frontend

* HTML
* CSS

---

## Methodology

1. User enters a website URL.
2. The system extracts URL features.
3. HTTPS availability is checked.
4. IP address usage is detected.
5. Domain age is obtained using WHOIS.
6. Features are passed to the Random Forest model.
7. The model predicts whether the website is Safe or Phishing.
8. The result is displayed to the user.

---

## Features

* URL Length Analysis
* HTTPS Detection
* IP Address Detection
* Domain Age Verification
* Machine Learning Prediction
* User-Friendly Web Interface

---

## Project Workflow

User Enters URL

↓

Feature Extraction

↓

HTTPS Detection

↓

IP Address Detection

↓

WHOIS Domain Analysis

↓

Random Forest Machine Learning Model

↓

Safe / Phishing Prediction

---

## Project Structure

```text
phishing-website-detector/
│
├── app.py
├── train_model.py
├── phishing_dataset.csv
├── phishing_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## Sample Output

### Input

```text
https://example.com
```

### Website Analysis

* URL Length: 18
* HTTPS: Yes
* IP Address Used: No
* Domain Age: 10491 Days

### Prediction

✅ Safe Website

---

## Results

The system successfully detects potentially malicious websites using URL analysis and Machine Learning techniques. It provides users with an easy-to-use interface for checking website safety.

---

## Future Enhancements

* SSL Certificate Validation
* Blacklist Integration
* Website Content Analysis
* Real-Time Threat Intelligence
* Advanced Machine Learning Algorithms

---

## Conclusion

The Phishing Website Detection System effectively identifies potentially dangerous websites using URL features and domain information. This project demonstrates practical cybersecurity concepts and the application of Machine Learning in phishing detection.

---

## Author

**Pavani Duvvuru**

Cyber Security Internship Project – 2026

Organization: Tech Vedhu

Domain: Cyber Security

---

## GitHub Repository

https://github.com/pavaniduvvuru63-ctrl/phishing-website-detector
