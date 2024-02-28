"""
Gov Jobs Safari Scraper

This script scrapes job data from a website and stores it in a MongoDB database.

Usage:
1. Set up a MongoDB server.
2. Create a .env file with the JOBS_URI environment variable.
3. Run the script.

Author: [Your Name]
"""

import pymongo
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

def scrapeData(url, db):
    """
    Scrapes job data from the specified URL and stores it in a MongoDB database.

    Args:
    - url (str): The URL of the website to scrape.
    - db: The MongoDB database object.

    Returns:
    - None
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assuming each job table has a common class, modify as needed
        job_tables = soup.find_all('table', class_='lattbl')

        for _, table in enumerate(job_tables):
            category = getCategory(table)
            job_data = processTable(table)
            storeInDB(db, category, job_data)

       
    else:
        print(f"Error: Unable to fetch data from {url}. Status Code: {response.status_code}")

def getCategory(table):
    """
    Extracts the category of jobs from the HTML table.

    Args:
    - table: BeautifulSoup object representing an HTML table.

    Returns:
    - str: The category of jobs.
    """
    heading = table.find_previous('h4', class_='latsec')
    if heading:
        return heading.text.strip()
    else:
        return 'Uncategorized'

def storeInDB(db, collection_name, data):
    """
    Stores job data in the specified MongoDB collection.

    Args:
    - db: The MongoDB database object.
    - collection_name (str): The name of the collection.
    - data: List of job data dictionaries.

    Returns:
    - None
    """
    # Get or create the MongoDB collection
    collection = db[collection_name]

    # Insert the data into the collection
    collection.insert_many(data)

def processTable(table):
    """
    Processes an HTML table and extracts job data.

    Args:
    - table: BeautifulSoup object representing an HTML table.

    Returns:
    - list: List of dictionaries containing job details.
    """
    rows = table.find_all('tr')

    table_data = []

    for row in rows:
        # Process each cell in the row
        cells = row.find_all('td')

        # Check if there are enough cells in the row
        if len(cells) >= 6:
            # Extracting information based on the position of the data in the row
            post_date = cells[0].text.strip()
            bank_name = cells[1].text.strip()
            post_name = cells[2].text.strip()
            qualification = cells[3].text.strip()
            last_date = cells[5].text.strip()

            # Store the extracted information in a dictionary or any other data structure
            job_details = {
                "Post Date": post_date,
                "Bank Name": bank_name,
                "Post Name": post_name,
                "Qualification": qualification,
                "Last Date": last_date
            }

            # Append the dictionary to the list
            table_data.append(job_details)

    return table_data

def main():
    """
    Main function to run the scraper.
    """
    # Load environment variables from .env file
    load_dotenv()
    url = os.environ.get('JOBS_URI')

    if not url:
        print("Error: JOBS_URI environment variable not set.")
        return

    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['Gov_Jobs_Safari']

    scrapeData(url, db)

if __name__ == '__main__':
    main()
