from rest_framework import serializers
from .models import Invoice, Screenshot

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
    
class ScreenshotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = [
            'screenshot'
        ]