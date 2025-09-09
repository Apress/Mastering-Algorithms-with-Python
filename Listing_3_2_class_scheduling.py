def convert_am_pm_to_mins(time_stamp):
    hour, minutes = time_stamp.split()[0].split(":")
    am_pm = time_stamp.split()[1]
    hour, minutes = int(hour), int(minutes)
    return hour * 60 + minutes if am_pm == "am" else (hour % 12 + 12) * 60 + minutes

def max_class_scheduling(class_schedules):
    classes_selected = []
    # sort classes by end time
    class_schedules.sort(key = lambda s: (convert_am_pm_to_mins(s[2]), convert_am_pm_to_mins(s[1])), reverse=True)
    first_class, _, cur_class_end_time = class_schedules.pop()
    classes_selected.append(first_class)
    while class_schedules:
        next_class, next_class_start_time, next_class_end_time = class_schedules.pop()
        if convert_am_pm_to_mins(cur_class_end_time) <= convert_am_pm_to_mins(next_class_start_time):
            classes_selected.append(next_class)
            cur_class_end_time = next_class_end_time
    return classes_selected

if __name__ == "__main__":
    schedules = [("Art", "9:30 am", "11:30 am"), 
                 ("Literature", "12:00 pm", "1:30 pm"),
                 ("Math", "8:00 am", "10:00 am"),
                 ("Physics", "9:00 am", "10:00 am"),
                 ("History", "8:30 am", "9:30 am"),
                 ("Biology", "2:00 pm", "3:00 pm"),
                 ("Latin", "12:30 pm", "2:00 pm")]
    print (max_class_scheduling(schedules))