import numpy as np 
from mailmerge import MailMerge 
from datetime import date 
import json 
import os 


def read_name(f):
    with open(f, "r") as f:
        data = f.read()

cust1_1 = {
    'city': 'THÀNH PHỐ HÀ NỘI',
    'town': 'THỊ XÃ SƠN TÂY',
    'ward1': 'UBND PHƯỜNG QUANG TRUNG',
    'ward2' : 'Phường Quang Trung',
    'day': '07',
    'month': '05',
    'year': '2021',
    'name': 'BÙI THỊ LIÊN',
    'dob': '20/10/1998',
    'dob_chu': "ngày hai mươi, tháng mười, năm một nghìn chín trăm chín tám",
    'gender': 'Nữ',
    "nation": "Kinh",
    'nationality': "Việt Nam",
    'place_of_birth': 'Phòng khám bệnh thị xã Sơn Tây',
    'hown_town': "",
    'person_id': "",
    'name_mother':"CẨN THỊ HIỀN",
    'dob_mother': "1963",
    'nation_mother': "Kinh",
    'nationality_mother': "Việt Nam",
    'residence_mother': "Khu tập thể cầu đường 3",
    'name_father':"NGUYỄN VĂN MINH",
    'dob_father': "1964",
    'nation_father': "Kinh",
    'nationality_father': "Việt Nam",
    'residence_father': "Đội 7 thôn văn Gia, xã Trung Hưng, Sơn Tây",
    'register_address': "UBND phường Quang Trung, thị xã Sơn Tây, thành phố Hà Nội",
    'number_id': "14",
    'date': "26/01/1991",
    'note': "Thực hiện việc trích lục từ Sổ đăng kí khai sinh/"
}

def gen_register_address():
    
    return register_address

def gen_note():

    note = "Thực hiện việc trích lục từ Sổ đăng kí khai sinh/"

    return note 

def gen_numberid():

    number_id = np.random.randint(10, 1000)
    return str(number_id)

def gen_random_day():
    day = np.random.randint(1, 32)
    return str(day)

def gen_random_month():
    month = np.random.randint(1, 13)
    return str(month)

def gen_random_year():
    year = np.random.randint(1900, 2080)
    return str(year)

def gen_random_city():
    tinh = ['an giang', 'bà rịa - vũng tàu', 'bà rịa vũng tàu', 'bà rịa, vũng tàu', 'bắc giang', 'bắc kạn', 'bạc liêu', 'bắc ninh', 'bến tre', 'bình định', 'bình dương', 
                'bình phước', 'bình thuận', 'cà mau', 'cao bằng', 'đắk lắk', 'đắk nông', 'điện biên', 'đồng nai', 'đồng tháp', 'gia lai', 'hà giang', 
                'hà nam', 'hà tĩnh', 'hải dương', 'hậu giang', 'hòa bình', 'hưng yên', 'khánh hòa', 'kiên giang', 'kon tum', 'lai châu', 'lâm đồng', 
                'lạng sơn', 'lào cai', 'long an', 'nam định', 'nghệ an', 'ninh bình', 'ninh thuận', 'phú thọ', 'quảng bình', 'quảng nam', 'quảng ngãi',
                 'quảng ninh', 'quảng trị', 'sóc trăng', 'sơn la', 'tây ninh', 'thái bình', 'thái nguyên', 'thanh hóa', 'thừa thiên huế', 'tiền giang',
                  'trà vinh', 'tuyên quang', 'vĩnh long', 'vĩnh phúc', 'yên bái', 'phú yên', 'hải phòng', 'hà nội', 'hà tây', 'cần thơ', 
                  'cần thơ','đà nẵng', 'đà nẵng', 'hồ chí minh']

    n = len(tinh)
    i = np.random.randint(0, n)
    city = "THÀNH PHỐ " + tinh[i].upper() 

    return city 

def gen_random_town():
    tinh = ['an giang', 'bà rịa - vũng tàu', 'bà rịa vũng tàu', 'bà rịa, vũng tàu', 'bắc giang', 'bắc kạn', 'bạc liêu', 'bắc ninh', 'bến tre', 'bình định', 'bình dương', 
                'bình phước', 'bình thuận', 'cà mau', 'cao bằng', 'đắk lắk', 'đắk nông', 'điện biên', 'đồng nai', 'đồng tháp', 'gia lai', 'hà giang', 
                'hà nam', 'hà tĩnh', 'hải dương', 'hậu giang', 'hòa bình', 'hưng yên', 'khánh hòa', 'kiên giang', 'kon tum', 'lai châu', 'lâm đồng', 
                'lạng sơn', 'lào cai', 'long an', 'nam định', 'nghệ an', 'ninh bình', 'ninh thuận', 'phú thọ', 'quảng bình', 'quảng nam', 'quảng ngãi',
                 'quảng ninh', 'quảng trị', 'sóc trăng', 'sơn la', 'tây ninh', 'thái bình', 'thái nguyên', 'thanh hóa', 'thừa thiên huế', 'tiền giang',
                  'trà vinh', 'tuyên quang', 'vĩnh long', 'vĩnh phúc', 'yên bái', 'phú yên', 'hải phòng', 'hà nội', 'hà tây', 'cần thơ', 
                  'cần thơ','đà nẵng', 'đà nẵng', 'hồ chí minh']

    n = len(tinh)
    i = np.random.randint(0, n)
    town = "THỊ XÃ " + tinh[i].upper() 

    return town 


def gen_random_ward():
    tinh = ['an giang', 'bà rịa - vũng tàu', 'bà rịa vũng tàu', 'bà rịa, vũng tàu', 'bắc giang', 'bắc kạn', 'bạc liêu', 'bắc ninh', 'bến tre', 'bình định', 'bình dương', 
                'bình phước', 'bình thuận', 'cà mau', 'cao bằng', 'đắk lắk', 'đắk nông', 'điện biên', 'đồng nai', 'đồng tháp', 'gia lai', 'hà giang', 
                'hà nam', 'hà tĩnh', 'hải dương', 'hậu giang', 'hòa bình', 'hưng yên', 'khánh hòa', 'kiên giang', 'kon tum', 'lai châu', 'lâm đồng', 
                'lạng sơn', 'lào cai', 'long an', 'nam định', 'nghệ an', 'ninh bình', 'ninh thuận', 'phú thọ', 'quảng bình', 'quảng nam', 'quảng ngãi',
                 'quảng ninh', 'quảng trị', 'sóc trăng', 'sơn la', 'tây ninh', 'thái bình', 'thái nguyên', 'thanh hóa', 'thừa thiên huế', 'tiền giang',
                  'trà vinh', 'tuyên quang', 'vĩnh long', 'vĩnh phúc', 'yên bái', 'phú yên', 'hải phòng', 'hà nội', 'hà tây', 'cần thơ', 
                  'cần thơ','đà nẵng', 'đà nẵng', 'hồ chí minh']

    n = len(tinh)
    i = np.random.randint(0, n)
    ward1 = "UBND PHƯỜNG " + tinh[i].upper() 
    ward2 = tinh[i].title()

    return ward1, ward2

def gen_random_nation():
    nation = ["Kinh", "Tày", "Thái", "Mường", "Khmer", "Hoa", "Nùng", "H'Mông", "Dao","Ê Đê", "Chăm"]
    n = len(nation)
    i = np.random.randint(0, n)
    c = [0, 0, 0, 0, 1, 1, 2]
    i1 = np.random.randint(0, 7)
    if c[i1] == 0:
        return nation[i]
    elif c[i1] == 1:
        return " " + nation[i]
    else:
        return "  " + nation[i]

def gen_random_nationality():

    nationality = ['Việt Nam', "Lào", "Mỹ", "Pháp", "Trung Quốc"]
    n = len(nationality)
    i = np.random.randint(0, n)

    return nationality[i]


def gen_random_date():
    date = np.random.randint(1, 32)
    month = np.random.randint(1, 13)
    year = np.random.randint(1900, 2080)
    return '{:02}/{:02}/{:04}'.format(date, month, year)

dict1 = { '0': 'không', '1' : 'một', '2' : 'hai', '3' : 'ba', '4' : 'bốn', '5' : 'năm', '6' : 'sáu', '7' : 'bảy', '8' : 'tám', '9' : "chín"}


def read_day(day):
    res1 = ""
    if len(day) == 1:
        res1 = dict1[day]

    elif day[0] == '0':
        res1 = dict1[day[1]]

    elif day[0] == '1':
        if day[1] == '0':
            res1 = "mười"
        else:
            res1 = "mười " + dict1[day[1]]
    else:
        if day[1] == '0':
            res1 = dict1[day[0]] + " mươi"
        elif day[1] == "1":
            res1 = dict1[day[0]] + " mươi mốt"
        elif day[1] == "5":
            res1 = dict1[day[0]] + " mươi lăm"
        else:
            res1 = dict1[day[0]] + " mươi " + dict1[day[1]]

    return res1 


def read_month(day):
    res1 = ""
    if len(day) == 1:
        res1 = dict1[day]

    elif day[0] == '0':
        res1 = dict1[day[1]]

    elif day[0] == '1':
        if day[1] == '0':
            res1 = "mười"
        elif day[1] == '5':
            res1 = "mười lăm"
        else:
            res1 = "mười " + dict1[day[1]]

    return res1 

def read_year2(year):

    y1 = year[0]
    y2 = year[1]
    y3 = year[2]
    y4 = year[3]

    re = read_day(year[2:])
    res1 = dict1[y1] + " " + dict1[y2] + " " + dict1[y3] + " " +  dict1[y4]

    return res1


def read_year(year):

    y1 = year[0]
    y2 = year[1]
    y3 = year[2]
    y4 = year[3]
    y = int(year)
    
    str_year = ""
    if y % 1000 == 0:
        str_year = dict1[y1] + " nghìn"
    elif y % 100 == 0:
        str_year = dict1[y1] + " nghìn " + dict1[y2] + " trăm "
    elif year[2] == '0':
        str_year = dict1[y1] + " nghìn " + dict1[y2] + " trăm linh "  + dict1[y4]
    else:
        re = read_day(year[2:])
        str_year = dict1[y1] + " nghìn " + dict1[y2] + " trăm " + re

    return str_year


def read_dob(text):
    s = text.split("/")
    day = s[0]
    month = s[1]
    year = s[2]


   
    str_day = read_day(day)
    str_month = read_month(month)
    str_year = read_year(year)
    
    res = "ngày "  + str_day + ", tháng " + str_month + ", năm " + str_year

    return res 

def gen_residence(address):

    residence = gen_random_address(address)

    return residence 

def gen_random_id():

    i1 = np.random.randint(100000, 999999)
    i2 = np.random.randint(100000, 999999)
    return str(i1) + str(i2)

def gen_instance(boy, girl, last_names, address):

    person = dict()
    person['city'] = gen_random_city()
    person['town'] = gen_random_town()
    person['ward1'], person['ward2'] = gen_random_ward()
    person['day'] = gen_random_day()
    person['month'] = gen_random_month()
    person['year'] = gen_random_year()

    i = np.random.randint(0, 2)
    if i == 0:
        person['gender'] = 'Nam'
        person['name'] = gen_random_boy(boy, last_names)
    else:
        person['gender'] = 'Nữ'
        person['name'] = gen_random_girl(girl, last_names)
    

    dob = gen_random_date()
    person['dob'] = dob
    person['dob_chu'] = read_dob(dob)

    person['nation'] = gen_random_nation()
    person['nationality'] = gen_random_nationality()
    person['place_of_birth'] = gen_random_address(address)
    person['home_town'] = gen_random_address(address)
    person['person_id'] = gen_random_id()


    person['name_mother'] = gen_random_girl(girl, last_names)
    person['dob_mother'] = gen_random_date()
    person['nation_mother'] = gen_random_nation()
    person['nationality_mother'] = gen_random_nationality()
    person['residence_mother'] = gen_residence(address)
    

    person['name_father'] = gen_random_boy(boy, last_names)
    person['dob_father'] = gen_random_date()
    person['nation_father'] = gen_random_nation()
    person['nationality_father'] = gen_random_nationality()
    person['residence_father'] = gen_residence(address)

    person['register_address'] = gen_random_address(address)  
    person['number_id'] = gen_numberid()
    person['date'] = gen_random_date()
    person['note'] = gen_note()

    return person 




f = "vocab/boy.txt"
with open(f, "r", encoding='utf-8') as f:
    boy = f.read()

boy = boy.split("\n")
boy = boy[: -1]
# print(boy)

f = "vocab/girl.txt"
with open(f, "r", encoding='utf-8') as f:
    girl = f.read()

girl = girl.split("\n")
girl = girl[: -1]
# print(girl)

f = "vocab/last_names.txt"
with open(f, "r", encoding='utf-8') as f:
    last_names = f.read()

last_names = last_names.split("\n")
last_names = last_names[: -1]
# print(last_names)

f = "vocab/address.txt"
with open(f, "r", encoding='utf-8') as f:
    address = f.read()

address = address.split("\n")
address = address[: -1]

def gen_random_address(address):

    n = len(address)
    i = np.random.randint(0, n)
    return address[i]

def gen_random_girl(girl, last_names):
    n1 = len(girl)
    n2 = len(last_names)

    i1 = np.random.randint(0, n1)
    i2 = np.random.randint(0, n2)

    name = (last_names[i2]).upper() + " " + girl[i1].upper()

    return name 

def gen_random_boy(boy, last_names):
    n1 = len(boy)
    n2 = len(last_names)

    i1 = np.random.randint(0, n1)
    i2 = np.random.randint(0, n2)

    name = (last_names[i2]).upper() + " " + boy[i1].upper()

    return name 
# print(gen_random_girl(girl, last_names))
# print(gen_random_boy(boy, last_names))

path_template = "template/template_full/"
# template = "template1_day_du.docx"
files = os.listdir(path_template)
i = 0
idx = 0
while ( i < 3):
    
    for f in files:

        template = path_template + f
        print(template)

        person = gen_instance(boy, girl, last_names, address)

        # if i  % 10 == 0:
        #     person['person_id'] = ''
        document = ""
        document = MailMerge(template)

        document.merge(**person)

        result = "GEN1000/" + 'gen' + str(idx) + ".docx"

        json_path = "Key/" + "gen" + str(idx) + ".json"
        with open( json_path, 'w', encoding='utf-8') as myfile:
            json.dump(person, myfile)

        document.write(result)

        idx += 1
    i = i + 1

    # print(person)


template = "template2_day_du.docx"
for i in range(idx, idx + 30):
    person = gen_instance(boy, girl, last_names, address)
    if i  % 10 == 0:
        person['person_id'] = ''

    document = MailMerge(template)

    document.merge(**person)

    result = "GEN1000/" + 'gen' + str(i) + ".docx"

    json_path = "Key/" + "gen" + str(i) + ".json"
    with open( json_path, 'w', encoding='utf-8') as myfile:
        json.dump(person, myfile)

    document.write(result)


template = "template3_thieu_tt_me.docx"
for i in range(idx + 30, idx + 60 ):
    person = gen_instance(boy, girl, last_names, address)
    if i  % 10 == 0:
        person['person_id'] = ''

    person['name_mother'] = ""
    person['dob_mother'] = ""
    person['nation_mother'] = ""
    person['nationality_mother'] = ""
    person['residence_mother'] = ""


    document = MailMerge(template)

    document.merge(**person)

    result = "GEN1000/" + 'gen' + str(i) + ".docx"

    json_path = "Key/" + "gen" + str(i) + ".json"
    with open( json_path, 'w', encoding='utf-8') as myfile:
        json.dump(person, myfile)

    document.write(result)


template = "template4_thieu_tt_bo.docx"
for i in range(idx + 60, 1000):
    person = gen_instance(boy, girl, last_names, address)
    if i  % 10 == 0:
        person['person_id'] = ''
    person['name_father'] = ""
    person['dob_father'] = ""
    person['nation_father'] = ""
    person['nationality_father'] = ""
    person['residence_father'] = ""

    document = MailMerge(template)

    document.merge(**person)

    result = "GEN1000/" + 'gen' + str(i) + ".docx"

    json_path = "Key/" + "gen" + str(i) + ".json"
    with open( json_path, 'w', encoding='utf-8') as myfile:
        json.dump(person, myfile)

    document.write(result)

