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

Train the model (optional — a pre-trained `data.pth` is included):

    python train.py

Start the application:

    python chat.py

Then open the chat interface in your browser at `http://127.0.0.1:5000`.

## 📁 Project Structure

    ├── chat.py          # Flask app and chatbot logic
    ├── model.py         # Neural network model definition (PyTorch)
    ├── nltk_utils.py    # Text preprocessing helpers (NLTK)
    ├── train.py         # Model training script
    ├── intents.json     # Training data (intents and responses)
    ├── data.pth         # Trained model weights
    ├── static/          # CSS and JavaScript files
    └── templates/       # HTML files

## 🔮 Future Improvements

- Sentiment analysis for crisis detection
- Larger and more diverse intent dataset
- Cloud deployment

---

*Developed as a final year project for a Bachelor's degree.*
```





<img width="950" height="500" alt="0001" src="https://github.com/user-attachments/assets/49589fab-048c-4575-8c44-93cc41718a7f" />


<img width="950" height="500" alt="1" src="https://github.com/user-attachments/assets/dce4c3fa-c7ef-4708-bc0b-110206dabc66" />


<img width="950" height="500" alt="2" src="https://github.com/user-attachments/assets/20056347-aa89-49af-ad0f-f962d5d28158" />

<img width="950" height="500" alt="use_case_iheb_4_page-0001" src="https://github.com/user-attachments/assets/bd09a9ea-ba26-4061-95b8-999235d7ce48" />

