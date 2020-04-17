from rest_framework import serializers
from .serializer_tag import TagSerializer
from ..models import Plan, Tag


class PlanSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Plan
        # fields = ('title', 'description', 'image', 'price', 'tags')
        # fields = ('title', 'tags',)

        # "{"title":"ファ","description":"ファ","image":"電話.jpg","price":"12","tags":["インスターグラマー","aaaa"]}"

    def create(self, validated_data):
        print(f'{"="*125}')
        print("PlanSerializer(serializers.ModelSerializer")
        print(validated_data)
        res_dict = {}

        # タグの保存のクラスメソッド
        # ex)tags:[<Tag: 試し1>,<Tag: 試し2>]
        tags = Tag.multi_get_or_create(validated_data)

        # タグを削除して新たなオブジェクトを作成する
        # {'title': '試し67', 'tags': [OrderedDict([('name', 'try67')])]}
        validated_data.pop('tags')

        # **validated_data {'title': '試し67'} => 'titile'='試し67'
        plan = Plan.objects.create(**validated_data)

        # セットの場合は配列にしないといけない
        plan.tags.set(tags)

        return plan

        # res_dict['title'] = plan.title
        # res_dict['tags'] = tags

        # return res_dict

        # print("タグのタイプ")
        # print(type(tags[0]))
        # print(tags)
        # print(tags[0].name)

        # validated_data.pop('tags')

        # print(validated_data)

        # print("作成されたもの")
        # print(plan)
        # print(type(plan))
        # print("タグ全て")
        # print(Tag.objects.all())

        # print("タグデータの呼び出し")
        # print(Tag.objects.all())

        # print("try10を呼び出す")
        # # print(Tag.objects.get(name="try10"))
        # print(Tag.objects.get(name="try10"))
        # # t10 = Tag.objects.get(name="try10")
        # print("try60は何者 <class 'str'>")
        # # <class 'str'>
        # print(type(tags[0]))
        # # t10 = Tag.objects.get(name="try59")
        # t10 = Tag.objects.get(name=tags[0])
        # print(type(t10))

        # # <class 'yorozu.models.Tag'>
        # print(t10)

        # 重要コード
        # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

        # 以下のコードが重要
        # plan.tags.add(t10)

        # セットの場合は配列にしないといけない
        # plan.tags.set([t10])
        # plan.tags.set(tags)
        # plan.tags.set(tags)
        # print("見たいもの")
        # print(plan.tags.all())

        # print("変更後")
        # print(plan)

        # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

        # plan.tags.set("新しいタグ")
        # print(Plan.objects.all())
        # plan.tags.set(tags, bulk=False)

        # entry = form.save()
        # entry.tags.set(Tag.multi_get_or_create(params.get("tags")))

        res_dict['title'] = plan.title
        # res_dict['tags'] = [t10]
        res_dict['tags'] = tags
        # res_dict['tags'] = tagssss
        print(res_dict)
        # リターンはこの形
        # {'title': '試し60', 'tags': [OrderedDict([('name', 'try60')])]}
        # だめパターン
        # {'title': '試し62', 'tags': ['try62']}
        return res_dict

    # tag = Tag.objects.all()
    # ko = Plan.objects.get(**validated_data)

    # plan = Plan.objects.get_or_create(**validated_data)
    # # plan = Plan.objects.all()
    # print(plan)
    # plan, created = Plan.objects.get_or_create(**validated_data)
    # print(plan)
    # print(created)

    # def create(self, validated_data):
    #     print(validated_data)
    #     res_dict = {}
    #     tags = validated_data.pop('tags')
    #     plan = Plan.objects.get_or_create(**validated_data)
    #     res_dict['plan'] = plan
    #     res_dict['plan']['tags'] = []
    #     for tag_data in tags:
    #         tag = Tag.objects.create(plan=plan, **tag_data)
    #         res_dict['plan']['tags'].append(tag)
    #     return res_dict
