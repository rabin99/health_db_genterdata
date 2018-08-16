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




        resident_name =
        gmt_interview =
        symptom_code =
        symptom_desc =
        interview_way =
        interview_way_desc =
        l_sbp =
        l_dbp =
        r_sbp =
        r_dbp =
        weight =
        bmi =
        heart_rate =
        dpa =
        dpa_desc =
        physical_other =
        daily_smoke_amount =
        daily_drink_amount =
        sport_frequency =
        sport_duration_per =
        staple_food =
        mind_status =
        mind_desc =
        obey_status =
        obey_status2 =
        fpg =
        salt_intake_status =
        auxiliary_other =
        dar_code =
        dar_desc =
        rhg_code =
        rhg_desc =
        drug_dependence_code =
        drug_dependence_desc =
        classification_code =
        classification_desc =
        drug_name1 =
        drug_way1 =
        drug_dose1 =
        drug_name2 =
        drug_way2 =
        drug_dose2 =
        drug_name3 =
        drug_way3 =
        drug_dose3 =
        insulin_type =
        insulin_way_dose =
        tt_code =
        tt_reason =
        tt_org_name =
        tt_department_name =
        doctor_id =
        doctor_name =
        org_id =
        org_name =
        gmt_next =
        create_time =
        update_time =
        status = '0'

        mLine = " %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s\n" % (
            id,
            record_no,
            resident_name,
            gmt_interview,
            symptom_code,
            symptom_desc,
            interview_way,
            interview_way_desc,
            l_sbp,
            l_dbp,
            r_sbp,
            r_dbp,
            weight,
            bmi,
            heart_rate,
            dpa,
            dpa_desc,
            physical_other,
            daily_smoke_amount,
            daily_drink_amount,
            sport_frequency,
            sport_duration_per,
            staple_food,
            mind_status,
            mind_desc,
            obey_status,
            obey_status2,
            fpg,
            salt_intake_status,
            auxiliary_other,
            dar_code,
            dar_desc,
            rhg_code,
            rhg_desc,
            drug_dependence_code,
            drug_dependence_desc,
            classification_code,
            classification_desc,
            drug_name1,
            drug_way1,
            drug_dose1,
            drug_name2,
            drug_way2,
            drug_dose2,
            drug_name3,
            drug_way3,
            drug_dose3,
            insulin_type,
            insulin_way_dose,
            tt_code,
            tt_reason,
            tt_org_name,
            tt_department_name,
            doctor_id,
            doctor_name,
            org_id,
            org_name,
            gmt_next,
            create_time,
            update_time,
            status
        )

        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\tbl_diabetes_interview.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
