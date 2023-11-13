a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Tìm ước số chung lớn nhất (UCLN) sử dụng thuật toán Euclid
while b != 0:
    a, b = b, a % b

print(f"Ước số chung lớn nhất (UCLN) là: {abs(a)}")