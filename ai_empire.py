# Glory's AI Empire - Day 14 - FINAL CAPSTONE - Graduation!
print("--- 👑 GLORY'S AI EMPIRE v14.0 - GRADUATION DAY ---")
print("Combining 14 Days of Knowledge into ONE Company!")

# Uses: file handling (Day 9) + data analysis (Day 10) + prediction (Day 11) + learning (Day 12)

customers = []

def add_customer():
    name = input("Customer name: ")
    balance = int(input("Balance: $"))
    score = int(input("Credit score (0-100): "))
    
    # Save to memory + file (Day 9)
    customers.append({"name": name, "balance": balance, "score": score})
    with open("empire_data.txt", "a") as f:
        f.write(f"{name},{balance},{score}\n")
    print(f"✅ {name} added to Empire!")

def analyze_empire():
    if not customers:
        print("No customers yet!")
        return
    
    # Data Analysis (Day 10)
    total = sum(c["balance"] for c in customers)
    avg = total / len(customers)
    richest = max(customers, key=lambda x: x["balance"])
    
    print(f"\n--- 📊 EMPIRE ANALYSIS ---")
    print(f"Total customers: {len(customers)}")
    print(f"Total money: ${total}")
    print(f"Average: ${avg:.2f}")
    print(f"Richest: {richest['name']} - ${richest['balance']}")

    # Prediction (Day 11)
    print(f"\n--- 🔮 LOAN PREDICTIONS ---")
    for c in customers:
        if c["balance"] > 5000 and c["score"] > 70:
            print(f"✅ {c['name']}: APPROVED")
        else:
            print(f"❌ {c['name']}: DENIED")

def load_empire():
    try:
        with open("empire_data.txt", "r") as f:
            for line in f:
                name, balance, score = line.strip().split(",")
                customers.append({"name": name, "balance": int(balance), "score": int(score)})
        print(f"📂 Loaded {len(customers)} customers from file! Empire never forgets!")
    except:
        print("🆕 Starting new empire...")

# MAIN APP - uses chatbot loop (Day 8)
load_empire()

while True:
    print("\n--- GLORY'S AI EMPIRE MENU ---")
    print("1. Add Customer (Day 9 + 6)")
    print("2. Analyze Empire (Day 10 + 11 + 12)")
    print("3. Show All (Day 4)")
    print("4. Exit & Graduate!")

    ch = input("Choose: ")

    if ch == "1":
        add_customer()
    elif ch == "2":
        analyze_empire()
    elif ch == "3":
        print("\n--- ALL CUSTOMERS ---")
        for c in customers:
            print(f"👤 {c['name']} | ${c['balance']} | Score: {c['score']}")
    elif ch == "4":
        print("\n🎓🎓🎓 CONGRATULATIONS GLORY!!! 🎓🎓🎓")
        print("You built an AI COMPANY in 14 days on phone!")
        print("From Calculator.py to AI Empire!")
        print("Ebonyi girl is now AI Engineer!")
        print("Go and apply for internships now!")
        break
