from django import forms


class CategoriesListForm(forms.Form):
    order_by = forms.ChoiceField(choices=(
        ('title', 'Title asc'),
        ('-title', 'Title desc'),
        ('id', 'ID'),
        ('events.count', 'Events number')
    ), required=False)
    search = forms.CharField(required=False)
