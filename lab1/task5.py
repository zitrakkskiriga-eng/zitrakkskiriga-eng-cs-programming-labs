dist = 250
cons = 7.5
price = 60
fuel = dist * cons / 100
cost = fuel * price
print(f"Топливо: {fuel:.2f} л")
print(f"Стоимость: {cost:.2f} руб")