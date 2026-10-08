# Glory's AI Predictor - Day 11 - Sees The Future!
print("--- 🔮 GLORY'S LOAN PREDICTOR AI ---")
print("Same AI FairMoney uses to approve loans!")

def predict_loan(name, balance, credit_score, has_job):
    print(f"\n--- Analyzing {name} ---")
    print(f"Balance: ${balance} | Credit: {credit_score} | Job: {has_job}")

    score = 0

    # AI Brain - Machine Learning Logic
    if balance > 5000:
        score += 40
        print("✅ Good balance +40")
    else:
        print("❌ Low balance +0")

    if credit_score > 70:
        score += 40
        print("✅ Good credit score +40")
    else:
        print("❌ Low credit score +0")

    if has_job.lower() == "yes":
        score += 20
        print("✅ Has job +20")
    else:
        print("❌ No job +0")

    print(f"Total AI Score: {score}/100")

    # AI Decision
    if score >= 80:
        print(f"🎉 APPROVED! {name} will get loan! Rich bank loves you!")
        return True
    elif score >= 60:
        print(f"⚠️ MAYBE - {name} needs more balance!")
        return False
    else:
        print(f"❌ DENIED! {name} too risky!")
        return False

# Test the predictor like real bank
print("\n--- BANK TESTING CUSTOMERS ---")
predict_loan("Glory", 10000, 85, "yes")
predict_loan("Random Guy", 1000, 50, "no")
predict_loan("Uchechi", 6000, 75, "yes")

# Let YOU try!
print("\n--- YOUR TURN - TRY YOURSELF ---")
your_name = input("Your name: ")
your_balance = int(input("Your balance: $"))
your_credit = int(input("Your credit score (0-100): "))
your_job = input("Do you have job? yes/no: ")

predict_loan(your_name, your_balance, your_credit, your_job)

print("\n✅ Day 11 Complete! You built FUTURE AI!")
print("This is called Machine Learning Logic!")
