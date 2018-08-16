# -*- coding: utf-8 -*-

import data_values
import f
import random
import datetime
import time

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

        resident_name = name
        guardian_name = f.genRandomString(10)
        relation_name = f.genRandomString(10)
        guardian_addr = f.genRandomString(10)
        guardian_tel = f.genRandomString(10)
        contact_name = f.genRandomString(10)
        contact_tel = f.genRandomString(10)
        household_type = f.genRandomString(1)
        household_desc = f.genRandomString(10)
        employment_code = f.genRandomString(1)
        employment_desc = f.genRandomString(10)
        is_agreed = f.genRandomString(1)
        is_agreed_desc = f.genRandomString(10)
        sign_name = f.genRandomString(10)
        sign_date = str(f.genRandomDay())
        first_ill_date = str(f.genRandomDay())
        past_symptom = f.genRandomString(10)
        past_symptom_desc = f.genRandomString(10)
        past_close_lock = f.genRandomString(1)
        past_close_lock_desc = f.genRandomString(10)
        treatment_od_code = f.genRandomString(1)
        treatment_od_desc = f.genRandomString(10)
        treatment_od = f.genRandomString(10)
        treatment_his = f.genRandomString(10)
        stay_hospital_num = f.genRandomString(6)
        first_treat_date = str(f.genRandomDay())
        diagnosis_desc = f.genRandomString(10)
        diagnosis_org_id = f.genRandomString(10)
        diagnosis_org_name = f.genRandomString(10)
        diagnosis_date = str(f.genRandomDay())
        last_effect_code = f.genRandomString(1)
        last_effect_desc = f.genRandomString(10)
        has_danger_act = f.genRandomString(10)
        act_affray_num = f.genRandomString(5)
        act_trouble_num = f.genRandomString(5)
        act_disaster_num = f.genRandomString(5)
        act_other_num = f.genRandomString(5)
        act_self_injury_num = f.genRandomString(5)
        act_attempted_suicide_num = f.genRandomString(5)
        endowment_position = f.genInt(1)
        endowment_position_desc = f.genRandomString(10)
        doctor_advice = f.genRandomString(10)
        reg_date = f.genRandomString(10)
        doctor_id = f.genRandomString(10)
        doctor_name = f.genRandomString(10)
        org_id = f.genRandomString(10)
        org_name = data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        create_time = f.createTime()
        update_time = f.createTime()
        status = 0

        mLine = "  %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s \n" % (
        id,
        record_no,
        resident_name,
        guardian_name,
        relation_name,
        guardian_addr,
        guardian_tel,
        contact_name,
        contact_tel,
        household_type,
        household_desc,
        employment_code,
        employment_desc,
        is_agreed,
        is_agreed_desc,
        sign_name,
        sign_date,
        first_ill_date,
        past_symptom,
        past_symptom_desc,
        past_close_lock,
        past_close_lock_desc,
        treatment_od_code,
        treatment_od_desc,
        treatment_od,
        treatment_his,
        stay_hospital_num,
        first_treat_date,
        diagnosis_desc,
        diagnosis_org_id,
        diagnosis_org_name,
        diagnosis_date,
        last_effect_code,
        last_effect_desc,
        has_danger_act,
        act_affray_num,
        act_trouble_num,
        act_disaster_num,
        act_other_num,
        act_self_injury_num,
        act_attempted_suicide_num,
        endowment_position,
        endowment_position_desc,
        doctor_advice,
        reg_date,
        doctor_id,
        doctor_name,
        org_id,
        org_name,
        create_time,
        update_time,
        status)

        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\data\\tbl_alloeosis_record.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
