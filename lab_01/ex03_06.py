def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
my_dict = {'a':1,'b':2,'c':3,'d':4}
key_to_delete ='b'
result = xoa_phan_tu(my_dict,key_to_delete)
if result:
    print("Phần tử đã được xoá từ Dictionary",my_dict)
else:
    print("Khong tìm thấy phần tử cần xoá trong Dictionary")