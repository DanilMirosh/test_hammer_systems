from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_friends_friends_friends_user_id_020709_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField()),
                ('refresh_token', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'db_table': 'tokens',
            },
        ),
        migrations.AddIndex(
            model_name='tokens',
            index=models.Index(fields=['user'], name='tokens_user_id_0d1983_idx'),
        ),
        migrations.AddConstraint(
            model_name='tokens',
            constraint=models.UniqueConstraint(fields=('user',), name='unique_user_token'),
        ),
    ]
