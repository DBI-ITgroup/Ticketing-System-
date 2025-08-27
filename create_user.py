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

# --- NORMAL USERS ---
users_data = [
    {
        "username": "Sinelizwi.Gebeda@dbi-itgroup.co.za",
        "email": "Sinelizwi.Gebeda@dbi-itgroup.co.za",
        "password": "Katlego@25",
        "full_name": "Sine DBI",
        "role": "End-User",
    },
    {
        "username": "hhelpdesk83@gmail.com",
        "email": "hhelpdesk83@gmail.com",
        "password": "Katlego@25",
        "full_name": "Technician L1-1",
        "role": "L1_Technician",
    },
  {
        "username": "sinelizwigebeda9@gmail.com",
        "email": "sinelizwigebeda9@gmail.com",
        "password": "Katlego@25",
        "full_name": "Technician L1-2",
        "role": "L1_Technician",
    },
     {
        "username": "Training@dbi-itgroup.co.za",
        "email": "Training@dbi-itgroup.co.za",
        "password": "Katlego@25",
        "full_name": "Technician L2-1",
        "role": "L2_Technician",
    },
     {
        "username": "ITSupport@dbi-itgroup.co.za",
        "email": "ITSupport@dbi-itgroup.co.za",
        "password": "Katlego@25",
        "full_name": "Technician L2-2",
        "role": "L2_Technician",
    }
    ]

for user in users_data:
    if not CustomUser.objects.filter(username=user["username"]).exists():
        CustomUser.objects.create_user(**user)
        print(f"User {user['username']} created successfully.")
    else:
        print(f"User {user['username']} already exists.")
