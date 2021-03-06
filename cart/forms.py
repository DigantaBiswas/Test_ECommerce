from django import forms

PRODUCT_QUANTITY_CHOISE = [(i, str(i)) for i in range(1,26)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOISE, coerce = int)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
	