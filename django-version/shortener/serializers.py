from rest_framework import serializers

from shortener.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    shorted_url = serializers.CharField(read_only=True)

    class Meta:
        model = ShortUrl
        fields = "__all__"
