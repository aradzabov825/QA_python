products = ['яблоки','груши','веники','угли','мясо']
prices = [100,200,300,400,500]
total = 0


for i in prices:
    total += i


if total > 200:
    discount = total * 0.1 #10%
    total -= discount
print(total)