import wikipedia
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from datetime import datetime

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_and_save_words(topic, min_length=3):
    try:
        # Fetch Wikipedia content
        wiki_page = wikipedia.page(topic)
        text = wiki_page.content

        # Tokenize and tag parts of speech
        tokens = word_tokenize(text)
        tagged_words = pos_tag(tokens)

        # Track categories for logging
        word_categories = {
            'nouns': set(),
            'verbs': set(),
            'adjectives': set(),
            'others': set()
        }

        # Set for all valid words
        all_valid_words = set()

        # Process words
        for word, tag in tagged_words:
            # Basic validation
            if (len(word) >= min_length and
                    word.isalnum() and
                    word.isascii() and
                    not word.isnumeric()):

                word = word.lower()
                all_valid_words.add(word)

                # Categorize for logging only
                if tag.startswith('NN'):
                    word_categories['nouns'].add(word)
                elif tag.startswith('VB'):
                    word_categories['verbs'].add(word)
                elif tag.startswith('JJ'):
                    word_categories['adjectives'].add(word)
                else:
                    word_categories['others'].add(word)

        # Save all words to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"words_{topic.replace(' ', '_')}_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            for word in sorted(all_valid_words):
                f.write(word + '\n')

        return filename, word_categories

    except wikipedia.exceptions.DisambiguationError as e:
        return None, f"Disambiguation Error: {e.options}"
    except wikipedia.exceptions.PageError:
        return None, "Error: Page not found"


if __name__ == "__main__":
    topic = "Ocean"
    filename, categories = extract_and_save_words(topic)

    if isinstance(categories, dict):
        print(f"\nWord extraction complete for theme: '{topic}'\n")
        print("Category Statistics:")
        print("-" * 50)

        for category, words in categories.items():
            print(f"\n{category.upper()} ({len(words)} words)")
            print(f"Sample: {', '.join(sorted(list(words))[:5])}...")

        total_words = sum(len(words) for words in categories.values())
        print(f"\n{'-' * 50}")
        print(f"Total unique words saved: {total_words}")
        print(f"Words saved to: {filename}")

    else:
        print(categories)  # Print error message if any