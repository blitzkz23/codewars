# Categorize New Member [https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python]

def open_or_senior(data):
    category = []
    for tuple in data:
        if (tuple[0] >= 55 and tuple[1] > 7):
            category.append('Senior')
        else:
            category.append('Open')
    return category

# people's one liner
def open_or_senior2(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]