from django.db import models

from cloudloop import helper


class Session(models.Model):
    """Session for looping

    - Users join a session when added to clients
    """
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)
    title = models.CharField(max_length=64)
    clients = models.ManyToManyField('userauth.User', blank=True)
    timestamp = models.IntegerField(default=helper.time_stamp)
    loops = models.ForeignKey('looper.Loop', null=True, blank=True, on_delete=models.SET_NULL, related_name='loops_set')


class Loop(models.Model):
    """Session Loop
    """
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)
    timestamp = models.IntegerField(default=helper.time_stamp)
    beats = models.IntegerField()
    sample_rate = models.IntegerField(choices=[(44100,'44.1Khz'), (48000, '48Khz'), (96000, '96Khz')])
    bit_depth = models.IntegerField(choices=[(24,'24 bit'), (16, '16 bit')])
    channels = models.IntegerField(choices=[(1,'mono'),(2,'stereo')])
    frame_count = models.IntegerField()
    wav_link = models.URLField(unique=True)
    creator = models.ForeignKey('userauth.User', on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)

# Create your models here.
