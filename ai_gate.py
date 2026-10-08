# Glory's AI Gate - Day 2
print("--- Glory's AI Security Gate ---")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nScanning {name}...")

if age >= 18:
    print("✅ ACCESS GRANTED: You can drive Tesla!")
    print("Welcome to NVIDIA AI Lab!")
elif age >= 13:
    print("⚠️  YOUTH ACCESS: You can learn AI, but can't drive yet")
    print("Keep coding, Future Engineer!")
else:
    print("❌ ACCESS DENIED: Too young for AI Lab")
    print("Come back when you're older!")

print(f"\nGlory's AI Gate checked {name} at age {age}")
