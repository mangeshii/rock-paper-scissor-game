import  random
tools=['rock','paper','scissor']
computer=random.choice(tools)

user=''

while user not in tools:
  user = raw_input('Select between rock,paper,scissor:')
  

  

  if user==computer:
   print('we matched,So its a draw')

  if user=='rock' and computer=='paper':
   print('Computer wins')

  elif user=='paper' and computer=='rock':
   print('User wins')
  
  if user=='scissor' and computer=='paper':
   print('user wins')

  elif user=='paper' and computer=='scissor':
   print('computer wins')
  
  if user=='rock' and computer=='scissor':
   print('user wins')
  
  elif user=='scissor' and computer=='rock':
   print('computer wins')

print('Computer is {}'.format(computer))
print('User is {}'.format(user))
