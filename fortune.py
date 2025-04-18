# fortune.py (v1.0)

print("🔮 Welcome to Vaibhav Kalkani's Fortune Teller (21JE1015) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Vaibhav! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Every storm passes—better days are coming. ✨")
elif mood == "neutral":
    print("✨ Your fortune: An ordinary day hides extraordinary moments. ✨")
else:
    print("Hmm... that's a unique feeling! Try again later.")
