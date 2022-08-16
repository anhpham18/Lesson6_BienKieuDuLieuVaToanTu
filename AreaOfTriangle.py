import math
from stringprep import in_table_c3

a = int(input("Nhập độ dài cạnh a: "))
b = int(input("Nhập độ dài cạnh b: "))
c = int(input("Nhập độ dài cạnh c: "))

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Diện tích hình tam giác là: ", area)