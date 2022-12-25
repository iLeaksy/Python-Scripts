import requests
import bs4

def find_script_links(script_name):
  # Replace spaces in the script name with "+" for use in the search query
  query = script_name.replace(" ", "+")
  # Set the URL for the search query
  url = f"https://www.google.com/search?q=download+fivem+script+{query}"
  
  # Send a GET request to the URL
  response = requests.get(url)
  
  # Check the status code of the response
  if response.status_code != 200:
    print("Error: Could not retrieve search results")
    return []
  
  # Parse the HTML of the response
  soup = bs4.BeautifulSoup(response.text, "html.parser")
  
  # Find all the links in the search results
  links = soup.find_all("a")
  
  # Filter the links to only those that contain "download" in the text
  download_links = [link for link in links if "download" in link.text.lower()]
  
  # Extract the href attribute from each link and return the list of URLs
  return [link["href"] for link in download_links]

# Prompt the user for a script name
script_name = input("Enter the name of the FiveM script you are looking for: ")

# Find the download links for the script
links = find_script_links(script_name)

# Print the links
for i, link in enumerate(links):
  print(f"Link {i+1}: {link}")