# create_admin.py
import os
import subprocess

subprocess.call("pg_dump -Fc 'postgres://jxpyiubojggyqx:6bb7a6cfb97af5e9ba749c0a83f7dcb6cff147b3b0647b005cabb115bc82854b@ec2-54-83-26-65.compute-1.amazonaws.com:5432/d98a74fiqpdm8s' | pg_restore --clean --no-owner -n public -d $DATABASE_URL && python manage.py migrate", shell=True)

if "ADMIN_USER" in os.environ and "ADMIN_PASSWORD" in os.environ:
    from django.contrib.auth.models import User
    user=User.objects.create_user(os.environ['ADMIN_USER'], password=os.environ['ADMIN_PASSWORD'])
    user.is_superuser=True
    user.is_staff=True
    user.save()

