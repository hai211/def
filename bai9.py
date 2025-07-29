def tinh_tong_list(danh_sach:list[int]) -> int:
    tong = 0
    for so in danh_sach:
        tong += so
    return tong
print(tinh_tong_list([1,2,3,]))