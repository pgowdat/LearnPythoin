for i in range(11):
    if(i==7):
      print("come out of loop") 
      break
    print("5 X",i," =",5*i)



for i in range(11):
    if(i==7):
      print("skip the  iteration") 
      continue
    print("5 X",i," =",5*i)

i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break
   