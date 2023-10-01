import streamlit as st
import requests

# Define the API endpoint URL
API_ENDPOINT = "http://127.0.0.1:8080/completion"

# Streamlit app title
st.title("LLAMA-Gita")

# Create a text input for the user to enter the prompt
prompt = st.text_input("Enter a prompt:")
prompt = f"{prompt} answer using quotes from the bhagvad gita"

# Define the POST request payload
payload = {
    "prompt": prompt,
    "n_predict": 512
}

# Create a button to trigger the API request
if st.button("Submit"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            # Make the API request
            response = requests.post(API_ENDPOINT, json=payload)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                result = response.json()  # Assuming the API returns JSON
                st.success("API request successful!")

                # Display the 'content' field from the JSON response
                content = result.get('content', '')
                st.text(content)  # Display the content as text
            else:
                st.error(f"API request failed with status code {response.status_code}")
