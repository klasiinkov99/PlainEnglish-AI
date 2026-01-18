import os
import google.generativeai as genai

# Njibou el Key men el system (security khouya)
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def start_ai(command):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Act as a video automation assistant. The user wants to: {command}. Explain what ffmpeg command is needed briefly.")
        return response.text
    except Exception as e:
        return f"Error: {e}"

def main():
    print("--- 🚀 PlainEnglish-AI + Gemini v1.0 ---")
    if not api_key:
        print("⚠️ Warning: No API Key found. Run 'export GEMINI_API_KEY=your_key' in Termux.")
        return
    
    user_cmd = input("What do you want to do? ")
    print("\n🤖 Gemini is thinking...")
    print(start_ai(user_cmd))

if __name__ == "__main__":
    main()
