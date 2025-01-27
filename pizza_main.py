# import pizza_order as po
from pizza_order import *

pizza_menu = {'페퍼로니 피자':3000, '치즈 피자':3200,
            '콤비네이션 피자':3500, '불고기 피자':3600, '해산물 피자':3800}
drink_menu={'콜라':1500, '사이다':1500, '생수':1000}
#피자 주문
order_pizza = menu_select(pizza_menu, '피자')           #po.menu_select()
# print(order_pizza)
#피음료 주문
order_drink = menu_select(drink_menu, '음료')
# print(order_drink)

# 계산
pizza_money = money_calc(order_pizza,pizza_menu)
drink_money = money_calc(order_drink,drink_menu)

print(f'전체금액:', pizza_money+drink_money)