from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# マネージャーは、モデルとクエリーの中間にあるもの 変換器と言うところか
# パスワードをハッシュ化してデータベースに保存する
# マネージャーは、データベースに保存する前の下ごしらえ
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        # emailの大文字、小文字を変換する
        # マネジャメソッドが自分の属しているモデルクラスを取り出すために self.model にアクセスできる
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # djangoのclIコマンドを使うときの設定
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# AbstractBaseUserを利用してカスタマイズユーザーを作成する場合、
# BaseUserManagerを継承したカスタムマネージャーを実装する必要があります
class MyUser(AbstractBaseUser):

    class Meta:
        # 管理画面でアプリのタイトルの名前を変更
        verbose_name_plural = "アカウント"

    username = models.CharField(
        "ユーザー名", max_length=30, unique=False, default=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password = models.CharField("password", max_length=255, unique=True)
    profile = models.CharField('profile', max_length=255, blank=True)
    # name = models.CharField(max_length=255)
    # date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin


class Tag(models.Model):
    """タグ"""

    class Meta:
        # 管理画面でアプリのタイトルの名前を変更
        verbose_name_plural = "タグ"

    name = models.CharField("名称", max_length=64, unique=True)

    @classmethod
    def get_or_create(cls, tag):
        """指定された名称のタグを生成して返す、既にあればそれを取得して返す"""
        ret = cls.objects.filter(name=tag).first()
        if not ret:
            # オブジェクトの作成と保存を一つの処理で行う
            ret = cls.objects.create(name=tag)
        return ret

    # ============================================================
    # objects.create(name=name)
    # オブジェクトの作成と保存を一つの処理で行う

    # (1)と(2)は同じ
    # (1) p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
    # (2) p = Person(first_name="Bruce", last_name="Springsteen")
    #     p.save(force_insert=True)
  # ============================================================

    # PlanSerializerで使うクラスメソッド
    @classmethod
    def multi_get_or_create(cls, validated_data):
        tags = []
        validated_tags = validated_data.get("tags")
        if not validated_tags:
            return []
        for tag in validated_tags:
            tags.append(Tag.get_or_create(tag))
        return tags


#   @classmethod
#   def multi_get_or_create(cls, validated_data):
#         validated_tags = validated_data.get("tags")
    # tags = []
    # for tag in validated_tags:
    #     tags.append(Tag.get_or_create(tag))

    # @classmethod
    # def multi_get_or_create(cls, names):
    #     if not names:
    #         return []
    #     tags = []
    #     for name in names:
    #         tags.append(Tag.get_or_create(name))
    #     return tags

    def __str__(self):
        return self.name


class Plan(models.Model):
    class Meta:
        # 管理画面でアプリのタイトルの名前を変更
        verbose_name_plural = "プラン"

    title = models.CharField("プランタイトル", max_length=255)
    description = models.CharField("プランの説明", max_length=255)
    image = models.ImageField("イメージ画像", upload_to='', default="")
    price = models.PositiveIntegerField("料金", default=0)
    tags = models.ManyToManyField(Tag)

    # tags = models.ManyToManyField(Tag)
    # tags = TaggableManager("タグ", blank=True)

    def __str__(self):
        # タイトルの名前を押して詳細に入ったときの名前を変更できる
        return self.title
