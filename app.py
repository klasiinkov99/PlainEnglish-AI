import os
import requests

api_key = os.getenv("GEMINI_API_KEY")
user_credits = 1 

def start_ai(yt_link, task):
    if user_credits <= 0:
        return f"\n💳 OUT OF CREDITS!\nGet 50 more for $5: https://paypal.me/YOUR_USER\nSend screenshot to: your@email.com"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    prompt = f"Act as a professional American News Assistant. Summarize this: {yt_link}. Key points only."
    
    try:
        response = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]})
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "❌ Error: Service busy. Try again."

def main():
    global user_credits
    print(f"--- 🇺🇸 USA TIME-SAVER AI | Credits: {user_credits} ---")
    link = input("Paste Video Link: ")
    
    print("\n🤖 Processing for you...")
    res = start_ai(link, "summarize")
    print("\n" + res)
    
    if "https://paypal.me" not in res:
        user_credits -= 1
        print(f"\n✅ 1 Credit used. Remaining: {user_credits}")

if __name__ == "__main__":
    main()
