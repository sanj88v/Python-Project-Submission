import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of predefined genres
VALID_GENRES = [
    'Action', 'Adventure', 'Animation', 'Historical', 'Comedy',
    'Musical', 'Drama', 'War', 'Documentary'
]

# Function to map scraped genre to predefined genres
def map_genre(scraped_genre):
    genre_mapping = {
        'Action': 'Action',
        'Adventure': 'Adventure',
        'Animation': 'Animation',
        'Comedy': 'Comedy',
        'Drama': 'Drama',
        'Documentary': 'Documentary',
        'Historical': 'Historical',
        'Musical': 'Musical',
        'World War': 'War'
    }

    # Check if scraped genre matches any of the predefined genres directly
    for key, value in genre_mapping.items():
        if key.lower() in scraped_genre.lower():
            return value

    # If no direct match, map to the most appropriate genre
    for genre in VALID_GENRES:
        if genre.lower() in scraped_genre.lower():
            return genre

    return 'Action'  # Default to 'Action' if no match is found

# Function to scrape top movies from Box Office Mojo with genre
def scrape_top_movies_with_genre():
    try:
        url = "https://www.boxofficemojo.com/genre/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        print(f"Request status code: {response.status_code}")
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.content, 'html.parser')
        movies = []

        movie_items = soup.find_all('tr')

        for item in movie_items[1:]:
            columns = item.find_all('td')
            title = columns[3].text.strip()
            gross = columns[1].text.strip()
            genre = columns[0].text.strip()
            mapped_genre = map_genre(genre)
            movies.append({'title': title, 'gross': gross, 'genre': genre, 'Movie Genre': mapped_genre})
            print(f"Scraped movie: {title}, Gross: {gross}, Genre: {genre}, Mapped Genre: {mapped_genre}")

        return movies

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return []
    except Exception as e:
        print(f"Error occurred during scraping: {e}")
        return []

# Saving to CSV
def save_movies_to_csv(movies, filename="movies.csv"):
    try:
        if movies:
            df = pd.DataFrame(movies)
            df.to_csv(filename, index=False)
            print(f"Movies data saved to {filename} successfully.")
        else:
            print("No movies to save.")
    except Exception as e:
        print(f"Error occurred while saving to CSV: {e}")

def suggest_top_movies_by_genre(genre, movies):
    filtered_movies = [movie for movie in movies if genre.lower() in movie['Movie Genre'].lower()]

    if not filtered_movies:
        return f"No movies found for the genre: {genre}"

    sorted_movies = sorted(filtered_movies, key=lambda x: float(x['gross'].replace('$', '').replace(',', '')), reverse=True)[:5]

    return sorted_movies

if __name__ == "__main__":
    print("Starting movie scraping...")
    movies_data = scrape_top_movies_with_genre()

    if movies_data:
        save_movies_to_csv(movies_data, filename="top_movies.csv")
    else:
        print("No data scraped, nothing to save.")

    try:
        df = pd.read_csv("top_movies.csv")
    except FileNotFoundError:
        print("CSV file not found. Please run the scraping function first.")
        df = pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("CSV file is empty.")
        df = pd.DataFrame()
    except pd.errors.ParserError:
        print("Error parsing CSV file.")
        df = pd.DataFrame()

    if not df.empty:
        print("Available genres:")
        for i, genre in enumerate(VALID_GENRES, start=1):
            print(f"{i}. {genre}")

        while True:
            genre_choice = input("Please enter the genre of the movie you want to watch (e.g., Action, Comedy, Drama, Documentary): ").strip()

            if genre_choice not in VALID_GENRES:
                print(f"The genre '{genre_choice}' is not available in the dataset.")
                continue

            print(f"Searching for top 5 movies in {genre_choice}...")
            result = suggest_top_movies_by_genre(genre_choice, df.to_dict('records'))

            if isinstance(result, str):  # If result is a string, it's an error message
                print(result)
            else:
                print(f"\nTop 5 {genre_choice} movies based on gross collections:")
                for i, movie in enumerate(result, start=1):
                    print(f"{i}. {movie['title']} - Gross: {movie['gross']}")

            choice = input("\nDo you want to search for another genre? (yes/no): ").strip().lower()
            if choice != 'yes':
                break
    else:
        print("No movies data available.")
