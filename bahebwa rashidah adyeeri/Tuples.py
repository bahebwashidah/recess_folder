tuples=("samsung","iphone","tecno")
print(tuples)
z=list(tuples)
z.append("nokia")
tuples=tuple(z)
print(tuples)
laptops=("dell","hp","acer")
laptop=("microsft")
laptops += laptop
newstock=laptops+laptop

print(laptops)
print(laptop)
print(newstock)