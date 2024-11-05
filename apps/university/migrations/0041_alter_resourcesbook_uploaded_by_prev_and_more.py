# Generated by Django 5.0.6 on 2024-08-02 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0040_rename_academic_staff_university_num_academic_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcesbook',
            name='uploaded_by_prev',
            field=models.CharField(blank=True, choices=[('Zahid Hasan', 'Zahid Hasan'), ('Subrina Jahan Meem', 'Subrina Jahan Meem'), ('Maria Islam', 'Maria Islam'), ('Syfuddin Naeem', 'Syfuddin Naeem'), ('Md. Sadekur Rahman Sahad', 'Md. Sadekur Rahman Sahad'), ('Md. Emon Howlader', 'Md. Emon Howlader'), ('Myself Nuha', 'Myself Nuha'), ('Sadman Sadid', 'Sadman Sadid'), ('Obaydul Hasan Nayeem', 'Obaydul Hasan Nayeem'), ('Deepanwita Roy', 'Deepanwita Roy'), ('Md Rayhanul Islam Rony', 'Md Rayhanul Islam Rony'), ('Md. Anis Molla', 'Md. Anis Molla'), ('Baishakhi Bir', 'Baishakhi Bir'), ('Md Readul Haque Sohan', 'Md Readul Haque Sohan'), ('Syfur Rahman', 'Syfur Rahman'), ('Md. Mahruf Alam Sowad', 'Md. Mahruf Alam Sowad'), ('Shawmitra Das Dwip', 'Shawmitra Das Dwip'), ('Md. Asad Mondal', 'Md. Asad Mondal'), ('Sumaiya Habib Meem', 'Sumaiya Habib Meem'), ('Farjana Joynob Mim', 'Farjana Joynob Mim'), ('Ramisa Noushin Sohely', 'Ramisa Noushin Sohely'), ('Utsojet Paticor', 'Utsojet Paticor'), ('Sumia Jahan Jyoti', 'Sumia Jahan Jyoti'), ('Sumaia Islam Taj', 'Sumaia Islam Taj'), ('Md Yeamen Talukder', 'Md Yeamen Talukder'), ('Dip Dey', 'Dip Dey'), ('Samia', 'Samia'), ('Md Tanvir Ahmed', 'Md Tanvir Ahmed'), ('Yeasin Arafat', 'Yeasin Arafat'), ('Md Moonaz Rahman', 'Md Moonaz Rahman'), ('Jarin Tasnim', 'Jarin Tasnim'), ('Md. Moniruzzaman', 'Md. Moniruzzaman'), ('Tahira Anee', 'Tahira Anee'), ('Arafat Islam', 'Arafat Islam'), ('Lazmi Rahman', 'Lazmi Rahman'), ('Saykot', 'Saykot'), ('Tanvir Ahamed Foysal', 'Tanvir Ahamed Foysal'), ('Md Imam Hosen', 'Md Imam Hosen'), ('Tethi Rani Debnath', 'Tethi Rani Debnath'), ('Md Zakir Hossen', 'Md Zakir Hossen'), ('Md. Meherab Hossain', 'Md. Meherab Hossain'), ('Muaaz Bin Zahid', 'Muaaz Bin Zahid'), ('Md Ahad', 'Md Ahad'), ('Neamul Haq', 'Neamul Haq'), ('Sarna Das', 'Sarna Das'), ('Israt Jahan Tamanna', 'Israt Jahan Tamanna'), ('Rahatul Islam Rifat', 'Rahatul Islam Rifat'), ('Shihab Khan', 'Shihab Khan'), ('Mahbubur Rahman Antor', 'Mahbubur Rahman Antor'), ('Antor Sarker', 'Antor Sarker'), ('Md.Wahidujjaman', 'Md.Wahidujjaman'), ('Md Khalid Hossen Muktadir', 'Md Khalid Hossen Muktadir'), ('Tian Mahamud', 'Tian Mahamud'), ('Md. Mosaraf Hossen', 'Md. Mosaraf Hossen'), ('Sayed Rakibul Alam', 'Sayed Rakibul Alam'), ('Sinkia Akter', 'Sinkia Akter'), ('Md. Abu Hossain Mohalder', 'Md. Abu Hossain Mohalder'), ('Md. Abdul Karim', 'Md. Abdul Karim'), ('Hafsa Rashid', 'Hafsa Rashid'), ('Subrota Mondol', 'Subrota Mondol'), ('Rakibul Islam', 'Rakibul Islam'), ('Nabiha Taieba Nuha', 'Nabiha Taieba Nuha'), ('Rupa Samadder', 'Rupa Samadder'), ('Md Jannatul Ferdous Emon', 'Md Jannatul Ferdous Emon'), ('Arifin Junnut Mim', 'Arifin Junnut Mim')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resourceslecture',
            name='uploaded_by_prev',
            field=models.CharField(blank=True, choices=[('Zahid Hasan', 'Zahid Hasan'), ('Subrina Jahan Meem', 'Subrina Jahan Meem'), ('Maria Islam', 'Maria Islam'), ('Syfuddin Naeem', 'Syfuddin Naeem'), ('Md. Sadekur Rahman Sahad', 'Md. Sadekur Rahman Sahad'), ('Md. Emon Howlader', 'Md. Emon Howlader'), ('Myself Nuha', 'Myself Nuha'), ('Sadman Sadid', 'Sadman Sadid'), ('Obaydul Hasan Nayeem', 'Obaydul Hasan Nayeem'), ('Deepanwita Roy', 'Deepanwita Roy'), ('Md Rayhanul Islam Rony', 'Md Rayhanul Islam Rony'), ('Md. Anis Molla', 'Md. Anis Molla'), ('Baishakhi Bir', 'Baishakhi Bir'), ('Md Readul Haque Sohan', 'Md Readul Haque Sohan'), ('Syfur Rahman', 'Syfur Rahman'), ('Md. Mahruf Alam Sowad', 'Md. Mahruf Alam Sowad'), ('Shawmitra Das Dwip', 'Shawmitra Das Dwip'), ('Md. Asad Mondal', 'Md. Asad Mondal'), ('Sumaiya Habib Meem', 'Sumaiya Habib Meem'), ('Farjana Joynob Mim', 'Farjana Joynob Mim'), ('Ramisa Noushin Sohely', 'Ramisa Noushin Sohely'), ('Utsojet Paticor', 'Utsojet Paticor'), ('Sumia Jahan Jyoti', 'Sumia Jahan Jyoti'), ('Sumaia Islam Taj', 'Sumaia Islam Taj'), ('Md Yeamen Talukder', 'Md Yeamen Talukder'), ('Dip Dey', 'Dip Dey'), ('Samia', 'Samia'), ('Md Tanvir Ahmed', 'Md Tanvir Ahmed'), ('Yeasin Arafat', 'Yeasin Arafat'), ('Md Moonaz Rahman', 'Md Moonaz Rahman'), ('Jarin Tasnim', 'Jarin Tasnim'), ('Md. Moniruzzaman', 'Md. Moniruzzaman'), ('Tahira Anee', 'Tahira Anee'), ('Arafat Islam', 'Arafat Islam'), ('Lazmi Rahman', 'Lazmi Rahman'), ('Saykot', 'Saykot'), ('Tanvir Ahamed Foysal', 'Tanvir Ahamed Foysal'), ('Md Imam Hosen', 'Md Imam Hosen'), ('Tethi Rani Debnath', 'Tethi Rani Debnath'), ('Md Zakir Hossen', 'Md Zakir Hossen'), ('Md. Meherab Hossain', 'Md. Meherab Hossain'), ('Muaaz Bin Zahid', 'Muaaz Bin Zahid'), ('Md Ahad', 'Md Ahad'), ('Neamul Haq', 'Neamul Haq'), ('Sarna Das', 'Sarna Das'), ('Israt Jahan Tamanna', 'Israt Jahan Tamanna'), ('Rahatul Islam Rifat', 'Rahatul Islam Rifat'), ('Shihab Khan', 'Shihab Khan'), ('Mahbubur Rahman Antor', 'Mahbubur Rahman Antor'), ('Antor Sarker', 'Antor Sarker'), ('Md.Wahidujjaman', 'Md.Wahidujjaman'), ('Md Khalid Hossen Muktadir', 'Md Khalid Hossen Muktadir'), ('Tian Mahamud', 'Tian Mahamud'), ('Md. Mosaraf Hossen', 'Md. Mosaraf Hossen'), ('Sayed Rakibul Alam', 'Sayed Rakibul Alam'), ('Sinkia Akter', 'Sinkia Akter'), ('Md. Abu Hossain Mohalder', 'Md. Abu Hossain Mohalder'), ('Md. Abdul Karim', 'Md. Abdul Karim'), ('Hafsa Rashid', 'Hafsa Rashid'), ('Subrota Mondol', 'Subrota Mondol'), ('Rakibul Islam', 'Rakibul Islam'), ('Nabiha Taieba Nuha', 'Nabiha Taieba Nuha'), ('Rupa Samadder', 'Rupa Samadder'), ('Md Jannatul Ferdous Emon', 'Md Jannatul Ferdous Emon'), ('Arifin Junnut Mim', 'Arifin Junnut Mim')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesnote',
            name='uploaded_by_prev',
            field=models.CharField(blank=True, choices=[('Zahid Hasan', 'Zahid Hasan'), ('Subrina Jahan Meem', 'Subrina Jahan Meem'), ('Maria Islam', 'Maria Islam'), ('Syfuddin Naeem', 'Syfuddin Naeem'), ('Md. Sadekur Rahman Sahad', 'Md. Sadekur Rahman Sahad'), ('Md. Emon Howlader', 'Md. Emon Howlader'), ('Myself Nuha', 'Myself Nuha'), ('Sadman Sadid', 'Sadman Sadid'), ('Obaydul Hasan Nayeem', 'Obaydul Hasan Nayeem'), ('Deepanwita Roy', 'Deepanwita Roy'), ('Md Rayhanul Islam Rony', 'Md Rayhanul Islam Rony'), ('Md. Anis Molla', 'Md. Anis Molla'), ('Baishakhi Bir', 'Baishakhi Bir'), ('Md Readul Haque Sohan', 'Md Readul Haque Sohan'), ('Syfur Rahman', 'Syfur Rahman'), ('Md. Mahruf Alam Sowad', 'Md. Mahruf Alam Sowad'), ('Shawmitra Das Dwip', 'Shawmitra Das Dwip'), ('Md. Asad Mondal', 'Md. Asad Mondal'), ('Sumaiya Habib Meem', 'Sumaiya Habib Meem'), ('Farjana Joynob Mim', 'Farjana Joynob Mim'), ('Ramisa Noushin Sohely', 'Ramisa Noushin Sohely'), ('Utsojet Paticor', 'Utsojet Paticor'), ('Sumia Jahan Jyoti', 'Sumia Jahan Jyoti'), ('Sumaia Islam Taj', 'Sumaia Islam Taj'), ('Md Yeamen Talukder', 'Md Yeamen Talukder'), ('Dip Dey', 'Dip Dey'), ('Samia', 'Samia'), ('Md Tanvir Ahmed', 'Md Tanvir Ahmed'), ('Yeasin Arafat', 'Yeasin Arafat'), ('Md Moonaz Rahman', 'Md Moonaz Rahman'), ('Jarin Tasnim', 'Jarin Tasnim'), ('Md. Moniruzzaman', 'Md. Moniruzzaman'), ('Tahira Anee', 'Tahira Anee'), ('Arafat Islam', 'Arafat Islam'), ('Lazmi Rahman', 'Lazmi Rahman'), ('Saykot', 'Saykot'), ('Tanvir Ahamed Foysal', 'Tanvir Ahamed Foysal'), ('Md Imam Hosen', 'Md Imam Hosen'), ('Tethi Rani Debnath', 'Tethi Rani Debnath'), ('Md Zakir Hossen', 'Md Zakir Hossen'), ('Md. Meherab Hossain', 'Md. Meherab Hossain'), ('Muaaz Bin Zahid', 'Muaaz Bin Zahid'), ('Md Ahad', 'Md Ahad'), ('Neamul Haq', 'Neamul Haq'), ('Sarna Das', 'Sarna Das'), ('Israt Jahan Tamanna', 'Israt Jahan Tamanna'), ('Rahatul Islam Rifat', 'Rahatul Islam Rifat'), ('Shihab Khan', 'Shihab Khan'), ('Mahbubur Rahman Antor', 'Mahbubur Rahman Antor'), ('Antor Sarker', 'Antor Sarker'), ('Md.Wahidujjaman', 'Md.Wahidujjaman'), ('Md Khalid Hossen Muktadir', 'Md Khalid Hossen Muktadir'), ('Tian Mahamud', 'Tian Mahamud'), ('Md. Mosaraf Hossen', 'Md. Mosaraf Hossen'), ('Sayed Rakibul Alam', 'Sayed Rakibul Alam'), ('Sinkia Akter', 'Sinkia Akter'), ('Md. Abu Hossain Mohalder', 'Md. Abu Hossain Mohalder'), ('Md. Abdul Karim', 'Md. Abdul Karim'), ('Hafsa Rashid', 'Hafsa Rashid'), ('Subrota Mondol', 'Subrota Mondol'), ('Rakibul Islam', 'Rakibul Islam'), ('Nabiha Taieba Nuha', 'Nabiha Taieba Nuha'), ('Rupa Samadder', 'Rupa Samadder'), ('Md Jannatul Ferdous Emon', 'Md Jannatul Ferdous Emon'), ('Arifin Junnut Mim', 'Arifin Junnut Mim')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resourcesquestion',
            name='uploaded_by_prev',
            field=models.CharField(blank=True, choices=[('Zahid Hasan', 'Zahid Hasan'), ('Subrina Jahan Meem', 'Subrina Jahan Meem'), ('Maria Islam', 'Maria Islam'), ('Syfuddin Naeem', 'Syfuddin Naeem'), ('Md. Sadekur Rahman Sahad', 'Md. Sadekur Rahman Sahad'), ('Md. Emon Howlader', 'Md. Emon Howlader'), ('Myself Nuha', 'Myself Nuha'), ('Sadman Sadid', 'Sadman Sadid'), ('Obaydul Hasan Nayeem', 'Obaydul Hasan Nayeem'), ('Deepanwita Roy', 'Deepanwita Roy'), ('Md Rayhanul Islam Rony', 'Md Rayhanul Islam Rony'), ('Md. Anis Molla', 'Md. Anis Molla'), ('Baishakhi Bir', 'Baishakhi Bir'), ('Md Readul Haque Sohan', 'Md Readul Haque Sohan'), ('Syfur Rahman', 'Syfur Rahman'), ('Md. Mahruf Alam Sowad', 'Md. Mahruf Alam Sowad'), ('Shawmitra Das Dwip', 'Shawmitra Das Dwip'), ('Md. Asad Mondal', 'Md. Asad Mondal'), ('Sumaiya Habib Meem', 'Sumaiya Habib Meem'), ('Farjana Joynob Mim', 'Farjana Joynob Mim'), ('Ramisa Noushin Sohely', 'Ramisa Noushin Sohely'), ('Utsojet Paticor', 'Utsojet Paticor'), ('Sumia Jahan Jyoti', 'Sumia Jahan Jyoti'), ('Sumaia Islam Taj', 'Sumaia Islam Taj'), ('Md Yeamen Talukder', 'Md Yeamen Talukder'), ('Dip Dey', 'Dip Dey'), ('Samia', 'Samia'), ('Md Tanvir Ahmed', 'Md Tanvir Ahmed'), ('Yeasin Arafat', 'Yeasin Arafat'), ('Md Moonaz Rahman', 'Md Moonaz Rahman'), ('Jarin Tasnim', 'Jarin Tasnim'), ('Md. Moniruzzaman', 'Md. Moniruzzaman'), ('Tahira Anee', 'Tahira Anee'), ('Arafat Islam', 'Arafat Islam'), ('Lazmi Rahman', 'Lazmi Rahman'), ('Saykot', 'Saykot'), ('Tanvir Ahamed Foysal', 'Tanvir Ahamed Foysal'), ('Md Imam Hosen', 'Md Imam Hosen'), ('Tethi Rani Debnath', 'Tethi Rani Debnath'), ('Md Zakir Hossen', 'Md Zakir Hossen'), ('Md. Meherab Hossain', 'Md. Meherab Hossain'), ('Muaaz Bin Zahid', 'Muaaz Bin Zahid'), ('Md Ahad', 'Md Ahad'), ('Neamul Haq', 'Neamul Haq'), ('Sarna Das', 'Sarna Das'), ('Israt Jahan Tamanna', 'Israt Jahan Tamanna'), ('Rahatul Islam Rifat', 'Rahatul Islam Rifat'), ('Shihab Khan', 'Shihab Khan'), ('Mahbubur Rahman Antor', 'Mahbubur Rahman Antor'), ('Antor Sarker', 'Antor Sarker'), ('Md.Wahidujjaman', 'Md.Wahidujjaman'), ('Md Khalid Hossen Muktadir', 'Md Khalid Hossen Muktadir'), ('Tian Mahamud', 'Tian Mahamud'), ('Md. Mosaraf Hossen', 'Md. Mosaraf Hossen'), ('Sayed Rakibul Alam', 'Sayed Rakibul Alam'), ('Sinkia Akter', 'Sinkia Akter'), ('Md. Abu Hossain Mohalder', 'Md. Abu Hossain Mohalder'), ('Md. Abdul Karim', 'Md. Abdul Karim'), ('Hafsa Rashid', 'Hafsa Rashid'), ('Subrota Mondol', 'Subrota Mondol'), ('Rakibul Islam', 'Rakibul Islam'), ('Nabiha Taieba Nuha', 'Nabiha Taieba Nuha'), ('Rupa Samadder', 'Rupa Samadder'), ('Md Jannatul Ferdous Emon', 'Md Jannatul Ferdous Emon'), ('Arifin Junnut Mim', 'Arifin Junnut Mim')], max_length=100, null=True),
        ),
    ]
