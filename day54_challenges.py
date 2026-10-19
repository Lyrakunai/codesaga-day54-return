# Codesaga Day 54 — Mini Challenge
# Delivery Fee Calculator


def calculate_delivery(order_amount):
    if order_amount >= 500:
        delivery_charge = 0
    else:
        delivery_charge = 40

    final_amount = order_amount + delivery_charge

    return final_amount, delivery_charge


# Test Case 1
final_amount, delivery_charge = calculate_delivery(700)

print("Order Amount: 700")
print("Delivery Charge:", delivery_charge)
print("Final Amount:", final_amount)


print()


# Test Case 2
final_amount, delivery_charge = calculate_delivery(350)

print("Order Amount: 350")
print("Delivery Charge:", delivery_charge)
print("Final Amount:", final_amount)