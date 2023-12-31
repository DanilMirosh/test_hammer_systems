from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('identifier', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['phone_number', 'identifier'], name='users_phone_n_65306b_idx'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('phone_number',), name='unique_phone_number'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('identifier',), name='unique_identifier'),
        ),
        migrations.RunSQL(
            sql="""
            CREATE FUNCTION generate_unique_identifier_after_insert_trigger_proc()
            RETURNS TRIGGER
            AS $$
            DECLARE
                identifier VARCHAR(6);
            BEGIN
                UPDATE users SET identifier = (SELECT array_to_string(ARRAY(SELECT chr((48 + round(random() * 59)) :: integer) 
                FROM generate_series(1,6)), '')) WHERE id = NEW.id;
                RETURN NEW;
            END $$ LANGUAGE plpgsql;
            """,
            reverse_sql="DROP FUNCTION generate_unique_identifier_after_insert_trigger_proc",

        ),
        migrations.RunSQL(
            sql="""
            CREATE TRIGGER generate_unique_identifier_after_insert_trigger AFTER INSERT ON users FOR EACH ROW EXECUTE PROCEDURE generate_unique_identifier_after_insert_trigger_proc() 
            """,
            reverse_sql="DROP TRIGGER generate_unique_identifier_after_insert_trigger ON users",
        ),

    ]