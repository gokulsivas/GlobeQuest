import requests

# URL of the webpage you want to save
url = "https://www.veenaworld.com/world"  # Replace with the URL of your target website

# Make a request to get the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open a file in write mode with UTF-8 encoding
    with open("webpage.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Webpage saved as webpage.html")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
