# Generated by Django 2.0.3 on 2020-03-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0013_auto_20200321_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestigationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investigationTaken', models.TextField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketStatus', to='firstPage.Issue')),
            ],
        ),
    ]
