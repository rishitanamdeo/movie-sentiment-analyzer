import streamlit as st
import string
import joblib

# Title
st.title("🎬 Movie Sentiment Analyzer")

# Clean text function (keep this)
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Load trained model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Input box
review = st.text_area("Enter your movie review:")

# Button
if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        review_clean = clean_text(review)
        review_vector = vectorizer.transform([review_clean])
        prediction = model.predict(review_vector)

        if prediction[0] == "positive":
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")