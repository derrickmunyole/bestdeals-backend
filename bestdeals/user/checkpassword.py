from django.contrib.auth.hashers import check_password


def check_user_password(hashed_password, user_password):
    return check_password(user_password, hashed_password)
