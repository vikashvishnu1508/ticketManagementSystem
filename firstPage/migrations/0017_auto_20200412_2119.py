# Generated by Django 3.0.5 on 2020-04-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0016_issueupdatedetails_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='issueassignmentdetails',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='media/documents/Assignment/'),
        ),
        migrations.AlterField(
            model_name='issueupdatedetails',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='media/documents/Updates/'),
        ),
    ]