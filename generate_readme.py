import os
import requests
from pathlib import Path

# GitHub repo details
GITHUB_USER = "Fanu2"
REPO = "my-colab-notebooks"
BRANCH = "main"  # or "master"

# Local download directory
LOCAL_DIR = Path.home() / "my-colab-notebooks"
LOCAL_DIR.mkdir(exist_ok=True, parents=True)

# Maximum notebooks per folder
MAX_PER_FOLDER = 5

# Markdown README file
README_FILE = LOCAL_DIR / "README.md"

# GitHub API URL to list repo contents
API_URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO}/contents"

def fetch_notebooks(url, category_path=""):
    notebooks = {}
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching {url}: {response.status_code}")
        return notebooks

    items = response.json()
    for item in items:
        if item["type"] == "file" and item["name"].endswith(".ipynb"):
            folder = category_path or "Misc"
            notebooks.setdefault(folder, []).append(item["download_url"])
        elif item["type"] == "dir":
            sub_folder = item["name"]
            sub_url = item["url"]
            sub_notebooks = fetch_notebooks(sub_url, sub_folder)
            for k, v in sub_notebooks.items():
                notebooks.setdefault(k, []).extend(v)
    return notebooks

def download_notebooks(notebooks_dict):
    """
    Download notebooks and collect info for Markdown README
    Returns dict: {folder: [(filename, colab_url)]}
    """
    md_data = {}
    for folder, urls in notebooks_dict.items():
        folder_dir = LOCAL_DIR / folder
        folder_dir.mkdir(exist_ok=True)
        md_data.setdefault(folder, [])
        for url in urls[:MAX_PER_FOLDER]:
            filename = url.split("/")[-1]
            local_file = folder_dir / filename
            if not local_file.exists():
                print(f"Downloading {filename} to {folder_dir}")
                r = requests.get(url)
                with open(local_file, "wb") as f:
                    f.write(r.content)
            else:
                print(f"Skipping existing file: {local_file}")
            github_path = f"{folder}/{filename}" if folder != "Misc" else filename
            colab_url = f"https://colab.research.google.com/github/{GITHUB_USER}/{REPO}/blob/{BRANCH}/{github_path}"
            md_data[folder].append((filename, colab_url))
    return md_data

def generate_markdown(md_data):
    lines = ["# My Colab Notebooks\n"]
    for folder in sorted(md_data.keys()):
        lines.append(f"## {folder}\n")
        for filename, link in md_data[folder]:
            lines.append(f"- [{filename}]({link})")
        lines.append("\n")
    with open(README_FILE, "w") as f:
        f.write("\n".join(lines))
    print(f"✅ Markdown README generated at {README_FILE}")

def main():
    print(f"Fetching notebooks from {GITHUB_USER}/{REPO}...")
    notebooks = fetch_notebooks(API_URL)
    print("Download plan per category:")
    for k, v in notebooks.items():
        print(f" - {k}: {len(v)} notebooks found")
    md_data = download_notebooks(notebooks)
    generate_markdown(md_data)
    print("✅ All done! You can now browse notebooks via the Markdown README.")

if __name__ == "__main__":
    main()
