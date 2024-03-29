from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        
class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = models.Profile
        fields = '__all__'
        
class AddressSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = models.Address
        fields = '__all__'
        
class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beneficiary
        fields = '__all__'
        
class BankAccountSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # beneficiary = BeneficiarySerializer()
    class Meta:
        model = models.Bank_Account
        fields = '__all__'
        
class TransactionSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # bank_account = BankAccountSerializer()
    # beneficiary = BeneficiarySerializer()
    class Meta:
        model = models.Transaction
        fields = '__all__'
        
class CardSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = models.Card
        fields = '__all__'
        
class LoanSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = models.Loan
        fields = '__all__'
        
class LoanPaymentSerializer(serializers.ModelSerializer):
    # loan = LoanSerializer()
    # user = UserSerializer()
    class Meta:
        model = models.Loan_Payment
        fields = '__all__'