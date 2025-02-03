import wikipedia
from collections import defaultdict
import time
import json
from bs4 import BeautifulSoup, GuessedAtParserWarning
import warnings

# Suppress the BeautifulSoup warning
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)


def explore_wiki_network(main_topic):
    """
    Comprehensively explores Wikipedia articles related to a main topic
    """
    results = defaultdict(list)
    explored = set()

    def safe_wiki_request(func, arg, max_retries=3):
        """Generic safe Wikipedia request with retry mechanism"""
        for attempt in range(max_retries):
            try:
                time.sleep(1)  # Rate limiting
                result = func(arg)
                # Handle case where result is a list (disambiguation)
                if isinstance(result, list):
                    return None
                return result
            except wikipedia.DisambiguationError as e:
                print(f"Disambiguation found for '{arg}', skipping...")
                return None
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"Error with '{arg}': {str(e)}")
                    return None
                time.sleep(2)
        return None

    def explore_article(title):
        """Explores a single article and its related links"""
        if title in explored:
            return None

        print(f"\nExploring: {title}")
        explored.add(title)

        # Get page content
        try:
            page = wikipedia.page(title, auto_suggest=False)
        except (wikipedia.DisambiguationError, wikipedia.PageError) as e:
            print(f"Skipping '{title}': {str(e)}")
            return None
        except Exception as e:
            print(f"Error exploring '{title}': {str(e)}")
            return None

        if not page:
            return None

        # Get categories
        try:
            categories = page.categories
        except:
            categories = []

        # Determine main category
        main_category = "General"
        for cat in categories:
            cat_lower = cat.lower()
            if main_topic.lower() in cat_lower:
                main_category = cat.replace("Category:", "").strip()
                break

        # Store article information
        article_info = {
            "title": page.title,
            "url": page.url,
            "summary": page.summary[:200] + "..." if page.summary else "No summary available",
            "categories": categories[:5] if categories else []
        }

        results[main_category].append(article_info)

        try:
            return page.links
        except:
            return []

    # Start with main topic exploration
    print(f"Starting exploration of {main_topic}...")

    # First get the main topic page
    main_page = safe_wiki_request(wikipedia.page, main_topic)
    if main_page:
        main_links = explore_article(main_topic)

        if main_links:
            # Explore related topics
            total_explored = 0
            for link in main_links:
                if total_explored >= 50:  # Limit to prevent too many requests
                    break

                if (main_topic.lower() in link.lower() and
                        link not in explored and
                        not any(skip in link.lower() for skip in ['list of', 'index of', 'template:'])):
                    explore_article(link)
                    total_explored += 1
                    print(f"Progress: {total_explored}/50 articles explored")

    return dict(results)


def save_results(results, topic):
    """Save results to a JSON file"""
    filename = f"{topic.lower()}_wiki_network_{time.strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    return filename


def print_results(results):
    """Print results in a readable format"""
    total_articles = sum(len(articles) for articles in results.values())
    print("\n" + "=" * 80)
    print(f"Total articles found: {total_articles}")
    print(f"Total categories discovered: {len(results)}")
    print("=" * 80)

    for category, articles in sorted(results.items()):
        print(f"\n{category.upper()} ({len(articles)} articles):")
        print("-" * 40)
        for article in articles[:5]:  # Show first 5 articles per category
            print(f"\n• {article['title']}")
            print(f"  {article['summary'][:200]}...")
        if len(articles) > 5:
            print(f"\n  ... and {len(articles) - 5} more articles")


if __name__ == "__main__":
    main_topic = "France"
    print(f"Starting comprehensive exploration of Wikipedia articles related to {main_topic}...")

    results = explore_wiki_network(main_topic)

    # Save results
    filename = save_results(results, main_topic)
    print(f"\nResults saved to {filename}")

    # Print results
    print_results(results)