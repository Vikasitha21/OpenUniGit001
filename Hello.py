import requests

def download_file(url, local_filename):
    # Send a GET request to fetch the raw content
    try:
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Open a local file in write mode and save the content
            with open(local_filename, 'w') as file:
                file.write(response.text)
            print(f"File downloaded successfully and saved as {local_filename}")
        else:
            print(f"Failed to retrieve the file. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the raw file URL and the local filename
    file_url = 'https://raw.githubusercontent.com/anuraam/OpenUniGit001/main/SourceCodeForDashboard.txt'
    local_file = 'SourceCodeForDashboard.txt'

    # Download the file
    download_file(file_url, local_file)