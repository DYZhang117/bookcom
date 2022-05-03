from django import forms
from webinfo.models import Book, Author, Post, Comment, Activity, SystemUser, Participate, Prefer, Like, Explain, Write
from django.forms.widgets import DateInput, TimeInput
# from django.forms.widgets import DateTimeInput


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_book_name(self):
        return self.cleaned_data['book_name'].strip()


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class UserForm(forms.ModelForm):
    class Meta:
        model = SystemUser
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean_post_title(self):
        return self.cleaned_data['post_title'].strip()

    def clean_content(self):
        if self.cleaned_data['content'] == 'NA':
            result = self.cleaned_data['content']
        else:
            result = self.cleaned_data['content'].strip()
        return result


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def clean_content(self):
        return self.cleaned_data['content'].strip()


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
        }


    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_address(self):
        return self.cleaned_data['address'].strip()

    def clean_description(self):
        if self.cleaned_data['description'] == 'NA':
            result = self.cleaned_data['description']
        else:
            result = self.cleaned_data['description'].strip()
        return result


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__'


class PreferForm(forms.ModelForm):
    class Meta:
        model = Prefer
        fields = '__all__'


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = '__all__'


class ExplainForm(forms.ModelForm):
    class Meta:
        model = Explain
        fields = '__all__'


class ParticipateForm(forms.ModelForm):
    class Meta:
        model = Participate
        fields = '__all__'
