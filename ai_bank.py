# Glory's AI Bank - Day 9 - Never Forgets!
print("--- 💰 GLORY'S AI BANK SYSTEM ---")

def save_user(name, amount):
    # Save to file like real bank database
    with open("bank_data.txt", "a") as file:
        file.write(f"{name},{amount}\n")
    print(f"✅ Saved {name} with ${amount} to bank file!")

def show_all_users():
    try:
        with open("bank_data.txt", "r") as file:
            print("\n--- BANK RECORDS ---")
            total = 0
            for line in file:
                name, amount = line.strip().split(",")
                print(f" 👤 {name}: ${amount}")
                total += int(amount)
            print(f"\n💰 Total Bank Balance: ${total}")
    except FileNotFoundError:
        print("No bank records yet. Add users first!")

while True:
    print("\n1. Add customer")
    print("2. Show all customers")
    print("3. Exit bank")

    choice = input("Choose: ")

    if choice == "1":
        n = input("Customer name: ")
        a = input("Amount: $")
        save_user(n, a)
    elif choice == "2":
        show_all_users()
    elif choice == "3":
        print("🏦 Bank closing... but data saved forever!")
        print("This is how real banks never lose your money!")
        break
    else:
        print("Invalid!")
