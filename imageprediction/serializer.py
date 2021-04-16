from rest_framework import serializers

from .models import SampleData


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = [
            'image_name',
            'test_type',
            'patient_id',
            'user_id',
            'result_length',
            'result',
            'mode'
        ]


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = [
            'testdetail',
            'record'
        ]
