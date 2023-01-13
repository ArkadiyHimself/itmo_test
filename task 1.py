def summ(a, b, c = 1, d = 3):
    return a**2 + b**2 + c**2 + d**2


def three_times(a, b):
    for i in range(1, 4):
        result = summ(a, b)
        print("Iteration ", i, ':', result)
    return ""


a = int(input())
d = int(input())
print(three_times(a, d))