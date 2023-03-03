# Total Amount of Points [https://www.codewars.com/kata/5bb904724c47249b10000131/train/python]
def points(games):
    x_points = 0
    for score in games:
        x, y = int(score[0]), int(score[2])
        if x > y:
            x_points += 3
        elif x < y:
            x_points += 0
        elif x == y:
            x_points += 1
    return x_points


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))