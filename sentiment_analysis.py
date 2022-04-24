from afinn import Afinn
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def sentence_sentiment_analysis(_input_text, _sentiment_analyzer="afinn"):
    if _sentiment_analyzer == "afinn":
        sent_analyzer = Afinn()
        return sent_analyzer.score(_input_text)
        
    # nltk - vader
    elif _sentiment_analyzer == "nltk":
        sent_analyzer = SentimentIntensityAnalyzer()
        result = sent_analyzer.polarity_scores(_input_text)
        result.pop('compound')
        return result
        
    elif _sentiment_analyzer == "textblob":
        return TextBlob(_input_text).sentiment.polarity
        
        
def words_sentiment_analysis(_input_tokens, _sentiment_analyzer="afinn"):
    token_polarity_list = []
    if _sentiment_analyzer == "afinn":
        sent_analyzer = Afinn()
        for tk in _input_tokens:
            token_polarity_list.append(sent_analyzer.score(tk))
        
    # nltk - vader
    elif _sentiment_analyzer == "nltk":
        sent_analyzer = SentimentIntensityAnalyzer()
        for tk in _input_tokens:
            result = sent_analyzer.polarity_scores(tk)
            result.pop('compound')
            token_polarity_list.append(result)
        
    elif _sentiment_analyzer == "textblob":
        for tk in _input_tokens:
            token_polarity_list.append(TextBlob(tk).sentiment.polarity)

    return token_polarity_list
