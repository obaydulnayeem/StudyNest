from django.shortcuts import get_object_or_404
from django.contrib import messages
from ..models import CoinTransaction, Profile

def add_coin_transaction(profile, activity, coins):
    print('hiiiiiiiiiiiii')
    """Add a coin transaction for a profile based on activity."""
    if activity not in [choice[0] for choice in CoinTransaction.ACTIVITY_CHOICES]:
        raise ValueError("Invalid activity type.")

    if coins <= 0:
        raise ValueError("Coins must be greater than zero.")

    # Create a new coin transaction
    CoinTransaction.objects.create(
        profile=profile,
        activity=activity,
        coins=coins
    )

    # Update the user's total coins
    profile.total_coins += coins
    profile.save()