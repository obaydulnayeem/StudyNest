# Generated by Django 5.0.6 on 2024-07-12 03:44

import apps.account.models.education_models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('student', 'Student'), ('departmental_moderator', 'Departmental Moderator'), ('batch_ambassador', 'Batch Ambassador'), ('departmental_ambassador', 'Departmental Ambassador'), ('university_ambassador', 'University Ambassador'), ('admin', 'Admin'), ('mentor', 'Mentor')], max_length=100, null=True)),
                ('bio', models.TextField(blank=True)),
                ('fullname', models.CharField(blank=True, max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=100)),
                ('profile_image', models.ImageField(blank=True, default='profile_images/default.png', null=True, upload_to='profile_images/')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('session', models.CharField(blank=True, choices=[('24-25', '24-25'), ('23-24', '23-24'), ('22-23', '22-23'), ('21-22', '21-22'), ('20-21', '20-21'), ('19-20', '19-20'), ('18-19', '18-19')], max_length=50, null=True)),
                ('departmental_batch', models.CharField(blank=True, choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')], max_length=50, null=True)),
                ('year', models.PositiveIntegerField(blank=True, choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year')], null=True)),
                ('semester', models.PositiveIntegerField(blank=True, choices=[(1, '1st Semester'), (2, '2nd Semester'), (3, '3rd Semester'), (4, '4th Semester'), (5, '5th Semester'), (6, '6th Semester'), (7, '7th Semester'), (8, '8th Semester')], null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('facebook_id', models.CharField(blank=True, max_length=100)),
                ('codeforces_id', models.CharField(blank=True, max_length=100)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EduUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, choices=[('Bachelor of Science', 'Bachelor of Science'), ('Bachelor of Arts', 'Bachelor of Arts'), ('Bachelor of Commerce', 'Bachelor of Commerce'), ('Master of Science', 'Master of Science'), ('Master of Arts', 'Master of Arts'), ('Master of Commerce', 'Master of Commerce'), ('Phd (Doctor of Philosophy)', 'Phd (Doctor of Philosophy)'), ('Others', 'Others')], max_length=100, null=True)),
                ('start_year', models.PositiveIntegerField(blank=True, choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)], default=apps.account.models.education_models.current_year, null=True)),
                ('end_year', models.PositiveIntegerField(blank=True, choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)], default=apps.account.models.education_models.current_year, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]
