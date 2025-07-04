def apply_discount(price, hello):
    discount_sum = price * (hello/100)
    return discount_sum

price=float(input("Enter number: "))
# x=apply_discount(price, 10)
# print(x)

x=apply_discount(price, 20)
print(x)