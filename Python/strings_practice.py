# 0
a=""
length=0
# The empty string has length zero

b= "it's ok"
length=7
# Python includes spaces (and punctuation) when counting string length

c='it\'s ok'
length=7
# Backslash is not part of the string, so it doesn't contribute to its length

d="""hey"""
length=3
# This string is exactly the same as 'hey'.

e='\n'
length=1
# The newline character is just a single character

# 1 
def is_valid_zip(zip_str):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_str) == 5 and zip_str.isdigit()

# 2
# str.split() str.lower() str.strip()
def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

# 3
def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

