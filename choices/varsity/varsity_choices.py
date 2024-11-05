UNIVERSITY_TYPE_CHOICES = (
    ('public', 'Public'),
    ('private', 'Private'),
    ('Science and Technology', 'Science and Technology'),
    ('Engineering', 'Engineering'),
)

LAYER_CHOICES = (
    ('university', 'university'),
    ('faculty', 'faculty'),
    ('institute', 'institute'),
    ('school', 'school'),
    ('center', 'center'),
    ('department', 'department'),
    ('discipline', 'discipline'),
    ('course', 'course'),
    ('subject', 'subject'),
)


SYSTEM_CHOICES = (
    ('Year', 'Year'),
    ('Semester', 'Semester'),
)

# YEAR -------------------------------------------------
YEAR_CHOICES = (
    ('1st', '1st Year'),
    ('2nd', '2nd Year'),
    ('3rd', '3rd Year'),
    ('4th', '4th Year'),
    ('Graduated', 'Graduated'),
)

# SEMESTER -------------------------------------------------
SEMESTER_CHOICES = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th', '11th'),
    ('12th', '12th'),
)


COURSE_TYPE_CHOICES = (
    ('Theory', 'Theory'),
    ('Laboratory/Practical', 'Laboratory/Practical'),
    ('Sessional', 'Sessional'),
    ('Thesis/Project', 'Thesis/Project'),
    ('Viva Voce', 'Viva Voce'),
)

COURSE_STATUS_CHOICES = (
    ('Mandatory', 'Mandatory'),
    ('Optional', 'Optional'),
)

# EXAM NAME-------------------------------------------------
EXAM_CHOICES = (
    ('1st Mid', '1st Mid'),
    ('2nd Mid', '2nd Mid'),
    ('3rd Mid', '3rd Mid'),
    ('Class Test', 'Class Test'),
    ('Quiz', 'Quiz'),
    ('Supply', 'Supply'),
    ('Final', 'Final'),
    ('Lab Test', 'Lab Test'),
    ('Lab Final', 'Lab Final'),
    ('Others', 'Others'),
)

# SESSION----------------------------------------------
SESSION_24_25 = '24-25'
SESSION_23_24 = '23-24'
SESSION_22_23 = '22-23'
SESSION_21_22 = '21-22'
SESSION_20_21 = '20-21'
SESSION_19_20 = '19-20'
SESSION_18_19 = '18-19'


SESSION_CHOICES = (
    ('25-26', '25-26'),
    ('24-25', '24-25'),
    ('23-24', '23-24'),
    ('22-23', '22-23'),
    ('21-22', '21-22'),
    ('20-21', '20-21'),
    ('19-20', '19-20'),
    ('18-19', '18-19'),
    ('17-18', '17-18'),
    ('16-17', '16-17'),
    ('15-16', '15-16'),
    ('14-15', '14-15'),
    ('13-14', '13-14'),
)

# DEPARTMENT OR VARSITY BATCH----------------------------------------------
DEPARTMENT_OR_VARCITY_BATCH_CHOICES = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th', '11th'),
    ('12th', '12th'),
    ('13th', '13th'),
    ('14th', '14th'),
    ('15th', '15th'),
    ('16th', '16th'),
    ('17th', '17th'),
    ('18th', '18th'),
    ('19th', '19th'),
    ('20th', '20th'),
    ('21st', '21st'),
    ('22nd', '22nd'),
    ('23rd', '23rd'),
    ('24th', '24th'),
    ('25th', '25th'),
    ('26th', '26th'),
    ('27th', '27th'),
    ('28th', '28th'),
    ('29th', '29th'),
    ('30th', '30th'),
    ('31st', '31st'),
    ('32nd', '32nd'),
    ('33rd', '33rd'),
    ('34th', '34th'),
    ('35th', '35th'),
    ('36th', '36th'),
    ('37th', '37th'),
    ('38th', '38th'),
    ('39th', '39th'),
    ('40th', '40th'),
    ('41st', '41st'),
    ('42nd', '42nd'),
    ('43rd', '43rd'),
    ('44th', '44th'),
    ('45th', '45th'),
    ('46th', '46th'),
    ('47th', '47th'),
    ('48th', '48th'),
    ('49th', '49th'),
    ('50th', '50th'),
    ('51st', '51st'),
    ('52nd', '52nd'),
    ('53rd', '53rd'),
    ('54th', '54th'),
    ('55th', '55th'),
    ('56th', '56th'),
    ('57th', '57th'),
    ('58th', '58th'),
    ('59th', '59th'),
    ('60th', '60th'),
    ('61st', '61st'),
    ('62nd', '62nd'),
    ('63rd', '63rd'),
    ('64th', '64th'),
    ('65th', '65th'),
    ('66th', '66th'),
    ('67th', '67th'),
    ('68th', '68th'),
    ('69th', '69th'),
    ('70th', '70th'),
    ('71st', '71st'),
    ('72nd', '72nd'),
    ('73rd', '73rd'),
    ('74th', '74th'),
    ('75th', '75th'),
    ('76th', '76th'),
    ('77th', '77th'),
    ('78th', '78th'),
    ('79th', '79th'),
    ('80th', '80th'),
    ('81st', '81st'),
    ('82nd', '82nd'),
    ('83rd', '83rd'),
    ('84th', '84th'),
    ('85th', '85th'),
    ('86th', '86th'),
    ('87th', '87th'),
    ('88th', '88th'),
    ('89th', '89th'),
    ('90th', '90th'),
    ('91st', '91st'),
    ('92nd', '92nd'),
    ('93rd', '93rd'),
    ('94th', '94th'),
    ('95th', '95th'),
    ('96th', '96th'),
    ('97th', '97th'),
    ('98th', '98th'),
    ('99th', '99th'),
    ('100th', '100th'),
    ('101st', '101st'),
    ('102nd', '102nd'),
    ('103rd', '103rd'),
    ('104th', '104th'),
    ('105th', '105th'),
    ('106th', '106th'),
    ('107th', '107th'),
    ('108th', '108th'),
    ('109th', '109th'),
    ('110th', '110th'),
    ('111st', '111st'),
    ('112nd', '112nd'),
    ('113rd', '113rd'),
    ('114th', '114th'),
    ('115th', '115th'),
    ('116th', '116th'),
    ('117th', '117th'),
    ('118th', '118th'),
    ('119th', '119th'),
    ('120th', '120th'),
    ('121st', '121st'),
    ('122nd', '122nd'),
    ('123rd', '123rd'),
    ('124th', '124th'),
    ('125th', '125th'),
    ('126th', '126th'),
    ('127th', '127th'),
    ('128th', '128th'),
    ('129th', '129th'),
    ('130th', '130th'),
    ('131st', '131st'),
    ('132nd', '132nd'),
    ('133rd', '133rd'),
    ('134th', '134th'),
    ('135th', '135th'),
    ('136th', '136th'),
    ('137th', '137th'),
    ('138th', '138th'),
    ('139th', '139th'),
    ('140th', '140th'),
    ('141st', '141st'),
    ('142nd', '142nd'),
    ('143rd', '143rd'),
    ('144th', '144th'),
    ('145th', '145th'),
    ('146th', '146th'),
    ('147th', '147th'),
    ('148th', '148th'),
    ('149th', '149th'),
    ('150th', '150th'),
)

# # DEPARTMENTAL BATCH----------------------------------------------
# D_BATCH_1 = '1st'
# D_BATCH_2 = '2nd'
# D_BATCH_3 = '3rd'
# D_BATCH_4 = '4th'
# D_BATCH_5 = '5th'
# D_BATCH_6 = '6th'
# D_BATCH_7 = '7th'
# D_BATCH_8 = '8th'
# D_BATCH_9 = '9th'
# D_BATCH_10 = '10th'

# DEPARTMENTAL_BATCHES = (
#     (D_BATCH_1, '1st'),
#     (D_BATCH_2, '2nd'),
#     (D_BATCH_3, '3rd'),
#     (D_BATCH_4, '4th'),
#     (D_BATCH_5, '5th'),
#     (D_BATCH_6, '6th'),
#     (D_BATCH_7, '7th'),
#     (D_BATCH_8, '8th'),
#     (D_BATCH_9, '9th'),
#     (D_BATCH_10, '10th'),
# )

BOOK_EDITION_CHOICES = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('11th', '11th'),
    ('12th', '12th'),
    ('13th', '13th'),
    ('14th', '14th'),
    ('15th', '15th'),
    ('16th', '16th'),
    ('17th', '17th'),
    ('18th', '18th'),
    ('19th', '19th'),
    ('20th', '20th'),
)


TEACHER_DESIGNATION_CHOICES = (
    ('Lecturer', 'Lecturer'),
    ('Assistant Professor', 'Assistant Professor'),
    ('Associate Professor', 'Associate Professor'),
    ('Professor', 'Professor'),
)


TEAM_MEMBERS_CHOICES = (
    ('Maria Islam', 'Maria Islam'),
    ('Baishakhi Bir', 'Baishakhi Bir'),
    ('Ritu Akter Samia', 'Ritu Akter Samia'),
    ('Md. Tanvir Ahmed', 'Md. Tanvir Ahmed'),
    ('Md Rayhanul Islam Rony', 'Md Rayhanul Islam Rony'),
)

PREV_USERS_CHOICES = (
    ('Arafat Islam', 'Arafat Islam'),
    ('Antor Sarker', 'Antor Sarker'), # done
    ('Arifin Junnut Mim', 'Arifin Junnut Mim'),
    ('Baishakhi Bir', 'Baishakhi Bir'), # done
    ('Deepanwita Roy', 'Deepanwita Roy'),
    ('Dip Dey', 'Dip Dey'), #done
    ('Farjana Joynob Mim', 'Farjana Joynob Mim'),
    ('Hafsa Rashid', 'Hafsa Rashid'),
    ('Israt Jahan Tamanna', 'Israt Jahan Tamanna'),
    ('Jarin Tasnim', 'Jarin Tasnim'),
    ('Lazmi Rahman', 'Lazmi Rahman'),
    ('Mahbubur Rahman Antor', 'Mahbubur Rahman Antor'), # Done
    ('Maria Islam', 'Maria Islam'), # done
    ('Md Abdul Karim', 'Md Abdul Karim'),
    ('Md Abu Hossain Mohalder', 'Md Abu Hossain Mohalder'),
    ('Md Ahad', 'Md Ahad'),
    ('Md Anis Molla', 'Md Anis Molla'),
    ('Md Emon Howlader', 'Md Emon Howlader'),
    ('Md Imam Hosen', 'Md Imam Hosen'),
    ('Md Jannatul Ferdous Emon', 'Md Jannatul Ferdous Emon'),
    ('Md Khalid Hossen Muktadir', 'Md Khalid Hossen Muktadir'),
    ('Md Meherab Hossain', 'Md Meherab Hossain'),
    ('Md Mahruf Alam Sowad', 'Md Mahruf Alam Sowad'),
    ('Md Moniruzzaman', 'Md Moniruzzaman'),
    ('Md Moonaz Rahman', 'Md Moonaz Rahman'),
    ('Md Mosaraf Hossen', 'Md Mosaraf Hossen'),
    ('Md Rayhanul Islam Rony', 'Md Rayhanul Islam Rony'),
    ('Md Sadekur Rahman Sahad', 'Md Sadekur Rahman Sahad'),
    ('Md Tanvir Ahmed', 'Md Tanvir Ahmed'), # done
    ('Md Wahidujjaman', 'Md Wahidujjaman'),
    ('Md Yeamen Talukder', 'Md Yeamen Talukder'),
    ('Md Zakir Hossen', 'Md Zakir Hossen'),
    ('Muaaz Bin Zahid', 'Muaaz Bin Zahid'),
    ('Myself Nuha', 'Myself Nuha'),
    ('Nabiha Taieba Nuha', 'Nabiha Taieba Nuha'),
    ('Neamul Haq', 'Neamul Haq'),
    ('Obaydul Hasan Nayeem', 'Obaydul Hasan Nayeem'),
    ('Rahatul Islam Rifat', 'Rahatul Islam Rifat'),
    ('Rakibul Islam', 'Rakibul Islam'),
    ('Ramisa Noushin Sohely', 'Ramisa Noushin Sohely'),
    ('Rupa Samadder', 'Rupa Samadder'),
    ('Sadman Sadid', 'Sadman Sadid'),
    ('Samia', 'Samia'), # done
    ('Sarna Das', 'Sarna Das'),
    ('Saykot', 'Saykot'),
    ('Sayed Rakibul Alam', 'Sayed Rakibul Alam'),
    ('Shawmitra Das Dwip', 'Shawmitra Das Dwip'), # done
    ('Shihab Khan', 'Shihab Khan'),
    ('Sinkia Akter', 'Sinkia Akter'),
    ('Subrina Jahan Meem', 'Subrina Jahan Meem'), # done
    ('Subrota Mondol', 'Subrota Mondol'),
    ('Sumaiya Habib Meem', 'Sumaiya Habib Meem'),
    ('Sumia Jahan Jyoti', 'Sumia Jahan Jyoti'),
    ('Sumaia Islam Taj', 'Sumaia Islam Taj'),
    ('Syfuddin Naeem', 'Syfuddin Naeem'),
    ('Syfur Rahman', 'Syfur Rahman'),
    ('Tahira Anee', 'Tahira Anee'),
    ('Tanvir Ahamed Foysal', 'Tanvir Ahamed Foysal'),
    ('Tethi Rani Debnath', 'Tethi Rani Debnath'),
    ('Tian Mahamud', 'Tian Mahamud'),
    ('Utsojet Paticor', 'Utsojet Paticor'),
    ('Yeasin Arafat', 'Yeasin Arafat'),
    ('Zahid Hasan', 'Zahid Hasan'), # done
)
