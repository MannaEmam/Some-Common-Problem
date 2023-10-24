def power(n, exp):
    if exp == 1:
        return n
    x = power(n, exp // 2)
    if exp & 1:
        return n * x * x
    return x * x


print(power(2, 31))
x = 40
r = x // 3 + (x % 3 > 0)
print(r)
