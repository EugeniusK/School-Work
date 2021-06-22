def check_number_equal(a, b):
	if a == b:
		return f"{a} and {b} are equal"
	else:
		return f"{a} and {b} are not equal"


print(check_number_equal(5, 6))


def check_number_odd(a):
	if bool(a % 2):
		return f"{a} is an odd integer"
	else:
		return f"{a} is not an odd integer"


print(check_number_odd(15))


def isNegative(a):
	if abs(a) != abs:
		return f"{a} is a negative integer"
	else:
		return f"{a} is a positive integer"


print(isNegative(-15))


def isLeapYear(a):
	if a % 4 != 0 or a % 400 != 0:
		return f"{a} is not a leap year"
	else:
		return f"{a} is a leap year"


print(isLeapYear(1900))


def canVote(a):
	if a >= 18:
		return "congratulations! you are eligible for casting your vote"
	else:
		return "you are ineligible for casting your vote due to your age"


print(canVote(18))


def compareZero(a):
	if a > 0:
		return "1"
	elif a < 0:
		return "-1"
	else:
		return "0"


print(compareZero(5))


def heightNick(a):
	if a < 140:
		return "Dwarf"
	elif a < 170:
		return "average"
	else:
		return "Damn ur tall"


print(heightNick(150))


def biggestNum(a, b, c):
  index_biggest = [a,b,c].index(max([a,b,c]))
  return f"1st number = {a} 2nd number = {b} 3rd number = {c} \nThe {index_biggest+1}{['st','nd','rd'][index_biggest]} number is the greatest number among three"


print(biggestNum(5, 6, 7))

def quadrant(x,y):
    if abs(x) == x:
        if abs(y) == y:
            return f"The coordinate point ({x},{y}) lies on the First quadrant."
        else:
            return f"The coordinate point ({x},{y}) lies on the Fourth quadrant."

    
    else:
        if abs(y) == y:
            return f"The coordinate point ({x},{y}) lies on the Second quadrant."
        else:
            return f"The coordinate point ({x},{y}) lies on the Third quadrant."

print(quadrant(5,5))

def eligibility(p,c,m):
    if m >= 65 and p >= 55 and c >= 50 and p+c+m >= 180 or sum(m,p) >= 140:
        return "The candidate is eligible for admission"
    else:
        return "The candidate is not eligible for admission"

print(eligibility(65,51,72))

def root(a,b,c):
    if b**2-4*a*c < 0:
        return "Roots are imaginary"
    elif b**2-4*a*c == 0:
        return "There is one solution"
    else:
        return "There are two solutions"

print(root(1,5,7))

def grade(roll,name,marks)
