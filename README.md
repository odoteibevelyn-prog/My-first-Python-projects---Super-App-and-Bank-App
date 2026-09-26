wat of, import random

while True:
    print("\n=== MY SUPER APP ===")
    print("1. Calculator")
    print("2. Grade Checker")
    print("3. Guess Game")
    print("4. Login Test")
    print("5. Exit")
    
    choice = input("Choose 1-5: ")
    
    if choice == "1":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"{a} + {b} = {a+b}")
        print(f"{a} * {b} = {a*b}")
    
    elif choice == "2":
        score = int(input("Enter score: "))
        if score >= 80:
            print("A - Excellent!")
        elif score >= 60:
            print("B - Good!")
        elif score >= 50:
            print("C - Pass!")
        else:
            print("F - Fail!")
    
    elif choice == "3":
        secret = random.randint(1, 20)
        guess = int(input("Guess 1-20: "))
        if guess == secret:
            print(f"YES! It was {secret}")
        else:
            print(f"Nope, it was {secret}")
    
    elif choice == "4":
        u = input("Username: ")
        p = input("Password: ")
        if u == "admin" and p == "1234":
            print("Welcome admin!")
        else:
            print("Access denied!")
    
    elif choice == "5":
        print("Bye! Super App closed.")
        break
    
    else:
        print("Invalid choice!")
