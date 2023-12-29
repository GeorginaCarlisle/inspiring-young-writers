from django import forms
from .models import Feedback


SWEAR_WORD_LIST = ['fuck', 'shit', 'crap', 'bollocks', 'bitch', 'cock',
                   'cunt', 'cum', 'fucker', 'dick', 'bastard']


def validate_no_swearing(value):
    """
    Custom validator checking for any of the listed swear words and
    should any be found inform the user that the word in question
    is not allowed. Code copied and adapted from an example given
    by chatgpt.
    """
    for swear_word in SWEAR_WORD_LIST:
        if swear_word.lower() in value.lower():
            raise forms.ValidationError(
                f"Swear word '{swear_word}' is not allowed. Please remove."
            )


class GiveFeedbackForm(forms.ModelForm):
    """
    Form to handle creating a new instance of feedback.
    Including form styling and validation
    """

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

    def __init__(self, *args, **kwargs):
        """
        Function to add borders around input boxes
        """
        super().__init__(*args, **kwargs)
        self.fields['star_one'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['star_two'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['wish'].widget.attrs.update(
            {'class': 'border border-black'})

    def clean_star_one(self):
        """
        Function to clean and validate star one
        """
        star_one = self.cleaned_data.get('star_one')

        return star_one

    def clean_star_two(self):
        """
        Function to clean and validate star two
        """
        star_two = self.cleaned_data.get('star_two')

        return star_two

    def clean_wish(self):
        """
        Function to clean and validate the wish
        """
        wish = self.cleaned_data.get('wish')

        return wish

    # Add additional fields to be generated on saving of the form
    def save(
            self,
            commit=True,
            giver=None,
            writing=None,
            date_created=None,
            date_last_edit=None,
            approved=None):
        """
        Function to save the form and therefore create a new instance of
        feedback also passing in data created within the view
        """

        feedback = super().save(commit=False)

        if giver:
            feedback.giver = giver

        if writing:
            feedback.writing = writing

        if date_created:
            feedback.date_created = date_created

        if date_last_edit:
            feedback.date_last_edit = date_last_edit

        if approved:
            feedback.approved = approved

        if commit:
            feedback.save()

        return feedback
