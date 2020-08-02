from rest_framework import serializers


class LambdaRequestSerializer(serializers.Serializer):
    question = serializers.ListField(
        required=True,
        min_length=1,
        child=serializers.IntegerField()
    )
