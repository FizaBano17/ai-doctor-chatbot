# doctor.py
from speech import get_voice_input
from chat import medical_chat
from vision import analyze_image

def main():
    print("\n🤖 AI Doctor (Free stack)")
    print("1 = Text question")
    print("2 = Voice question (record mic)")
    print("3 = Image diagnosis\n")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        text = input("Your question: ")
        print("\n🩺 Thinking...")
        reply = medical_chat(text)
        print("\n🩺 AI Doctor:", reply)

    elif choice == "2":
        dur = input("Recording seconds (default 5): ").strip()
        try:
            dur = float(dur) if dur else 5.0
        except:
            dur = 5.0
        voice_text = get_voice_input(duration=dur)
        if not voice_text:
            print("No transcription. Try again.")
            return
        print("\n🩺 Asking AI...")
        reply = medical_chat(voice_text)
        print("\n🩺 AI Doctor:", reply)

    elif choice == "3":
        path = input("Enter image path (e.g., acne.jpg): ").strip()
        try:
            print("🩺 Analyzing image...")
            result = analyze_image(path)
            print("\n🩺 Diagnosis:", result)
        except Exception as e:
            print("Error calling vision API:", e)
            print("Check GROQ_KEY, model name and package version.")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


