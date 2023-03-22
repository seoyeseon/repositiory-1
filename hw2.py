def get_integer(prompt):
    res=int(input(prompt))
    return res

def exchange(cost):
    n500 = cost//500
    cost %= 500
    n100 = cost //100
    cost %= 100
    n50 = cost//50
    cost %= 50
    n10 = cost //10

    print("500원 동전의 개수:",n500)
    print("100원 동전의 개수:",n100)
    print("50원 동전의 개수:",n50)
    print("10원 동전의 개수:",n10)

cost=int(input("동전으로 교환하고자 하는 금액은? "))
exchange(cost)

