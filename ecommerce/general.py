from .models import Setting


def send_setting_data(request):
    content = {
        'settingData': Setting.objects.last()
    }

    return content


def make_title(request):
    content = {
        'title': 'My-Project'
    }
    return content
