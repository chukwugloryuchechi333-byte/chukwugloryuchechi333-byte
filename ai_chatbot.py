# Glory's AI Chatbot - Day 8 - Week 2 Start!
import random
print("--- 🤖 GLORY'S RANDOM AI CHATBOT ---")

# AI Knowledge base (Week 1 + Week 2 combined)
responses = {
    "hello": ["Hello Glory! 🚀", "Hi boss! Ready for NVIDIA?", "Hey Ebonyi star! 🔥"],
    "how are you": ["I am amazing because you built me!", "Powered by Glory's 8% battery 😅", "Ready to work at Tesla!"],
    "dream": ["NVIDIA is waiting for you!", "Tesla will hire you soon!", "Your dream is VALID!"],
    "bye": ["Bye Glory! See you at NVIDIA!", "Shutting down... but your dream continues!", "Goodbye star!"]
}

jokes = [
    "Why did Python cross the road? To get to NVIDIA! 😂",
    "Your battery at 8% has more energy than my code! 🔋",
    "Glory's code is so clean, Tesla wants to hire it!"
]

print("Chat with your AI! Type 'bye' to exit, 'joke' for joke")
print("-" * 40)

while True:
    user = input("\nYou: ").lower()

    if user == "bye":
        print(f"AI: {random.choice(responses['bye'])}")
        break
    elif "hello" in user or "hi" in user:
        print(f"AI: {random.choice(responses['hello'])}")
    elif "how are you" in user:
        print(f"AI: {random.choice(responses['how are you'])}")
    elif "dream" in user or "nvidia" in user or "tesla" in user:
        print(f"AI: {random.choice(responses['dream'])}")
    elif "joke" in user:
        print(f"AI: {random.choice(jokes)}")
    else:
        print(f"AI: Hmm, '{user}'? Tell me more! I am learning from you Glory!")
        print(f"AI: Try saying hello, dream, or joke!")

print("\n--- Day 8 Complete! You built Chatbot AI! ---")
