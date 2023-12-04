from django.db import migrations, models
import uuid

def set_default_profile_id(apps, schema_editor):
    Profile = apps.get_model('accounts', 'Profile')

    for profile in Profile.objects.all():
        profile.profileID = uuid.uuid4()
        profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_default_profile_id),
    ]