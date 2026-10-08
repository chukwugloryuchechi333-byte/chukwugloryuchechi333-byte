# Glory's Smart AI Assistant - Day 7 - FINAL
print("--- 🤖 GLORY'S SMART AI ASSISTANT v1.0 ---")
print("Built in 7 days from Ebonyi to NVIDIA!")

# Knowledge (Day 5 - Dictionary)
assistant_profile = {
    "name": "Glory AI",
    "creator": "Chukwu Glory Uchechi",
    "version": "1.0",
    "mission": "Work at NVIDIA"
}

# Memory (Day 4 - List)
users = []

# Functions (Day 6)
def greet():
    print(f"\nHello! I am {assistant_profile['name']}")
    print(f"Created by {assistant_profile['creator']}")
    print(f"Mission: {assistant_profile['mission']}")

def add_user():
    name = input("Enter user name to remember: ")
    users.append(name)
    print(f"✅ AI memorized {name}. Total users: {len(users)}")

def show_memory():
    if len(users) == 0:
        print("AI memory empty")
    else:
        print(f"\nAI remembers {len(users)} people:")
        for i, u in enumerate(users, 1):
            print(f" {i}. {u}")

def ai_gate():
    dream = input("Enter your dream: ")
    if "nvidia" in dream.lower() or "tesla" in dream.lower():
        print(f"🚀 AMAZING! {dream.upper()} is waiting for you!")
    else:
        print(f"🔥 Great dream! Go for {dream}!")

# Main Brain (Day 2 - if/else + Day 3 - Loop)
greet()

while True:
    print("\n--- MENU ---")
    print("1. Add person to AI memory")
    print("2. Show AI memory")
    print("3. AI Gate - Check dream")
    print("4. Exit AI")

    choice = input("Choose 1-4: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        show_memory()
    elif choice == "3":
        ai_gate()
    elif choice == "4":
        print(f"\n👋 Goodbye! {assistant_profile['name']} shutting down.")
        print("Glory - 7 days ago you started, today you built Siri!")
        break
    else:
        print("Invalid choice, try again")
