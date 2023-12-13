from django import forms
from django.core.exceptions import ValidationError
#from profanity_check import predict
from .models import Writing


""" Validator which predicts whether the strings in the array it is passed are offensive
If they are predicted to be offensive the string is given a value of 1, else a value of 0 """
#def no_profanity(value):
#    prediction = predict([value])
#
#    if prediction != 0:
#        raise ValidationError(
#            "Profanity is not allowed at Inspiring Writers. Please ask your\
#                parent/gardian to take out any text that might be classed as profanity"
#        )


class CreateWritingForm(forms.ModelForm):

    # Run field values through profanity validator
    title = forms.CharField(
        max_length=50,
        #validator=[no_profanity]
        widget=forms.TextInput(attrs={
            'style': 'width: 85%;',
            'placeholder': 'Draw others in. What is your writing about?'}))
    body = forms.CharField(
        #validator=[no_profanity],
        widget=forms.Textarea(attrs={
            'style': 'width: 100%;',
            'placeholder': 'A poem, a joke, a story, an article? It is up to you!'})
        )

    class Meta:
        model = Writing
        fields = ("title", "body")

    # Add borders around input boxes and .....
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'border border-black'})
        self.fields['body'].widget.attrs.update(
            {'class': 'border border-black'})


    # Check title is unique
    def clean_title(self):
        title = self.cleaned_data.get('title')

        if Writing.objects.filter(title=title).exists():
            raise forms.ValidationError(
                'Your title must be unique and there is already work with this title. \
                        Please make a change to your title and try again.'
            )
        
        return title


    # Add additional fields to be generated on saving of the form
    def save(self, commit=True, author=None, slug=None, updated_on=None, pending_approval=False, date_submitted=None):
        writing = super().save(commit=False)

        if author:
             writing.author = author

        if slug:
             writing.slug = slug

        if updated_on:
            writing.updated_on = updated_on

        if pending_approval:
            writing.pending_approval = pending_approval
            
        if date_submitted:
            writing.date_submitted = date_submitted

        if commit:
            writing.save()
        return writing


