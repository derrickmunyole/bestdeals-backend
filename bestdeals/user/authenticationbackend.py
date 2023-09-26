from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTAuthenticationBackend:
    def authenticate(self, request):
        auth = JWTAuthentication()
        user, _ = auth.authenticate(request)
        return user
