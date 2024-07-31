import io
import os
import zipfile

import requests


def download_github_repo(repo_url, destination_folder):
    # Extract the username and repo name from the URL
    _, _, _, username, repo_name = repo_url.rstrip("/").split("/")

    # Construct the API URL for the repo
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/zipball/master"

    # Send a GET request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        # Create a ZipFile object from the response content
        z = zipfile.ZipFile(io.BytesIO(response.content))

        # Extract all contents to the destination folder
        z.extractall(destination_folder)

        # Get the name of the extracted folder (it usually includes the commit hash)
        extracted_folder = z.namelist()[0].split("/")[0]

        print(
            f"Repository downloaded and extracted to: {os.path.join(destination_folder , extracted_folder)}"
        )
    else:
        print(f"Failed to download repository. Status code: {response.status_code}")


# Example usage
repo_url = "https://github.com/coq-community/exact-real-arithmetic"
destination_folder = "community_repo"

download_github_repo(repo_url, destination_folder)
