# Lỗi: Đặt vòng lặp ngoài duyệt theo tháng thay vì duyệt theo chi nhánh nên dữ liệu bị hiển thị theo từng tháng, 
# không gom đủ 3 tháng của từng chi nhánh trước

# code đúng 
doanh_thu = []

for chi_nhanh in range(3):
    ds_thang = []

    for thang in range(3):
        tien = int(input(f"Nhập doanh thu Chi nhánh {chi_nhanh + 1}, tháng {thang + 1}: "))
        ds_thang.append(tien)

    doanh_thu.append(ds_thang)

print("\n-------------- Kết quả --------------")

for chi_nhanh in range(3):
    for thang in range(3):
        print(f"Chi nhánh {chi_nhanh + 1}, tháng {thang + 1}: {doanh_thu[chi_nhanh][thang]} triệu đồng")