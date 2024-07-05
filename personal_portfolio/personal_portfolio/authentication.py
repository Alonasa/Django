from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None

        except user_model.DoesNotExist:
            return None

    def get_user(self, id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=id)
        except user_model.DoesNotExist:
            return None
