from django import forms

from .models import CaseManagement


class CaseManagementForm(forms.ModelForm):
    class Meta:
        model = CaseManagement
        fields = ["return_info", "reason", "status"]
