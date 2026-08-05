# Word Frequency Counter in Python

def analyze_text(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    word_count = {}

    for word in words:
        # Strip simple punctuation characters
        cleaned_word = word.strip(".,!?;:")
        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    return word_count

if __name__ == "__main__":
    sample_text = "Python is a great language. Python is easy to learn and write!"
    print("Original Text:", sample_text)
    
    results = analyze_text(sample_text)
    print("\nWord Frequencies:")
    for word, count in results.items():
        print(f"'{word}': {count}")
