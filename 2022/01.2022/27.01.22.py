
#Q03

cameras = [["Sony Compact",10300,2016],
            ["Nikon Compact",10500,2017],
            ["Canon Compact",11200,2015],
            ["Lumix Compact",10000,2020],
            ["Polaroid Compact",9500,2019],
            ["Sony DSLR",67000,2014],
            ["Nikon DSLR",35000,2015],
            ["Canon DSLR",47500,2019]]

theLabels = []   # Put the new camera label into this structure

def generate_label(camera_info):
    return camera_info[0] + " " + str(camera_info[1]) + "JPY YoM:" + str(camera_info[2])

for camera in cameras:
    theLabels.append(generate_label(camera))

#output the list of labels at the end
for label in theLabels:
    print(label)

#find the cheapest camera
cheapest_camera = sorted(cameras, key=lambda x:x[1])[0]
print(cheapest_camera[0] + " " + str(cheapest_camera[1]) + "JPY")

#or
name = ""
price = -1
yom = 0
for camera in cameras:
    if camera[1] < price:
        name = camera[0]
        price = camera[1]
        yom = camera[2]
    elif price == -1:
        name = camera[0]
        price = camera[1]
        yom = camera[2]
print(name + " " + str(price) + "JPY")
#find the newest camera 
newest_camera = sorted(cameras, key=lambda x:x[2], reverse=True)[0]
print(newest_camera[0] + " " + str(newest_camera[1]) + "JPY")

#or

name = ""
price = 0
yom = 0
for camera in cameras:
    if camera[2] > yom:
        name = camera[0]
        price = camera[1]
        yom = camera[2]
print(name + " " + str(price) + "JPY")
"""
Write a program to calculate and display:
Each students’ average performance over the three tests
The classes average performance on each test
The overall average score for male students
The overall average score for female students
The name and the average of the highest performing male student
The name and the average of the highest performing female student
The name and the average of the lowest performing male student
The name and the average of the lowest performing female student
"""
studentScores = [["Vashti","F",86,33,52],
                    ["Lynnette","F",37,24,62],
                    ["Janyce","F",65,89,73],
                    ["Elaine","F",10,32,94],
                    ["Felton","M",43,86,70],
                    ["Bettye","F",76,67,66],
                    ["Felicidad","F",89,27,44],
                    ["Alise","F",37,81,45],
                    ["Ernest","M",22,40,91],
                    ["Julio","M",69,36,36],
                    ["Hilma","F",65,72,70],
                    ["Riva","F",60,35,53],
                    ["Clementina","F",37,25,47],
                    ["Olin","M",31,62,13],
                    ["Tam","M",14,49,14],
                    ["Rodney","M",91,18,83],
                    ["Mireya","F",32,33,12],
                    ["Darline","F",23,77,38],
                    ["Tamar","M",43,26,36],
                    ["Tami","F",38,94,11]]
one_total = 0
two_total = 0
three_total = 0
count = 0
male_total = 0
male_count = 0
female_total = 0
female_count = 0
highest_male = ""
highest_male_score = 0
highest_female = ""
highest_female_score = 0
lowest_male = ""
lowest_male_score = -1
lowest_female = ""
lowest_female_score = -1
for student in studentScores:
    average_student_score = sum(student[2:5]) / 3
    print(str(student[0]) + "'s average score was " + str(round(average_student_score, 2)))
    one_total += student[2]
    two_total += student[3]
    three_total += student[4]
    count += 1
    if student[1] == "M":
        male_total += average_student_score
        male_count += 1
        if average_student_score > highest_male_score:
            highest_male_score = average_student_score
            highest_male = student[0]
        if average_student_score < lowest_male_score:
            lowest_male_score = average_student_score
            lowest_male = student[0]
        elif lowest_male_score == -1:
            lowest_male_score = average_student_score
            lowest_male = student[0]
    else:
        female_total += average_student_score
        female_count += 1
        if average_student_score > highest_female_score:
            highest_female_score = average_student_score
            highest_female = student[0]
        if average_student_score < lowest_female_score:
            lowest_female_score = average_student_score
            lowest_female = student[0]
        elif lowest_female == -1:
            lowest_female_score = average_student_score
            lowest_female = student[0]
print("The average performance of the class in test 1 : " + str(int(one_total/count)))
print("The average performance of the class in test 2 : " + str(int(two_total/count)))
print("The average performance of the class in test 3 : " + str(int(three_total/count)))

print("The average performance of the boys in the class : " + str(int(male_total/male_count)))
print("The average performance of the girls in the class : " + str(int(female_total/female_count)))

print(highest_male + " got " + str(highest_male_score) + " and got the best result out of the boys")
print(highest_female + " got " + str(highest_female_score) + " and got the best result out of the girls")

print(lowest_male + " got " + str(lowest_male_score) + " and got the worst result out of the boys")
print(lowest_female + " got " + str(lowest_female_score) + " and got the worst result out of the girls")