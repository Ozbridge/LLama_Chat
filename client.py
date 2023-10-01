import requests

# Get user input
user_input = input("Enter your prompt: ")

# Append the desired text to the user's input
prompt_with_quote = f"{user_input} answer using quotes from the bhagvad gita"

# Define the POST request payload
payload = {
    "prompt": prompt_with_quote,
    "n_predict": 128
}

# Send the POST request to 127.0.0.1:8080
url = "http://127.0.0.1:8080/completion"
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    print("Request successful.")
    print("Response:")
    print(response.json()['content'])
else:
    print(f"Request failed with status code {response.status_code}:")
    print(response.text)


