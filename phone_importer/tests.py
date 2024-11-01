# from django.test import TestCase
# from phone_importer.models import PhoneNumber
#
# class PhoneNumberTestCase(TestCase):
#     def setUp(self):
#         PhoneNumber(phone_number='09012345678').save()
#
#     def tearDown(self):
#         PhoneNumber.drop_collection()  # پاک کردن کل مجموعه برای جلوگیری از تکرار داده‌ها
#
#     def test_duplicate_phone_number(self):
#         try:
#             PhoneNumber(phone_number='09012345678').save()
#             self.assertTrue(True)  # شماره تکراری باید ذخیره شود
#         except Exception as e:
#             self.fail(f"Failed to save duplicate phone number: {e}")
