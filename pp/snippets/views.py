from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

#使用mixin类，我们重写了视图，使用比以前稍少的代码，但是我们可以更进一步。 REST框架提供了一组已经混合的通用视图，我们可以使用这些通用视图来重构我们的views.py模块

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
