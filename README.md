# Phone Data Importer Project

## Overview
این پروژه یک API ایجاد می‌کند که به کاربران اجازه می‌دهد شماره‌های تلفن را از فایل‌های Excel وارد کرده و داده‌ها را در MongoDB ذخیره کنند. همچنین شامل قابلیت‌های کامل CRUD (ایجاد، خواندن، به‌روزرسانی و حذف) برای شماره‌های تلفن است.

## Features
- **Import Phone Numbers:** دریافت و ذخیره شماره‌های تلفن از فایل Excel.
- **CRUD Operations:** قابلیت ایجاد، خواندن، به‌روزرسانی و حذف برای شماره‌های تلفن.

## Requirements
- Python 3.9+
- MongoDB
- Docker (برای اجرای کانتینرهای پروژه)

## Installation
کلون کردن پروژه:

```bash
git clone <your-repository-url>
cd phone_Project
نصب وابستگی‌ها:

bash

pip install -r requirements.txt
اجرای Docker Compose: برای اجرای پروژه و MongoDB با Docker:

bash

docker-compose up --build
API Endpoints
Import Phone Numbers
URL: /api/phones/import/
Method: POST
Description: این اندپوینت برای آپلود فایل Excel و وارد کردن شماره‌های تلفن به MongoDB استفاده می‌شود.
cURL Example:
bash

curl -X POST "http://localhost:8000/api/phones/import/" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your/excel_file.xlsx"
Create a Phone Number
URL: /api/phones/
Method: POST
Description: ایجاد یک شماره تلفن جدید.
cURL Example:
bash

curl -X POST "http://localhost:8000/api/phones/" \
     -H "Content-Type: application/json" \
     -d '{"phone_number": "1234567890"}'
Read All Phone Numbers
URL: /api/phones/
Method: GET
Description: دریافت لیست تمام شماره‌های تلفن.
cURL Example:
bash

curl -X GET "http://localhost:8000/api/phones/"
Update a Phone Number
URL: /api/phones/<id>/
Method: PUT
Description: به‌روزرسانی شماره تلفن با شناسه مشخص.
cURL Example:
bash

curl -X PUT "http://localhost:8000/api/phones/<id>/" \
     -H "Content-Type: application/json" \
     -d '{"phone_number": "0987654321"}'
Delete a Phone Number
URL: /api/phones/<id>/
Method: DELETE
Description: حذف شماره تلفن با شناسه مشخص.
cURL Example:
bash

curl -X DELETE "http://localhost:8000/api/phones/<id>/"
