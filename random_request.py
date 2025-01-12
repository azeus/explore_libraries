import requests
import json
import os
from datetime import datetime
import schedule
import time
import logging
import random

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('image_fetcher.log'),
        logging.StreamHandler()
    ]
)


class WikimediaImageFetcher:
    def __init__(self, save_dir='downloaded_images'):
        self.save_dir = save_dir
        self.categories = [
            'Featured_pictures_on_Wikimedia_Commons',
            'Quality_images',
            'Featured_maps_on_Wikimedia_Commons',
            'Images_of_the_day',
            'Picture_of_the_day',
            'Valued_images_sorted_by_promotion_date'
        ]
        self.api_url = 'https://commons.wikimedia.org/w/api.php'
        self.headers = {
            'User-Agent': 'WikimediaImageFetcher/1.0 (https://github.com/yourusername/wikimedia-fetcher; your@email.com) Python/3.x requests/2.x',
        }

        # Create save directory if it doesn't exist
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

    def get_random_image(self):
        """Fetch a random image from specified categories"""
        # Randomly select a category
        category = random.choice(self.categories)

        params = {
            'action': 'query',
            'format': 'json',
            'list': 'categorymembers',
            'cmtitle': f"Category:{category}",
            'cmtype': 'file',
            'cmlimit': 50,  # Get multiple files to choose from
            'cmsort': 'timestamp',
            'cmdir': 'desc'
        }

        try:
            # Get list of files in category
            response = requests.get(self.api_url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            if 'query' not in data or 'categorymembers' not in data['query']:
                raise Exception("Invalid API response structure")

            # Get a random file from the results
            files = data['query']['categorymembers']
            if not files:
                raise Exception(f"No files found in category {category}")

            selected_file = random.choice(files)
            file_title = selected_file['title']

            # Get file information
            file_params = {
                'action': 'query',
                'format': 'json',
                'prop': 'imageinfo',
                'titles': file_title,
                'iiprop': 'url|extmetadata|size',
                'iiurlwidth': 1920  # Limit image size
            }

            file_response = requests.get(self.api_url, params=file_params, headers=self.headers)
            file_response.raise_for_status()
            file_data = file_response.json()

            # Extract image information
            pages = file_data.get('query', {}).get('pages', {})
            if not pages:
                raise Exception("No image information found")

            page = next(iter(pages.values()))
            if 'imageinfo' not in page or not page['imageinfo']:
                raise Exception("No image info available")

            image_info = page['imageinfo'][0]

            # Use thumbnailed URL if available, otherwise use original
            image_url = image_info.get('thumburl', image_info.get('url'))

            # Extract metadata
            metadata = image_info.get('extmetadata', {})
            description = metadata.get('ImageDescription', {}).get('value', 'No description available')
            author = metadata.get('Artist', {}).get('value', 'Unknown')
            license_info = metadata.get('License', {}).get('value', 'Unknown')

            return {
                'url': image_url,
                'title': file_title,
                'description': description,
                'author': author,
                'license': license_info,
                'category': category
            }

        except Exception as e:
            logging.error(f"Error fetching image: {str(e)}")
            return None

    def download_image(self, image_info):
        """Download the image and save it with metadata"""
        if not image_info:
            return False

        try:
            # Download image with headers
            response = requests.get(image_info['url'], headers=self.headers)
            response.raise_for_status()

            # Generate filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            file_extension = image_info['url'].split('.')[-1].split('?')[0]  # Handle URLs with parameters
            filename = f"wikimedia_{timestamp}.{file_extension}"
            filepath = os.path.join(self.save_dir, filename)

            # Save image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            # Save metadata
            metadata_filename = f"{filename}.json"
            metadata_filepath = os.path.join(self.save_dir, metadata_filename)
            with open(metadata_filepath, 'w', encoding='utf-8') as f:
                json.dump({
                    'title': image_info['title'],
                    'description': image_info['description'],
                    'author': image_info['author'],
                    'license': image_info['license'],
                    'category': image_info['category'],
                    'source_url': image_info['url'],
                    'download_date': timestamp
                }, f, indent=4, ensure_ascii=False)

            logging.info(f"Successfully downloaded image: {filename}")
            return True

        except Exception as e:
            logging.error(f"Error downloading image: {str(e)}")
            return False

    def fetch_daily_image(self):
        """Main function to fetch and download a daily image"""
        logging.info("Starting daily image fetch")
        max_attempts = 3

        for attempt in range(max_attempts):
            image_info = self.get_random_image()
            if image_info:
                success = self.download_image(image_info)
                if success:
                    logging.info("Daily image fetch completed successfully")
                    return

            logging.warning(f"Attempt {attempt + 1} of {max_attempts} failed")
            if attempt < max_attempts - 1:
                time.sleep(5)  # Wait 5 seconds before retry

        logging.error("Failed to fetch daily image after all attempts")


def main():
    # Create fetcher instance
    fetcher = WikimediaImageFetcher()

    # Schedule the job to run daily at midnight
    schedule.every().day.at("00:00").do(fetcher.fetch_daily_image)

    # Run once immediately
    fetcher.fetch_daily_image()

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()