from django.urls import path
from .views import ExcelUploadView
from . import views

urlpatterns = [
    # path('upload/', views.upload_phone_numbers, name='upload_phone_numbers'),
    path('upload-file/', ExcelUploadView.as_view(), name='upload-file'),
    path('phone-numbers/', views.PhoneNumberListView.as_view(), name='phone-number-list'),
    path('phone-numbers/<int:pk>/', views.PhoneNumberDetailView.as_view(), name='phone-number-detail'),
]


