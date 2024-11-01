# import requests
# from mongoengine import connect
# from phone_importer.models import PhoneNumber
#
#
# # اتصال به دیتابیس
# connect('phone_data_db', host='localhost', alias='default')
# # پاک کردن تمام شماره‌ها
# PhoneNumber.objects.delete()
#
#
# url = 'http://127.0.0.1:8000/phone/upload/'
#
# # باز کردن فایل با دستور with تا پس از ارسال درخواست بسته شود
# with open('../file/users_sample_data_with_random_phone.xlsx', 'rb') as file:
#     files = {'file': file}
#     response = requests.post(url, files=files)
#
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
