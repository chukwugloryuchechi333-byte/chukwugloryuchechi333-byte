# Glory's AI Data Analyzer - Day 10 - DOUBLE DIGITS!
print("--- 📊 GLORY'S AI DATA ANALYZER v1.0 ---")
print("The same AI Dangote uses to analyze cement sales!")

# Sample bank data (like real company data)
customers = [
    {"name": "Glory", "balance": 10000, "state": "Ebonyi"},
    {"name": "Chukwu", "balance": 7500, "state": "Lagos"},
    {"name": "Uchechi", "balance": 15000, "state": "Abuja"},
    {"name": "Mama", "balance": 5000, "state": "Ebonyi"},
    {"name": "Papa", "balance": 12000, "state": "Rivers"}
]

print(f"\nAnalyzing {len(customers)} customers...")

# AI Analysis
total = 0
highest = customers[0]
lowest = customers[0]
ebonyi_customers = []

for person in customers:
    total += person["balance"]

    if person["balance"] > highest["balance"]:
        highest = person

    if person["balance"] < lowest["balance"]:
        lowest = person

    if person["state"] == "Ebonyi":
        ebonyi_customers.append(person["name"])

average = total / len(customers)

print("\n--- AI ANALYSIS RESULTS ---")
print(f"💰 Total Money: ${total}")
print(f"📈 Average Balance: ${average:.2f}")
print(f"👑 Richest: {highest['name']} with ${highest['balance']}")
print(f"💸 Lowest: {lowest['name']} with ${lowest['balance']}")
print(f"🏠 From Ebonyi: {', '.join(ebonyi_customers)} ({len(ebonyi_customers)} people)")

# AI Prediction
print("\n
