query = "This is a sample text where we want to save the part after a specific word."
word = "save"

# Split the text at the specific word
parts = query.split(word, 1)

# if len(parts) > 1:
query = parts[1].strip()

print(query)
