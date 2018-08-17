# -*- coding: utf-8 -*-

import random
import datetime
import time
import uuid
import data_values
import hashlib
# 住院
dataCount = 1000  # 1k.
codeRange = range(ord('a'), ord('z'))
alphaRange = [chr(x) for x in codeRange]
alphaMax = len(alphaRange)
daysMax = 4000
theDay = datetime.date(1990, 1, 1)


def genPK(randomlength=19):
    random_str = ''
    base_str = 'abcdefg0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def genRandomString(nameLength):
    global alphaRange, alphaMax
    length = random.randint(1, nameLength)
    name = ''
    for i in range(length):
        name += alphaRange[random.randint(0, alphaMax - 1)]
    return name


def genRandomDay():
    global daysMax, theDay
    mDays = random.randint(0, daysMax)
    mDate = theDay + datetime.timedelta(days=mDays)
    # return mDate.isoformat()
    return mDate


def genRandomTime():
    return str(time.strftime(" %H:%M:%S", time.localtime()))


def genRandomNum(maxNum):
    return random.randint(1, maxNum) / float(100)


def genRandomDecimal(minN, maxN):
    return random.uniform(minN, maxN)


def genRandomTypes(types):
    return random.choice(types)


def genId():
    return uuid.uuid1()


def genPhoneNum():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def genDateList():
    time_now = datetime.datetime.now()
    t1 = (time_now + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
    t2 = (time_now + datetime.timedelta(days=0)).strftime("%Y-%m-%d")
    t3 = (time_now + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    return [t1, t2, t3]


def genBeforeDate():
    time_now = datetime.datetime.now()
    return (time_now + datetime.timedelta(days=genInt(99))).strftime("%Y-%m-%d")


def createTime():
    return datetime.datetime.now()


def genInt(max, min=0):
    return (random.randint(min, max - 1))


if __name__ == '__main__':
    print(genRandomDay())
    print(str(genRandomDay()) + str(genRandomTime()))
    print(genPhoneNum())
    print(genRandomString(10))
    print(genRandomTypes((1, 2, 3)))

    print(111)
    print(genDateList())

    print(createTime())

    print(genInt(5))
    print(data_values.steer_person_desc[genInt(len(data_values.steer_person_desc))])

    print(genBeforeDate())


    print(genPK())

    for count in range(10):
        print(genInt(4,1))


# load data local infile 'D:\\PycharmProjects\\health_db_genterdata\\data\\tb_lunger_flup.txt' into TABLE tb_lunger_flup character set utf8 FIELDS TERMINATED by ',' ;
# load data local infile 'D:\\PycharmProjects\\health_db_genterdata\\data\\tbl_alloeosis_followup.txt' into TABLE tbl_alloeosis_followup character set utf8 FIELDS TERMINATED by ',' ;
# load data local infile 'D:\\PycharmProjects\\health_db_genterdata\\data\\tbl_alloeosis_record.txt' into TABLE tbl_alloeosis_record character set utf8 FIELDS TERMINATED by ',' ;
# load data local infile 'D:\\PycharmProjects\\health_db_genterdata\\data\\tbl_diabetes_interview.txt' into TABLE tbl_diabetes_interview character set utf8 FIELDS TERMINATED by ',' ;
# load data local infile 'D:\\PycharmProjects\\health_db_genterdata\\data\\tbl_hypertension_interview.txt' into TABLE tbl_hypertension_interview character set utf8 FIELDS TERMINATED by ',' ;
# load data local infile 'D:\\PycharmProjects\\health_db_genterdata\\data\\tbl_lunger_first_flup.txt' into TABLE tbl_lunger_first_flup character set utf8 FIELDS TERMINATED by ',' ;