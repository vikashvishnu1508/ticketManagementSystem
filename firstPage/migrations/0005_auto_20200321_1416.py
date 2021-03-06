# Generated by Django 2.0.3 on 2020-03-21 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0004_auto_20200301_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='company',
        ),
        migrations.RemoveField(
            model_name='client',
            name='partner',
        ),
        migrations.RemoveField(
            model_name='client',
            name='product',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='company',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categoryName',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='assignedBy',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='assignedTo',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='client',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='serviceDeliveryLevel',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='severity',
        ),
        migrations.RemoveField(
            model_name='ticketcommentdetails',
            name='assignedBy',
        ),
        migrations.RemoveField(
            model_name='ticketcommentdetails',
            name='assignedTo',
        ),
        migrations.RemoveField(
            model_name='ticketcommentdetails',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ServiceDeliveryLevel',
        ),
        migrations.DeleteModel(
            name='Severity',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='TicketCommentDetails',
        ),
    ]
