# Counting Sheep [https://www.codewars.com/kata/54edbc7200b811e956000556/train/python]
def count_sheeps(sheepArr):
    count = 0
    for sheepPosition in sheepArr:
        if (type(sheepPosition) != None) and sheepPosition == True:
            count += 1
        else:
            pass
    return count
