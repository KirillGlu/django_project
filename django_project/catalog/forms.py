from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    unused_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    version = forms.ModelChoiceField(queryset=Version.objects.all(), empty_label="Выберите версию", required=False)

    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'purchase_price', 'image',)

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        for word in self.unused_words:
            if word in cleaned_name:
                raise forms.ValidationError(f'Слово {word} запрещено')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        for word in self.unused_words:
            if word in cleaned_description:
                raise forms.ValidationError(f'Слово {word} запрещено')
        return cleaned_description

    def clean(self):
        cleaned_version = super().clean()
        active_versions = [version for version in self.cleaned_data.get('versions', []) if version.is_active]

        if len(active_versions) > 1:
            raise forms.ValidationError("Выберите одну активную версию продукта.")