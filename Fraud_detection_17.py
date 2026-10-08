# PROJECT 17: AI BANK FRAUD DETECTION
# Author: Triple Glory 333-byte
# From Ebonyi to NVIDIA

print("=== TRIPLE GLORY FRAUD DETECTION - PROJECT 17 ===")

def check_fraud(amount, hour, location):
    score = 0
    reasons = []

    if amount > 50000:
        score += 2
        reasons.append(f"Big amount N{amount}")

    if hour < 6 or hour > 22:
        score += 2
        reasons.append(f"Night transfer {hour}:00")

    if location.lower() != "ph" and location.lower() != "port harcourt":
        score += 1
        reasons.append(f"Strange location {location}")

    if score >= 3:
        print(f"🚨 FRAUD ALERT! Score {score}/5")
        print(f"Reason: {', '.join(reasons)}")
        print("ACTION: BLOCKED!")
        return True
    else:
        print(f"✅ SAFE! Score {score}/5 - Transaction Allowed")
        return False

# --- AUTO TEST ---
print("\nTest 1: You - 10k by 2pm for PH")
check_fraud(10000, 14, "PH")

print("\nTest 2: Thief - 300k by 3am for Lagos")
check_fraud(300000, 3, "Lagos")

print("\nTest 3: Thief - 200k by 2am for Abuja")
check_fraud(200000, 2, "Abuja")

# --- YOUR TURN ---
print("\n--- Try your own ---")
amt = int(input("Enter amount: "))
hr = int(input("Enter hour 0-23: "))
loc = input("Enter location: ")

check_fraud(amt, hr, loc)

print("\nProject 17 Done! 17 projects complete!")
