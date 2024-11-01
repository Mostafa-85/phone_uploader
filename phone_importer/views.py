import pandas as pd
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExcelUploadSerializer
from .serializers import PhoneNumberSerializer
from .models import PhoneNumber

logging.basicConfig(level=logging.INFO)

class ExcelUploadView(APIView):
    def post(self, request):
        serializer = ExcelUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']

            df = pd.read_excel(file)
            df.dropna(how="all", inplace=True)

            phone_numbers = df.iloc[:, 0].dropna().astype(str).tolist()

            total_inserted = 0
            for phone_number in phone_numbers:
                try:
                    PhoneNumber(phone_number=phone_number).save()
                    total_inserted += 1
                except Exception as e:
                    logging.warning(f"Could not save phone number {phone_number}: {e}")

            return Response({"total_inserted": total_inserted}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        aa = PhoneNumber.objects.all()
        return Response(aa, status=status.HTTP_200_OK)

class PhoneNumberListView(APIView):
    # Create and List phone numbers
    def get(self, request):
        phone_numbers = PhoneNumber.objects.all()
        serializer = PhoneNumberSerializer(phone_numbers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneNumberDetailView(APIView):
    # Retrieve, Update, and Delete a single phone number by ID
    def get_object(self, pk):
        try:
            return PhoneNumber.objects.get(pk=pk)
        except PhoneNumber.DoesNotExist:
            return None

    def get(self, request, pk):
        phone_number = self.get_object(pk)
        if phone_number is None:
            return Response({"error": "Phone number not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PhoneNumberSerializer(phone_number)
        return Response(serializer.data)

    def put(self, request, pk):
        phone_number = self.get_object(pk)
        if phone_number is None:
            return Response({"error": "Phone number not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PhoneNumberSerializer(phone_number, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        phone_number = self.get_object(pk)
        if phone_number is None:
            return Response({"error": "Phone number not found"}, status=status.HTTP_404_NOT_FOUND)
        phone_number.delete()
        return Response(status=status.HTTP_204_NO_CONT)