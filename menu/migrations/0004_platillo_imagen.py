<<<<<<< HEAD
# Generated by Django 5.1.6 on 2025-04-07 17:33
=======
# Generated by Django 5.2 on 2025-04-04 06:05
>>>>>>> 5a2ec44e7f0178c781151ad9ae7a94ca0f40f858

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='platillos/'),
        ),
    ]
