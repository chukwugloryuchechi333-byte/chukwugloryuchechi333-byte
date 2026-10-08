# PROJECT 18: TRIPLE GLORY 333-BYTE SPAM DETECTOR
# Author: Chukwugloryuchechi333-byte
# From Ebonyi to NVIDIA - 18 Projects!

print("=== TRIPLE GLORY SPAM DETECTOR - PROJECT 18 ===")

def is_spam(email_text):
    text = email_text.lower()
    score = 0
    reasons = []

    spam_words = [
        "win money", "free money", "lottery", "jackpot",
        "urgent", "click here", "act now",
        "prince", "inheritance", "million dollars",
        "free gift", "congratulations you won"
    ]

    # Check spam words
    for word in spam_words:
        if word in text:
            score += 2
            reasons.append(f"Found '{word}'")

    # Check signs
    if "!!!" in email_text or "$$$" in email_text:
        score += 1
        reasons.append("Too many !!! or $$$")

    if email_text.count("!") > 3:
        score += 1
        reasons.append("Many exclamation")

    # Check if ALL CAPS
    if len(email_text) > 20 and email_text.isupper():
        score += 2
        reasons.append("ALL CAPS")

    if score >= 3:
        print(f"🚨 SPAM! Score {score}/10")
        print(f"Reasons: {', '.join(reasons)}")
        print("ACTION: Move to SPAM folder!")
        return True
    else:
        print(f"✅ SAFE EMAIL! Score {score}/10 - Inbox")
        return False

# --- AUTO TEST ---
print("\nTest 1: Normal email from boss")
is_spam("Hello Glory, please send the report for today meeting. Thank you.")

print("\nTest 2: Spam - Lottery")
is_spam("CONGRATULATIONS!!! You win 1 MILLION DOLLARS!!! Click here NOW!!!")

print("\nTest 3: Spam - Prince")
is_spam("Dear friend, I am a Prince and I want to give you free inheritance money")

print("\nTest 4: Your old bank email")
is_spam("Your account has been hacked! Urgent! Click here to win money!")

# --- YOUR TURN ---
print("\n--- Test your own email ---")
my_email = input("Paste email text: ")
is_spam(my_email)

print("\nProject 18 Done! You now have 18 projects!")
