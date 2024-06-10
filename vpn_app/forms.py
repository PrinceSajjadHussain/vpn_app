from django import forms
from .models import VPNUser


COUNTRY_CHOICES = [
    ('af', 'Afghanistan'), ('al', 'Albania'), ('dz', 'Algeria'), ('as', 'American Samoa'), 
    ('ad', 'Andorra'), ('ao', 'Angola'), ('ai', 'Anguilla'), ('ag', 'Antigua and Barbuda'), 
    ('ar', 'Argentina'), ('am', 'Armenia'), ('aw', 'Aruba'), ('au', 'Australia'), 
    ('at', 'Austria'), ('az', 'Azerbaijan'), ('bs', 'Bahamas'), ('bh', 'Bahrain'), 
    ('bd', 'Bangladesh'), ('bb', 'Barbados'), ('by', 'Belarus'), ('be', 'Belgium'), 
    ('bz', 'Belize'), ('bj', 'Benin'), ('bm', 'Bermuda'), ('bt', 'Bhutan'), 
    ('bo', 'Bolivia'), ('ba', 'Bosnia and Herzegovina'), ('bw', 'Botswana'), ('br', 'Brazil'), 
    ('bn', 'Brunei'), ('bg', 'Bulgaria'), ('bf', 'Burkina Faso'), ('bi', 'Burundi'), 
    ('kh', 'Cambodia'), ('cm', 'Cameroon'), ('ca', 'Canada'), ('cv', 'Cape Verde'), 
    ('ky', 'Cayman Islands'), ('cf', 'Central African Republic'), ('td', 'Chad'), ('cl', 'Chile'), 
    ('cn', 'China'), ('co', 'Colombia'), ('km', 'Comoros'), ('cg', 'Congo'), 
    ('cd', 'Congo, Democratic Republic of the'), ('ck', 'Cook Islands'), ('cr', 'Costa Rica'), 
    ('ci', "Côte d'Ivoire"), ('hr', 'Croatia'), ('cu', 'Cuba'), ('cy', 'Cyprus'), 
    ('cz', 'Czech Republic'), ('dk', 'Denmark'), ('dj', 'Djibouti'), ('dm', 'Dominica'), 
    ('do', 'Dominican Republic'), ('ec', 'Ecuador'), ('eg', 'Egypt'), ('sv', 'El Salvador'), 
    ('gq', 'Equatorial Guinea'), ('er', 'Eritrea'), ('ee', 'Estonia'), ('et', 'Ethiopia'), 
    ('fj', 'Fiji'), ('fi', 'Finland'), ('fr', 'France'), ('ga', 'Gabon'), 
    ('gm', 'Gambia'), ('ge', 'Georgia'), ('de', 'Germany'), ('gh', 'Ghana'), 
    ('gi', 'Gibraltar'), ('gr', 'Greece'), ('gl', 'Greenland'), ('gd', 'Grenada'), 
    ('gu', 'Guam'), ('gt', 'Guatemala'), ('gn', 'Guinea'), ('gw', 'Guinea-Bissau'), 
    ('gy', 'Guyana'), ('ht', 'Haiti'), ('hn', 'Honduras'), ('hk', 'Hong Kong'), 
    ('hu', 'Hungary'), ('is', 'Iceland'), ('in', 'India'), ('id', 'Indonesia'), 
    ('ir', 'Iran'), ('iq', 'Iraq'), ('ie', 'Ireland'), ('il', 'Israel'), 
    ('it', 'Italy'), ('jm', 'Jamaica'), ('jp', 'Japan'), ('jo', 'Jordan'), 
    ('kz', 'Kazakhstan'), ('ke', 'Kenya'), ('ki', 'Kiribati'), ('kw', 'Kuwait'), 
    ('kg', 'Kyrgyzstan'), ('la', 'Laos'), ('lv', 'Latvia'), ('lb', 'Lebanon'), 
    ('ls', 'Lesotho'), ('lr', 'Liberia'), ('ly', 'Libya'), ('li', 'Liechtenstein'), 
    ('lt', 'Lithuania'), ('lu', 'Luxembourg'), ('mo', 'Macau'), ('mk', 'Macedonia'), 
    ('mg', 'Madagascar'), ('mw', 'Malawi'), ('my', 'Malaysia'), ('mv', 'Maldives'), 
    ('ml', 'Mali'), ('mt', 'Malta'), ('mh', 'Marshall Islands'), ('mr', 'Mauritania'), 
    ('mu', 'Mauritius'), ('mx', 'Mexico'), ('fm', 'Micronesia'), ('md', 'Moldova'), 
    ('mc', 'Monaco'), ('mn', 'Mongolia'), ('me', 'Montenegro'), ('ma', 'Morocco'), 
    ('mz', 'Mozambique'), ('mm', 'Myanmar'), ('na', 'Namibia'), ('nr', 'Nauru'), 
    ('np', 'Nepal'), ('nl', 'Netherlands'), ('nz', 'New Zealand'), ('ni', 'Nicaragua'), 
    ('ne', 'Niger'), ('ng', 'Nigeria'), ('nu', 'Niue'), ('kp', 'North Korea'), 
    ('no', 'Norway'), ('om', 'Oman'), ('pk', 'Pakistan'), ('pw', 'Palau'), 
    ('pa', 'Panama'), ('pg', 'Papua New Guinea'), ('py', 'Paraguay'), ('pe', 'Peru'), 
    ('ph', 'Philippines'), ('pl', 'Poland'), ('pt', 'Portugal'), ('pr', 'Puerto Rico'), 
    ('qa', 'Qatar'), ('ro', 'Romania'), ('ru', 'Russia'), ('rw', 'Rwanda'), 
    ('kn', 'Saint Kitts and Nevis'), ('lc', 'Saint Lucia'), ('vc', 'Saint Vincent and the Grenadines'), 
    ('ws', 'Samoa'), ('sm', 'San Marino'), ('st', 'Sao Tome and Principe'), 
    ('sa', 'Saudi Arabia'), ('sn', 'Senegal'), ('rs', 'Serbia'), ('sc', 'Seychelles'), 
    ('sl', 'Sierra Leone'), ('sg', 'Singapore'), ('sk', 'Slovakia'), ('si', 'Slovenia'), 
    ('sb', 'Solomon Islands'), ('so', 'Somalia'), ('za', 'South Africa'), ('kr', 'South Korea'), 
    ('ss', 'South Sudan'), ('es', 'Spain'), ('lk', 'Sri Lanka'), ('sd', 'Sudan'), 
    ('sr', 'Suriname'), ('sz', 'Swaziland'), ('se', 'Sweden'), ('ch', 'Switzerland'), 
    ('sy', 'Syria'), ('tw', 'Taiwan'), ('tj', 'Tajikistan'), ('tz', 'Tanzania'), 
    ('th', 'Thailand'), ('tl', 'Timor-Leste'), ('tg', 'Togo'), ('to', 'Tonga'), 
    ('tt', 'Trinidad and Tobago'), ('tn', 'Tunisia'), ('tr', 'Turkey'), ('tm', 'Turkmenistan'), 
    ('tv', 'Tuvalu'), ('ug', 'Uganda'), ('ua', 'Ukraine'), ('ae', 'United Arab Emirates'), 
    ('gb', 'United Kingdom'), ('us', 'United States'), ('uy', 'Uruguay'), ('uz', 'Uzbekistan'), 
    ('vu', 'Vanuatu'), ('va', 'Vatican City'), ('ve', 'Venezuela'), ('vn', 'Vietnam'), 
    ('ye', 'Yemen'), ('zm', 'Zambia'), ('zw', 'Zimbabwe')
]


class VPNConfigForm(forms.Form):
      country = forms.ChoiceField(choices=COUNTRY_CHOICES)
      enable_vpn = forms.BooleanField(required=False)

      class Meta:
        model = VPNUser
        fields = ['country', 'is_enabled']


class SudoPasswordForm(forms.Form):
    sudo_password = forms.CharField(widget=forms.PasswordInput, label="Sudo Password")