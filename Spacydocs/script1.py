# Import the English Language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# Create by processing string of text with nlp object
doc = nlp('Hello there!')

# Iterate over tokens in a doc
for token in doc:
    print(token.text)

# Each entity in the document can be considered a token 
token = doc[1]

# Get the token via the text attribute
print(f"doc[1] = {token.text}")

# Span object - A slice from the Doc is a span object
span = doc[1:4]

# Get the span text via the .text attribute
print(f"Span from the doc: doc[1:4] = {span.text}")


