import nltk,contractions

#from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import MWETokenizer

mw = MWETokenizer()
wl=WordNetLemmatizer()
ps=PorterStemmer()

text1 = '''I'll be there within 5 min. Shouldn't you be there too?
          I'd love to see u there my dear. It's awesome to meet new friends.
          We've been waiting for this day for so long.'''
expanded_words = []
for word in text1.split():
    # using contractions.fix to expand the shortened words
    expanded_words.append(contractions.fix(word))

expanded_text = ' '.join(expanded_words)

print("")

print('Original text: ' + text1)

print("")

print('Expanded_text: ' + expanded_text)

print("")

print("     Stemming")

text2="studies studying cries cry"

tokenization1=nltk.word_tokenize(text2)

tokenization2=nltk.word_tokenize(text2)

for word1 in tokenization1:
    print("Stemming for {} is {}".format(word1,ps.stem(word1)))

print("")

print("     Lemmatization")

for word2 in tokenization2:
    print("Lemma for {} is {}".format(word2,wl.lemmatize(word2)))

print("")

#lemmarizer=WordNetLemmatizer()
#print("rocks : ",lemmarizer.lemmatize("rocks"))

#print("better :", lemmarizer.lemmatize("better", pos ="a"))

# import MWETokenizer() method from nltk
#from nltk.tokenize import MWETokenizer

# Create a reference variable for Class MWETokenizer
#tk=MWETokenizer([('N','Y','P','S'),('New','York','Port','Said')])         OR

print("     Tokenize multiword expressions")
tk=MWETokenizer()

tk.add_mwe(('New','York'))

tk.add_mwe(('Port','Said'))

# Create a string input
txt = "Hello every one in New York and Port Said "

# Use tokenize method
mlword = tk.tokenize(txt.split())

print(mlword)





