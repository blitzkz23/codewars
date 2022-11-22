# Counting Sheep [https://www.codewars.com/kata/54edbc7200b811e956000556/train/python]
def count_sheeps(sheep):
    count = 0
    for sheepPosition in sheep:
        if (type(sheepPosition) != None) and sheepPosition == True: 
            count+=1
        else:
            pass
    return count
        
        