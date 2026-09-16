```markdown
# 🤖 Intelligent Chatbot — Addiction Prevention Assistant

An NLP-driven conversational agent designed to support addiction prevention
through intent classification and supportive dialogue.

## ✨ Features

- Intent classification using a neural network built with PyTorch
- Text preprocessing with NLTK (tokenization, stemming, bag-of-words)
- REST API backend exposing model inference via Flask
- Responsive chat interface built with HTML5, CSS3, and JavaScript

## 🏗️ How It Works

User messages are sent from the chat interface to the Flask REST API,
preprocessed with NLTK, passed through the trained PyTorch model for
intent classification, and matched to a supportive response.

## 🛠️ Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Model    | PyTorch, NLTK           |
| Backend  | Python, Flask           |
| Frontend | JavaScript, HTML5, CSS3 |

## 🚀 Getting Started

Clone the repository:

    git clone https://github.com/YOUR-USERNAME/addiction-prevention-chatbot.git
    cd addiction-prevention-chatbot

Install the dependencies:

    pip install -r requirements.txt

Train the model and start the app:

    python train.py
    python app.py

Then open the chat interface in your browser at `http://127.0.0.1:5000`.

## 📁 Project Structure

    addiction-prevention-chatbot/
    ├── app.py            # Flask REST API
    ├── train.py          # Model training script
    ├── intents.json      # Training data (intents and responses)
    ├── static/           # CSS and JavaScript files
    └── templates/        # HTML files

## 🔮 Future Improvements

- Sentiment analysis for crisis detection
- Larger and more diverse intent dataset
- Cloud deployment

---

*Developed as a final year project for a Bachelor's degree.*
```

