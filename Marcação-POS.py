import bs4 as bs
import urllib.request
import nltk
import spacy

pln= spacy.load('pt_core_news_sm')

print(pln)

documento=pln('Estou aprendendo processamento de linguagem natural')

for token in documento:
    print(token.text, token.pos_)