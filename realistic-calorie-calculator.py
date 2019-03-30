import sys

PY2 = sys.version_info[0] == 2
if PY2:
    raise Exception("Python2 is not supported. Please use Python3.x.")

fatCalories = 4082 # 1 lb of weight loss or gain corresponds to 4082 calories

def main():

    print("Pick one and press enter:")
    print("1. Calculate calorie deficit or surplus over a period of time.")
    print("2. Calculate basal metabolism using caloric consumption data measured over a period of time.")
    print("3. Exit.")
    menu = input()
    if menu == "1":
        first()
    elif menu == "2":
        second()
    elif menu == "3":
        sys.exit()
    else:
        raise valueError("You can only pick existing options.")
        main()

def rerunCode():

    rerunCode = input("Would you like to try again? ").lower()
    if rerunCode == "yes":
        main()
    else:
        sys.exit()

def first():

    initialWeightStr = input("What was your starting weight (in lbs)? ")
    finalWeightStr = input("What was your final weight (in lbs)? ")
    timePeriodStr = input("How long did it take you to reach that weight (in days)? ")
    initialWeight = int(initialWeightStr)
    finalWeight = int(finalWeightStr)
    timePeriod = int(timePeriodStr)

    if (initialWeight and finalWeight and timePeriod) < 1:
        raise ValueError("Values have to be positive nonzero integers.")

    weightDifference = (initialWeight - finalWeight) / timePeriod
    deficit = fatCalories * weightDifference # number of calories in one pound of fat times the weightDifference

    if weightDifference > 0:
        print("On average, you have been at a", deficit, "daily calorie deficit. To lose around 1 pound a week aim for a deficit of 583 calories.\n")
    elif weightDifference == 0:
        print("Move on to the next section of this calculator.\n")
        main()
    else:
        print("On average, you have been at a", -deficit, "daily calorie surplus. To gain around 1 pound a week aim for a surplus of 583.\n")

    if timePeriod > 31:
        print("You are using a time period longer than 31 days. For an average that more closely resembles the present, use a shorter time period.\n")

    rerunCode()

def second():

    print("Using a period of time where you logged your calories on a daily basis, enter...")
    input_startingWeightStr = input("an initial weight: ")
    input_finalWeightStr = input("and a \"final\" weight: ")
    input_startingWeight = int(input_startingWeightStr)
    input_finalWeight = int(input_finalWeightStr)

    input_caloriepoints = input("Enter how many calories you consumed over that period of time, separated by commas: ")
    calorieList = input_caloriepoints.split(",")

    if (input_startingWeight and input_finalWeight) < 1:
        raise ValueError("Values have to be positive nonzero integers.")

    # take the average
    sum = 0
    for num in calorieList:
        sum += int(num)

    dayCount = len(calorieList)

    if dayCount < 2:
        raise ValueError("You need more data points.")
    elif 2 <= dayCount < 5:
        average = sum / dayCount
        print("It is recommended that you use at least 5 data points.")
    else:
        average = sum / dayCount

    averageWeightDifference = (input_startingWeight - input_finalWeight) / dayCount
    maintenanceCalories = averageWeightDifference * fatCalories + average

    print("At your current level of activity, your metabolism needs", maintenanceCalories, "calories per day to maintain your weight.")
    print("To lose around 1 pound a week, try to consume", maintenanceCalories - 583, "calories a day, or", maintenanceCalories + 583, "to gain 1 pound a week.")
    
    rerunCode()

main()
