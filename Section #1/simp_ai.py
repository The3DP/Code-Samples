"""
Improved NLTK-based simple chatbot with better structure and error handling.
"""

import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download required NLTK packages (silent mode to avoid clutter)
def download_nltk_data():
    """Download required NLTK data files."""
    required_packages = ['punkt', 'stopwords', 'averaged_perceptron_tagger']
    for package in required_packages:
        try:
            nltk.download(package, quiet=True)
        except Exception as e:
            print(f"Warning: Could not download {package}: {e}")

download_nltk_data()

# Predefined responses and keywords
RESPONSES = {
    "greeting": [
        "Hello!", 
        "Hi there!", 
        "Hey! How can I help?",
        "Greetings!"
    ],
    "farewell": [
        "Goodbye!", 
        "See you later!", 
        "Take care!",
        "Have a great day!"
    ],
    "default": [
        "Sorry, I didn't understand that.", 
        "Can you rephrase?", 
        "I'm not sure I understand. Can you elaborate?",
        "Tell me more about that."
    ]
}

# Keywords for intent recognition
KEYWORDS = {
    "greeting": ["hello", "hi", "hey", "greetings", "howdy"],
    "farewell": ["goodbye", "bye", "see you", "farewell", "exit", "quit"],
}

def preprocess_text(text):
    """
    Preprocess input text by converting to lowercase, tokenizing, and removing stopwords.
    
    Args:
        text (str): Input text to preprocess
        
    Returns:
        list: Tokens after removing stopwords and punctuation
    """
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords and punctuation
    filtered_tokens = [
        token for token in tokens 
        if token not in stop_words and token not in string.punctuation
    ]
    
    return filtered_tokens

def recognize_intent(user_input):
    """
    Recognize user intent from input text.
    
    Args:
        user_input (str): User's input text
        
    Returns:
        str: Detected intent ('greeting', 'farewell', or 'default')
    """
    tokens = preprocess_text(user_input)
    
    # Check for greeting
    if any(token in KEYWORDS["greeting"] for token in tokens):
        return "greeting"
    
    # Check for farewell
    if any(token in KEYWORDS["farewell"] for token in tokens):
        return "farewell"
    
    return "default"

def get_response(intent):
    """
    Get a random response for the given intent.
    
    Args:
        intent (str): The detected intent
        
    Returns:
        str: A random response from the intent category
    """
    return random.choice(RESPONSES.get(intent, RESPONSES["default"]))

def extract_keywords(text, num_keywords=5):
    """
    Extract the most common meaningful keywords from text.
    
    Args:
        text (str): Input text
        num_keywords (int): Number of keywords to extract
        
    Returns:
        list: Most common keywords
    """
    tokens = preprocess_text(text)
    
    if not tokens:
        return []
    
    # Count token frequency and get top keywords
    counter = Counter(tokens)
    return counter.most_common(num_keywords)

def run_chatbot():
    """Main chatbot loop."""
    print("Chatbot: Hi! Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Recognize intent and generate response
            intent = recognize_intent(user_input)
            response = get_response(intent)
            
            print(f"Chatbot: {response}\n")
            
            # Exit if farewell detected
            if intent == "farewell":
                break
                
        except KeyboardInterrupt:
            print("\n\nChatbot: Goodbye!")
            break
        except Exception as e:
            print(f"Error processing input: {e}\n")

if __name__ == "__main__":
    run_chatbot()
