import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..forms import RegisterPlanAPIForm
from io import BytesIO
from PIL import Image
from ..forms import UploadFileForm

# from core.forms import (
#     RegisterEntryAPIForm,
#     create_error_dict_from_form_errors,
# )


@csrf_exempt
def api_entry(request):
    """記事投稿API"""
    print(f'{"="*125}')
    print("ここまで届いた")
    print(request.body)
    print(len(request.body))
    print(type(request.body.title))
    # print(request.FILES["image"])
    print(f'{"="*125}')

    # img = Image.open(BytesIO(request.body.image))
    # img = Image.open(request.body)
    # print(img)
    # print(request.FILES['image'])

    # image = request.files['filename']
    # print(image)
    # img = Image.open(BytesIO(request.body))
    # print(img)
    # params = json.loads(request.body)
    # form = RegisterPlanAPIForm(params)

    # aa = form.is_valid()

    # print(form.errors)
    # print(aa)
    # print(params)
    return JsonResponse({"a": "aaa"})


# {'title': 'faああああ', 'description': 'a', 'image': '1802265top.jpg','price': '1222', 'tags': ['記念日', 'きょうは']}
# {'title': 'ファ', 'description': 'ああ', 'image': < InMemoryUploadedFile: 似顔絵.jpeg (image/jpeg) > , 'price': 12, 'tags': [ < Tag: インスターグラマー > ]}


# =====================================================================================

# form.is_valid()
# form.is_valid()はTrueを返し、不合格の場合はFalseを返す。
# is_valid()を行うことでバリデーションが行われる

# form.errorsを行うことで、バリデーションのエラーを見ることができる


# =====================================================================================


# def api_entry(request):
#     """ 記事投稿API """
#     params = json.loads(request.body)
#     form = RegisterEntryAPIForm(params)
#     if not form.is_valid():
#         return JsonResponse(create_error_dict_from_form_errors(form.errors), status=400)

#     entry = form.save()
#     entry.tags.set(Tag.multi_get_or_create(params.get("tags")))

#     return JsonResponse({})
