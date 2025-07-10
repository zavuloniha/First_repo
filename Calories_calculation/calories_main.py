
class Calories():
    def __init__(self, weight: float, height: int, age: int):
        self.weight = weight
        self.height = height
        self.age = age
       
    def cal_requered_at_rest(self):
        cal_requered_at_rest = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        # return cal_requered_at_rest
        print(f"dddd {cal_requered_at_rest}")
    
    def cal_with_no_physical_activity(self, cal_requered_at_rest):
        cal_with_no_physical_activity = cal_requered_at_rest * 1.2
        #return print(f' {cal_with_no_physical_activity}')
        print(f' {cal_with_no_physical_activity}')
    
    def cal_with_small_jogs_light_exercises(self, cal_requered_at_rest):
        cal_with_small_jogs_light_exercises = cal_requered_at_rest * 1.375
        return  cal_with_small_jogs_light_exercises
    
    def cal_with_exercise_moderate_exertion(self, cal_requered_at_rest):
        cal_with_exercise_moderate_exertion = cal_requered_at_rest * 1.55
        return  cal_with_exercise_moderate_exertion
    
    def cal_with_fully_exercising(self, cal_requered_at_rest):
        cal_with_fully_exercising = cal_requered_at_rest * 1.725
        return   cal_with_fully_exercising
    
    def cal_with_work_physical_activities(self, cal_requered_at_rest):
        cal_with_work_physical_activities = cal_requered_at_rest * 1.9
        return  cal_with_work_physical_activities

    #cal_with_deficit_15 = cal_with_no_physical_activity - cal_with_no_physical_activity * 0.15
    #return cal_requered_at_rest
    
   # return cal_requered_at_rest, cal_with_no_physical_activity, cal_with_deficit_15

# my_cal = Calories(72.5, 160, 45)
# print(my_cal.cal_requered_at_rest)
my_cal = Calories(77.3, 160, 45)
my_cal.cal_requered_at_rest
#my_cal.cal_with_no_physical_activity
# print(my_cal.cal_with_no_physical_activity)
# print(my_cal.cal_with_small_jogs_light_exercises)