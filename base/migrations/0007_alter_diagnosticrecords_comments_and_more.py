# Generated by Django 4.2.6 on 2023-10-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_diagnosticrecords_patient_diagnosticrecords_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticrecords',
            name='comments',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosticrecords',
            name='diagnosis',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosticrecords',
            name='prescription_code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='exerciserecords',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='exerciserecords',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='exerciserecords',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exerciserecords',
            name='exercise_type',
            field=models.CharField(choices=[('strength', '무산소'), ('cardio', '유산소')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='exerciserecords',
            name='iteration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exerciserecords',
            name='speed',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='exerciserecords',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='mediarecords',
            name='Field4',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mediarecords',
            name='inbody_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mediarecords',
            name='video_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mediarecords',
            name='xray_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='days',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='medicine',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='times',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='unit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='testrecords',
            name='BodyFatMass',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='testrecords',
            name='MuscleMass',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='testrecords',
            name='Muscular_strength',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='testrecords',
            name='agility',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='testrecords',
            name='cardio_endurance',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='testrecords',
            name='flexibility',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='treatmentrecords',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='treatmentrecords',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='treatmentrecords',
            name='time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='treatmentrecords',
            name='treatment_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]