price = input("물건의 가격을 입력하시오  " )
price = int(price)

sale = input("물건 할인율의 백분율을 입력하시오  " )
sale = int(sale)

fin_sale = sale * 0.01

print( price - (price * fin_sale)," 원 입니다.")
