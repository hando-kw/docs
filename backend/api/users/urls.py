from django.urls import path

from . import views

urlpatterns = [
    path('send-otp/', views.SendOtpView.as_view(), name='send-otp'),
    path('verify-otp/', views.VerifyOtpView.as_view(), name='verify-otp'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('profile/', views.ProfileRetrieveUpdateView.as_view(), name='profile'),
    
    path('update-mobile/', views.UpdateMobileView.as_view(), name='update-mobile'),
    path('verify-update-mobile/', views.VerifyUpdateMobileView.as_view(), name='verify-update-mobile'),
    
    path('address/', views.UserAddressListCreateView.as_view(), name='address'),
    path('address/<int:pk>/', views.UserAddressRetrieveUpdateDestroyView.as_view(), name='address-detail'),
]