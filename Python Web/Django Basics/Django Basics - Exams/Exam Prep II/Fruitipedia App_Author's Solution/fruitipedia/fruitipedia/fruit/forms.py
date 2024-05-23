from django import forms

from fruitipedia.fruit.models import Fruit


class BaseClassFruitForm(forms.ModelForm):

    class Meta:
        model = Fruit

        exclude = ('owner',)


class CreateFruitForm(BaseClassFruitForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)

        labels = {
            'fruit_name': '',
            'fruit_image_url': '',
            'description': '',
            'nutrition_info': '',
        }

        error_messages = {
            'fruit_name': {
                'unique': "This fruit name is already in use! Try a new one.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fruit_name'].widget.attrs['placeholder'] = 'Fruit Name'
        self.fields['fruit_image_url'].widget.attrs['placeholder'] = 'Fruit Image URL'
        self.fields['description'].widget.attrs['placeholder'] = 'Fruit Description'
        self.fields['nutrition_info'].widget.attrs['placeholder'] = 'Nutrition Info'


class EditFruitForm(BaseClassFruitForm):
    pass


class DeleteFruitForm(BaseClassFruitForm):

    class Meta:
        model = Fruit
        fields = ('fruit_name', 'fruit_image_url', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'