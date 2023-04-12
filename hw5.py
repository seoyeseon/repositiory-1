def read_single_digit(num):  #'한 자리'정수를 문자열로 변환하는 함수
    if num == 0:
        return '영'
    elif num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'

def read_number(num): #'세 자리' 정수를 문자열로 변환하는 함수
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    f= read_single_digit(hundreds)
    s= read_single_digit(tens)
    t= read_single_digit(ones)
    return f + s + t

num =int(input("세 자리 정수 입력:"))
result= read_number(num)
print(result)