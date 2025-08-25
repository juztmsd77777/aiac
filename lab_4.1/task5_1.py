def most_frequent_word(text):
    import string
    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find the most frequent word
    if not freq:
        return None
    max_count = max(freq.values())
    # In case of tie, return the first most frequent word in order of appearance
    for word in words:
        if freq[word] == max_count:
            return word
if __name__ == "__main__":
    user_input = input("Enter a paragraph: ")
    result = most_frequent_word(user_input)
    if result:
        print(f"The most frequent word is: {result}")
    else:
        print("No words found in the input.")

