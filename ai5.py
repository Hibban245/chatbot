import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Function to preprocess the input text
def preprocess_text(input1):
    # Convert the input text to lowercase
    input1 = input1.lower()
    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(input1)
    filtered_tokens = [token for token in tokens if token not in stop_words and token.isalnum()]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    print(lemmas)
    return lemmas

# Function to generate a response based on the input
def generate_response(input1):
    lemmas = preprocess_text(input1)
    if "hello" in lemmas:
        return "Hello! How are you doing?"
    elif "how" in lemmas and "you" in lemmas:
        return "I'm doing well. How about you?"
    elif "weather" in lemmas:
        return "The weather is nice today."
    elif "name" in lemmas:
        return "My name is Hibban. What's yours?"
    elif "favorite" in lemmas and "color" in lemmas:
        return "My favorite color is blue."
    elif "favorite" in lemmas and "food" in lemmas:
        return "My favorite food is pizza."
    elif "favorite" in lemmas and "activity" in lemmas:
        return "My favorite activity is learning."
    elif "age" in lemmas:
        return "I'm an AI, so I don't have an age."
    elif "location" in lemmas:
        return "I'm a virtual assistant, so I don't have a physical location."
    elif "time" in lemmas:
        return "I'm not sure what time it is. I am an AI and do not have the ability to access the current time."
    elif "like" in lemmas:
        return "I am an AI and do not have the ability to experience emotions or likes or dislikes."
    elif "can" in lemmas and "you" in lemmas and "help" in lemmas:
        return "I am here to assist with answering questions and providing information on a wide variety of topics. Just ask me whatever is on your mind and I'll do my best to provide a helpful response."
    else:
        return "I'm not sure what you mean. Can you please elaborate?"

# Function to process user input and generate a response
def process_input(input1):
  # Preprocess the input
  lemmas = preprocess_text(input1)
  
  
