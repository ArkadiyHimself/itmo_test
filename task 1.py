def summ(a, b, c = 1, d = 3):
    try:
        print(a**2 + b**2 + c**2 + d**2)
    except:
        a = int(a)
        b = int(b)
        print(a**2 + b**2 + c**2 + d**2)
    return ''

def three_times(a, b):
    for i in range(1, 4):
        result = summ(a, b)
        print("Iteration ", i, ':', result)
    return ""

a = '2'
b = '3'
c = '2'
d = 'three'
print(summ(a, b))
print(summ(c, d))
