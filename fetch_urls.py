import csv
import requests
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='fetch_urls.log', level=logging.INFO, format='%(asctime)s - %(message)s')

CSV_FILE = 'urls.csv'

def read_urls_from_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row['url'] for row in reader if 'url' in row and row['url'].strip()]
    except Exception as e:
        logging.error(f"Error reading CSV: {e}")
        return []

def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)
        logging.info(f"Fetched {url} - Status: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Failed to fetch {url} - Error: {e}")
        

def main():
    logging.info("Starting URL fetch job")
    print("Starting URL fetch job")
    urls = read_urls_from_csv(CSV_FILE)
    for url in urls:
        fetch_url(url)
    logging.info("Finished URL fetch job")
    print("Finished URL fetch job")
    print("Please refer to fetch logs for details on fetch job!")

if __name__ == "__main__":
    main()