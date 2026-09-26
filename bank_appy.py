print("=== SIMPLE BANK APP ===")
balance = 1000
print(f"Your balance is GHS {balance}")

amount = float(input("How much to withdraw? "))
if amount <= balance:
    balance -= amount
    print(f"Success! New balance is GHS {balance}")
else:
    print("Not enough money!")

print("Thank you for banking with us!")
