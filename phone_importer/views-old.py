import pandas as pd
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PhoneNumber

logging.basicConfig(level=logging.INFO)

@api_view(['POST'])
def upload_phone_numbers(request):
    if 'file' not in request.FILES:
        return Response({"message": "No file provided"}, status=400)

    file = request.FILES['file']

    # خواندن فایل اکسل
    try:
        df = pd.read_excel(file, header=None)
    except Exception as e:
        logging.error(f"Error reading Excel file: {e}")
        return Response({"message": "Error reading the Excel file"}, status=400)

    # حذف ردیف‌های خالی
    df.dropna(how="all", inplace=True)

    # ساخت لیستی از شماره‌ها
    phone_numbers = []
    for _, row in df.iterrows():
        for phone_number in row:
            if phone_number:  # بررسی خالی نبودن شماره
                phone_numbers.append(str(phone_number))

    logging.info(f"Phone numbers to be saved: {phone_numbers}")

    # ذخیره‌سازی با جلوگیری از تکرار
    total_inserted = 0
    for phone_number in phone_numbers:
        try:
            PhoneNumber(phone_number=phone_number).save()  # ذخیره شماره
            total_inserted += 1
        except Exception as e:
            logging.warning(f"Could not save phone number {phone_number}: {e}")

    total_records = PhoneNumber.objects.count()
    logging.info(f"Total records in database: {total_records}")
    return Response({"message": f"Phone numbers uploaded successfully. Total inserted: {total_inserted}, Total records in database: {total_records}"})
