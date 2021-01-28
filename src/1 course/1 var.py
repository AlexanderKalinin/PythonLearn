# x=5
# y=3
# print("x =", x , "; y=",y)
# print("x+y =", x+y)
# print("x-y =",x-y)
# print("x*y =",x*y)
# print("x/y =",x/y)
# print("x//y =",x//y)
# print("x%y =",x%y)
# print("x**y =",x**y)

credit = 1000000
cr_rate = 12.9
cr_years = 2

final_sum = credit + credit / 100 * cr_rate * cr_years
mount_pay = final_sum /  (cr_years * 12)

print(final_sum)
print(round(mount_pay,2))

