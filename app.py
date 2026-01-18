import os
import requests

# Njibou el Key men el system (security khouya)
api_key = os.getenv("GEMINI_API_KEY")

def start_ai(command):
    if not api_key:
        return "❌ Error: API Key is missing f Termux!"
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": f"Act as a video automation assistant. User wants: {command}. Explain what ffmpeg command is needed briefly."}]}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ Error: {e}"

def main():
    print("--- 🚀 PlainEnglish-AI + Gemini (Light) v1.0 ---")
    user_cmd = input("What do you want to do? ")
    print("\n🤖 Gemini is thinking...")
    print(start_ai(user_cmd))

if __name__ == "__main__":
    main()

