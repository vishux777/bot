import requests

MISTRAL_API_KEY = "Ynd1YZuLjwM02OPQVs3wInK4dNtXwFbT"
MISTRAL_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {MISTRAL_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "mistral-tiny",
    "messages": [{"role": "user", "content": "Categorize this expense: Bought a pizza"}],
    "temperature": 0.5
}

response = requests.post(MISTRAL_ENDPOINT, json=payload, headers=HEADERS)

print(response.status_code)  # Should be 200 if working
print(response.json())       # Should return JSON response
