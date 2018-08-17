# -*- coding: utf-8 -*-

import data_values
import f
import random
import datetime
import time

# 住院
dataCount = 1000  # 1k


def genDataBase(fileName, dataCount):
    outp = open(fileName, 'w',encoding='utf-8')
    i = 0
    while i < dataCount:
        people_item = f.genRandomTypes(data_values.people_list)
        doctor_name = f.genRandomTypes(data_values.name_list)

        id = f.genPK(19)
        record_no = people_item['record_id']
        name = people_item['name']

        resident_name = name
        gmt_interview = f.genRandomString(10)
        Interview_way = f.genRandomString(1)
        Interview_way_desc = f.genRandomString(10)
        loss_flup_reason = f.genRandomString(1)
        loss_flup_reason_desc = f.genRandomString(10)
        death_date = f.genRandomDay()
        die_reason_code = f.genRandomString(10)
        die_reason_desc = f.genRandomString(16)
        danger_grade = f.genRandomString(1)
        danger_grade_desc = f.genRandomString(10)
        symptom_code = f.genRandomString(32)
        symptom_desc = f.genRandomString(32)
        insight = f.genRandomString(1)
        insight_desc = f.genRandomString(10)
        sleep = f.genRandomString(1)
        sleep_desc = f.genRandomString(10)
        diet = f.genRandomString(1)
        diet_desc = f.genRandomString(10)
        sf_cuisine_life = f.genRandomString(1)
        sf_cuisine_life_desc = f.genRandomString(10)
        sf_housework = f.genRandomString(1)
        sf_housework_desc = f.genRandomString(10)
        sf_labor_work = f.genRandomString(1)
        sf_labor_work_desc = f.genRandomString(10)
        sf_learn_ability = f.genRandomString(1)
        sf_learn_ability_desc = f.genRandomString(10)
        sf_communication = f.genRandomString(1)
        sf_communication_desc = f.genRandomString(10)
        has_danger_act = f.genRandomString(1)
        has_danger_act_desc = f.genRandomString(10)
        act_affray_num = f.genRandomString(5)
        act_trouble_num = f.genRandomString(5)
        act_disaster_num = f.genRandomString(5)
        act_other_num = f.genRandomString(5)
        act_self_injury_num = f.genRandomString(5)
        act_attempted_suicide_num = f.genRandomString(5)
        interval_lock = f.genRandomString(1)
        interval_lock_desc = f.genRandomString(10)
        interval_his = f.genRandomString(1)
        interval_his_desc = f.genRandomString(10)
        leave_hospital_date = f.genRandomDay()
        lab_check = f.genRandomString(1)
        lab_check_desc = f.genRandomString(32)
        drug_dependence_code = f.genRandomString(32)
        drug_dependence_desc = f.genRandomString(32)
        dar_code = f.genRandomString(32)
        dar_desc = f.genRandomString(32)
        treat_effect = f.genRandomString(1)
        treat_effect_desc = f.genRandomString(10)
        tt_code = f.genRandomString(1)
        tt_desc = f.genRandomString(10)
        tt_reason = f.genRandomString(1)
        tt_org_name = data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        tt_department_name = data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        used_drug_name1 = f.genRandomString(10)
        used_drug_way1 = f.genRandomString(10)
        used_drug_dose1 = f.genRandomString(10)
        used_drug_name2 = f.genRandomString(10)
        used_drug_way2 = f.genRandomString(10)
        used_drug_dose2 = f.genRandomString(10)
        used_drug_name3 = f.genRandomString(10)
        used_drug_way3 = f.genRandomString(10)
        used_drug_dose3 = f.genRandomString(10)
        guide_drug_name1 = f.genRandomString(10)
        guide_drug_way1 = f.genRandomString(10)
        guide_drug_dose1 = f.genRandomString(10)
        guide_drug_name2 = f.genRandomString(10)
        guide_drug_way2 = f.genRandomString(10)
        guide_drug_dose2 = f.genRandomString(10)
        guide_drug_name3 = f.genRandomString(10)
        guide_drug_way3 = f.genRandomString(10)
        guide_drug_dose3 = f.genRandomString(10)
        rehab_measure = f.genRandomString(10)
        flup_classification_code = f.genRandomString(1)
        flup_classification_desc = f.genRandomString(10)
        doctor_id = f.genRandomString(19)
        doctor_name = data_values.name_list[f.genInt(len(data_values.name_list))]
        org_id = f.genRandomString(32)
        org_name = data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        gmt_next = f.genDateList()[2]
        create_time = f.createTime()
        update_time = f.createTime()
        status = 0

        mLine = " %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s\n" % (
        id,
        record_no,
        resident_name,
        gmt_interview,
        Interview_way,
        Interview_way_desc,
        loss_flup_reason,
        loss_flup_reason_desc,
        death_date,
        die_reason_code,
        die_reason_desc,
        danger_grade,
        danger_grade_desc,
        symptom_code,
        symptom_desc,
        insight,
        insight_desc,
        sleep,
        sleep_desc,
        diet,
        diet_desc,
        sf_cuisine_life,
        sf_cuisine_life_desc,
        sf_housework,
        sf_housework_desc,
        sf_labor_work,
        sf_labor_work_desc,
        sf_learn_ability,
        sf_learn_ability_desc,
        sf_communication,
        sf_communication_desc,
        has_danger_act,
        has_danger_act_desc,
        act_affray_num,
        act_trouble_num,
        act_disaster_num,
        act_other_num,
        act_self_injury_num,
        act_attempted_suicide_num,
        interval_lock,
        interval_lock_desc,
        interval_his,
        interval_his_desc,
        leave_hospital_date,
        lab_check,
        lab_check_desc,
        drug_dependence_code,
        drug_dependence_desc,
        dar_code,
        dar_desc,
        treat_effect,
        treat_effect_desc,
        tt_code,
        tt_desc,
        tt_reason,
        tt_org_name,
        tt_department_name,
        used_drug_name1,
        used_drug_way1,
        used_drug_dose1,
        used_drug_name2,
        used_drug_way2,
        used_drug_dose2,
        used_drug_name3,
        used_drug_way3,
        used_drug_dose3,
        guide_drug_name1,
        guide_drug_way1,
        guide_drug_dose1,
        guide_drug_name2,
        guide_drug_way2,
        guide_drug_dose2,
        guide_drug_name3,
        guide_drug_way3,
        guide_drug_dose3,
        rehab_measure,
        flup_classification_code,
        flup_classification_desc,
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
    genDataBase('.\\data\\tbl_alloeosis_followup.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
