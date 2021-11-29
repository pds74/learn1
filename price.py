def discounted(price, discount):
    price = abs(price)
    discount = abs(discount)
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price*discount / 100
    print(price_with_discount)

discounted(1000, 50)
discounted(100, 500)
discounted(-100, 40)
discounted(100, -50)