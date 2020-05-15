# Generated by Django 3.0.5 on 2020-05-12 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=2000)),
                ('description', models.TextField()),
                ('creadtedDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now_add=True)),
                ('closedDate', models.DateTimeField(blank=True, null=True)),
                ('assignedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketAssigner', to=settings.AUTH_USER_MODEL)),
                ('assignedTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketAssignee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issueType', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IssueUpdateDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('dateAdded', models.DateTimeField(auto_now=True)),
                ('update', models.TextField()),
                ('attachments', models.FileField(blank=True, null=True, upload_to='documents/Updates/')),
                ('addedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updatedBy', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updateRelatedIssue', to='ticket.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='IssueAssignmentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('attachments', models.FileField(blank=True, null=True, upload_to='documents/Assignment/')),
                ('assignedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignmentAssignee', to=settings.AUTH_USER_MODEL)),
                ('assignedTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignmentAssigner', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignmentIssue', to='ticket.Issue')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='issueType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestType', to='ticket.IssueType'),
        ),
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketPriority', to='ticket.Priority'),
        ),
        migrations.AddField(
            model_name='issue',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatedProduct', to='ticket.Product'),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketStatus', to='ticket.Status'),
        ),
        migrations.CreateModel(
            name='InvestigationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investigationTaken', models.TextField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketStatus', to='ticket.Issue')),
            ],
        ),
    ]