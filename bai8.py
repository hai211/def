def tim_min_list(danh_sach: list[int]) -> int:
    min_so = danh_sach[0]
    for so in danh_sach:
        if so < min_so:
            min_so = so
    return min_so

print(tim_min_list([1,2,3,4,5,6333,3,2,0]))