# FixTrack - Python console program

orders = []   # List to store repair orders

def add_order():
    customer = input("Enter customer name: ")
    device = input("Enter device type: ")
    issue = input("Enter issue: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")
    
    order = {
        "customer": customer,
        "device": device,
        "issue": issue,
        "due_date": due_date,
        "status": "Pending"
    }
    orders.append(order)
    print("\n Repair order added successfully!\n")

def show_orders():
    if not orders:
        print("\nNo repair orders available.\n")
        return
    
    print("\n Current Repair Orders:")
    for i, order in enumerate(orders, start=1):
        print(f"{i}. {order['customer']} - {order['device']} ({order['issue']}) | Due: {order['due_date']} | Status: {order['status']}")
    print()

def generate_bill():
    show_orders()
    if not orders:
        return
    
    try:
        choice = int(input("Select order number to bill: ")) - 1
        order = orders[choice]
    except (ValueError, IndexError):
        print(" Invalid order selection.")
        return
    
    # Parts input
    parts = {}
    while True:
        part_name = input("Enter part name (or 'done' to finish): ")
        if part_name.lower() == "done":
            break
        try:
            cost = float(input(f"Enter cost for {part_name}: "))
            parts[part_name] = cost
        except ValueError:
            print(" Please enter a valid number.")
    
    # Repair fee
    try:
        repair_fee = float(input("Enter repair service fee: "))
    except ValueError:
        print(" Invalid fee amount.")
        return
    
    subtotal = sum(parts.values()) + repair_fee
    tax = subtotal * 0.18   # 18% tax
    discount_choice = input("Apply 10% discount? (y/n): ")
    discount = subtotal * 0.10 if discount_choice.lower() == "y" else 0
    final_total = subtotal + tax - discount
    
    # Mark order as Completed
    order["status"] = "Completed"
    
    # Print formatted bill
    print("\n Repair Invoice")
    print("="*30)
    print(f"Customer: {order['customer']}")
    print(f"Device: {order['device']} | Issue: {order['issue']}")
    print("-"*30)
    for part, cost in parts.items():
        print(f"{part:<15} : ₹{cost:.2f}")
    print(f"Repair Fee        : ₹{repair_fee:.2f}")
    print("-"*30)
    print(f"Subtotal          : ₹{subtotal:.2f}")
    print(f"Tax (18%)         : ₹{tax:.2f}")
    print(f"Discount          : -₹{discount:.2f}")
    print("="*30)
    print(f"Final Amount      : ₹{final_total:.2f}")
    print("="*30 + "\n")

def main():
    while True:
        print("=== FixTrack Menu ===")
        print("1. Add new repair order")
        print("2. Show all orders")
        print("3. Generate bill")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_order()
        elif choice == "2":
            show_orders()
        elif choice == "3":
            generate_bill()
        elif choice == "4":
            print(" Exiting FixTrack. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.\n")

# Run program
main()
