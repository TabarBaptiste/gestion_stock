from django import forms
from .models import Piece

class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'

class ImportExcelForm(forms.Form):
    excel_file = forms.FileField()