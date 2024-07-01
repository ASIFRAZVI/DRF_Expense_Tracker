from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager, Group , Permission
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            return 
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password) #hahing the password
        user.save(using=self._db)

       # Assign user to 'user' group (assuming 'user' group exists)
        user_group, created = Group.objects.get_or_create(name='user')
        user.groups.add(user_group)


        # Assign read-only permission to 'user' group
        self.assign_permissions(user_group, ['view'])

        user.save()

        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user= self.create_user(email, username, password, **extra_fields)


        # Assign user to 'superuser' group
        superuser_group, created = Group.objects.get_or_create(name='superuser')
        user.groups.add(superuser_group)

        # Assign all permissions to 'superuser' group
        self.assign_all_permissions(superuser_group)

        user.save()

        return user
    
    def create_staff(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True) 
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # Assign user to 'staff' group (assuming 'staff' group exists)
        staff_group, created = Group.objects.get_or_create(name='staff')
        user.groups.add(staff_group)

        # Assign CRUD permissions to 'staff' group
        self.assign_permissions(staff_group, ['add', 'change', 'delete', 'view'])

        user.save()

        return user
    
    # get permissions from django
    def assign_permissions(self, group, permissions):
        content_type = ContentType.objects.get_for_model(CustomUser)  # Adjust if necessary
        for perm in permissions:
            permission = Permission.objects.get(content_type=content_type, codename=f'{perm}_customuser')
            group.permissions.add(permission)

    def assign_all_permissions(self, group):
        content_type = ContentType.objects.get_for_model(CustomUser)
        all_permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(all_permissions)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True , null=False, blank=False)
    password = models.CharField(max_length=128 ,null=False, blank=False) 
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    last_login = models.DateTimeField(default=datetime.now)
    date_joined = models.DateTimeField(default=datetime.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username or self.email
