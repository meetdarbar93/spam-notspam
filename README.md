# 📩 Email/SMS Spam Classifier

This is a simple **Machine Learning + NLP based Spam Classifier** built using Python and Streamlit.
It classifies whether a given message is **Spam** or **Not Spam**.

---

## Features

- Classifies SMS/Email messages
- Uses Natural Language Processing (NLP)
- Simple and interactive UI using Streamlit
- Fast prediction using trained ML model

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas & NumPy

---

## Project Structure

├── app.py # Main Streamlit app
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── spam.csv # Dataset
├── requirements.txt # Dependencies
├── notebook.ipynb # Model training (optional)
└── README.md

---

## How It Works

1. User enters a message
2. Text is preprocessed:
    - Lowercasing
    - Tokenization
    - Removing stopwords & punctuation
    - Stemming
3. Text is converted using TF-IDF
4. Model predicts:
    - `Spam`
    - `Not Spam`

---

## Text Preprocessing

The following NLP steps are applied:

- Tokenization
- Stopword removal
- Stemming using PorterStemmer

---

## Run the Project

### 1. Clone the repository

```bash
git clone "https://github.com/meetdarbar93/spam-notspam.git"
cd spam-notspam
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

### Requirements

```bash
streamlit
scikit-learn
pandas
numpy
nltk
```

### Dataset

SMS Spam Collection Dataset (spam.csv)

### Example

input

```bash
Congratulations! You have won a free ticket.
```

output

```bash
Spam
```

## Author

Meet Darbar
