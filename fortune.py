# fortune.py (v1.1)
import random

print("🔮 Welcome to Vaibhav Kalkani's Fortune Teller (21JE1015) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "Great things await you, Vaibhav! Keep smiling.",
        "Your happiness is contagious—spread it around!"
    ],
    "sad": [
        "Every storm passes—better days are coming.",
        "It's okay to feel sad, Aryan. Brighter times are near."
    ],
    "neutral": [
        "An ordinary day hides extraordinary moments.",
        "Something unexpectedly joyful is around the corner."
    ],
    "stressed": [
        "Breathe, Aryan. You’ve got this!",
        "Even pressure makes diamonds. You’re stronger than you think."
    ]
}

if mood in fortunes:
    print("✨ Your fortune:", random.choice(fortunes[mood]), "✨")
else:
    print("Hmm... that's a unique feeling! Try again later.")
