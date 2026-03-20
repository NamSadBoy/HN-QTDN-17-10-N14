# 🏢 Hệ thống Quản trị Nhân sự - Chấm công - Tính lương (Odoo 15)

Đây là mã nguồn Bài tập lớn phát triển các module mở rộng trên nền tảng ERP Odoo 15.0. Hệ thống cung cấp giải pháp toàn diện từ lúc nhân viên bước chân vào công ty (Hồ sơ), làm việc hàng ngày (Chấm công), nhận lương cuối tháng (Tính lương) cho đến việc lưu trữ giấy tờ (Quản lý văn bản).

## 📦 Cấu trúc Hệ thống

Dự án bao gồm 4 module cốt lõi được thiết kế liên kết chặt chẽ với nhau:

### 1. Module Nhân sự (`nhan_su`)
- Quản lý hồ sơ nhân viên, phòng ban.
- Cấu hình **Chức vụ** kèm theo **Hệ số lương** và **Lương cơ bản mặc định** (Tự động áp dụng cho nhân viên).
- Quản lý **Danh sách Bằng cấp/Chứng chỉ** và **Lịch sử công tác**.
- Cấu hình thông tin tham gia Bảo hiểm (Tỷ lệ đóng BHXH, BHYT, BHTN).

### 2. Module Chấm công (`cham_cong`)
- Quản lý danh mục **Ca làm việc** (Giờ vào/ra chuẩn, thời gian cho phép đi muộn).
- Lên **Lịch đăng ký ca** cho từng nhân viên theo ngày.
- Ghi nhận thời gian **Check-in / Check-out** thực tế.
- **Tính năng tự động:** - Tự động nhận diện đi muộn / về sớm và áp dụng mức phạt (100.000 VNĐ/lần).
  - Tự động đối chiếu **Danh mục Ngày lễ** để nhân đôi (x2) công làm việc.

### 3. Module Tính lương (`tinh_luong`)
- Tự động tổng hợp dữ liệu từ Nhân sự và Chấm công.
- Tính toán **Ngày công thực tế** và **Tiền phạt đi muộn/về sớm**.
- Tự động khấu trừ tiền Bảo hiểm (BHXH 8%, BHYT 1.5%, BHTN 1%).
- Cho phép Kế toán thêm các khoản **Thưởng / Phạt thủ công**.
- Xuất **Phiếu lương** tổng hợp với con số Thực lãnh (Net Salary) chính xác.

### 4. Module Quản lý Văn bản (`quan_ly_van_ban`)
- Số hóa hồ sơ, tài liệu liên quan đến nhân sự.
- Quản lý Hợp đồng lao động, Quyết định bổ nhiệm, Biên bản kỷ luật...
- Cho phép đính kèm file (PDF, Word, Ảnh) trực tiếp lên hệ thống.

---

## ⚙️ Hướng dẫn Cài đặt & Khởi chạy

**Yêu cầu môi trường:** Ubuntu / WSL, Python 3.x, PostgreSQL và Odoo 15.0.

**Bước 1: Tải mã nguồn**
Mở Terminal và clone kho lưu trữ này về máy:
```bash
git clone [https://github.com/NamSadBoy/HN-QTDN-17-10-N14.git](https://github.com/NamSadBoy/HN-QTDN-17-10-N14.git)
```

Cài đặt các thư viện cần thiết
Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
Khởi tạo môi trường ảo.
- Khởi tạo môi trường ảo
```
python3.10 -m venv ./venv
```
- Thay đổi trình thông dịch sang môi trường ảo
```
source venv/bin/activate
```
- Chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
pip3 install -r requirements.txt
```
Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo docker-compose up -d
```
Setup tham số chạy cho hệ thống
Tạo tệp **odoo.conf** có nội dung như sau:
```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5431
xmlrpc_port = 8069
```
Có thể kế thừa từ file **odoo.conf.template**
Chạy hệ thống và cài đặt các ứng dụng cần thiết
Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```
Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.



---

    
