def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to python")
    calculate_bmi(weight = 57, height = 1.73)
    temp_list = get_user_input()
    sort_temp_list= sort_temperature(temp_list)
    print(f"average value = {calc_average(sort_temp_list):.2f}")
    print(f"minimum value = {find_min_max(sort_temp_list)}")
    print(f"sort temperature = {sort_temp_list}")
    print(f"median temperature = {calc_median_temperature(sort_temp_list)}")
    
def sort_temperature(num_list):
    return sorted(num_list)

def display_main_menu():
    print("display main menu")
    
def get_user_input():
    list_of_numbers = input("Enter some numbers seperated by commas (e.g. 5, 67, 32): ")
    list_of_numbers = [float(i.strip()) for i in list_of_numbers.split(",") if i.strip()]
    return list_of_numbers

   
def calc_average(num_list):
    sum = 0
    temp_list = num_list
    for i in temp_list:
        sum +=i
    return (sum)/len(temp_list) if temp_list else 0.0 

def find_min_max(num_list):
    temp_list = num_list
    min_val = min(temp_list)
    max_val = max(temp_list)
    return [min_val, max_val]
    
def calc_median_temperature(num_list):
    sorted_list = num_list
    length = len(sorted_list)
    if length % 2 != 0:
        mid = length // 2
        median = sorted_list[mid]
    else:
        mid1 = (length // 2) - 1
        mid2 = (length // 2)
        median = (sorted_list[mid1]+sorted_list[mid2]) /2
    return median
    
    
    
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("weight = " + str(weight))
    
    bmi = weight/(height*height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("under weight")
        return -1
    elif bmi > 25.0:
        print("Over weight")
        return 1
    else:
        print("Normal Weight")
        return 0
        
        

if __name__ == "__main__":
    main()