from transformers import pipeline

def analyze_social_media(posts):
    sentiment_analyzer = pipeline("sentiment-analysis")
    results = sentiment_analyzer(posts)
    return results
