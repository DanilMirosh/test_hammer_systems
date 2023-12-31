from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_codes_codes_codes_user_id_70dec6_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_friend',
                                             to='api.user')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me', to='api.user')),
            ],
            options={
                'db_table': 'friends',
            },
        ),
        migrations.AddIndex(
            model_name='friends',
            index=models.Index(fields=['user', 'friend'], name='friends_user_id_020709_idx'),
        ),
        migrations.AddConstraint(
            model_name='friends',
            constraint=models.UniqueConstraint(fields=('user', 'friend'), name='unique_friend'),
        ),
    ]
