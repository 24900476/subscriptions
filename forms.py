from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan', 'end_date', 'is_active']  # Removed start_date
        widgets = {
            'end_date': forms.SelectDateWidget(),
        }
