import nltk
import re

def getStopwords(idioma = 'portuguese'):
    nltk.download('stopwords')
    return nltk.corpus.stopwords.words(idioma)

def stemmatizar(tokens, lancaster: True):
    stemmer = nltk.LancasterStemmer() if lancaster  else nltk.PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

def lemmatizar(tokens):
    lemmatizer = nltk.WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def separarPorTokens(texto):
    from nltk.tokenize import word_tokenize
    return word_tokenize(texto)

def separarPorFrases(texto):
    from nltk.tokenize import sent_tokenize
    return sent_tokenize(texto)

def pre_processar(texto):
    from unidecode import unidecode
    texto_letras_minusculas = re.findall(r'\b[A-zÀ-úü]+\b', texto.lower())

    stopwords = getStopwords()

    texto_sem_stopwords = [unidecode(w) for w in texto_letras_minusculas if w not in stopwords]

    texto_limpo = " ".join(texto_sem_stopwords)
    
    return texto_limpo
