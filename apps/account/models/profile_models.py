from django.db import models
from django.contrib.auth.models import User
from apps.university.models import *
from choices.varsity.varsity_choices import *
from choices.choices import *
from django.utils.text import slugify
import uuid

class Profile(models.Model):
    VISIBILITY_CHOICES = [
        ('only_me', 'Only Me'),
        ('my_batch', 'My Batch'),
        ('my_department', 'My Department'),
        ('my_university', 'My University'),
        ('public', 'Public'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, blank=True, null=True, default="Student")
    
    edu_university = models.ForeignKey('account.EduUniversity', related_name='profile_edu_university', on_delete=models.CASCADE, blank=True, null=True)
    
    moderator_type = models.CharField(max_length=100, choices=MODERATOR_TYPE_CHOICES, blank=True, null=True)
    
    # moderator_info = models.ForeignKey('admin_panel.ModeratorRequest', related_name='profile_moderator_info', on_delete=models.CASCADE, blank=True, null=True)
    
    moderator_info = models.OneToOneField('admin_panel.ModeratorRequest', related_name='profile_moderator_info', on_delete=models.CASCADE, blank=True, null=True)
    
    bio = models.TextField(blank=True)
    
    fullname = models.CharField(max_length=100, blank=True)
    
    nickname = models.CharField(max_length=100, blank=True)
    
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png', blank=True, null=True)
    
    email = models.EmailField(max_length=254, blank=True)
    email_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='my_department')
    
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    blood_group_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='only_me')
    
    mobile_number = models.CharField(max_length=15, blank=True)
    mobile_number_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='my_batch')
    
    facebook_id = models.CharField(max_length=100, blank=True)
    facebook_id_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='my_batch')
    
    instagram_id = models.CharField(max_length=100, blank=True)
    instagram_id_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='my_batch')
    
    linkedin_id = models.CharField(max_length=100, blank=True)
    linkedin_id_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    
    youtube_channel = models.CharField(max_length=100, blank=True)
    youtube_channel_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    
    twitter_id = models.CharField(max_length=100, blank=True)
    twitter_id_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='my_batch')
    
    github_id = models.CharField(max_length=100, blank=True)
    github_id_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    
    google_scholar = models.CharField(max_length=100, blank=True)
    google_scholar_visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    
    total_coins = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    is_verified = models.BooleanField(default=False)

    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    
    referred_by = models.ForeignKey('self', related_name='referrals', on_delete=models.SET_NULL, blank=True, null=True)
    
    referred_by_code = models.CharField(max_length=10, blank=True, null=True)
    
    is_referral_done = models.BooleanField(default=False)
    
    is_visited_check_referral = models.BooleanField(default=False)

    has_req_for_prev_coin = models.BooleanField(default=False)
    
    given_prev_coin = models.BooleanField(default=False)
    
    is_team_member = models.BooleanField(default=False)

    # Method to generate a referral code
    def generate_referral_code(self):
        if not self.referral_code:
            self.referral_code = uuid.uuid4().hex[:10].upper()
            self.save()

    
    def save(self, *args, **kwargs):
        if not self.pk:  # If the Profile instance is new (not yet saved to the database)
            super().save(*args, **kwargs)  # Save it to get a primary key (id)
            self.generate_referral_code()  # Generate the referral code
        super().save(*args, **kwargs)  # Save again to store the referral code


    def calculate_total_coins(self):
        return self.coin_transactions.aggregate(total=models.Sum('coins'))['total'] or 0

    def __str__(self):
        return self.user.username


class CoinTransaction(models.Model):
    ACTIVITY_CHOICES = [
        ('add_question', 'Add Question'),
        ('add_book', 'Add Book'),
        ('add_note', 'Add Note'),
        ('add_lecture', 'Add Lecture Slide'),
        ('refer_new_user', 'Refer New User'),
        ('team_contribution', 'Team Contribution'),
        # Add more activities here as needed
    ]

    profile = models.ForeignKey(Profile, related_name='coin_transactions', on_delete=models.CASCADE)
    activity = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    coins = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username} - {self.activity}: {self.coins} coins"

# class TeacherUniversity(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     university = models.ForeignKey(University, on_delete=models.CASCADE)
#     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     designation = models.CharField(max_length=100, choices=TEACHER_DESIGNATION_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #         return f"{self.profile.user.username} - {self.university.name}"