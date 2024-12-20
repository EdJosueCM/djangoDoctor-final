# Generated by Django 4.2.16 on 2024-11-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attention', '0003_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='curriculum',
            field=models.FileField(blank=True, null=True, upload_to='curriculums/', verbose_name='Curriculum Vitae'),
        ),
        migrations.AlterField(
            model_name='examen',
            name='archivo_resultado',
            field=models.FileField(blank=True, null=True, upload_to='examen/', verbose_name='Examenes'),
        ),
    ]
