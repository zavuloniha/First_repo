weight = 91.2
height = 168
age = 41

# weight = 72
# height = 160
# age = 45

# p 30%  = 560/4 = 140g
# c 30%  = 560/4 = 140g
# f 40%  = 746,8/9 = 83g


cal_requered_at_rest = 10 * weight + 6.25 * height - 5 * age - 161

cal_with_no_physical_activity = cal_requered_at_rest * 1.2
cal_with_deficit_15 = cal_with_no_physical_activity - cal_with_no_physical_activity * 0.15
protein1 = cal_with_deficit_15 * 0.3 / 4
carbohydrates1 = cal_with_deficit_15 * 0.3 / 4
fats1 = cal_with_deficit_15 * 0.4 / 9

cal_with_small_jogs_light_exercises = cal_requered_at_rest * 1.375
cal_with_deficit_15_2 = cal_with_small_jogs_light_exercises - cal_with_small_jogs_light_exercises * 0.15
protein2 = cal_with_deficit_15_2 * 0.3 / 4
carbohydrates2 = cal_with_deficit_15_2 * 0.3 / 4
fats2 = cal_with_deficit_15_2 * 0.4 / 9

cal_with_exercise_moderate_exertion = cal_requered_at_rest * 1.55
cal_with_deficit_15_3 = cal_with_exercise_moderate_exertion - cal_with_exercise_moderate_exertion * 0.15
protein3 = cal_with_deficit_15_3 * 0.3 / 4
carbohydrates3 = cal_with_deficit_15_3 * 0.3 / 4
fats3 = cal_with_deficit_15_3 * 0.4 / 9

cal_with_fully_exercising = cal_requered_at_rest * 1.725
cal_with_deficit_15_4 = cal_with_fully_exercising - cal_with_fully_exercising * 0.15
protein4 = cal_with_deficit_15_4 * 0.3 / 4
carbohydrates4 = cal_with_deficit_15_4 * 0.3 / 4
fats4 = cal_with_deficit_15_4 * 0.4 / 9

cal_with_work_physical_activities = cal_requered_at_rest * 1.9
cal_with_deficit_15_5 = cal_with_work_physical_activities - cal_with_work_physical_activities * 0.15
protein5 = cal_with_deficit_15_5 * 0.3 / 4
carbohydrates5 = cal_with_deficit_15_5 * 0.3 / 4
fats5 = cal_with_deficit_15_5 * 0.4 / 9

print(f"Калории необходимые для функционирования организма в состоянии покоя: {cal_requered_at_rest}")
print(f"Если у вас нет физических нагрузок и сидячая работа ваши калории: {cal_with_no_physical_activity}")
print(f"Если у вас нет физических нагрузок и сидячая работа ваши калории с дефицитом 15%: {cal_with_deficit_15}")
print(f"Количество белка: {protein1}гр")
print(f"Количество углеводов: {carbohydrates1}гр")
print(f"Количество жиров: {fats1}гр")

print(f"Если вы совершаете небольшие пробежки или делаете легкую гимнастику 1–3 раза в неделю ваши калории: {cal_with_small_jogs_light_exercises}")
print(f"Если вы совершаете небольшие пробежки или делаете легкую гимнастику 1–3 раза в неделю ваши калории с дефицитом 15%: {cal_with_deficit_15_2}")
print(f"Количество белка: {protein2}гр")
print(f"Количество углеводов: {carbohydrates2}гр")
print(f"Количество жиров: {fats2}гр")

print(f"Если вы занимаетесь спортом со средними нагрузками 3–5 раз в неделю ваши калории: {cal_with_exercise_moderate_exertion}")
print(f"Если вы занимаетесь спортом со средними нагрузками 3–5 раз в неделю ваши калории с дефицитом 15%: {cal_with_deficit_15_3}")
print(f"Количество белка: {protein3}гр")
print(f"Количество углеводов: {carbohydrates3}гр")
print(f"Количество жиров: {fats3}гр")

print(f"Если вы полноценно тренируетесь 6–7 раз в неделю ваши калории: {cal_with_fully_exercising}")
print(f"Если вы полноценно тренируетесь 6–7 раз в неделю ваши калории с дефицитом 15%: {cal_with_deficit_15_4}")
print(f"Количество белка: {protein4}гр")
print(f"Количество углеводов: {carbohydrates4}гр")
print(f"Количество жиров: {fats4}гр")

print(f"Если ваша работа связана с физическим трудом, вы тренируетесь 2 раза в день и включаете в программу тренировок силовые упражнения ваши калории: {cal_with_work_physical_activities}")
print(f"Если ваша работа связана с физическим трудом, вы тренируетесь 2 раза в день и включаете в программу тренировок силовые упражнения ваши калории с дефицитом 15%: {cal_with_deficit_15_5}")
print(f"Количество белка: {protein5}гр")
print(f"Количество углеводов: {carbohydrates5}гр")
print(f"Количество жиров: {fats5}гр")


