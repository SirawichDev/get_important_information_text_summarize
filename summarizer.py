import bs4 as bs
import urllib.request
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')

#ทำ Preprocessing
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Go_(programming_language)').read()

soup = bs.BeautifulSoup(source, 'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

text = re.sub(r'\[[0-9]*\]',' ', text)
text = re.sub(r'\s+',' ',text)
new_text = text.lower()
new_text = re.sub(r'\W', ' ',new_text)
new_text = re.sub(r'\d', ' ',new_text)
new_text = re.sub(r'\s+',' ', new_text)

#แบ่งบทความเป็นแต่ละประโยค
sentences = nltk.sent_tokenize(text)

cutting_words = nltk.corpus.stopwords.words('english')

count_each_word = {}
for word in nltk.word_tokenize(new_text):
    if word not in cutting_words:
        if word not in count_each_word.keys():
            count_each_word[word] = 1
        else:
            count_each_word[word] += 1
        
#หา weignt  
for key in count_each_word.keys():
    count_each_word[key] = count_each_word[key]/max(count_each_word.values())

join_score = {}
for sentence in sentences:
    #wordtokenize แบ่ง sentence เป็น แต่ละคำ
    for word in nltk.word_tokenize(sentence.lower()):
        if word in count_each_word.keys():
            if sentence not in join_score.keys():
                join_score[sentence] = count_each_word[word]
            else:
                join_score[sentence] += count_each_word[word]
    