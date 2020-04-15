from django import forms
from .models import Plan


class RegisterPlanAPIForm(forms.ModelForm):
    """プラン登録APIのバリデーションForm"""

    def clean_description(self):
        print(f'{"="*25}')
        print(self.cleaned_data)
        print(f'{"="*25}')
        print(self._errors)
        if len(self.cleaned_data.get("description")) < 3:
            raise forms.ValidationError("内容は3文字以上で入力してください")
        return self.cleaned_data["description"]

    def clean_image(self):

        print(self.cleaned_data.get("image"))
        # if len(self.cleaned_data.get("image")) < 3:
        #     raise forms.ValidationError("内容は3文字以上で入力してください")
        return self.cleaned_data["image"]

    class Meta:
        model = Plan
        fields = (
            "title",
            "image",
            "price",
            "description",
        )


class UploadFileForm(forms.Form):
    file = forms.FileField()
