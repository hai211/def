def dem_so_lan_xuat_hien(danh_sach: list, phan_tu: any) -> int:
    dem = 0
    for i in danh_sach:
        if i == phan_tu:
            dem += 1
    return dem

print(dem_so_lan_xuat_hien([1,2,2,3,3], 2))