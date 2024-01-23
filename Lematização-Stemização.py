import bs4 as bs
import urllib.request
import nltk
import spacy
nltk.download('rslp')
pln= spacy.load('pt_core_news_sm')



##lematização
documento=pln('Estou aprendendo processamento de linguagem natural, curso em Curitiba')

for token in documento:
    print(token.text, token.lemma_)

doc = pln('encontrei encontraram encontrarão encontrariam cursando curso cursei')
for token in doc:
    print(token.lemma_)


#stemização
stemmer=nltk.stem.RSLPStemmer()
p=stemmer.stem('aprender')
print(p)
print()

#comparando o stematização e lematização
for token in documento:
  print(token.text, token.lemma_, stemmer.stem(token.text))