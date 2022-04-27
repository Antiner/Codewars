from re import findall

n = "&z _upon 40729810a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()"
numbers = findall("\d{1,3}", n)
print(numbers)



# while n > 0:
#   b.append(n % 1000)
#   n = n // 1000
#   print(n)
# b = b[::-1] # так можно развернуть, если бы нам был важен порядок
# print (b)
#
# #print(int(''.join(reversed(str(n)))))