from rest_framework import serializers
from .models import *


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'product',
            'summary',
            'description',
        ]
    
    def create(self, validated_data):
        issue = {}
        issue['issueType'] = IssueType.objects.get(pk=3)
        issue['assignedTo'] = User.objects.get(pk=13)
        issue['assignedBy'] = User.objects.get(pk=13)
        issue['status'] = Status.objects.get(pk=1)
        issue['priority'] = Priority.objects.get(pk=1)
        issue['product'] = validated_data['product']
        issue['summary'] = validated_data['summary']
        issue['description'] = validated_data['description']
        raisedTicket = Issue.objects.create(**issue)
        return raisedTicket