from django import forms

from catalog.models import Product, Version

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        for word in forbidden_words:
            if word in cleaned_name:
                raise forms.ValidationError('Название не может содержать запрещенные слова')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in cleaned_description:
                raise forms.ValidationError('Описание не может содержать запрещенные слова')
        return cleaned_description


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
