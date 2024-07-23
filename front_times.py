#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;



def front_times(str, n):
  string = ""
  if(len(str) < 4):
    for i in range(n):
      string = string + str
      
    return string

  front = str[:3]
  result = ""
  
  for i in range(n):
    result = result + front
    
  return result


print(front_times('Chocolate', 2)) #→ 'ChoCho'
print(front_times('Chocolate', 3)) #→ 'ChoChoCho'
print(front_times('AbcAbc', 3)) #→ 'AbcAbcAbc'
