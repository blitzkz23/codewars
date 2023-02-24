# If you can't sleep, just count sheep!! [https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python]
def count_sheep(n):
    countingSheep = ""
    for sheepCount in range(n):
        countingSheep += "{} sheep...".format(sheepCount+1)
    return countingSheep