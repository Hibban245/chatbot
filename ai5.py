
import google.auth
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import google.auth
from googleapiclient.discovery import build
import tkinter as tk
def preprocess_text(input1):
    input1 = input1.lower()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(input1)
    filtered_tokens = [token for token in tokens if token not in stop_words and token.isalnum()]
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return lemmas
def generate_response(input1):
    lemmas = preprocess_text(input1)
    if "hello" in lemmas:
        return "Hello! How are you doing?"
    elif "how" in lemmas and "you" in lemmas:
        return "I'm doing well. How about you?"
    
    else:
        # Replace YOUR_API_KEY with your actual API key
        api_key = 'AIzaSyBf9gYscT4iTQybzR2M48uEM7_XCbojO8A'
        service = build('customsearch', 'v1', developerKey=api_key)
        query = input1
        response = service.cse().list(q=query, cx='81546eac52fcd4195').execute()
        return response['items'][0]['link']
def process_input(input1):
  lemmas = preprocess_text(input1)
  response = generate_response(input1)
  return response
def process_input_and_display_output():
    input1 = text_field.get()
    response = process_input(input1)
    output_label.config(text=response)
window = tk.Tk()
window.title("AI Assistant")
label = tk.Label(text="Enter your query:")
label.pack()
text_field = tk.Entry()
text_field.pack()
submit_button = tk.Button(text="Submit", command=process_input_and_display_output)
submit_button.pack()
output_label = tk.Label(text="")
output_label.pack()
window.mainloop()
