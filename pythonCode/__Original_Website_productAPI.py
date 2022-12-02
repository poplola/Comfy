
import requests
import json

# response = requests.get("https://course-api.com/javascript-store-products")
response = requests.get("https://course-api.com/javascript-store-single-product?id=rec43w3ipXvP28vog")
json_response = response.json()
pretty_response = json.dumps(json_response, indent=4)

# You could also write:
pretty_response = json.dumps(response.json(), indent=4)

print(pretty_response)
print(len(pretty_response))