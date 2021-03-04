from django import forms

from webapp.models import List

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('describe', 'description', 'status', 'date_of_completion')

# class ListDeleteForm(forms.Form):
#     describe = forms.TimeField(max_length=150, required=True, label='Enter of the task, to delete! ')