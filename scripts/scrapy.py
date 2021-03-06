from bs4 import BeautifulSoup
import requests
import json

# This script scrapes the website for the content of interest
page = requests.get("https://www.ncbi.nlm.nih.gov/pubmed/?term=vitamin+d3")

soup = BeautifulSoup(page.content, 'html.parser')

# this line grabs the NCBI search results (only 3 now sadly, the "best results") and returns text
text = soup.find_all('div', class_='sensor_content')[0].get_text()

# strings cleanup, returns a dict with title, year and author
arr = text.split("\n", 100)

arr = list(filter(None, arr))
arr.pop()

# TODO: There must be a way to get the link, without it the plan is foiled

# there must be more efficient way, but it must only work for now
data = {
    "first" : {"title": arr[0],
             "author": arr[1],
             "year": arr[2]},
    "second": {"title": arr[3],
             "author": arr[4],
             "year": arr[5]},
    "third" : {"title": arr[6],
             "author": arr[7],
             "year": arr[8]},
}
print(data)
# Saves a python dict object to JSON format file.
def python_dict_to_json_file(file_path):
    try:
        # Gets a file object with write permission.
        file_object = open(file_path, 'w')
        # Saves dict data into the JSON file.
        json.dump(data, file_object)
        print(file_path + " created. ")
    except FileNotFoundError:
        print(file_path + " not found. ")

if __name__ == '__main__':
    python_dict_to_json_file("./data.json")
