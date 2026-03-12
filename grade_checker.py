
def grade_checker(score): # score är en parameter
    if score > 90:
        grade = "MVG"
    elif 80 >= score > 50: # and betyder att båda villkoren måste uppfyllas
        grade = "G"
    elif 90>= score > 80:
        grade = "VG"
    else:
        grade = "IG"

    return grade