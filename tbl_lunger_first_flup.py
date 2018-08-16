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




        flup_date =
        flup_type =
        flup_desc =
        user_type =
        user_type_desc =
        pb_type =
        pb_type_desc =
        resist_drug_situation =
        resist_drug_situation_desc =
        symptom_code =
        symptom_desc =
        chemotherapy_plan =
        drug_use =
        drug_use_desc =
        drug_dose =
        drug_dose_desc =
        steer_selection =
        steer_selection_desc =
        single_room =
        single_room_desc =
        ventilation =
        ventilation_desc =
        daily_smoke =
        daily_drink =
        drug_addr =
        drug_time =
        drug_record_form =
        drug_record_form_desc =
        drug_method_deposit =
        drug_method_deposit_desc =
        lunger_course =
        lunger_course_desc =
        irregular_harm =
        irregular_harm_desc =
        drug_harm_deal =
        drug_harm_deal_desc =
        phlegm_recovery =
        phlegm_recovery_desc =
        take_medicine =
        take_medicine_desc =
        habit_attention_item =
        habit_attention_item_desc =
        contact_check =
        contact_check_desc =
        doctor_id =
        doctor_name =
        org_id =
        org_name =
        gmt_next =
        create_time =
        update_time =
        status = '0'

        mLine = " %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s \n" % (id                        ,
record_no                 ,
name                      ,
flup_date                 ,
flup_type                 ,
flup_desc                 ,
user_type                 ,
user_type_desc            ,
pb_type                   ,
pb_type_desc              ,
resist_drug_situation     ,
resist_drug_situation_desc,
symptom_code              ,
symptom_desc              ,
chemotherapy_plan         ,
drug_use                  ,
drug_use_desc             ,
drug_dose                 ,
drug_dose_desc            ,
steer_selection           ,
steer_selection_desc      ,
single_room               ,
single_room_desc          ,
ventilation               ,
ventilation_desc          ,
daily_smoke               ,
daily_drink               ,
drug_addr                 ,
drug_time                 ,
drug_record_form          ,
drug_record_form_desc     ,
drug_method_deposit       ,
drug_method_deposit_desc  ,
lunger_course             ,
lunger_course_desc        ,
irregular_harm            ,
irregular_harm_desc       ,
drug_harm_deal            ,
drug_harm_deal_desc       ,
phlegm_recovery           ,
phlegm_recovery_desc      ,
take_medicine             ,
take_medicine_desc        ,
habit_attention_item      ,
habit_attention_item_desc ,
contact_check             ,
contact_check_desc        ,
doctor_id                 ,
doctor_name               ,
org_id                    ,
org_name                  ,
gmt_next                  ,
create_time               ,
update_time               ,
status                    )

        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\tbl_lunger_first_flup.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
