import requests, os, json
# curl --request POST \
#       --url https://deep-image.ai/rest_api/deep_image/transform \
#       --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
#       --header 'x-api-key: dacba010-f071-11ea-a2f8-e77afd882aa5' \
#       --header 'x-application-name: deep_image' \
#       --form donald.jpg=@/path_to_local_file \
#       --form transformations=ganzoom2

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "output/out.jpg"
abs_file_path = os.path.join(script_dir, rel_path)

# Read the api key in the api-key-tweeter.txt
with open(script_dir + "/api-key-deepai.txt", "r") as api_key_file:     #get credentials from json
	api_key = json.load(api_key_file)

headers={api_key,
         'x-application-name': 'deep_image',
         'fileName': abs_file_path
         }

r = requests.post( url = "https://deep-image.ai/rest_api/deep_image/transform",
                   headers = headers
                   )

response = r.json()
print(response)