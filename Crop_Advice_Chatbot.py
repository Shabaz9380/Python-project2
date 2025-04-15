import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample corpus of text related to crop advice
corpus = [
    'For successful soybean cultivation in India, ensure warm weather and adequate rainfall, particularly in regions like Uttar Pradesh, Maharashtra, and Karnataka.',
    'To cultivate sugarcane effectively in India, focus on states like Uttar Pradesh, Maharashtra, and Karnataka, where it thrives well.',
    'Optimize cotton production in India by choosing suitable regions like Gujarat, Maharashtra, and Andhra Pradesh, known for their favorable conditions.',
    # Add more sentences here
]

# Sample intents
intents = {
    'soybean': ['soybean', 'soya', 'soybean cultivation'],
    'sugarcane': ['sugarcane', 'sugar cane cultivation'],
    'cotton': ['cotton', 'cotton production']
    # Add more intents and associated keywords here
}

# Tokenize the corpus
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
lemmatizer = nltk.stem.WordNetLemmatizer()

def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

corpus = [preprocess(sentence) for sentence in corpus]

# Extract features and labels for training the intent classifier
X_train = []
y_train = []
for intent, keywords in intents.items():
    for keyword in keywords:
        X_train.append(keyword)
        y_train.append(intent)

# Train the intent classifier
intent_classifier = make_pipeline(TfidfVectorizer(), MultinomialNB())
intent_classifier.fit(X_train, y_train)

# Vectorize the corpus using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Function to classify user input and get response
def get_response(user_input):
    user_input = preprocess(user_input)
    intent = intent_classifier.predict([user_input])[0]
    if intent not in intents:
        return "I'm sorry, I'm not sure how to respond to that."
    
    input_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(input_vector, X)
    most_similar_index = np.argmax(similarities)
    max_similarity = similarities[0, most_similar_index]
    if max_similarity < 0.001:  # Adjust threshold as needed
        return "No match found in the database."
    else:
        return corpus[most_similar_index]

# Main loop for the chatbot
print("Hello BOSS!! CROPER at your service. Ask me anything related to crops!")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("BOSS if you need any assistance regarding any crops in future, feel free to reach out.\nHave A Nice Day BOSS. BYE")
        break
    else:
        response = get_response(user_input)
        print("CROPER:", response)
