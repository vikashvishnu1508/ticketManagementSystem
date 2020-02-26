# Generated by Django 2.0.3 on 2020-02-26 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0003_remove_user_empid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=8000)),
                ('location', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceType', models.CharField(max_length=1000)),
                ('isActive', models.BooleanField(default=False)),
                ('company', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='partnerCompany', to='firstPage.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=1000)),
                ('modelNumber', models.CharField(default='1.0', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDeliveryLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supportLevel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceCategory', models.CharField(max_length=8000)),
                ('issueSubject', models.CharField(max_length=8000)),
                ('issueDescription', models.TextField()),
                ('creadtedDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('closedDate', models.DateTimeField(null=True)),
                ('assignedBy', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ticketAssignedBy', to='firstPage.User')),
                ('assignedTo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ticketAssignedTo', to='firstPage.User')),
                ('client', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_s_Client', to='firstPage.Client')),
                ('serviceDeliveryLevel', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='serviceLevel', to='firstPage.ServiceDeliveryLevel')),
                ('severity', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_s_severity', to='firstPage.Severity')),
            ],
        ),
        migrations.CreateModel(
            name='TicketCommentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('modifiedDate', models.DateTimeField(auto_now=True)),
                ('assignedBy', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='commentAssignedBy', to='firstPage.User')),
                ('assignedTo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='commentAssignedTo', to='firstPage.User')),
                ('ticket', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='commentForTicket', to='firstPage.Ticket')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categoryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='firstPage.ProductCategory'),
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientCompany', to='firstPage.Company'),
        ),
        migrations.AddField(
            model_name='client',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientPartner', to='firstPage.Partner'),
        ),
        migrations.AddField(
            model_name='client',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientProduct', to='firstPage.Product'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actulClientUser', to='firstPage.User'),
        ),
    ]
