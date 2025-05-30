import requests
from openai import OpenAI

def call_llm(prompt, llm_key, llms):
    api_key = llms[llm_key]["api_key"]
    name = llms[llm_key]["name"]
    model = llms[llm_key].get("model", "")
    if "gemini" in name.lower():
        # Google Gemini API call (API key as query param)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "contents": [{"role": "user", "parts": [{"text": prompt}]}]
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "[No response]")
        else:
            return f"Error: {response.status_code} - {response.text}"
    elif "nvidia" in name.lower() or "nim" in name.lower():
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )

        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            top_p=0.7,
            max_tokens=4096,
            stream=False
        )
        return completion.choices[0].message.content
