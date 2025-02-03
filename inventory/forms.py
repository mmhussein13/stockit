from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['part_number'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['bin_location'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['cost_per_item'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['reorder_level'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})


    class Meta:
        model = Stock
        fields = ['category', 'part_number', 'bin_location', 'name', 'quantity', 'cost_per_item', 'reorder_level']


class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']