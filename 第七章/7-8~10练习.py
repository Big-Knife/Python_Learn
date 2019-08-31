# 熟食店
sandwiche_orders=['原味','加辣','海鲜']
finished_sandwiches=[]
while sandwiche_orders:
    current=sandwiche_orders.pop()
    finished_sandwiches.append(current)
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

# 五香烟熏牛肉
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
