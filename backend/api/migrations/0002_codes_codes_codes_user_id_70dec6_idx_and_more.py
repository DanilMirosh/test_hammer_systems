from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'codes',
            },
        ),
        migrations.AddIndex(
            model_name='codes',
            index=models.Index(fields=['user'], name='codes_user_id_70dec6_idx'),
        ),
        migrations.AddConstraint(
            model_name='codes',
            constraint=models.UniqueConstraint(fields=('user',), name='unique_user'),
        ),
    ]
