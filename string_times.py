def string_times(str, n):
  N = ""
  for i in range(n):
    N = N + str
    
  return N

# Test
print(string_times('Hi', 2)) #→ 'HiHi'
print(string_times('Hi', 3)) #→ 'HiHiHi'
print(string_times('Hi', 1)) #→ 'Hi'