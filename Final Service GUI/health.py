def bmi(height , weight):
    bmi_h = height * height
    bmi_w = weight * 10000
    bmi = bmi_w / bmi_h
    returnDic = {}
    returnDic['bmi'] = bmi
    if bmi > 30:
        returnDic['bmi상태'] = ("비만")
    elif bmi >= 25:
        returnDic['bmi상태'] = ("과체중")
    elif bmi >= 18.5:
        returnDic['bmi상태'] = ("정상")
    else:
        returnDic['bmi상태'] = ("저체중")
    return returnDic

def encouraged(gender, age):
    # 남성: 1, 여성: 2 // 단위: ~세
    kcal_man1 = 1700
    kcal_man2 = 2100
    kcal_man3 = 2500
    kcal_man4 = 2700
    kcal_man5 = 2600
    kcal_man6 = 2400
    kcal_man7 = 2200
    kcal_man8 = 2000
    kcal_man9 = 2000

    kcal_woman1 = 1500
    kcal_woman2 = 1800
    kcal_woman3 = 2000
    kcal_woman4 = 2000
    kcal_woman5 = 2100
    kcal_woman6 = 1900
    kcal_woman7 = 1800
    kcal_woman8 = 1600
    kcal_woman9 = 1600

    protein_man1 = 30
    protein_man2 = 40
    protein_man3 = 55
    protein_man4 = 65
    protein_man5 = 65
    protein_man6 = 60
    protein_man7 = 60
    protein_man8 = 55
    protein_man9 = 55

    protein_woman1 = 25
    protein_woman2 = 40
    protein_woman3 = 50
    protein_woman4 = 50
    protein_woman5 = 55
    protein_woman6 = 50
    protein_woman7 = 50
    protein_woman8 = 45
    protein_woman9 = 45

    sodium_man1 = 2000
    sodium_man2 = 2000
    sodium_man3 = 2000
    sodium_man4 = 2000
    sodium_man5 = 2000
    sodium_man6 = 2000
    sodium_man7 = 2000
    sodium_man8 = 2000
    sodium_man9 = 2000

    sodium_woman1 = 2000
    sodium_woman2 = 2000
    sodium_woman3 = 2000
    sodium_woman4 = 2000
    sodium_woman5 = 2000
    sodium_woman6 = 2000
    sodium_woman7 = 2000
    sodium_woman8 = 2000
    sodium_woman9 = 2000

    potassium_man1 = 2600
    potassium_man2 = 3000
    potassium_man3 = 3500
    potassium_man4 = 3500
    potassium_man5 = 3500
    potassium_man6 = 3500
    potassium_man7 = 3500
    potassium_man8 = 3500
    potassium_man9 = 3500

    potassium_woman1 = 2600
    potassium_woman2 = 3000
    potassium_woman3 = 3500
    potassium_woman4 = 3500
    potassium_woman5 = 3500
    potassium_woman6 = 3500
    potassium_woman7 = 3500
    potassium_woman8 = 3500
    potassium_woman9 = 3500

    calcium_man1 = 700
    calcium_man2 = 800
    calcium_man3 = 1000
    calcium_man4 = 900
    calcium_man5 = 800
    calcium_man6 = 800
    calcium_man7 = 750
    calcium_man8 = 700
    calcium_man9 = 700

    calcium_woman1 = 700
    calcium_woman2 = 800
    calcium_woman3 = 900
    calcium_woman4 = 800
    calcium_woman5 = 700
    calcium_woman6 = 700
    calcium_woman7 = 800
    calcium_woman8 = 800
    calcium_woman9 = 800

    returnDic = {}

    if gender == 1:
        if age >= 75:
            returnDic = {"칼로리": kcal_man9,
                         "단백질": protein_man9,
                         "단백질:": protein_man9,
                         "나트륨": sodium_man9,
                         "칼륨": potassium_man9,
                         "칼슘": calcium_man9}
        elif age >= 65:
            returnDic = {"칼로리": kcal_man8,
                         "단백질": protein_man8,
                         "단백질:": protein_man8,
                         "나트륨": sodium_man8,
                         "칼륨": potassium_man8,
                         "칼슘": calcium_man8}

        elif age >= 50:
            returnDic = {"칼로리": kcal_man7,
                         "단백질": protein_man7,
                         "단백질:": protein_man7,
                         "나트륨": sodium_man7,
                         "칼륨": potassium_man7,
                         "칼슘": calcium_man7}

        elif age >= 30:
            returnDic = {"칼로리": kcal_man6,
                         "단백질": protein_man6,
                         "단백질:": protein_man6,
                         "나트륨": sodium_man6,
                         "칼륨": potassium_man6,
                         "칼슘": calcium_man6}

        elif age >= 19:
            returnDic = {"칼로리": kcal_man5,
                         "단백질": protein_man5,
                         "단백질:": protein_man5,
                         "나트륨": sodium_man5,
                         "칼륨": potassium_man5,
                         "칼슘": calcium_man5}

        elif age >= 15:
            returnDic = {"칼로리": kcal_man4,
                         "단백질": protein_man4,
                         "단백질:": protein_man4,
                         "나트륨": sodium_man4,
                         "칼륨": potassium_man4,
                         "칼슘": calcium_man4}

        elif age >= 12:
            returnDic = {"칼로리": kcal_man3,
                         "단백질": protein_man3,
                         "단백질:": protein_man3,
                         "나트륨": sodium_man3,
                         "칼륨": potassium_man3,
                         "칼슘": calcium_man3}

        elif age >= 9:
            returnDic = {"칼로리": kcal_man2,
                         "단백질": protein_man2,
                         "단백질:": protein_man2,
                         "나트륨": sodium_man2,
                         "칼륨": potassium_man2,
                         "칼슘": calcium_man2}

        else:
            returnDic = {"칼로리": kcal_man1,
                         "단백질": protein_man1,
                         "단백질:": protein_man1,
                         "나트륨": sodium_man1,
                         "칼륨": potassium_man1,
                         "칼슘": calcium_man1}
    else:
        if age >= 75:
            returnDic = {"칼로리": kcal_woman9,
                         "단백질": protein_woman9,
                         "단백질:": protein_woman9,
                         "나트륨": sodium_woman9,
                         "칼륨": potassium_woman9,
                         "칼슘": calcium_woman9}

        elif age >= 65:
            returnDic = {"칼로리": kcal_woman8,
                         "단백질": protein_woman8,
                         "단백질:": protein_woman8,
                         "나트륨": sodium_woman8,
                         "칼륨": potassium_woman8,
                         "칼슘": calcium_woman8}


        elif age >= 50:
            returnDic = {"칼로리": kcal_woman7,
                         "단백질": protein_woman7,
                         "단백질:": protein_woman7,
                         "나트륨": sodium_woman7,
                         "칼륨": potassium_woman7,
                         "칼슘": calcium_woman7}

        elif age >= 30:
            returnDic = {"칼로리": kcal_woman6,
                         "단백질": protein_woman6,
                         "단백질:": protein_woman6,
                         "나트륨": sodium_woman6,
                         "칼륨": potassium_woman6,
                         "칼슘": calcium_woman6}


        elif age >= 19:
            returnDic = {"칼로리": kcal_woman5,
                         "단백질": protein_woman5,
                         "단백질:": protein_woman5,
                         "나트륨": sodium_woman5,
                         "칼륨": potassium_woman5,
                         "칼슘": calcium_woman5}


        elif age >= 15:
            returnDic = {"칼로리": kcal_woman4,
                         "단백질": protein_woman4,
                         "단백질:": protein_woman4,
                         "나트륨": sodium_woman4,
                         "칼륨": potassium_woman4,
                         "칼슘": calcium_woman4}


        elif age >= 12:
            returnDic = {"칼로리": kcal_woman3,
                         "단백질": protein_woman3,
                         "단백질:": protein_woman3,
                         "나트륨": sodium_woman3,
                         "칼륨": potassium_woman3,
                         "칼슘": calcium_woman3}


        elif age >= 9:
            returnDic = {"칼로리": kcal_woman2,
                         "단백질": protein_woman2,
                         "단백질:": protein_woman2,
                         "나트륨": sodium_woman2,
                         "칼륨": potassium_woman2,
                         "칼슘": calcium_woman2}
        else:
            returnDic = {"칼로리": kcal_woman1,
                         "단백질": protein_woman1,
                         "단백질:": protein_woman1,
                         "나트륨": sodium_woman1,
                         "칼륨": potassium_woman1,
                         "칼슘": calcium_woman1 }

    return returnDic

def recommendCal(height,weight,age,gender,activity):
#     gender = int(input("* 성별을 입력하세요(남성: 1, 여성: 2)"))
#     age = int(input("* 나이를 입력하세요(단위: 살)"))
#     height = int(input("* 키를 입력하세요(단위: cm)"))
#     weight = int(input("* 몸무게를 입력하세,요(단위: kg)"))
#     activity = int(
#         input("* 활동량을 입력하세요\ndef getRecommendation(data, person, sim_function=sim_pearson):"))
    returnDic = {}
    if gender == 1:
        basic1 = 66.47 + (13.75 * weight) + (5 * height) - (6.76 * age)

        if activity == 1:
            activity_A = basic1 * 0.2
        elif activity == 2:
            activity_A = basic1 * 0.375
        elif activity == 3:
            activity_A = basic1 * 0.555
        else:
            activity_A = basic1 * 0.725
        activity_all = basic1 + activity_A
        returnDic = {"기초대사량": basic1, "활동대사량": activity_A, "권장칼로리": activity_all}

    else:
        basic2 = 65.51 + (9.56 * weight) + (1.85 * height) - (4.68 * age)

        if activity == 1:
            activity_A2 = basic2 * 0.2
        elif activity == 2:
            activity_A2 = basic2 * 0.375
        elif activity == 3:
            activity_A2 = basic2 * 0.555
        else:
            activity_A2 = basic2 * 0.725

        activity_all2 = basic2 + activity_A2
        returnDic = {"기초대사량": basic2, "활동대사량": activity_A2, "권장칼로리": activity_all2}
    return returnDic

def healthMain(height , weight, age, gender,activity=2):
    dic = {}
    tempDic = {}
    for i in bmi(height,weight):
        dic[i]=bmi(height,weight)[i]
    for i in encouraged(gender,age):
        dic[i]= encouraged(gender,age)[i]
    for i in recommendCal(height,weight,age,gender,activity):
        dic[i] = recommendCal(height,weight,age,gender,activity)[i]

    return dic

# list = [174,70,27,1,2]
# healthMain(list[0],list[1],list[2],list[3],list[4])
# print(healthMain(list[0],list[1],list[2],list[3],list[4]))

