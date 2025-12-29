🛡️ FraudShield – AI-Based Scam Detection System

FraudShield is a multimodal AI-powered scam detection system that identifies fraudulent calls by analyzing text, audio, and metadata.
The project combines Natural Language Processing (NLP), Deep Learning, Machine Learning, and Quality Assurance Automation in a single end-to-end application.

🚀 Key Features

🔤 Text Scam Detection using BERT (Transformer-based NLP)

🎙️ Audio Scam Detection using CNN on MFCC features

📊 Metadata-Based Detection using Scikit-Learn

🧠 Majority Voting Logic for final decision

🌐 Flask Web Application

🧪 Manual & Automated QA Testing

🤖 Selenium + PyTest Automation

📄 HTML Test Execution Reports

🧰 Technologies Used
Component	Technology
Backend Framework	Flask (Python)
Text Classification	BERT (HuggingFace + PyTorch)
Audio Classification	CNN (TensorFlow + Keras)
Metadata Classification	Scikit-Learn
Audio Processing	Librosa
Model Storage	Joblib
Frontend	HTML, CSS, Jinja2
Automation Testing	Selenium, PyTest
Test Reporting	pytest-html
🧠 System Architecture (High Level)

User provides:

Call transcript (Text)

Audio file (.wav / .mp3)

Call-related metadata

Individual Models Predict:

Text → BERT

Audio → CNN

Metadata → ML Classifier

Voting Logic:

If 2 or more models predict Scam → ⚠️ Scam Detected

Else → ✅ Legitimate Call

📂 Project Structure
FraudShield/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── fraud.jpg
├── tests/
│   ├── test_homepage.py
│   ├── test_text_input.py
│   ├── test_audio_upload.py
│   └── test_empty_input.py
├── FraudShield_QA/
│   ├── FraudShield_Test_Plan.docx
│   ├── FraudShield_TestCases.xlsx
│   └── FraudShield_BugReport.xlsx
└── README.md


⚠️ Large model files, audio uploads, and virtual environments are intentionally excluded using .gitignore.

▶️ How to Run the Project
1️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Flask Application
python app.py


Open in browser:

http://127.0.0.1:5000

🧪 Quality Assurance (QA)
✔ Manual Testing

Test Plan created

Functional & edge case testing

Bug reporting

📁 Location:

FraudShield_QA/

✔ Automation Testing

Black-box testing using Selenium

Test execution using PyTest

HTML report generation

Run Automation Tests:
pytest tests/ --html=fraudshield_report.html
