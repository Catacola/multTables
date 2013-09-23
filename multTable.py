import random

upperLimit=30
nProblems=10

nCorrect=0
nWrong=0

for i in range(nProblems):
  n1 = random.randint(1,upperLimit)
  n2 = random.randint(1,upperLimit)

  usrAns = raw_input(str(n1)+'x'+str(n2)+'=')

  if usrAns == int(usrAns):
    print 'Correct!'
    nCorrect+=1
  else:
    print 'Wrong, it\'s ',n1*n2
    nWrong+=1

print '-----------------------'
print nCorrect, ' correct, ', nWrong, ' wrong'
print nCorrect*100.0/nProblems, '% correct'
