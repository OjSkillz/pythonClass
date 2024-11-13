

def get_discount(price, discount):
    PERCENTAGE = 100
    price_after_discount = price - ((discount / 100 ) * price)
    return round(price_after_discount, 2)

