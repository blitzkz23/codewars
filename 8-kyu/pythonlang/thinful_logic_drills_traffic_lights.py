# Thinkful - Logic Drills: Traffic light [https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python]
def update_light(current):
    # Python3.10 solution
    match current:
        case "green":
            current = "yellow"
        case "yellow":
            current = "red"
        case _:
            current = "green"
    
    return current

# People's one liner solution
def update_light2(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]