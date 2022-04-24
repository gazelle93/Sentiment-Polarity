import argparse

from text_processing import word_tokenization
from sentiment_analysis import sentence_sentiment_analysis, words_sentiment_analysis

def main(args):
    text_list = ["This is utterly excellent!", 
             "This is a horrible idea.",
            "This is certinaly not a good idea."]

    for sen in text_list:
        print("Sentence: {} -> Polarity: {}".format(sen,
                                                    sentence_sentiment_analysis(sen, args.sentiment_analyzer)))
        cul_tks = word_tokenization(sen, args.nlp_pipeline)
        for tk, pol in zip(cul_tks, words_sentiment_analysis(cul_tks, args.sentiment_analyzer)):
            print("Token: {} {}".format(tk, pol))
        print()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--nlp_pipeline", default="spacy", type=str, help="NLP preprocessing pipeline.")
    parser.add_argument("--sentiment_analyzer", default="afinn", type=str, help="Selected sentimen analyzer.")
    
    args = parser.parse_args()

    main(args)
