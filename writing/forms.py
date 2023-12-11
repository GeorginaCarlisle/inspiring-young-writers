from django import forms
from django.core.exceptions import ValidationError
from profanity_check import predict
from .models import Writing


""" Validator which predicts whether the strings in the array it is passed are offensive
If they are predicted to be offensive the string is given a value of 1, else a value of 0 """
def no_profanity(value):
    prediction = predict([value])

    if prediction != 0:
        raise ValidationError(
            "Profanity is not allowed at Inspiring Writers. Please ask your\
                parent/gardian to take out any text that might be classed as profanity"
        )


class CreateWritingForm(forms.ModelForm):

    # Run field values through profanity validator
    title = forms.CharField(validator=[no_profanity])
    body = forms.Textarea(validator=[no_profanity])

    class Meta:
        model = Writing
        fields = ("title", "body")

    # Add borders around input boxes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['body'].widget.attrs.update(
            {'class': 'border border-black'})