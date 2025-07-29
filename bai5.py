def demm_so_nguyen_am(chuoi:str) -> int:
    nguyen_am = 'ueoaiUEOAI'
    dem = 0
    for i in chuoi:
        if i in nguyen_am:
            dem += 1
    return dem
print(demm_so_nguyen_am("Hello World"))

