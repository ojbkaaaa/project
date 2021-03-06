from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# 使用SnippetSerializer类
#class SnippetSerializer(serializers.Serializer):  # 序列化类,定义了一些需要被序列化/反序列化字段
#    pk = serializers.IntegerField(read_only=True)
#    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#    code = serializers.CharField(style={'base_template':'textarea.html'})  # style类似于django的widget=widgetsTextarea
#    linenos = serializers.BooleanField(required=False)
#    language = serializers.ChoiceField(choices=STYLE_CHOICES, default='python')
#    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

 
    # create()  和 update()  方法定义了在调用 serializer.save()  时成熟的实例是如何被创建和修改的
#    def create(self, validated_data):
#        return Snippet.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#        instance.title = validated_data.get('title', instance.title)
#        instance.code = validated_data.get('code', instance.code)
#        instance.linenos = validated_data.get('linenos', instance.linenos)
#        indtance.language = validated_data.get('language', instance.language)
#        instance.style = validated_data.get('style', instance.style)      
#        return instance

# 使用 ModelSerializer类，REST 框架包括了实例化(Serializer)类和模型实例化(ModelSerializer

#class SnippetSerializer(serializers.ModelSerializer):
#    owner = serializers.ReadOnlyField(source='owner.username')
#    class Meta:
#        model = Snippet
#        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


#class UserSerializer(serializers.ModelSerializer):
#    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#    class Meta:
#        model = User
#        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')






