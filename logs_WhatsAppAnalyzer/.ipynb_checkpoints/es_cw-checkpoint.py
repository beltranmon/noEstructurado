import nltk
from nltk.corpus import stopwords

whatsapp_keys = ['multimedia', 'omitido', 'eliminaste', 'este', 'mensaje', 'fue', 'eliminado']

common_words = stopwords.words('spanish') + whatsapp_keys