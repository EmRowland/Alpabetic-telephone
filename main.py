from time import sleep


txt = input("Enter a number in the format xxx-xxx:")

print("You entered :" + " " + txt)
sleep(2)
print("Formatting Your input  ............")
sleep (5)
for i in txt:
  if(i.isalpha() and 
    i == 'a' or
    i=='b' or
    i == 'C'):
    txt = txt.replace(i, '2')

  elif(i.isalpha() and

    i == 'd' or
    i == 'e' or
    i == 'f'):
    txt = txt.replace(i ,'3')
  elif(i.isalpha() and

    i == 'g' or
    i == 'h' or
    i == 'i'):
    txt = txt.replace(i ,'4')
  elif(i.isalpha() and

    i == 'j' or
    i == 'k' or
    i == 'l'):
    txt = txt.replace(i ,'5')
  elif(i.isalpha() and

    i == 'm' or
    i == 'n' or
    i == 'o'):
    txt = txt.replace(i ,'6')
  elif(i.isalpha() and

    i == 'p' or
    i == 'q' or
    i == 's' or
    i == 'r'):
    txt = txt.replace(i ,'7')
  elif(i.isalpha() and

  
    i == 't' or
    i == 'u'):
    txt = txt.replace(i ,'8')
  elif(i.isalpha() and

    i == 'v' or
    i == 'w' or
    i == 'x' or
    i == 'y'):
    txt = txt.replace(i ,'9')
print(txt)

