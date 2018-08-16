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

        flup_date = f.genRandomDay()
        flup_type = f.genRandomString(1)
        flup_desc = f.genRandomString(10)
        user_type = f.genRandomString(1)
        user_type_desc = f.genRandomString(10)
        pb_type = f.genRandomString(1)
        pb_type_desc = f.genRandomString(10)
        resist_drug_situation = f.genRandomString(1)
        resist_drug_situation_desc = f.genRandomString(10)
        symptom_code = f.genRandomString(10)
        symptom_desc = f.genRandomString(10)
        chemotherapy_plan = f.genRandomString(10)
        drug_use = f.genRandomString(1)
        drug_use_desc = f.genRandomString(10)
        drug_dose = f.genRandomString(1)
        drug_dose_desc = f.genRandomString(10)
        steer_selection = f.genRandomString(1)
        steer_selection_desc = data_values.steer_person_desc[f.genInt(len(data_values.steer_person_desc))]
        single_room = f.genRandomString(1)
        single_room_desc = f.genRandomString(10)
        ventilation = f.genRandomString(1)
        ventilation_desc = f.genRandomString(10)
        daily_smoke = f.genRandomString(8)
        daily_drink = f.genRandomString(16)
        drug_addr = f.genRandomString(10)
        drug_time = f.genRandomString(10)
        drug_record_form = f.genRandomString(1)
        drug_record_form_desc = f.genRandomString(10)
        drug_method_deposit = f.genRandomString(1)
        drug_method_deposit_desc = f.genRandomString(10)
        lunger_course = f.genRandomString(1)
        lunger_course_desc = f.genRandomString(10)
        irregular_harm = f.genRandomString(1)
        irregular_harm_desc = f.genRandomString(10)
        drug_harm_deal = f.genRandomString(1)
        drug_harm_deal_desc = f.genRandomString(10)
        phlegm_recovery = f.genRandomString(1)
        phlegm_recovery_desc = f.genRandomString(10)
        take_medicine = f.genRandomString(1)
        take_medicine_desc = f.genRandomString(10)
        habit_attention_item = f.genRandomString(1)
        habit_attention_item_desc = f.genRandomString(10)
        contact_check = f.genRandomString(1)
        contact_check_desc = f.genRandomString(10)
        doctor_id = f.genRandomString(10)
        doctor_name = data_values.name_list[f.genInt(len(data_values.name_list))]
        org_id = f.genRandomString(10)
        org_name = data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        gmt_next = f.genDateList()[2]
        create_time = f.createTime()
        update_time = f.createTime()
        status = 0

        mLine = " %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s \n" % (
        id,
        record_no,
        name,
        flup_date,
        flup_type,
        flup_desc,
        user_type,
        user_type_desc,
        pb_type,
        pb_type_desc,
        resist_drug_situation,
        resist_drug_situation_desc,
        symptom_code,
        symptom_desc,
        chemotherapy_plan,
        drug_use,
        drug_use_desc,
        drug_dose,
        drug_dose_desc,
        steer_selection,
        steer_selection_desc,
        single_room,
        single_room_desc,
        ventilation,
        ventilation_desc,
        daily_smoke,
        daily_drink,
        drug_addr,
        drug_time,
        drug_record_form,
        drug_record_form_desc,
        drug_method_deposit,
        drug_method_deposit_desc,
        lunger_course,
        lunger_course_desc,
        irregular_harm,
        irregular_harm_desc,
        drug_harm_deal,
        drug_harm_deal_desc,
        phlegm_recovery,
        phlegm_recovery_desc,
        take_medicine,
        take_medicine_desc,
        habit_attention_item,
        habit_attention_item_desc,
        contact_check,
        contact_check_desc,
        doctor_id,
        doctor_name,
        org_id,
        org_name,
        gmt_next,
        create_time,
        update_time,
        status)

        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\data\\tbl_lunger_first_flup.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
