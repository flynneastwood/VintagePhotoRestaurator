import requests, json, os, wget

# Path to images
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "images/photo01.jpg"
abs_file_path = os.path.join(script_dir, rel_path)

# Read the api key in the api-key.txt
with open(script_dir + "/api-key.txt", "r") as api_key_file:     #get credentials from json
	api_key = json.load(api_key_file)

r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open(abs_file_path, 'rb'),
    },
    headers=api_key
)

#print(r.json())
response = r.json()
url = response.get('output_url')

image_filename = wget.download(url, out=script_dir + "/output/" + "out.jpg")



