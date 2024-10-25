from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from shortener.handler import UrlShortenerHandler
from shortener.serializers import ShortUrlSerializer


class ShortenerCreateView(generics.GenericAPIView):
    permission_classes = [AllowAny]  # TODO need to revise
    serializer_class = ShortUrlSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data["url"]
        short_url_object = UrlShortenerHandler.create_url(url)
        return Response({"url": url, "shorted_url": short_url_object.shorted_url}, status=status.HTTP_201_CREATED)


class RedirectToUrlView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(self, request, shorted_url: str):
        url = UrlShortenerHandler.get_url(shorted_url)
        if not url:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Redirecting..."}, status=status.HTTP_302_FOUND, headers={"Location": url})
