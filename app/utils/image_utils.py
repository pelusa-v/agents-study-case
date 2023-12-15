import base64
import os

import requests


def get_text_from_image(path_image : str):
    """This function reads an image and returns the text found in it"""

    base64_image = encode_image(path_image)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv("OPENAI_API_KEY")}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Give me the text in the image"
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print("Searching text in image: " + path_image)
    print(response.json())


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

function_metadata = {
  "name": "get_text_from_image",
  "description": "This function reads an image and returns the text found in it",
  "parameters": {
      "type": "object",
      "properties": {
        "path_image": {
          "type": "string",
          "description": "local path of image to read"
        },
      }
  },
  "required": ["path_image"]
}