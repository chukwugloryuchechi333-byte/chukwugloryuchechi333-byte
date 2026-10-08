# Glory's AI Functions - Day 6
print("--- Glory's AI Function Machine ---")

# Function 1: AI Greeter
def ai_greet(name):
    print(f"🚀 Hello {name}! Glory's AI welcomes you to NVIDIA!")

# Function 2: AI Calculator
def ai_add(a, b):
    result = a + b
    print(f"AI calculated: {a} + {b} = {result}")
    return result

# Function 3: AI Dream Checker (from Day 2, but now as function!)
def ai_gate_checker(dream):
    if "nvidia" in dream.lower() or "tesla" in dream.lower():
        print(f"✅ AI GATE: Welcome to {dream.upper()}!")
    else:
        print(f"🔥 Nice dream: {dream}")

# Use your AI buttons
ai_greet("Glory")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
ai_add(num1, num2)

my_dream = input("Enter your dream job: ")
ai_gate_checker(my_dream)

print("\nGlory now has 3 AI buttons she can press anytime!")
print("This is how real AI engineers build Tesla autopilot!")
