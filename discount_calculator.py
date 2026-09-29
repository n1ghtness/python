product_price = float(input("Enter the product price: "))
if product_price <= 100:
    discount = product_price * 0
    final_price = product_price - discount
elif product_price <= 300:
    discount = product_price * 0.10
    final_price = product_price - discount
else:
    discount = product_price * 0.20
    final_price = product_price - discount
print(f"Original price:{product_price}")
print(f"Discount:{discount}")
print(f"Final price:{final_price}")