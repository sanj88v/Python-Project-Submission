Index:
- Project Overview: Provides a high-level view of what the project does.
- Getting Started: Guides the user on what they need to get the project running.
- How It Works: Explains the logic and flow of the application.
- Usage: Demonstrates how to use the application with an example.
- Error Handling: Describes how the application manages potential errors.

Project Overview:
- The application fetches movie data, including the title, gross earnings, and genre, from Box Office Mojo. It then maps the scraped genres to predefined genres and saves the data to a CSV file. Users can request the top 5 movies in a specific genre, and the application will provide recommendations based on gross earnings.

Features
- Scrapes movie data from Box Office Mojo.
- Maps scraped genres to a list of predefined genres.
- Saves movie data to a CSV file.
- Allows users to get top movie recommendations by genre.

Getting Started
- Clone the reporitory: git clone https://github.com/your-username/top-movies-scraper.git
- Navigate to the project directory: cd top-movies-scraper
- Run the Script: python movies_suggestion.py

Prerequisites
- Ensure you have the following software installed using Python libraries using pip or pip3
- Python 3.x
- requests library
- beautifulsoup4  or bs4
- pandas

How It Works
- The script uses the requests library to fetch the HTML content of the Box Office Mojo website and BeautifulSoup to parse the HTML and extract movie data. The scraped data includes:
- Title: The name of the movie.
- Gross: The gross earnings of the movie.
- Genre: The genre of the movie.

Mapping Genres
- The scraped genres are mapped to a predefined list of genres to ensure consistency. The predefined genres include: Action, Adventure, Animation, Historical, Comedy, Musical, Drama, War & Documentary
- The movie data is saved to a CSV file named top_movies.csv using the pandas library. This file contains columns for the title, gross earnings, original genre, and mapped genre.

After running the script, follow the on-screen prompts:
- The script will scrape and save the movie data to a CSV file.
- The available genres will be displayed.
- Input the genre you want to explore (e.g., Action, Comedy, Drama).
- The script will output the top 5 movies in that genre based on gross earnings.

Screenshots
Example_1 Scraping Movie and saving in CSV: ![image](https://github.com/user-attachments/assets/d7fba25c-168a-4e23-8318-b1d60ca881ae)

Example_2 Top Movies showing for the selected Genre image: ![image](https://github.com/user-attachments/assets/9d5fa9a9-bee9-4fd4-8c68-04417f21def6)


Error Handling
The application includes error handling for:
- Network Issues: If the request to Box Office Mojo fails.
- File Handling: If there are issues reading or writing to the CSV file.
- User Input: If the user inputs a genre not available in the predefined list.

Conclusion
- This project showcases the power of Python for web scraping, data processing, and creating interactive applications. By integrating multiple Python libraries, the Movie Genre Recommendation System provides users with a simple yet effective tool to explore top movies across various genres.
