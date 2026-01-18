def main():
    print("--- 🚀 QuickTools AI v1.0 ---")
    user_cmd = input("What do you want to do? (e.g., make tiktok): ").lower()
    
    if "tiktok" in user_cmd:
        print("✅ Action: Preparing TikTok Video Automation...")
    elif "audio" in user_cmd:
        print("✅ Action: Extracting Audio...")
    else:
        print("✅ Action: Command received. Starting AI processing.")

if __name__ == "__main__":
    main()
