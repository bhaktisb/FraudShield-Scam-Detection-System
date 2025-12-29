from flask import Flask, render_template, request
import os
import numpy as np
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from tensorflow.keras.models import load_model
import joblib
import librosa

app = Flask(__name__)  # Corrected: __name__ instead of name
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load models
text_model_path = 'models/text_model'
text_model = BertForSequenceClassification.from_pretrained(text_model_path)
text_model.eval()
tokenizer = BertTokenizer.from_pretrained(text_model_path)

audio_model = load_model('models/audio_model.h5')
metadata_model = joblib.load('models/metadata_model.pkl')
metadata_vectorizer = joblib.load('models/metadata_vectorizer.pkl')

# Prediction function
def predict_call_scam(audio_path=None, text_input=None, metadata_dict=None):
    result = {}
    scam_votes = 0

    # Text Prediction
    if text_input:
        inputs = tokenizer(text_input, return_tensors="pt", truncation=True, padding=True, max_length=128)
        with torch.no_grad():
            outputs = text_model(**inputs)
            text_pred = torch.argmax(outputs.logits, dim=1).item()
            result['text_prediction'] = 'Scam' if text_pred == 1 else 'Legit'
            scam_votes += (text_pred == 1)
    else:
        result['text_prediction'] = 'Not Provided'

    # Audio Prediction
    if audio_path:
        try:
            y, sr = librosa.load(audio_path, sr=16000)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
            if mfcc.shape[1] < 130:
                mfcc = np.pad(mfcc, ((0, 0), (0, 130 - mfcc.shape[1])), mode='constant')
            else:
                mfcc = mfcc[:, :130]
            mfcc = mfcc.reshape(1, 40, 130, 1)
            audio_pred = audio_model.predict(mfcc)[0][0]
            result['audio_prediction'] = 'Scam' if audio_pred > 0.5 else 'Legit'
            scam_votes += (audio_pred > 0.5)
        except Exception as e:
            result['audio_prediction'] = f'Error: {e}'
    else:
        result['audio_prediction'] = 'Not Provided'

    # Metadata Prediction
    if metadata_dict:
        try:
            combined_text = metadata_dict.get('Issue', '') + " " + \
                            metadata_dict.get('Type of Call or Message', '') + " " + \
                            metadata_dict.get('Form', '') + " " + \
                            metadata_dict.get('Method', '')
            vectorized_input = metadata_vectorizer.transform([combined_text])
            metadata_pred = metadata_model.predict(vectorized_input)[0]
            result['metadata_prediction'] = 'Scam' if metadata_pred == 1 else 'Legit'
            scam_votes += (metadata_pred == 1)
        except Exception as e:
            result['metadata_prediction'] = f'Error: {e}'
    else:
        result['metadata_prediction'] = 'Not Provided'

    # Final decision
    result['final_decision'] = '⚠️ Scam Detected' if scam_votes >= 2 else '✅ Legitimate Call'
    return result

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text_input = request.form.get('text')

    metadata = {
        'Issue': request.form.get('issue', ''),
        'Type of Call or Message': request.form.get('type', ''),
        'Form': request.form.get('form', ''),
        'Method': request.form.get('method', '')
    }

    # Handle file upload
    audio_file = request.files.get('audio')
    audio_path = None
    if audio_file and audio_file.filename:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(audio_path)

    # Run prediction
    result = predict_call_scam(audio_path=audio_path, text_input=text_input, metadata_dict=metadata)
    return render_template('index.html', result=result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
