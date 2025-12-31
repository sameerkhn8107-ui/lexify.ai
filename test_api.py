import requests

url = "http://localhost:8000/api/chat"
headers = {"Content-Type": "application/json"}
data = {
    "messages": [{"role": "user", "content": "Hello"}],
    "model": "gpt-4o-mini"
}

response = requests.post(url, json=data, headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
