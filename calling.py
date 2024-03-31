
"""
systemctl stop ollama.service
ollama serve
ollama run zephyr
ngrok http
ngrok http 11434
"""

# import requests
# url = "https://84da-103-207-171-178.ngrok-free.app/api/generate"

# user_input="What is a headphone?"


# data = f'''{
#   "model": "mistral",
#   "prompt": "{user_input}",
#   "stream": false
# }'''
# response = requests.post(url, data=data)

# if response.status_code == 200:
#     # Request was successful
#     data = response.json()
#     data = data['response']  # If the response contains JSON data
#     print(data)
# else:
#     # Request failed
#     print(f"Error: {response.status_code}")
#     print(response.text)  # Print the response content for debugging purposes

import requests

url = "https://dfb7-223-190-244-97.ngrok-free.app/api/generate"

def ask(txt):

    data = {
        "model": "mylord",
        "prompt": txt,
        "stream": False
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        # Request was successful
        data = response.json()
        data = data['response']  # If the response contains JSON data
        # print(txt)
        # print(data)
        return data
    else:
        # Request failed
        print(f"Error: {response.status_code}")
        print(response.text)  # Print the response content for debugging purposes

if __name__=="__main__":
    print("")
    # while True:
    #     a=input(" : ")
    #     print(ask(a))