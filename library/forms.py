from django import forms
from django.core.exceptions import ValidationError
from .models import Feedback

"""
Code for validation against swear words copied and adapted from an example given by Chatgpt
"""
SWEAR_WORD_LIST = ['fuck', 'shit', 'crap', 'bollocks', 'bitch', 'cock', 'cunt', 'cum', 'fucker', 'dick']

def validate_no_swearing(value):
    for swear_word in SWEAR_WORD_LIST:
        if swear_word.lower() in value.lower():
            raise forms.ValidationError(
                f"Swear word '{swear_word}' is not allowed. Please remove."
            )


class GiveFeedbackForm(forms.ModelForm):

    # Run field values through profanity validator
    star_one = forms.CharField(
        max_length=400,
        widget=forms.Textarea(attrs={
            'style': 'width: 100%; height: 3.5rem; padding: 4px'}),
        validators=[validate_no_swearing]
        )
    star_two = forms.CharField(
        max_length=400,
        widget=forms.Textarea(attrs={
            'style': 'width: 100%; height: 3.5rem; padding: 4px'}),
        validators=[validate_no_swearing]
        )
    wish = forms.CharField(
        max_length=400,
        widget=forms.Textarea(attrs={
            'style': 'width: 100%; height: 3.5rem; padding: 4px'}),
        validators=[validate_no_swearing]
        )
    
    class Meta:
        model = Feedback
        fields = ("star_one", "star_two", "wish")

    # Add borders around input boxes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['star_one'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['star_two'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['wish'].widget.attrs.update(
            {'class': 'border border-black'})
    
    # Make sure star_one is cleaned
    def clean_star_one(self):
        star_one = self.cleaned_data.get('star_one')

        return star_one

    # Make sure star_two is cleaned
    def clean_star_two(self):
        star_two = self.cleaned_data.get('star_two')

        return star_two
    
    # Make sure wish is cleaned
    def clean_wish(self):
        wish = self.cleaned_data.get('wish')

        return wish

    # Add additional fields to be generated on saving of the form
    def save(self, commit=True, giver=None, writing=None, date_created=None, date_last_edit=None):
        feedback = super().save(commit=False)

        if giver:
             feedback.giver = giver

        if writing:
             feedback.writing = writing

        if date_created:
            feedback.date_created = date_created

        if date_last_edit:
            feedback.date_last_edit = date_last_edit

        if commit:
            feedback.save()

        return feedback
