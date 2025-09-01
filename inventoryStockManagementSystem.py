from numpy import negative

inventory = []
def add_product():
    skus_str = input("Enter SKUs: ")
    product_names_str = input("Enter product names: ")
    quantities_str = input("Enter quantities: ")
    prices_str = input("Enter prices: ")

    skus = [s.strip() for s in skus_str.split(',')]
    product_names = [pn.strip() for pn in product_names_str.split(',')]
    quantities = [q.strip() for q in quantities_str.split(',')]
    prices = [p.strip() for p in prices_str.split(',')]

    if not (len(skus) == len(product_names) == len(quantities) == len(prices)):
        return "Error: The number of SKUs, names, quantities, and prices must match."

    products_to_add = []
    for i in range(len(skus)):
        try:
            sku = int(skus[i])
            product_name = product_names[i]
            quantity = int(quantities[i])
            price = float(prices[i])

            if any(item['sku'] == sku for item in inventory):
                return f"Product with SKU {sku} already exists. No products were added."
            if quantity < 0 or price < 0:
                return "Quantity and price must be non-negative. No products were added."
            if not product_name:
                return "Product name cannot be empty. No products were added."
            if any(char.isdigit() for char in product_name):
                return "Product name cannot contain numbers. No products were added."
            if len(product_name) < 3:
                return "Product name must be at least 3 characters long. No products were added."
            if len(inventory) + len(products_to_add) >= 50:
                return "Inventory is full, cannot add more products."

            product = {
                'sku': sku,
                'product_name': product_name,
                'quantity': quantity,
                'price': price
            }
            products_to_add.append(product)

        except ValueError:
            return "Invalid input for SKU, quantity, or price. Please ensure they are correct numbers. No products were added."

    inventory.extend(products_to_add)
    return f"{len(products_to_add)} product(s) added successfully."

def view_inventory():
    print("Current Inventory:\n")
    for item in inventory:
        print("\n------------------\n",
              "Product ID:", 
              item.get('sku'), 
              "\nProduct name:", 
              item.get('product_name'), 
              "\nQuantity:", 
              item.get('quantity'), 
              "\nPrice:", 
              item.get('price'), "\n------------------")

while True:
    print("----------------------------------------------\n"
        "Welcome to the Vidit Chaap Inventory Stock Management System!\n"
            "\nPress 1 to add a product\n" \
            "Press 2 to view inventory\n" \
            "Press 3 to search for a product by Product Name\n"
            "Press 4 to search for a product by SKU\n"
            "Press 5 to exit\n"
            "-----------------------------------------------\n\n")
    
    choice = int(input("Enter your choice: "))
    
    if choice ==1:
        output = add_product()
        print(output)
    elif choice == 2:
        view_inventory()
        if input("Do you want to continue? (yes/no)") == "yes":
            continue
        elif input("Do you want to exit? (yes/no)") == "no":
            break
        else:
            print("Invalid input. Taking to main menu.")
            continue

    elif choice == 3:
        product_name = input("Enter the product name to search: ")
        found = False
        for item in inventory:
            if item['product_name'].lower() == product_name.lower():
                print("Product found:")
                print("SKU:", item['sku'])
                print("Product Name:", item['product_name'])
                print("Quantity:", item['quantity'])
                print("Price:", item['price'])
                found = True
                break
        if not found:
            print("Product not found.")

    elif choice == 4:
        sku = int(input("Enter the SKU to search: "))
        found = False
        for item in inventory:
            if item['sku'] == sku:
                print("Product found:")
                print("SKU:", item['sku'])
                print("Product Name:", item['product_name'])
                print("Quantity:", item['quantity'])
                print("Price:", item['price'])
                found = True
                break
        if not found:
            print("Product not found.")

    elif choice == 5:
        print("Exiting the system. Goodbye! Never come again!")
        break
    else:
        print("Invalid choice. Please try again.")
