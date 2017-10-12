# create_admin.py
import os
import subprocess

if "ADMIN_USER" in os.environ and "ADMIN_PASSWORD" in os.environ:
    from django.contrib.auth.models import User

    if "DATABASE_URL" in os.environ:
        password = "database"
    else:
        password = os.environ['ADMIN_PASSWORD']
    user=User.objects.create_user(os.environ['ADMIN_USER'], password=password)
    user.is_superuser=True
    user.is_staff=True
    user.save()

