import matplotlib.pyplot as plt
import numpy as np
def main():
    userData = getData()
    if userData["weight"] < userData["goal"] or userData["calories"] <= 0 or userData["intensity"] <= 0:
        print("error: data not valid")
    else:
        upperLoss = (userData["intensity"] / 100) * 2
        minTime = (userData["weight"] - userData["goal"]) / upperLoss
        x = np.array([0, minTime])
        y = userData["weight"] - (x * upperLoss)
        increment = upperLoss * 500
        if userData["calories"] - increment < 0:
            print("error: no suitable course for specified intensity")
        else:
            print("Daily Calories: %d (%d calories less than original %d calories)" % (userData["calories"] - increment, increment, userData["calories"]))
            plt.plot(x, y)
            plt.xlabel("Week")
            plt.ylabel("Weight")
            plt.show()
            #y=ax+b; b=0, x=41.66 weeks, y < 2, a < 2/41.66
            print(minTime)
def getData():
    userFile = open("user1.data", "r")
    userFile = [line.rstrip('\n') for line in userFile]
    userData = {}
    userData["weight"] = int(userFile[0].split(":")[1])
    userData["age"] = int(userFile[1].split(":")[1])
    userData["height"] = int(userFile[2].split(":")[1])
    userData["sex"] = userFile[3].split(":")[1]
    userData["calories"] = int(userFile[4].split(":")[1])
    userData["goal"] = int(userFile[5].split(":")[1])
    userData["intensity"] = int(userFile[6].split(":")[1])
    return userData
main()