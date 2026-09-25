#Hoạt động 6: Đệ quy – Giai thừa, Fibonacci
#Bài tập 6.1 – Giai thừa bằng đệ quy
print ("\n========== BÀI 6.1 ==========")

def giai_thua_de_quy(n):
    if n <= 1:
        return 1
    return n * giai_thua_de_quy(n - 1)


def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

n = 5

print("Giai thua bang de quy:", giai_thua_de_quy(n))
print("Giai thua bang vong lap:", giai_thua_lap(n))

#Bài tập 6.2 – Số Fibonacci thứ n bằng đệ quy:
print ("\n========== BÀI 6.2 ==========")

def fibonacci_de_quy(n):
    if n <= 1: # dieu kien dung
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()