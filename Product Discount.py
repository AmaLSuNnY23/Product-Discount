catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 5,
    "bulk_10_discount": 10,
    "tiered_50_discount": 50
}

gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

quantities = {}
gift_wrap_info = {}

for product in catalog:
    quantities[product] = int(input(f"Enter quantity for {product}: "))
    gift_wrap_info[product] = input(f"Wrap {product} as a gift? (yes/no): ").lower() == "yes"

subtotal = 0
for product, quantity in quantities.items():
    subtotal += catalog[product] * quantity

discount_name = ""
discount_amount = 0

if subtotal > 200:
    discount_name = "flat_10_discount"
    discount_amount = discount_rules[discount_name]
elif any(quantity > 10 for quantity in quantities.values()):
    discount_name = "bulk_5_discount"
    discount_amount = max(catalog[product] * quantities[product] * discount_rules[discount_name] / 100 for product in quantities.keys())
elif sum(quantities.values()) > 20:
    discount_name = "bulk_10_discount"
    discount_amount = discount_rules[discount_name]
elif sum(quantities.values()) > 30 and any(quantity > 15 for quantity in quantities.values()):
    discount_name = "tiered_50_discount"
    discount_amount = sum(max(0, quantities[product] - 15) * catalog[product] * discount_rules[discount_name] / 100 for product in quantities.keys())

gift_wrap_fee_total = sum(gift_wrap_fee * quantities[product] for product, is_wrapped in gift_wrap_info.items() if is_wrapped)

num_packages = sum(quantities.values()) // items_per_package
shipping_fee = num_packages * shipping_fee_per_package

total = subtotal - discount_amount + gift_wrap_fee_total + shipping_fee

print("Order Details:")
print("<--------------------->")
for product, quantity in quantities.items():
    print(f"{product} - Quantity: {quantity} - Total: ${catalog[product] * quantity}")
print("<--------------------->")
print(f"Subtotal: ${subtotal}")
print(f"Discount Applied: {discount_name} - Amount: ${discount_amount}")
print(f"Gift Wrap Fee: ${gift_wrap_fee_total}")
print(f"Shipping Fee: ${shipping_fee}")
print("<--------------------->")
print(f"Total: ${total}")