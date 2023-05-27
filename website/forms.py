from django import forms
from website.models import Benchmark

class BenchmarkForm(forms.ModelForm):
    class Meta:
        model = Benchmark
        fields = ('type_analysis', 'country', 'industry', 'credit_rating_borrower', 'currency', 'principal', 'type_of_interest_rate', 'base_rate')

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

