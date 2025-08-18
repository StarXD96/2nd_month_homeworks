from homeworks.distance import Distance

d1 = Distance(100, "m")
d2 = Distance(1, "km")
d3 = Distance(50, "cm")
d4 = Distance(1000, "m")
# d5 = Distance(1000, "kg") Ошибка
print(d1, d2, d3)
print(d1 + d2)
print(d2 + d3)
print(d2 - d1)
print(d4 - d2)
# print(d1 - d4) Ошибка
print(d1 == Distance(0.1, "km"))
print(d2 > d1)
print(d3 < d1)
print(d4 == d2)