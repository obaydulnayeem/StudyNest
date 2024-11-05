# myapp/middleware.py
from django.shortcuts import get_object_or_404
from apps.account.models import Profile

class ReferralMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if 'ref' is in the GET parameters
        referral_code = request.GET.get('ref')
        
        if referral_code and request.user.is_authenticated:
            try:
                profile = request.user.profile
                # Check if the profile doesn't already have a referred_by_code
                if not profile.referred_by_code:
                    # Store the referral code in the user's profile
                    profile.referred_by_code = referral_code
                    profile.save()
            except Profile.DoesNotExist:
                pass  # If the user doesn't have a profile, do nothing

        response = self.get_response(request)
        return response
