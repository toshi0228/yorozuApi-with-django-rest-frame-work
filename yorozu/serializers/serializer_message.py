from rest_framework import serializers
from ..models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message

        fields = ("id", "sender_yorozu_id", "receiver_yorozu_id",
                  "message_content", "created_at", "updated_at")

        # receiver_yorozu_id

        # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
        # シリアライザーのcreateのオーバーライドではviewsでモデルの型チェックを行ったデータが入ってくる
        # is_valied()を呼び出さないとcreateも,実装されない
        # viewssetに以下のようなコードをかいても意味がない

        # def create(self, validated_data):
        #     print("messageシリアライザ")
        #     print(validated_data)
        #     return
        # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
