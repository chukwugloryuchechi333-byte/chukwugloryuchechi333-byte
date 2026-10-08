# Glory's AI Profile - Day 5
print("--- Glory's AI Profile Maker ---")

# Create AI knowledge box
profile = {}

profile["name"] = input("Enter name: ")
profile["age"] = input("Enter age: ")
profile["state"] = input("Enter state: ")
profile["dream_job"] = input("Enter dream job (NVIDIA/Tesla): ")
profile["skill"] = input("Enter best skill (Python/AI): ")

print("\n--- AI Knowledge Stored ---")
for key, value in profile.items():
    print(f"{key.upper()}: {value}")

# AI makes decision based on knowledge
print("\n--- AI Analysis ---")
if "nvidia" in profile["dream_job"].lower() or "tesla" in profile["dream_job"].lower():
    print(f"🚀 WOW {profile['name']}! AI sees BIG dream! You will enter {profile['dream_job']}!")
else:
    print(f"🔥 Nice dream {profile['name']}! {profile['dream_job']} is powerful!")

# Bonus: AI counts knowledge
print(f"\nAI knows {len(profile)} things about {profile['name']}")
print("Glory's AI now knows everything!")
