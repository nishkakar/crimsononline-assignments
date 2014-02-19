# Write a function that will take a number n followed by an arbitrary number of string arguments and return the 
# concatenation of the longest n arguments from longest to shortest. If n is -1, concatenate all of the arguments 
# in this fashion. (Optional: Try passing a non-string argument after the first one. What happens? What are some 
# ways to handle this gracefully?)

# sorted(args, key = lambda args: for a in args: len(a[n:]), reverse = True)

def sortcat(n,*args):
  if n == -1:
    print "".join(sorted(args, key = len, reverse = True))
  else:
    stringlist = sorted(args, key = len, reverse = True)
    print "".join(stringlist[:n])

sortcat(1,'abc','bc')
sortcat(2,'abc','c','bc')
