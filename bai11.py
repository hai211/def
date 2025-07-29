def kiem_tra_nam_nhuan(nam: int) -> bool:
    if nam % 400 == 0 or nam % 4 == 0 and nam % 100!=0:
        return True
   
    return False
print(kiem_tra_nam_nhuan(2025))