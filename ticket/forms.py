from django.forms import ModelForm
from .models import Ticket
from django import forms

class AddTicketForm(forms.ModelForm):
    """Форма добавления тикетов"""
    
    class Meta:
        model = Ticket
        fields = ('category', 'title', 'text')