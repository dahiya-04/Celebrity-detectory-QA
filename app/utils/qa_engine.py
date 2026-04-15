import os
import requests

class QAEngine:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "meta-llama/llama-4-scout-17b-16e-instruct"

    def ask_about_celebrities(self, name, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        prompt = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": f"You are a celebrity expert AI. Answer the following question about {name}:\n\n{question}"
                }
            ],
            "temperature": 0.3,
            "max_tokens": 512
        }
        response = requests.post(self.api_url, headers=headers, json=prompt)
        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content']
            return result
        return "Sorry, I couldn't retrieve the information at this time."