# Topic: Dictionaries
# Example: Word frequency counter

feedback = "service is good support is good response is fast"
word_count = {}

# split() breaks the sentence into words.
for word in feedback.split():
    # get() returns existing count or 0 for a new word.
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
