from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training data
training_texts = [

    "financial fraud and cheating under IPC 420",

    "online scam and cyber fraud case",

    "murder and violent attack case",

    "property dispute in civil court",

    "bank fraud and fake transactions",

    "bail granted in civil dispute"
]

# Labels
# 1 = Fraud
# 0 = Non-Fraud

labels = [1, 1, 0, 0, 1, 0]

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(training_texts)

# Train ML model
model = LogisticRegression()

model.fit(X, labels)

def predict_case(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    probability = model.predict_proba(text_vector)[0]

    return prediction, probability