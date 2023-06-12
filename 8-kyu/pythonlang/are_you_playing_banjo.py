# Are you playing banjo? [https://www.codewars.com/kata/53af2b8861023f1d88000832/solutions/python]
def areYouPlayingBanjo(name):
   return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"