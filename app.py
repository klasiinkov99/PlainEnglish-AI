import os
import requests

api_key = os.getenv("GEMINI_API_KEY")
user_credits = 1  # 1 Free Credit kima bghit

def start_ai(command, duration):
    if user_credits <= 0:
        return "❌ No credits left! Please pay via PayPal or RedotPay to continue."
    
    # Chart ta3 2 minutes
    if duration > 120:
        return "⚠️ Free Tier: Video must be under 2 minutes. Upgrade for longer videos!"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": f"User duration: {duration}s. Command: {command}. Explain what to do."}]}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ Error: {e}"

def main():
    global user_credits
    print(f"--- 🚀 PlainEnglish-AI | Credits: {user_credits} ---")
    
    duration = int(input("Video duration (in seconds): "))
    cmd = input("What do you want to do? ")
    
    print("\n🤖 Processing...")
    result = start_ai(cmd, duration)
    print(result)
    
    if "Processing" in result or "Gemini" in result:
        user_credits -= 1
        print(f"\n✅ Done! Remaining credits: {user_credits}")

if __name__ == "__main__":
    main()
