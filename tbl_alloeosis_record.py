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
        doctor_name = f.genRandomTypes(data_values.name_list)

        id = f.genId()
        record_no = people_item['record_id']
        name = people_item['name']



        resident_name =name
        guardian_name =
        relation_name =
        guardian_addr =
        guardian_tel =
        contact_name =
        contact_tel =
        household_type =
        household_desc =
        employment_code =
        employment_desc =
        is_agreed =
        is_agreed_desc =
        sign_name =
        sign_date =
        first_ill_date =
        past_symptom =
        past_symptom_desc =
        past_close_lock =
        past_close_lock_desc =
        treatment_od_code =
        treatment_od_desc =
        treatment_od =
        treatment_his =
        stay_hospital_num =
        first_treat_date =
        diagnosis_desc =
        diagnosis_org_id =
        diagnosis_org_name =
        diagnosis_date =
        last_effect_code =
        last_effect_desc =
        has_danger_act =
        act_affray_num =
        act_trouble_num =
        act_disaster_num =
        act_other_num =
        act_self_injury_num =
        act_attempted_suicide_num =
        endowment_position =
        endowment_position_desc =
        doctor_advice =
        reg_date =
        doctor_id =
        doctor_name =
        org_id =
        org_name =
        create_time =
        update_time =
        status = '0'

        mLine = "  %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s \n" % (id                        ,
record_no                 ,
resident_name             ,
guardian_name             ,
relation_name             ,
guardian_addr             ,
guardian_tel              ,
contact_name              ,
contact_tel               ,
household_type            ,
household_desc            ,
employment_code           ,
employment_desc           ,
is_agreed                 ,
is_agreed_desc            ,
sign_name                 ,
sign_date                 ,
first_ill_date            ,
past_symptom              ,
past_symptom_desc         ,
past_close_lock           ,
past_close_lock_desc      ,
treatment_od_code         ,
treatment_od_desc         ,
treatment_od              ,
treatment_his             ,
stay_hospital_num         ,
first_treat_date          ,
diagnosis_desc            ,
diagnosis_org_id          ,
diagnosis_org_name        ,
diagnosis_date            ,
last_effect_code          ,
last_effect_desc          ,
has_danger_act            ,
act_affray_num            ,
act_trouble_num           ,
act_disaster_num          ,
act_other_num             ,
act_self_injury_num       ,
act_attempted_suicide_num ,
endowment_position        ,
endowment_position_desc   ,
doctor_advice             ,
reg_date                  ,
doctor_id                 ,
doctor_name               ,
org_id                    ,
org_name                  ,
create_time               ,
update_time               ,
status )

        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\tbl_alloeosis_record.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
