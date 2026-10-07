"""Download the MovieLens small dataset into the data/ folder."""
import urllib.request
import zipfile
from pathlib import Path

URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
ZIP_PATH = DATA_DIR / "ml-latest-small.zip"

def main():
    DATA_DIR.mkdir(exist_ok=True)
    if (DATA_DIR / "ml-latest-small").exists():
        print("Data already downloaded.")
        return
    print("Downloading MovieLens...")
    urllib.request.urlretrieve(URL, ZIP_PATH)
    with zipfile.ZipFile(ZIP_PATH) as z:
        z.extractall(DATA_DIR)
    ZIP_PATH.unlink()
    print("Done. Files are in data/ml-latest-small/")

if __name__ == "__main__":
    main()
