def menu_select(menulist, etc):
    order={}
    print(f'{etc}를 선택해주세요>> ')
    for name, price in menulist.items():
        print(f'{name}({price:,})원')

    while True:
        menu_name = input(f'{etc} 메뉴 이름 입력하세요(종료:exit)')
        if menu_name == 'exit':
            break
        elif menu_name in menulist:
            count = int(input('수량을 입력하세요: '))
            order[menu_name]=count
            print('주문 완료')
    return order

def money_calc(order,menu):
    totprice=0
    for k in order.keys():
        if k in menu.keys():
            price = order[k] * menu[k]
            print(f'{k}, {menu[k]}원 * {order[k]} = {price:,}원')
        totprice = totprice + price
    print(f'전체금액 : {totprice:,}원')
    return totprice

# ========================



