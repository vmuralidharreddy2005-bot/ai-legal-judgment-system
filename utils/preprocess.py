import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Process text using spaCy
    doc = nlp(text)

    cleaned_tokens = []

    for token in doc:

        # Remove stopwords and punctuation
        if not token.is_stop and not token.is_punct:

            # Convert words to root form
            cleaned_tokens.append(token.lemma_)

    return " ".join(cleaned_tokens)