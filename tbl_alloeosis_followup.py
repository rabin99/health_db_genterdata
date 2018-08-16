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


        resident_name = name
        gmt_interview = f.genRandomString(10)
        Interview_way =f.genRandomString(1)
        Interview_way_desc =f.genRandomString()
        loss_flup_reason =f.genRandomString()
        loss_flup_reason_desc =f.genRandomString()
        death_date =f.genRandomString()
        die_reason_code =f.genRandomString()
        die_reason_desc =f.genRandomString()
        danger_grade =f.genRandomString()
        danger_grade_desc =f.genRandomString()
        symptom_code =f.genRandomString()
        symptom_desc =f.genRandomString()
        insight =f.genRandomString()
        insight_desc =f.genRandomString()
        sleep =f.genRandomString()
        sleep_desc =f.genRandomString()
        diet =f.genRandomString()
        diet_desc =f.genRandomString()
        sf_cuisine_life =f.genRandomString()
        sf_cuisine_life_desc =f.genRandomString()
        sf_housework =f.genRandomString()
        sf_housework_desc =f.genRandomString()
        sf_labor_work =f.genRandomString()
        sf_labor_work_desc =f.genRandomString()
        sf_learn_ability =f.genRandomString()
        sf_learn_ability_desc =f.genRandomString()
        sf_communication =f.genRandomString()
        sf_communication_desc =f.genRandomString()
        has_danger_act =f.genRandomString()
        has_danger_act_desc =f.genRandomString()
        act_affray_num =f.genRandomString()
        act_trouble_num =f.genRandomString()
        act_disaster_num =f.genRandomString()f.genRandomString()
        act_other_num =f.genRandomString()f.genRandomString()
        act_self_injury_num =f.genRandomString()f.genRandomString()
        act_attempted_suicide_num =f.genRandomString()f.genRandomString()
        interval_lock =f.genRandomString()f.genRandomString()
        interval_lock_desc =f.genRandomString()f.genRandomString()
        interval_his =f.genRandomString()f.genRandomString()
        interval_his_desc =f.genRandomString()f.genRandomString()
        leave_hospital_date =f.genRandomString()f.genRandomString()
        lab_check =f.genRandomString()f.genRandomString()
        lab_check_desc =f.genRandomString()f.genRandomString()
        drug_dependence_code =f.genRandomString()f.genRandomString()
        drug_dependence_desc =f.genRandomString()f.genRandomString()
        dar_code =f.genRandomString()f.genRandomString()
        dar_desc =f.genRandomString()f.genRandomString()
        treat_effect =f.genRandomString()f.genRandomString()
        treat_effect_desc =f.genRandomString()f.genRandomString()
        tt_code =f.genRandomString()f.genRandomString()
        tt_desc =f.genRandomString()f.genRandomString()
        tt_reason =f.genRandomString()f.genRandomString()
        tt_org_name =f.genRandomString()
        tt_department_name =f.genRandomString()
        used_drug_name1 =f.genRandomString()
        used_drug_way1 =f.genRandomString()
        used_drug_dose1 =f.genRandomString()
        used_drug_name2 =f.genRandomString()
        used_drug_way2 =f.genRandomString()
        used_drug_dose2 =f.genRandomString()
        used_drug_name3 =f.genRandomString()
        used_drug_way3 =f.genRandomString()
        used_drug_dose3 =f.genRandomString()
        guide_drug_name1 =f.genRandomString()
        guide_drug_way1 =f.genRandomString()
        guide_drug_dose1 =f.genRandomString()
        guide_drug_name2 =f.genRandomString()
        guide_drug_way2 =f.genRandomString()
        guide_drug_dose2 =f.genRandomString()
        guide_drug_name3 =f.genRandomString()
        guide_drug_way3 =f.genRandomString()
        guide_drug_dose3 =f.genRandomString()
        rehab_measure =f.genRandomString()
        flup_classification_code =f.genRandomString()
        flup_classification_desc =f.genRandomString()
        doctor_id =
        doctor_name =
        org_id =
        org_name =
        gmt_next =f.genDateList()[2]
        create_time =f.createTime()
        update_time = f.createTime()
        status = 0

        mLine = " %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s\n" % (id                       ,
record_no                ,
resident_name            ,
gmt_interview            ,
Interview_way            ,
Interview_way_desc       ,
loss_flup_reason         ,
loss_flup_reason_desc    ,
death_date               ,
die_reason_code          ,
die_reason_desc          ,
danger_grade             ,
danger_grade_desc        ,
symptom_code             ,
symptom_desc             ,
insight                  ,
insight_desc             ,
sleep                    ,
sleep_desc               ,
diet                     ,
diet_desc                ,
sf_cuisine_life          ,
sf_cuisine_life_desc     ,
sf_housework             ,
sf_housework_desc        ,
sf_labor_work            ,
sf_labor_work_desc       ,
sf_learn_ability         ,
sf_learn_ability_desc    ,
sf_communication         ,
sf_communication_desc    ,
has_danger_act           ,
has_danger_act_desc      ,
act_affray_num           ,
act_trouble_num          ,
act_disaster_num         ,
act_other_num            ,
act_self_injury_num      ,
act_attempted_suicide_num,
interval_lock            ,
interval_lock_desc       ,
interval_his             ,
interval_his_desc        ,
leave_hospital_date      ,
lab_check                ,
lab_check_desc           ,
drug_dependence_code     ,
drug_dependence_desc     ,
dar_code                 ,
dar_desc                 ,
treat_effect             ,
treat_effect_desc        ,
tt_code                  ,
tt_desc                  ,
tt_reason                ,
tt_org_name              ,
tt_department_name       ,
used_drug_name1          ,
used_drug_way1           ,
used_drug_dose1          ,
used_drug_name2          ,
used_drug_way2           ,
used_drug_dose2          ,
used_drug_name3          ,
used_drug_way3           ,
used_drug_dose3          ,
guide_drug_name1         ,
guide_drug_way1          ,
guide_drug_dose1         ,
guide_drug_name2         ,
guide_drug_way2          ,
guide_drug_dose2         ,
guide_drug_name3         ,
guide_drug_way3          ,
guide_drug_dose3         ,
rehab_measure            ,
flup_classification_code ,
flup_classification_desc ,
doctor_id                ,
doctor_name              ,
org_id                   ,
org_name                 ,
gmt_next                 ,
create_time              ,
update_time              ,
status                   )
        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\tb_lunger_flup.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
