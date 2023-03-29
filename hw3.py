def get_fixed_price_a(discounted_price_a, discount_rate):
    fixed_price_a = discounted_price_a / (1 - discount_rate)
    return fixed_price_a

def get_fixed_price_b(discounted_price_b, discount_rate):
    fixed_price_b = discounted_price_b / (1 - discount_rate)
    return fixed_price_b

discount_rate= int(input("할인율은?"))
discounted_price_a= int(input("A 상품의 할인된 가격은?"))
discounted_price_b= int(input("B 상품의 할인된 가격은?"))



print("A 상품의 정가는",fixed_price_a,"원")
print("B 상품의 정가는",fixed_price_b,"원")
