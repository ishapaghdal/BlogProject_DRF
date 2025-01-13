from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password, alias=None):
        user = self.model(
        email = self.normalize_email(email),
                username = username,)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user