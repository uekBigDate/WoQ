from django.forms import ModelForm
from .models import News
from django.forms.widgets import FileInput

class Up_img(ModelForm):
    class Meta:  # 元类
        model = News
        fields = ['img']
        labels = {
            'img': '',
        }
        widgets = {
            'img': FileInput(attrs={
                'class': '_sub_file',
                'onchange': 'lookImg(this)',
                'accept': 'image/*',
                'multiple': 'multiple'
            })
        }
    def __init__(self, *args, **kwargs):
        super(Up_img, self).__init__(*args, **kwargs)
        self.fields['img'].required = False


