def add_product(dict_name, product_name, product_qtt):
    dict_name[product_name] = int(product_qtt)

shopping_bag = {}

while True:
    print('[구입]')
    product_name = input('상품명? ')
    if product_name == '':
        break
    else:
        product_qtt = input('수량은? ')
        add_product(shopping_bag, product_name, product_qtt)
        print(f'장바구니에 {product_name} {product_qtt}개가 담겼습니다.\n')

print(f'장바구니 보기: {shopping_bag}\n')

while True:
    print('[검색]')
    product_to_find = input('장바구니에서 확인하고자 하는 상품은? ')
    if product_to_find.lower() in map(str.lower, shopping_bag):
        print(f'{product_to_find}은(는) {shopping_bag[product_to_find.lower()]}개 담겨 있습니다.\n')
    else:
        print(f'장바구니에 {product_to_find}은(는) 없습니다.\n')
