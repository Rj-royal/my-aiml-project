from textblob import TextBlob
def analyze_review(text):
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return "Positive 😊"
    elif analysis.sentiment.polarity == 0:
        return "Neutral 😐"
    else:
        return "Negative 😞"

review = input("Enter a movie review: ")
print(f"The sentiment is: {analyze_review(review)}")
