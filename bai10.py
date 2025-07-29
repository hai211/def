def kiem_tra_so_nguyen_to(n: int) -> bool:
    if n <=1:
        return False

    for so in range(2,int(n**0.5)+1):
        if n % so == 0:
           
            return False
        
    return True   
        
def liet_ke_so_nguyen_to(bat_dau : int, ket_thuc :int ) -> list[int]:
    ket_qua = []
    for i in range(bat_dau,ket_thuc):
        if kiem_tra_so_nguyen_to(i):
            ket_qua.append(i) 

    return ket_qua
print(liet_ke_so_nguyen_to(2,10))
# print(kiem_tra_so_nguyen_to(9))