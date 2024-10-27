# # Biến số nhập/xuat
# full_name = input("Nhập tên: ")
# print("Họ và tên:", full_name)

# #Biến số nguyên
# age = int(input("Nhập tuổi: "))
# print("Tuổi:", age)

# #Biến số thực
# height = float(input("Nhập chiều cao: "))
# print("Chieàu cao:", height)

# #if/else: câu lệnh rẽ nhánh
# if age >= 18:
#     print("Bạn đã đủ tuổi điều khiển")
# else:
#     print("Bạn chưa đủ tuổi điều khiển")

# high1 = int(input("Nhập chiều cao 1: "))
# high2 = int(input("Nhập chiều cao 2: "))
# high3 = int(input("Nhập chiều cao 3: "))
# if high1 > high2:
#    if high1 > high3:
#       print("chiều cao 1 lớn nhất")
#    else:
#       print("chiều cao 3 lớn nhất")
# else:
#    if high2 > high3:
#       print("chiều cao 2 lớn nhất")
#    else:
#       print("chiều cao 3 lớn nhất")

# ds_so = [1, 2, 3, 4, 5]
# thay = ds_so.append(6)
# print(thay)
# for i in range(len(ds_so)):
#     print(ds_so[i])

tong = 0
ds_so = [1, 2, 3, 4, 5]
for i in range(len(ds_so)):
    if ds_so[i] % 2 == 0:
        tong += ds_so[i]
print(tong)

# tạo danh sách trùng nhau
def remove_duplicates(input_list):
    # Sử dụng set để loại bỏ các phần tử trùng nhau
    return list(set(input_list))

# Nhập danh sách từ người dùng
user_input = input("Nhập các phần tử cách nhau bằng dấu phẩy: ")
input_list = user_input.split(',')

# Loại bỏ các phần tử trùng nhau
unique_list = remove_duplicates(input_list)

# Xuất danh sách đã loại bỏ trùng lặp
print("Danh sách sau khi loại bỏ phần tử trùng nhau:", unique_list)





