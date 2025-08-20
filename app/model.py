from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

#  training data
data = [("I love this product", "positive"),
        ("This is terrible", "negative"),
        ("I enjoy it", "positive"),
        ("I hate it", "negative")]

texts, labels = zip(*data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# here i save the model and vectorizer
pickle.dump((model, vectorizer), open("model.pkl", "wb"))
