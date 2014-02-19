# Write a function that takes one string argument and returns the string with the most common letter
# swapped with the least common letter

def swapchars(string):
  dict = {}
  for char in string:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  max_char = max(dict, key=dict.get) 
  min_char = min(dict, key=dict.get)
  new_string = ""
  for c in string:
    if c == max_char:
      new_string = new_string + min_char
    elif c == min_char:
      new_string = new_string + max_char
    else:
      new_string = new_string + c
  return new_string

print swapchars("There were a lot of escopeoples in the elevator on Tuesday.")