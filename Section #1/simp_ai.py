pip install nltk

import nltk
import random
import string
from nltk.corpus import stopwords

# Download required NLTK packages
nltk.download('punkt')
nltk.download('stopwords')

# Predefined responses and keywords
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase?", "I'm n$
}

# Basic function to preprocess input text
