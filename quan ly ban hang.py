print('Đăng nhập vào hệ thống')
while True:
	taikhoan=str(input('Tài khoản: '))
	matkhau=str(input('Mật khẩu: '))
	if taikhoan=='TastyUToo' and matkhau=='TastyUToo':
		print('Chào mừng')
		break
	else:
		print('Tài khoản hoặc mật khẩu sai. Xin vui lòng nhập lại.')
		continue
thanhvien=str(input("Đã có tài khoản thành viên chưa?:"))
if thanhvien=="Có":
	phieudatmon=str(input("Đã có phiếu đặt món chưa?: "))
	if phieudatmon=="Có":
		print("Tìm kiếm phiếu đặt món ")
		huyphieudatmon = str(input("có muốn hủy phiếu đặt món hay không?: "))
		if huyphieudatmon=='Có':
			laplaiphieudatmon=str(input("Có muốn lập lai phiếu đặt món hay không?"))
			if laplaiphieudatmon=="Có":
				print("Lập phiếu đặt món")
			print("End")
		elif huyTastyUToophieudatmon=="Không":
			kiemtraphieudatmon=str(input("kiểm tra phiếu đặt món:"))
			if kiemtraphieudatmon=="Đúng":
				print("in phiếu đặt món")
			else:
				print("Cập nhật phiếu đặt món:")
	elif phieudatmon=="Không":
		print("Lập phiếu đặt món")
		idphieudatmon=int(input("id phiếu đặt món: "))
		idkhachhang=int(input("id khách hàng: "))
		idban=int(input("id bàn: "))
		tenkhachhang=str(input("Tên khách hàng: "))
		tglap=str(input("Thời gian lập phiếu đặt món: "))

elif thanhvien== "Không":
	print("Tạo Tài Khoản Thành Viên")
	idkhachhang=int(input("id khách hàng: "))
	tenkhachhang=str(input("Tên khách hàng: "))
	gioitinh= str(input("Giới tính: "))
	diachi= str(input("Địa chỉ: "))
	sdt= int(input("SDT: "))
	phieudatmon = str(input("Đã có phiếu đặt món chưa?: "))
	if phieudatmon == "Có":
		print("Tìm kiếm phiếu đặt món ")
		huyphieudatmon = str(input("có muốn hủy phiếu đặt món hay không?: "))
		if huyphieudatmon == 'Có':
			laplaiphieudatmon = str(input("Có muốn lập lai phiếu đặt món hay không?"))
			if laplaiphieudatmon == "Có":
				print("Lập phiếu đặt món")
			print("End")
		elif huyphieudatmon == "Không":
			kiemtraphieudatmon = str(input("kiểm tra phiếu đặt món:"))
			if kiemtraphieudatmon == "Đúng":
				print("in phiếu đặt món")
			else:
				print("Cập nhật phiếu đặt món:")
	elif phieudatmon == "Không":
		print("Lập phiếu đặt món")
		idphieudatmon = int(input("id phiếu đặt món: "))
		idkhachhang = int(input("id khách hàng: "))
		idban = int(input("id bàn: "))
		tenkhachhang = str(input("Tên khách hàng"))
		tglap = str(input("Thời gian lập phiếu đặt món: "))



