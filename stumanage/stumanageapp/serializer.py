from rest_framework import serializers
from .models import Student,Marks

class StudentSerializer(serializers.Serializer):
    roll = serializers.CharField()
    name = serializers.CharField()
    dob = serializers.DateField()

    def create(self, valid_data):
        return Student.objects.create(**valid_data)

    def update(self, instance, valid_data):
        instance.roll= valid_data.get('roll', instance.roll)
        instance.name = valid_data.get('name', instance.name)
        instance.dob = valid_data.get('dob', instance.dob)
        instance.save()
        return instance
class MarkSerializer(serializers.Serializer):
    roll= serializers.SlugRelatedField(many=False, slug_field="roll", queryset=Student.objects.all())
    mark = serializers.IntegerField()

    class Meta:
        model = Marks
        fields = ['roll','mark']


    def create(self, valid_data):
        return Marks.objects.create(**valid_data)