from django import forms

from catalog.models import Product, Version

bad_name = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'flag_of_the_cur_ver':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for name in bad_name:
            if name in cleaned_data.lower():
                raise forms.ValidationError('Название продукта содержит запрещенные значения')
        return cleaned_data


class ModerProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'description', 'category')


class VersionForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

