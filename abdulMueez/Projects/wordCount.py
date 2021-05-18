# Ask user for input
sentence = str(input(" Tell me about your day : "))

# Using split to count words in sentence
count = len(sentence.split())
print ("That's great, you just told me about your day in", count, "words.")