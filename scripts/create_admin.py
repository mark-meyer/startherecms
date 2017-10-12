# create_admin.py
import os
import subprocess

if "ADMIN_USER" in os.environ and "ADMIN_PASSWORD" in os.environ:
    from django.contrib.auth.models import User
    user=User.objects.create_user(os.environ['ADMIN_USER'], password=os.environ['ADMIN_PASSWORD'])
    user.is_superuser=True
    user.is_staff=True
    user.save()

subprocess.call("pg_restore --clean --no-owner -n public -d $DATABASE_URL https://s3.us-east-2.amazonaws.com/database-dump-starthere/c5de9726-b709-4fd9-af32-e03fe390df16", shell=True)