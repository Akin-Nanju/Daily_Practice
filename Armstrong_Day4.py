def arm(num):
    sum = 0
    n = len(str(num))
    initial = num
    while num>0:
        sum += (num%10)**n
        num = num//10
    if sum == initial:
        return "Armstrong"
    else:
        return "Not Armstrong"

a = 153
arm(a)
