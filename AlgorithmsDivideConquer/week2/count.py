arr = [1,2,5,3,4,6]

def count_split(a, b):
  i = 0
  j = 0
  invs = 0
  sortd = []
  #print(a, b)
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
        #print('add a[' + str(i)+']')
      sortd.append(a[i])
      i += 1

    else:
      invs += len(a) - i
      #print('add b[' + str(j)+']')
      sortd.append(b[j])
      j += 1
  
  while i < len(a):
    sortd.append(a[i])
    i += 1
  while j < len(b):
    sortd.append(b[j])
    j += 1
      
  #print(sortd, invs)
  return (sortd, invs)

def sort_count(a):
    if len(a) <= 1:
        return (a, 0)
    else:
        a1, x = sort_count(a[:int(len(a)//2)])
        a2, y = sort_count(a[int(len(a)//2):])
        a1.sort()
        a2.sort()
        #print(a1, a2)
        s, z = count_split(a1, a2)
        return (s, x + y + z)
        
f = open('IntegerArray.txt', 'r')
x = list(map(int, f.readlines()))
f.close()


sx, r = sort_count(x)

#r = sort_count(arr)
print(r) 