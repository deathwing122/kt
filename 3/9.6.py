import requests

url = "https://jsonplaceholder.typicode.com/posts/66"

response = requests.get(url)

data = response.json()

print(data)
print(response)

input()