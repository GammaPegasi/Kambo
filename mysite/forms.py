from django import forms

from django.core.exceptions import ValidationError

# https://docs.djangoproject.com/es/2.1/ref/forms/validation/

# https://stackoverflow.com/questions/4914123/django-how-to-process-clean-a-field-before-validation

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    # password = forms.PasswordInput(attrs=None, render_value=True)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'for' : 'email'})


    def clean(self):
        if 'newsletter_sub' in self.data:
            # do subscribe
            pass
        elif 'newsletter_unsub' in self.data:
            # do unsubscribe
            pass


    # password = forms.CharField(max_length=100)
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # # cc_myself = forms.BooleanField(required=False)

    # def clean_subject(self):
    #     subjectCleaned = self.cleaned_data['subject']
    #     if len(subjectCleaned) < 3:
    #         raise ValidationError('Subject length should not be less than 3')

    #     if len(subjectCleaned) > 5:
    #         raise ValidationError('Subject length should not be more than 5')


    # def clean_message(self):
    #     messageCleaned= self.cleaned_data['message']

    #     if len(messageCleaned) <= 2:
    #         raise ValidationError('Messge length should not be more than 2')


class ValidForm(forms.Form):
    # password = forms.PasswordInput(attrs=None, render_value=True)
    username = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs = {'class' : 'myspecialClass'}), initial='write something here ...')
    sender = forms.EmailField()
    flag = forms.BooleanField(required=True)
    receive_newsletter = forms.BooleanField()

    error_css_class = 'error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(ValidForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'for' : 'email'})

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) >= 5:
            raise ValidationError('Too many characters ...')
        return message

    def clean(self):
        if 'newsletter_sub' in self.data:
            # do subscribe
            pass
        elif 'newsletter_unsub' in self.data:
            # do unsubscribe
            pass

