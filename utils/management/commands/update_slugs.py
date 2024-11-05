from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.account.models.profile_models import Profile
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Update slugs for Profile instances'

    def handle(self, *args, **kwargs):
        for profile in Profile.objects.all():
            if not profile.slug:
                profile.slug = slugify(profile.user.username)
            else:
                profile.slug = slugify(profile.slug)
            try:
                profile.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated slug for profile id {profile.id}'))
            except IntegrityError:
                self.stdout.write(self.style.ERROR(f'Duplicate slug found for profile id {profile.id}. Generating unique slug.'))
                unique_slug = profile.slug
                num = 1
                while Profile.objects.filter(slug=unique_slug).exists():
                    unique_slug = f"{profile.slug}-{num}"
                    num += 1
                profile.slug = unique_slug
                profile.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully updated slug for profile id {profile.id} with unique slug'))
