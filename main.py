import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords # Import the stop words list which is used to remove common words like “the” or “a”

response = urllib.request.urlopen("https://en.wikipedia.org/wiki/Bitcoin")
html = response.read()
print(html) #TO print the elements along with the tag
 
soup = BeautifulSoup(html, "html5lib")# Used toremove the html tags
text = soup.get_text(strip=True)
print(text)
tokens =[t for t in text.split()] # To split the words(Spliting is based on the space)
print(tokens)

sr = stopwords.words('english') # To remove the common words(is,was ,the ,a ,an etc)
clean_tokens = tokens[:]# To remove the common words
for token in tokens:
    if token in sr:
        clean_tokens.remove(token)
#print(clean_tokens)

freq = nltk.FreqDist(clean_tokens)# To find the frequency
for key, value in freq.items():# To print the frequency
    print(key, ":", value)
freq.plot(20)# To plot the frequency
import matplotlib.pyplot as plt 

# ... (rest of your code remains the same)

freq = nltk.FreqDist(clean_tokens)
for key, value in freq.items():
    print(key, ":", value)

# Plot the top 20 most frequent tokens
top_20 = freq.most_common(20)
labels, values = zip(*top_20)
plt.bar(labels, values)
plt.xlabel('Token')
plt.ylabel('Frequency')
plt.title('Top 20 Most Frequent Tokens')
plt.show()