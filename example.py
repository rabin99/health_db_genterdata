# -*- coding: utf-8 -*-

import data_values
import f
import random
import datetime
import time

# 住院
dataCount = 1000  #1k


def genDataBase(fileName, dataCount):
    outp = open(fileName, 'w')
    i = 0
    while i < dataCount:
        people_item = f.genRandomTypes(data_values.people_list)
        RECORD_ID = people_item['record_id']
        NAME = people_item['name']
        AMOUNT = f.genRandomDecimal(1, 10)
        DOCTOR_NAME = f.genRandomTypes(data_values.name_list)
        dept = f.genRandomTypes(data_values.dept_list)
        DEPT_CODE = dept[0]
        DEPT_NAME = dept[1]
        hospital = f.genRandomTypes(data_values.hospital_list)
        HOSPITAL_CODE = hospital[0]
        HOSPITAL_NAME = hospital[1]
        date = f.genRandomDay()
        REPORT_PERIOD = date.strftime("%Y%m%d")
        SYSTEM_TIME = date.strftime("%Y-%m-%d") + f.genRandomTime()

        mLine = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (RECORD_ID, NAME,
                                                     AMOUNT, DOCTOR_NAME, DEPT_CODE, DEPT_NAME,
                                                     HOSPITAL_CODE, HOSPITAL_NAME, REPORT_PERIOD, SYSTEM_TIME)
        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\example.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
