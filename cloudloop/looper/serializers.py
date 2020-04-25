from rest_framework import serializers

from . import models


class LoopSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='hash_id', read_only=True)
    creator_id = serializers.CharField(source='creator.hash_id', read_only=True)
    creator_username = serializers.CharField(source='creator.username', read_only=True)
    timestamp = serializers.CharField(source='timestamp', read_only=True)
    frame_count = serializers.IntegerField(source='frame_count', read_only=True)
    wav_link = serializers.URLField(source='wav_link', read_only=True)

    class Meta:
        model = models.Loop
        fields = ('id', 'creator_id', 'creator_username', 'timestamp', 'wav_link')


class LoopListSerializer(serializers.ListSerializer):
    child = LoopSerializer()
    many = True
    allow_null = True


class SessionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='hash_id', read_only=True)
    clients = serializers.CharField(source='clients', read_only=True)
    title = serializers.CharField(source='title', read_only=True)
    timestamp = serializers.IntegerField(source='timestamp', read_only=True)

    class Meta:
        model = models.Session
        fields = ('id', 'clients', 'title', 'timestamp')

class SessionListSerializer(serializers.ListSerializer):
    child = SessionSerializer()
    many = True
    allow_null = True