'''gen 1 sample GKS (giấy khai sinh)'''

from __future__ import print_function
from mailmerge import MailMerge 
from datetime import date 


sample = {
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
    'yob_mother': "1963",
    'nation_mother': "Kinh",
    'nationality_mother': "Việt Nam",
    'residence_mother': "Khu tập thể cầu đường 3",
    'name_father':"NGUYỄN VĂN MINH",
    'yob_father': "1964",
    'nation_father': "Kinh",
    'nationality_father': "Việt Nam",
    'residence_father': "Đội 7 thôn văn Gia, xã Trung Hưng, Sơn Tây",
    'register_address': "UBND phường Quang Trung, thị xã Sơn Tây, thành phố Hà Nội",
    'number_id': "14",
    'date': "26/01/1991",
    'note': "Thực hiện việc trích lục từ Sổ đăng kí khai sinh/"
}

def gen(template, result, cust):
    document = MailMerge(template)
    # print(document.get_merge_fields())

    document.merge(**cust)

    document.write(result)

gen("genGKS/template_gks.docx", "genGKS/gen_result/demo.docx", sample)

