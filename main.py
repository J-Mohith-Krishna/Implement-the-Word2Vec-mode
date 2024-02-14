
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt') 
sentences = [
    "Rajalakshmi Institute of Technology (An Autonomous Institution) is one of the best engineering colleges in Chennai and is part of Rajalakshmi Institution.",
    "Rajalakshmi Institute of Technology was established in 2008.",
    "RIT is accredited with the highest grade of A++ by NAAC. RIT is affiliated with Anna University Chennai.",
    "It is one of the AICTE-approved colleges in Chennai New Delhi and also offers NBA-approved courses."
]
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

model.save("word2vec_model_sentences.bin")

loaded_model = Word2Vec.load("word2vec_model_sentences.bin")

word_embedding = loaded_model.wv['engineering']
print("Word embedding for 'engineering':", word_embedding)
