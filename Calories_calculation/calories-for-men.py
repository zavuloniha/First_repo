weight = 91
height = 180
age = 45

cal_requered_at_rest = 10 * weight + 6.25 * height - 5 * age + 5

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

print(f"Calories required for the body to function at rest are: {cal_requered_at_rest}")

print(f"If you have no physical activity and a sedentary job your calories are: {cal_with_no_physical_activity}")
print(f"If you have no physical activity and a sedentary job your calories with 15 % deficit are: {cal_with_deficit_15}")
print(f"Proteins: {protein1}g")
print(f"Carbohydrates: {carbohydrates1}g")
print(f"Fats: {fats1}g")

print(f"If you take small jogs or do light exercises 1-3 times a week your calories are: {cal_with_small_jogs_light_exercises}")
print(f"If you take small jogs or do light exercises 1-3 times a week your calories with 15 % deficit are: {cal_with_deficit_15_2}")
print(f"Proteins: {protein2}g")
print(f"Carbohydrates: {carbohydrates2}g")
print(f"Fats: {fats2}g")

print(f"If you exercise with moderate exertion 3-5 times per week your calories are: {cal_with_exercise_moderate_exertion}")
print(f"If you exercise with moderate exertion 3-5 times per week your calories with 15 % deficit are: {cal_with_deficit_15_3}")
print(f"Proteins: {protein3}g")
print(f"Carbohydrates: {carbohydrates3}g")
print(f"Fats: {fats3}g")

print(f"If you are fully exercising 6-7 times a week your calories are: {cal_with_fully_exercising}")
print(f"If you are fully exercising 6-7 times a week your calories with 15 % deficit are: {cal_with_deficit_15_4}")
print(f"Proteins: {protein4}g")
print(f"Carbohydrates: {carbohydrates4}g")
print(f"Fats: {fats4}g")

print(f"If your job involves physical labor, you work out 2 times a day and include strength training exercises in your workout program your calories are: {cal_with_small_jogs_light_exercises}")
print(f"If your job involves physical labor, you work out 2 times a day and include strength training exercises in your workout program your calories with 15 % deficit are: {cal_with_deficit_15_5}")
print(f"Proteins: {protein5}g")
print(f"Carbohydrates: {carbohydrates5}g")
print(f"Fats: {fats5}g")

