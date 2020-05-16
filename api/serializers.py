from rest_framework import serializers
from ticket.models import *


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'product',
            'summary',
            'description',
            'issueType',
            'priority',
        ]
    
    def create(self, validated_data):
        issue = {}
        issue['assignedTo'] = User.objects.get(pk=12)
        issue['assignedBy'] = User.objects.get(pk=12)
        issue['status'] = Status.objects.get(pk=1)
        issue['issueType'] = validated_data['issueType']
        issue['priority'] = validated_data['priority']
        issue['product'] = validated_data['product']
        issue['summary'] = validated_data['summary']
        issue['description'] = validated_data['description']
        raisedTicket = Issue.objects.create(**issue)
        return raisedTicket