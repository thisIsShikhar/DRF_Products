from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication

class TokenAuthenticationWithAudience(JWTAuthentication):
    def authenticate(self, request):
        # Get the authenticated user from the JWT token
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            return None
        
        # Verify the audience claim in the JWT token
        _, user = user_auth_tuple
        token = self.get_token_from_request(request)
        if token is None:
            return None
        audience = token['aud']
        expected_audience = settings.AUDIENCE
        if audience != expected_audience:
            return None

        return user, token
