from django.urls import path, include
from . import views

urlpatterns = [
    # User
    path('users/register/', views.UserCreateView.as_view(), name='users_register'),
    path('users/', views.UserListView.as_view(), name='users_list'),
    path('users/<uuid:pk>/', views.CustomUser_DetailView.as_view(), name='user_detail'),
    
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # Profile
    path('profiles/', views.Profile_ListCreateAPIView.as_view(), name='profiles_list'),
    path('profiles/<uuid:pk>/', views.Profile_Detail_APIView.as_view(), name='profile_detail'),

    # Address
    path('address/', views.Address_ListCreateAPIView.as_view(), name="address_list"),
    path('address/<uuid:pk>/', views.Address_Detail_APIView.as_view(), name='address_detail'),

    # Beneficiary
    path('beneficiary/', views.Beneficiary_ListCreateAPIView.as_view(), name="beneficiary_list"),
    path('beneficiary/<uuid:pk>/', views.Beneficiary_Detail_APIView.as_view(), name='beneficiary_detail'),

    # Bank_Account
    path('bank_accounts/', views.Bank_Account_ListCreateAPIView.as_view(), name="bank_account_list"),
    path('bank_account/<uuid:pk>/', views.Bank_Account_Detail_APIView.as_view(), name='bank_account_detail'),

    # Transaction
    path('transactions/', views.Transaction_ListCreateAPIView.as_view(), name="transaction_list"),
    path('transaction/<uuid:pk>/', views.Transaction_Detail_APIView.as_view(), name='transaction_detail'),

    # Card
    path('cards/', views.Card_ListCreateAPIView.as_view(), name="card_list"),
    path('card/<uuid:pk>/', views.Card_Detail_APIView.as_view(), name='card_detail'),

    # Loan
    path('loans/', views.Loan_ListAPIView.as_view(), name="loan_list"),
    path('new_loans/', views.Loan_CreateAPIView.as_view(), name="new_loan"),
    path('loan/<uuid:pk>/', views.Loan_Detail_APIView.as_view(), name='loan_detail'),
    
    # Loan_Payment
    path('loan_payments/', views.Loan_Payment_ListCreateAPIView.as_view(), name="loan_payment_list"),
    path('loan_payment/<uuid:pk>/', views.Loan_Payment_Detail_APIView.as_view(), name='loan_payment_detail'),
    
    # Branches
    path('branches/', views.Branch_ListCreateAPIView.as_view(), name="card_list"),
    path('branches/<uuid:pk>/', views.Branch_Detail_APIView.as_view(), name='card_detail'),
]