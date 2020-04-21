from rest_framework import serializers
from .serializer_tag import TagSerializer
from ..models import Plan, Tag
from collections import OrderedDict


class PlanSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        # fields = ('title', 'description', 'image', 'price', 'tags')
        fields = ('title', 'description', 'image', 'price', "tags")
        # fields = ('title', 'tags',)
        # extra_kwargs = {
        #     # モデル上は必須フィールドだけれど、シリアライザでは Not必須にしたい場合は、required を上書きする
        #     'tags': {'required': False}
        # }

    # ["tags", {"name":"aa""]
    # "{"title":"ファ","description":"ファ","image":"電話.jpg","price":"12","tags":["インスターグラマー","aaaa"]}"

    # {'title': '試し1', 'tags': [OrderedDict([('name', 'try1')])]}
    # {'title': '試し2', 'tags': [OrderedDict([('name', 'try2')]), OrderedDict([('name', 'try3')])]}
    # [('name', 'try2')]

    # def run_validation(self, data=""):
    #     """
    #     We override the default `run_validation`, because the validation
    #     performed by validators and the `.validate()` method should
    #     be coerced into an error dictionary with a 'non_fields_error' key.
    #     """
    #     (is_empty_value, data) = self.validate_empty_values(data)
    #     if is_empty_value:
    #         return data

    #     '''
    #     以下のコードでtagsのリストの型でエラーをなくす
    #     '''
    #     # -----------------------------------
    #     values = data.pop("tags")
    #     split_values = values[0].split(",")

        # ex) [OrderedDict([('name', 'インスターグラマー')]), OrderedDict([('name', '記念日')])]
        # data["tags"] = OrderedDict([('name', 'try12')])

        # for index, value, in enumerate(split_values):
        #     index = OrderedDict()
        #     index['name'] = value
        #     data["tags"].append(index)
        # print(data["tags"])
        # print(data)

        # -----------------------------------

        # value = self.to_internal_value(data)
        # try:
        #     self.run_validators(value)
        #     value = self.validate(value)
        #     assert value is not None, '.validate() should return the validated data'
        # except:
        #     pass
        # except (ValidationError, DjangoValidationError) as exc:
        #     raise ValidationError(detail=as_serializer_error(exc))

        # return data

    # def run_validation(self, data="aa"):
    #     """
    #     We override the default `run_validation`, because the validation
    #     performed by validators and the `.validate()` method should
    #     be coerced into an error dictionary with a 'non_fields_error' key.
    #     """

    #     # print(data)
    #     # print(type(data))
    #     # print(data.get("tags"))
    #     values = data.pop("tags")
    #     print(values)
    #     print(type(values))

    #     # ['インスターグラマー,記念日'] => ['インスターグラマー', '記念日']
    #     split_values = values[0].split(",")
    #     print(split_values)

    #     # ex) [OrderedDict([('name', 'インスターグラマー')]), OrderedDict([('name', '記念日')])]
    #     new_tag_list = []

    #     for index, value, in enumerate(split_values):
    #         index = OrderedDict()
    #         index['name'] = value
    #         new_tag_list.append(index)
    #     print(new_tag_list)
    #     data["tags"] = new_tag_list
    #     print(data)

        # (is_empty_value, data) = self.validate_empty_values(data)
        # if is_empty_value:
        #     return data

        # value = self.to_internal_value(data)
        # try:
        #     self.run_validators(value)
        #     value = self.validate(value)
        #     assert value is not None, '.validate() should return the validated data'
        # except (ValidationError, DjangoValidationError) as exc:
        #     raise ValidationError(detail=as_serializer_error(exc))

        # return data

    # def create(self, validated_data):
    #     #     tags = serializers.CharField(default="aaa")
    #     print(f'{"="*125}')
    #     print("PlanSerializer(serializers.ModelSerializer")
    #     print(validated_data)
    #     return {}

    #     # タグの保存のクラスメソッド
    #     # ex)tags:[<Tag: 試し1>,<Tag: 試し2>]
    #     tags = Tag.multi_get_or_create(validated_data)

    #     # タグを削除して新たなオブジェクトを作成する
    #     # {'title': '試し67', 'tags': [OrderedDict([('name', 'try67')])]}
    #     validated_data.pop('tags')

    #     # **validated_data {'title': '試し67'} => 'titile'='試し67'
    #     plan = Plan.objects.create(**validated_data)

    #     # セットの場合は配列にしないといけない
    #     plan.tags.set(tags)

    #     return plan
