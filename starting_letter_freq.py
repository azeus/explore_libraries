import re
from collections import Counter
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.words = self._preprocess_text()
        self.letter_frequencies = self._calculate_frequencies()

    def _preprocess_text(self) -> List[str]:
        """
        Preprocess the text by splitting into words and removing special characters
        """
        # Split text into words and remove empty strings
        words = [word.strip() for word in re.split(r'\s+', self.text) if word.strip()]
        # Only keep words that start with letters
        return [word for word in words if word and word[0].isalpha()]

    def _calculate_frequencies(self) -> Dict[str, int]:
        """
        Calculate the frequency of each starting letter
        """
        # Get first letter of each word and convert to uppercase
        first_letters = [word[0].upper() for word in self.words]
        return dict(Counter(first_letters))

    def get_frequencies_sorted(self) -> List[Tuple[str, int]]:
        """
        Get frequencies sorted by count in descending order
        """
        return sorted(self.letter_frequencies.items(), key=lambda x: x[1], reverse=True)

    def print_analysis(self):
        """
        Print detailed analysis of the text
        """
        total_words = len(self.words)
        print(f"\nTotal words analyzed: {total_words}")
        print("\nStarting Letter Frequencies:")
        print("-" * 30)

        # Print frequencies with percentages
        for letter, count in self.get_frequencies_sorted():
            percentage = (count / total_words) * 100
            print(f"{letter}: {count} words ({percentage:.1f}%)")

    def plot_frequencies(self, title: str = "Starting Letter Frequencies"):
        """
        Create a bar plot of the letter frequencies
        """
        sorted_freq = self.get_frequencies_sorted()
        letters, counts = zip(*sorted_freq)

        plt.figure(figsize=(12, 6))
        plt.bar(letters, counts)
        plt.title(title)
        plt.xlabel("Starting Letter")
        plt.ylabel("Frequency")
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()


def analyze_text(text: str, plot: bool = True):
    """
    Main function to analyze text
    """
    analyzer = TextAnalyzer(text)
    analyzer.print_analysis()
    if plot:
        analyzer.plot_frequencies()


# Example usage
if __name__ == "__main__":
    sample_text = """
    As was common at the time, Julia Stephen did not believe in formal education for her daughters.[12] Virginia was educated in a piecemeal fashion by her parents: Julia taught her Latin, French, and history, while Leslie taught her mathematics. She also received piano lessons.[33][34] She also had unrestricted access to her father's vast library, exposing her to much of the literary canon.[35] This resulted in a greater depth of reading than any of her Cambridge contemporaries.[36] Later, Virginia recalled:

Even today there may be parents who would doubt the wisdom of allowing a girl of fifteen the free run of a large and quite unexpurgated library. But my father allowed it. There were certain facts – very briefly, very shyly he referred to them. Yet "Read what you like", he said, and all his books...were to be had without asking.[37]
Another source was the conversation of their father's friends, to whom she was exposed.[citation needed] Leslie Stephen described his circle as "most of the literary people of mark...clever young writers and barristers, chiefly of the radical persuasion...we used to meet on Wednesday and Sunday evenings, to smoke and drink and discuss the universe and the reform movement".[4]

From 1897 Virginia received private tuition in Latin and Ancient Greek. One of her tutors was Clara Pater, and another was Janet Case, with whom she formed a lasting friendship and who involved her in the suffrage movement.[38] Virginia also attended a number of lectures at the King's College Ladies' Department.[39]

Although Virginia could not attend Cambridge, she was profoundly influenced by her brother Thoby's experiences there. When Thoby went to Trinity in 1899, he befriended a circle of young men, including Clive Bell, Lytton Strachey, Leonard Woolf (whom Virginia would later marry), and Saxon Sydney-Turner, to whom he would introduce his sisters at the Trinity May Ball in 1900.[40] These men formed a reading group they named the Midnight Society, which the Stephen sisters would later be invited to.[41]
    """

    analyze_text(sample_text)