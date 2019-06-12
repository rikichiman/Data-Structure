# define a dictionary
# type o: open  c: close
Bchar = ({"c": '(', "id": 1, "type": 'o'},
         {"c": '[', "id": 2, "type": 'o'},
         {"c": '{', "id": 3, "type": 'o'},
         {"c": ')', "id": 1, "type": 'c'},
         {"c": ']', "id": 2, "type": 'c'},
         {"c": '}', "id": 3, "type": 'c'})


def checkType(c, t):
    for bc in Bchar:
        if c == bc["c"] and bc["type"] == t:
            return bc["id"]
    return 0


def testString(inS):
    stack = []  # contains all the IDs
    for c in inS:
        id = checkType(c, 'c')
        if (id != 0):  # it's a closing char
            if len(stack) != 0:
                if id == stack[len(stack)-1]:
                    stack.pop()  # just remove it and continue
                else:
                    return False
            else:
                return False
        else:
            # it's an openning char just push it to the stack
            stack.append(checkType(c, 'o'))
    if (len(stack) > 0):
        return False
    return True


# let's try it
def check(s):
    print("test for "+s)
    print(testString(s))


check("({([])})()")
check("({([])})()]")
check("(([])})()")
check("(([])){}()")
