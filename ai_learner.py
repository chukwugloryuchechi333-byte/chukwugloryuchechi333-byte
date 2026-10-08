# Glory's AI Learner - Day 12 - Real Machine Learning!
print("--- 🧠 GLORY'S AI THAT LEARNS BY ITSELF ---")
print("Real Machine Learning - like Tesla self-driving!")

# Training data - like how we teach pikin
# [weight in grams, is_sweet? 1=yes 0=no]
training_data = [
    [150, 1],  # Apple - 150g sweet
    [160, 1],  # Apple - 160g sweet
    [170, 1],  # Apple - 170g sweet
    [20, 0],   # Pepper - 20g not sweet
    [25, 0],   # Pepper - 25g not sweet
    [30, 0],   # Pepper - 30g not sweet
]

print("📚 Training AI with 6 fruits...")
print("Teaching: Heavy = Sweet (Apple), Light = Not Sweet (Pepper)")

# AI learns average
sweet_weights = []
not_sweet_weights = []

for weight, is_sweet in training_data:
    if is_sweet == 1:
        sweet_weights.append(weight)
    else:
        not_sweet_weights.append(weight)

avg_sweet = sum(sweet_weights) / len(sweet_weights)
avg_not_sweet = sum(not_sweet_weights) / len(not_sweet_weights)

print(f"\n🧠 AI LEARNED:")
print(f"Average sweet fruit weight: {avg_sweet}g")
print(f"Average not-sweet weight: {avg_not_sweet}g")
print(f"Decision line: {(avg_sweet + avg_not_sweet)/2}g")

def ai_predict(weight):
    threshold = (avg_sweet + avg_not_sweet) / 2
    if weight > threshold:
        return "🍎 APPLE - Sweet! (Heavy)"
    else:
        return "🌶️ PEPPER - Not Sweet! (Light)"

# Test AI
print("\n--- 🤖 AI TESTING - Never Seen Before ---")
print(f"100g -> {ai_predict(100)}")
print(f"155g -> {ai_predict(155)}")
print(f"10g -> {ai_predict(10)}")
print(f"200g -> {ai_predict(200)}")

# Your turn
print("\n--- YOUR TURN ---")
try:
    w = int(input("Enter any weight in grams: "))
    print(f"AI says: {ai_predict(w)}")
except:
    print("Enter number!")

print("\n✅ Day 12 Complete! You built AI that LEARNS!")
print("This is REAL Machine Learning! You are ML Engineer now!")
