from django import forms
from django.core.exceptions import ValidationError
from .models import Writing

"""
Code for validation against swear words copied and adapted from
an example given by Chatgpt
"""
SWEAR_WORD_LIST = ['fuck', 'shit', 'crap', 'bollocks', 'bitch', 'cock',
                   'cunt', 'cum', 'fucker', 'dick']


def validate_no_swearing(value):
    for swear_word in SWEAR_WORD_LIST:
        if swear_word.lower() in value.lower():
            raise forms.ValidationError(
                f"Swear word '{swear_word}' is not allowed. Please remove."
            )


class CreateWritingForm(forms.ModelForm):

    # Run field values through profanity validator
    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'style': 'width: 85%;',
            'placeholder': 'Draw others in. What is your writing about?'}),
        validators=[validate_no_swearing]
        )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'style': 'width: 100%; padding: 4px',
            'placeholder': 'A poem, a joke, a story, an article? \
                It is up to you!'}),
        validators=[validate_no_swearing]
        )

    class Meta:
        model = Writing
        fields = ("title", "body")

    def __init__(self, *args, **kwargs):
        # Add borders around input boxes
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['body'].widget.attrs.update(
            {'class': 'border border-black'})

    def clean_title(self):
        # Check title is unique but only when the writing is first created
        title = self.cleaned_data.get('title')

        """
        The following statement was adapted from an example provided
        by Chatgpt.
        """
        if Writing.objects.filter(title=title) \
                .exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                'Your title must be unique and there is already work with \
                    this title. Please make a change to your title and \
                        try again.'
            )
        return title

    def clean_body(self):
        # Make sure body is cleaned
        body = self.cleaned_data.get('body')

        return body

    def save(self, commit=True, author=None, slug=None, updated_on=None,
             pending_approval=None, date_submitted=None, approved=None,
             failed_approval=None):
        # Add additional fields to be generated on saving of the form

        writing = super().save(commit=False)

        if author:
            writing.author = author

        if slug:
            writing.slug = slug

        if updated_on:
            writing.updated_on = updated_on

        if pending_approval is not None:
            writing.pending_approval = pending_approval

        if date_submitted:
            writing.date_submitted = date_submitted

        if approved is not None:
            writing.approved = approved

        if failed_approval is not None:
            writing.failed_approval = failed_approval

        if commit:
            writing.save()

        return writing
