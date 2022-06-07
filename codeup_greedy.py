# 최소대금
menu = []
for i in range(5):
    menu.append(int(input()))
total = min(menu[:3])+min(menu[3:])
print(round(total*1.1,1))

# 거스름돈
n = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
count = 0
for i in money:
    count += n//i
    n%=i
print(count)

