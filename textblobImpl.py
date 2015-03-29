__author__ = 'liangdong'

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def analyze(text):
    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    sentiment = blob.sentiment
    return sentiment[0]
