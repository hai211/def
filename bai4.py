def tinh_giai_thua(n:int)->int:
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua
print(tinh_giai_thua(5))

