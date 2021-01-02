from rest_framework import serializers

from Stu.models import StuInfo


class AllStuinfoShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = StuInfo
        fields = ('__all__')


class AddStuinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuInfo
        fields = ('__all__')
class EditStuinfoSerializer(serializers.Serializer):
    stunum = serializers.CharField()
    stuname=serializers.CharField()
    stuphone=serializers.CharField()
    stubirth=serializers.DateField()
    stusex=serializers.IntegerField()
    stuidcard=serializers.CharField()
    stumajor = serializers.CharField()
    stufaculty = serializers.CharField()
    stuin = serializers.DateField()
    stuadress = serializers.CharField()

    def update(self, instance, validated_data):
        return  instance
    def create(self, validated_data):
        return validated_data