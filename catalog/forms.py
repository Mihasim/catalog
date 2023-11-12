from django import forms

from catalog.models import Product, Version

bad_name = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for name in bad_name:
            if name in cleaned_data.lower():
                raise forms.ValidationError('Название продукта содержит запрещенные значения')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'flag_of_the_cur_ver':
                field.widget.attrs['class'] = 'form-control'

    def active_version(self):
        cleaned_data = self.cleaned_data.get('flag_of_the_cur_ver')
        if cleaned_data:
            raise forms.ValidationError('Название продукта содержит запрещенные значения')
        return cleaned_data