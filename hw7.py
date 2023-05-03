shopping_bag = {}
while True :
    item = input('상품명? ')

    if item == '' :
        break
    else :
        num = input('수량은? ')
        shopping_bag[item] = num
        print(f'장바구니에  {num}개가 담겼습니다.')
        print()

print()
print('>>>장바구니 보기:', shopping_bag)
print()

find = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{find}은(는) {shopping_bag[find]}개 담겨 있습니다.')
