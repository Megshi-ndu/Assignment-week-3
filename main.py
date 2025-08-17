# Calculates final price after discount (applied only if >= 20%)
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (100 - discount_percent) / 100  # Apply discount
    return price  # No discount if < 20%

# Get user input
price = int(input("Enter original price: "))
discount = int(input("Enter discount percentage: "))

# Compute and display final price
final_price = calculate_discount(price, discount)
print("Final price:", final_price)