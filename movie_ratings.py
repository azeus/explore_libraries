import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta

# OMDb API Key
OMDB_API_KEY = "YOUR_OMDB_API_KEY"


def get_movies(year, month, debug=True):
    """
    Get movies released in a specific month and year from Wikipedia.
    """
    month_names = {
        1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL",
        5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
        9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER"
    }

    url = f"https://en.wikipedia.org/wiki/List_of_American_films_of_{year}"
    if debug:
        print(f"Accessing URL: {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', class_='wikitable sortable')
        movies = []
        target_month = month_names[month]

        for table in tables:
            rows = table.find_all('tr')[1:]
            current_month = None

            for row in rows:
                month_cell = row.find('th', {'rowspan': True})
                if month_cell:
                    current_month = month_cell.get_text().strip().upper()
                    continue

                if current_month and target_month in current_month:
                    cells = row.find_all(['td'])
                    if len(cells) >= 3:
                        movie_info = {
                            'number': cells[0].get_text().strip() if cells[0] else '',
                            'title': cells[1].get_text().strip() if cells[1] else '',
                            'production': cells[2].get_text().strip() if cells[2] else '',
                            'cast_crew': cells[3].get_text().strip() if len(cells) > 3 else 'N/A'
                        }
                        movies.append(movie_info)
        return movies

    except Exception as e:
        if debug:
            print(f"Error fetching data: {e}")
        return []


def fetch_movie_details_from_omdb(title):
    """
    Fetch movie details and ratings from OMDb API.
    """
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("Response") == "True":
            return {
                "IMDb Rating": data.get("imdbRating", "N/A"),
                "Rotten Tomatoes": next(
                    (rating["Value"] for rating in data.get("Ratings", []) if rating["Source"] == "Rotten Tomatoes"),
                    "N/A"),
                "Metacritic": next(
                    (rating["Value"] for rating in data.get("Ratings", []) if rating["Source"] == "Metacritic"), "N/A")
            }
        return {"IMDb Rating": "N/A", "Rotten Tomatoes": "N/A", "Metacritic": "N/A"}
    except Exception as e:
        print(f"Error fetching OMDb data for '{title}': {e}")
        return {"IMDb Rating": "N/A", "Rotten Tomatoes": "N/A", "Metacritic": "N/A"}


def print_movies_with_ratings(movies):
    """Print the movie list with ratings."""
    if not movies:
        print("No movies found or unable to fetch data.")
        return

    print(f"\nFound {len(movies)} movies:\n")
    for movie in movies:
        ratings = fetch_movie_details_from_omdb(movie['title'])
        movie.update(ratings)
        print(f"Number: {movie['number']}")
        print(f"Title: {movie['title']}")
        print(f"Production: {movie['production']}")
        print(f"Cast and Crew: {movie['cast_crew']}")
        print(f"IMDb Rating: {movie['IMDb Rating']}")
        print(f"Rotten Tomatoes: {movie['Rotten Tomatoes']}")
        print(f"Metacritic: {movie['Metacritic']}")
        print("-" * 50)


# Main program
if __name__ == "__main__":
    # Get the date two months before the current date
    current_date = datetime.now()
    two_months_ago = current_date - relativedelta(months=2)
    year = two_months_ago.year
    month = two_months_ago.month

    print(f"Fetching movies released in {year}-{month:02d} (2 months ago)...")
    movies = get_movies(year, month, debug=True)
    print_movies_with_ratings(movies)