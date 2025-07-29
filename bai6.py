def dao_nguoc_chuoi(s: str) -> str:
    return s[::-1]
print(dao_nguoc_chuoi("hello"))

def dao_nguoc_chuoi(s:str) -> str:
    ket_qua = ""
    for ky_tu in s:
        ket_qua = ky_tu + ket_qua
    return ket_qua
print(dao_nguoc_chuoi("world"))
