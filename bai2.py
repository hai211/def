def kiem_tra_so_chan_le(so:int) -> str:
    if so % 2 == 0:
        return "chan"
    else:
        return "le"

so = None
while True:
    so = int(input("nhap: "))
    if so == 0:
        break
    ket_qua  = kiem_tra_so_chan_le(so)

    print(ket_qua)
