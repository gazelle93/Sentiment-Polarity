# Overview
- In sentiment analysis, analyzing the polarity of the sentiment of a given text is a key aspect which shows the degree of positive or negative. This project aims to implement the result of the sentence-level and word-level polarity of a given text.

# Brief description
- text_processing.py
> Output format
> - output: Tokenized result of a given text. (list)
- sentiment_analysis.py
> Output format
> - output: Polarity score of given text.

# Prerequisites
- argparse
- stanza
- spacy
- nltk
- gensim
- afinn
- textblob

# Parameters
- nlp_pipeline(str, defaults to "spacy"): NLP preprocessing pipeline.
- sentiment_analyzer(str, defaults to "afinn"): Selected sentiment analyzer (afinn, nltk, textblob).

# References
- Stanza: Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. D. (2020). Stanza: A Python natural language processing toolkit for many human languages. arXiv preprint arXiv:2003.07082.
- Spacy: Matthew Honnibal and Ines Montani. 2017. spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing. To appear (2017).
- NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009). Natural Language Processing with Python.  O'Reilly Media Inc.
- Gensim: Rehurek, R., & Sojka, P. (2010). Software framework for topic modelling with large corpora. In In Proceedings of the LREC 2010 workshop on new challenges for NLP frameworks.
- Afinn: Nielsen, F. Å. (2011). A new ANEW: Evaluation of a word list for sentiment analysis in microblogs. arXiv preprint arXiv:1103.2903.
- Textblob: Loria, S. (2018). textblob Documentation. Release 0.16. (https://textblob.readthedocs.io/en/dev/)
