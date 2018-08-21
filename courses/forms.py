from django import forms
from django.forms.fields import ChoiceField


class ExamForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        questions = list(args).pop(0)
        
        choices = list()
        
        for question in questions:
            for alternative in question.alternatives.all():
                choices.append((alternative.pk, alternative.description))
            field = ChoiceField(widget=forms.RadioSelect, choices=choices)
            self.fields.append(field)    
        
        
        
        
        
        
    