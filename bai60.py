from datetime import datetime

class SinhVien:
    def __init__(self, ma_sv: str, ho_ten: str, ngay_sinh: str):
        """Khởi tạo sinh viên với Mã SV, Họ và Tên, Ngày sinh (định dạng YYYY-MM-DD)"""
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.ngay_sinh = datetime.strptime(ngay_sinh, "%Y-%m-%d")  # Chuyển chuỗi thành datetime

    @property
    def ho(self):
        """Lấy họ từ họ và tên"""
        return self.ho_ten.split()[0]  # Lấy phần đầu tiên

    @property
    def ten(self):
        """Lấy tên từ họ và tên"""
        return self.ho_ten.split()[-1]  # Lấy phần cuối cùng

    @property
    def tuoi(self):
        """Tính tuổi từ ngày sinh"""
        today = datetime.today()
        return today.year - self.ngay_sinh.year - ((today.month, today.day) < (self.ngay_sinh.month, self.ngay_sinh.day))

    def in_thong_tin(self):
        """Trả về chuỗi thông tin sinh viên"""
        return f"MSSV: {self.ma_sv} - Họ và Tên: {self.ho_ten} - Ngày sinh: {self.ngay_sinh.strftime('%d/%m/%Y')} - Tuổi: {self.tuoi}"

class QuanLySinhVien:
    def __init__(self):
        """Khởi tạo danh sách sinh viên"""
        self.danh_sach = []

    def them_sinh_vien(self, sv: SinhVien):
        """Thêm một sinh viên vào danh sách"""
        self.danh_sach.append(sv)

    def tong_so_sinh_vien(self):
        """Tính tổng số sinh viên"""
        return len(self.danh_sach)

    def tim_sinh_vien_theo_ten(self, ten: str):
        """Tìm sinh viên theo tên"""
        return [sv for sv in self.danh_sach if sv.ten.lower() == ten.lower()]

    def tim_sinh_vien_theo_thang_sinh(self, thang: int):
        """Tìm sinh viên có ngày sinh trong tháng hiện tại"""
        return [sv for sv in self.danh_sach if sv.ngay_sinh.month == thang]

    def sap_xep_tang_dan_tuoi(self):
        """Sắp xếp danh sách sinh viên tăng dần theo tuổi"""
        self.danh_sach.sort(key=lambda sv: sv.tuoi)

    def hien_thi_danh_sach(self):
        """In ra danh sách sinh viên"""
        for sv in self.danh_sach:
            print(sv.in_thong_tin())

qlsv = QuanLySinhVien()

# Thêm sinh viên
qlsv.them_sinh_vien(SinhVien("SV001", "Nguyễn Văn A", "2002-05-15"))
qlsv.them_sinh_vien(SinhVien("SV002", "Trần Thị B", "2001-12-20"))
qlsv.them_sinh_vien(SinhVien("SV003", "Lê Văn C", "2000-06-10"))

# Hiển thị danh sách sinh viên
print("Danh sách sinh viên:")
qlsv.hien_thi_danh_sach()

# Tìm sinh viên theo tên
ten_tim = "B"
print(f"\nTìm sinh viên tên '{ten_tim}':")
for sv in qlsv.tim_sinh_vien_theo_ten(ten_tim):
    print(sv.in_thong_tin())

# Tìm sinh viên theo tháng sinh hiện tại
thang_hien_tai = datetime.today().month
print(f"\nSinh viên có ngày sinh trong tháng {thang_hien_tai}:")
for sv in qlsv.tim_sinh_vien_theo_thang_sinh(thang_hien_tai):
    print(sv.in_thong_tin())

# Sắp xếp danh sách theo tuổi
qlsv.sap_xep_tang_dan_tuoi()
print("\nDanh sách sinh viên sau khi sắp xếp theo tuổi:")
qlsv.hien_thi_danh_sach()