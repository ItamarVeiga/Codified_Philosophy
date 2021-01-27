import nltk
import pre_processamento as pp
#baixando corpus machado de assis
nltk_id = 'machado'
nltk.download(nltk_id)

#pegando Dom Casmurro
dom_casmurro = nltk.corpus.machado.raw('romance/marm08.txt')

