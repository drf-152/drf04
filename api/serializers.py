from rest_framework import serializers

from core.models import AAAA, BBBB, CCCC


class CCCCSerializer(serializers.ModelSerializer):

    class Meta:
        model = CCCC
        fields = ('id', 'name', 'show_me')


class BBBBCCCCSerializer(serializers.ModelSerializer):

    bb_ccs = CCCCSerializer(many=True)

    class Meta:
        model = BBBB
        fields = ('id', 'name', 'bb_ccs')


class AAAASerializer(serializers.ModelSerializer):

    bbs = BBBBCCCCSerializer(many=True)

    class Meta:
        model = AAAA
        fields = ('id', 'name', 'bbs')
