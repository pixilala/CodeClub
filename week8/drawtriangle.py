def printNumbers(n):
  m = int(n)+1
  for i in range(1,n+1):
    print (" "*m, end="  ")
    for j in range(i):
      if i < 10 :
        print(i + " ")
      else:
        print (i, end="  ")
    print ("  ")
    m = m -1
printNumbers(int(input("enter a number:")))
