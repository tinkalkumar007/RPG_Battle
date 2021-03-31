def my_function(l,m):
      if(l==0):
          print(m)
      else:
          my_function(l-1,l+m)
my_function(2,3)
# In Case of infinite no of arguments you need to use a star(*) operator. let's see

def my_people(*people):
    for person in people:
        print('This Person name is',person)
my_people('Tinkal','Unknown','Anjali','Shobha','Sakshi')


