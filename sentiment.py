from transformers import pipeline
import logging

# Reduce warnings
logging.getLogger("transformers").setLevel(logging.ERROR)

# Load the zero-shot classification model
classifier = pipeline("zero-shot-classification", model="roberta-large-mnli")

def sentiment(text):
    candidate_labels = ["positive", "negative", "neutral", "very positive", "very negative"]
    result = classifier(str(text), candidate_labels=candidate_labels)
    return result
