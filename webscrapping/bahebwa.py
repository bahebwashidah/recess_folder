import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def fetch_bird_species_data(page_num):
    url = f"https://xeno-canto.org/explore?query=grp%3Abirds&pg={page_num}&dir=0&order=en"

    # Fetch the content from the website
    response = requests.get(url)
    if response.status_code != 200:
        return None

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract bird species, family, and more information from the website
    # Add your code here to locate and extract the relevant information

    # Return the extracted data as a list of dictionaries
    return bird_species_data

# Define the main function to fetch data from multiple pages and save to CSV and JSON
def main():
    all_bird_species_data = []
    total_pages = 10  # Set the total number of pages to fetch (adjust as needed)

    # Fetch data from each page and append to the main list
    for page_num in range(1, total_pages + 1):
        page_data = fetch_bird_species_data(page_num)
        if page_data:
            all_bird_species_data.extend(page_data)

    # Convert the data to a DataFrame
    df = pd.DataFrame(all_bird_species_data)

    # Save the data to a CSV file
    df.to_csv("bird_species_data.csv", index=False)

    # Save the data to a JSON file
    with open("bird_species_data.json", "w") as json_file:
        json.dump(all_bird_species_data, json_file, indent=4)

if __name__ == "__main__":
    main()



        


