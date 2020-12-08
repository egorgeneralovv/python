def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1/res
print(f'result : {my_func(float(input("Введите действительное положительное число: ")), int(input("Введите целое отрицательное число: ")))}')
