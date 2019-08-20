requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping =='green peppers':
        print("没有" + requested_topping.title())
    else:
        print("添加"+requested_topping.title())

#确定列表是不是空的
requested_toppings=[]
if requested_toppings:
     for requested_topping in requested_toppings:
         print("添加"+requested_topping)
else:
    print("这个列表是空的")

#使用多个列表
available_topping=['mushrooms','olives','green peppers',
                   'pepperoni','pineapple','extra cheese']