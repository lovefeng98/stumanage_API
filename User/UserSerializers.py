from rest_framework import serializers

from User.models import User


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=20,required=True)
    password = serializers.CharField(required=True,max_length=300)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = User.objects.filter(username=username)
        if not user.exists():
            raise serializers.ValidationError("用户不存在");
        user = user.first()
        if user.password !=password:
            raise serializers.ValidationError('用户密码错误');
        return attrs
