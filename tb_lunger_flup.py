# -*- coding: utf-8 -*-

import random
import time

import data_values
import f

# 住院
dataCount = 1000  # 1k


def genDataBase(fileName, dataCount):
    outp = open(fileName, 'w')
    i = 0
    while i < dataCount:
        people_item = f.genRandomTypes(data_values.people_list)
        doctor_name = f.genRandomTypes(data_values.name_list)

        id = f.genId()
        record_no = people_item['record_id']
        name = people_item['name']

        flup_date = f.genRandomDay()
        treat_month = str(f.genInt(29))
        steer_person = f.genInt(len(data_values.steer_person_desc))
        steer_person_desc = data_values.steer_person_desc[steer_person]

        flup_type = f.genInt(len(data_values.flup_type_desc))
        flup_type_desc = data_values.flup_type_desc[flup_type]

        symptom_code = f.genRandomString(5)
        symptom_desc = f.genRandomString(10)
        daily_smoke = f.genRandomString(8)
        daily_drink = f.genRandomString(16)
        chemotherapy_plan = f.genRandomString(32)
        drug_use = f.genRandomString(1)
        drug_use_desc = f.genRandomString(32)
        drug_dose = f.genRandomString(1)
        drug_dose_desc = f.genRandomString(16)
        leak_medicine_num = f.genRandomString(3)
        ad_reaction = f.genRandomString(1)
        ad_reaction_desc = f.genRandomString(10)
        complication = f.genInt(9)
        complication_desc = f.genRandomString(10)
        referral_reason = f.genRandomString(10)
        referral_org_name = data_values.dept_list[f.genInt(len(data_values.dept_list))][1]
        referral_department = data_values.dept_list[f.genInt(len(data_values.dept_list))][1]
        deal_advice = f.genRandomString(20)
        two_flup_result = f.genRandomString(10)
        stop_treat_time = f.genRandomDay()
        stop_treat_reason = f.genInt(9)
        stop_treat_reason_desc = f.genRandomString(20)
        flup_user_num = str(f.genInt(99))
        doctor_id = f.genRandomString(19)
        doctor_name = data_values.name_list[f.genInt(len(data_values.name_list))]
        gmt_next = f.genDateList()[2]

        doc = f.genInt(len(data_values.name_list))
        assess_doctor_id = doc
        assess_doctor_name = data_values.name_list[doc]

        org = f.genInt(len(data_values.hospital_list))
        org_id = data_values.hospital_list[org][0]
        org_name = data_values.hospital_list[org][1]
        assess_ = f.genInt(len(data_values.hospital_list))
        assess_org_id = data_values.hospital_list[assess_][0]
        assess_org_name = data_values.hospital_list[assess_][1]
        ttt = f.createTime()
        create_time = ttt
        update_time = ttt
        status = 0

        mLine = " %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
            id,
            record_no,
            name,
            flup_date,
            treat_month,
            steer_person,
            steer_person_desc,
            flup_type,
            flup_type_desc,
            symptom_code,
            symptom_desc,
            daily_smoke,
            daily_drink,
            chemotherapy_plan,
            drug_use,
            drug_use_desc,
            drug_dose,
            drug_dose_desc,
            leak_medicine_num,
            ad_reaction,
            ad_reaction_desc,
            complication,
            complication_desc,
            referral_reason,
            referral_org_name,
            referral_department,
            deal_advice,
            two_flup_result,
            stop_treat_time,
            stop_treat_reason,
            stop_treat_reason_desc,
            flup_user_num,
            doctor_id,
            doctor_name,
            gmt_next,
            assess_doctor_id,
            assess_doctor_name,
            org_id,
            org_name,
            assess_org_id,
            assess_org_name,
            create_time,
            update_time,
            status)
        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\data\\tb_lunger_flup.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
