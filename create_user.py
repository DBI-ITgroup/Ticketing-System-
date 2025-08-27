import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helpdesk.settings')
django.setup()

from helpdeskapp.models import CustomUser

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
full_name = os.environ.get("DJANGO_SUPERUSER_FULL_NAME")
role = os.environ.get("DJANGO_SUPERUSER_ROLE")

if not CustomUser.objects.filter(username=username).exists():
    CustomUser.objects.create_superuser(
        username=username,
        email=email,
        password=password,
        full_name=full_name,
        role=role
    )
    print(f"Superuser {username} created successfully.")
else:
    print(f"Superuser {username} already exists.")
