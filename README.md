# 🎬 Movie Sentiment Analyzer

## 🌐 Live Demo
🔗 https://movie-sentiment-analyzer-hxjp4k8ksnan9awtnddgah.streamlit.app/

---

## 📌 Overview
An AI-powered web application that predicts whether a movie review is **positive** or **negative** using Natural Language Processing (NLP) and Machine Learning.

---

## 🚀 Features
- Predicts sentiment of movie reviews (Positive / Negative)
- Interactive web interface built with Streamlit
- Real-time user input analysis
- Fast predictions using a pre-trained model

---

## 🧠 How It Works
1. Text data is cleaned and preprocessed  
2. Converted into numerical features using TF-IDF  
3. Model is trained using the Naive Bayes algorithm  
4. User input is analyzed and predicted instantly  

---

## 🛠 Tech Stack
- Python  
- scikit-learn  
- Streamlit  
- Joblib  

---

## 📂 Project Structure
```
app.py             # Main application  
train.py           # Model training script  
model.pkl          # Saved ML model  
vectorizer.pkl     # Saved TF-IDF vectorizer  
requirements.txt   # Dependencies  
README.md          # Documentation  
```

---

## ▶️ How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ⚠️ Note
The dataset is not included in this repository due to its large size.  
You can download the IMDB dataset from Kaggle if needed.

---

## 🚀 Future Improvements
- Add confidence score for predictions  
- Improve model accuracy  
- Enhance UI/UX  
- Use deep learning models  

---

## 📌 Author
Developed as part of an AI/ML learning project.