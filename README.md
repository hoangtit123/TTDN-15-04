---
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)


# Giới thiệu về dự án quản lý phòng họp
## Hệ thống sẽ được triển khai trong các doanh nghiệp có quy mô vừa và lớn, nơi có nhiều phòng họp và nhu cầu tổ chức cuộc họp thường xuyên. Ngoài ra, hệ thống cũng có thể được mở rộng để áp dụng cho các tổ chức giáo dục, cơ quan hành chính và doanh nghiệp đa chi nhánh có nhu cầu quản lý phòng họp phức tạp. Dự án bao gồm các chức năng sau:
- Quản lý phòng họp
- Quản lý thiết bị
- Người quản lý phòng
- Quản lý đặt phòng
- Tạo phòng họp
- Thêm thiết bị
- Thêm người quản lý phòng

  ![image](https://github.com/user-attachments/assets/5f578112-c6a3-4792-b639-380e8c7243a2)
  ![image](https://github.com/user-attachments/assets/757c8b67-1dca-43aa-bac4-5e7f4bd932b9)
  ![image](https://github.com/user-attachments/assets/0d139ed6-61d3-4f22-bbc5-a9a5ad54be6c)
  ![image](https://github.com/user-attachments/assets/19ecf9cd-9f64-4187-af8e-8e2f8fd92901)
  ![image](https://github.com/user-attachments/assets/6bf6c90f-34e1-40d0-a507-f6cb49d8271f)
  ![image](https://github.com/user-attachments/assets/9a2c5376-f828-49a5-a8a6-ead3e732e8f2)
  ![image](https://github.com/user-attachments/assets/a0c6b592-fefe-4324-91e1-521b68b85725)








# 1. Cài đặt công cụ, môi trường và các thư viện cần thiết

## 1.1. Clone project.
```
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
```
```
cd odoo-fitdnu
```

```
git checkout cntt15_04
```


## 1.2. cài đặt các thư viện cần thiết

Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
## 1.3. khởi tạo môi trường ảo.

Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
python3.10 -m venv ./venv
```
```
source venv/bin/activate
```
```
pip3 install -r requirements.txt
```

# 2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo apt install docker-compose
```
```
sudo docker-compose up -d
```

# 3. Setup tham số chạy cho hệ thống

## 3.1. Khởi tạo odoo.conf

Tạo tệp **odoo.conf** có nội dung như sau:

```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5434
xmlrpc_port = 8069
```

# 4. Chạy hệ thống và cài đặt các ứng dụng cần thiết

Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```


Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

Hoàn tất
    
