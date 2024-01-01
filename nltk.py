import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
mytext = "Have nice day, my friend !!! Programming in Python is fun"
print(sent_tokenize(mytext))