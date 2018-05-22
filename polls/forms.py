from django import forms
from .models import Answer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML

class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout.append(Submit('save', 'Eintragen', css_class="btn-success"))
        self.helper.layout.append(HTML('<a class="btn btn-danger" href="{% url "index" %}"><span class="glyphicon glyphicon-remove"></span>Abbrechen</a>'))

    class Meta:
        model = Answer
        exclude = []
