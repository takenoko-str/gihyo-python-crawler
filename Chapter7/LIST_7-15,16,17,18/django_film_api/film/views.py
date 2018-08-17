"""API用ビュー."""
from rest_framework import serializers, viewsets

# film/models.py のインポート
from film import models


# models.pyのLanguageモデルのデータをJSONに変換するためのクラス
class LanguageSerializer(serializers.ModelSerializer):
    """Languageシリアライザー."""

    class Meta:
        model = models.Language  # models.Languageとの紐付け
        fields = '__all__'  # 全フィールドを表示


# models.pyのFilmモデルをJSONに変換するためのクラス
class FilmSerializer(serializers.ModelSerializer):
    """Filmシリアライザー."""

    # languageフィールドには上で定義しておいた LanguageSerializerを適用
    language = LanguageSerializer()

    class Meta:
        model = models.Film  # models.Film との紐付け
        fields = '__all__'  # 全フィールドを表示


# /films のURLで呼ばれるクラス
class FilmViewSet(viewsets.ModelViewSet):
    """Film用ViewSet."""
    # Filmモデルからクエリオブジェクトを取得し queryset にセット (必須)
    queryset = models.Film.objects.all()

    # シリアライザークラスの指定 (必須)
    serializer_class = FilmSerializer

    # オプション
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)
