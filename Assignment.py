#Session 4 Functions
l1 = (1, 4, 7)
l2 = (2, 4, 6)

def defu(list1, list2):

  defu_set = set(list1 + list2) # set = remove duplicates
  defu_list = list(defu_set) # list = makes value into a list

  return defu_list # return = stores value
result = defu(l1, l2)
print(result)

#Extra Points! Recursions
def james(k):
  if(k > 0):
    result = k + james(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
james()