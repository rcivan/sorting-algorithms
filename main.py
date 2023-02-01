from time import perf_counter
from random import shuffle, randrange

def main():
  test_algorithm(merge_sort, 'merge_sort_test.csv')


def test_algorithm(sort_func, out_file_name, n_trials = 5, n_scrambles = 5, start = 20, stop = 5001, skip = 20):
  with open(out_file_name, 'w') as f:
    f.write('list_length,randomized,reversed,scrambled\n')
    for list_length in range(start, stop, skip):
      print(f"testing list of length {list_length}")

      randomized_list = list(range(list_length))
      shuffle(randomized_list)
      randomized_time, _ = time_exec(n_trials, sort_func, randomized_list)
      
      reversed_list = list(range(list_length))
      reversed_list.reverse()
      reversed_time, _ = time_exec(n_trials, sort_func, reversed_list)

      scrambled_list = list(range(list_length))
      scramble(scrambled_list, n_scrambles)
      scrambled_time, _ = time_exec(n_trials, sort_func, scrambled_list)

      out_string = f"{list_length},{randomized_time},{reversed_time},{scrambled_time}\n"
      f.write(out_string)


def scramble(mylist, n):
  list_len = len(mylist)
  for _ in range(n):
    i = randrange(list_len)
    j = randrange(list_len)
    swap(mylist, i, j)


def time_exec(num_iters, func, *args, **kwargs):
  sort_times = []
  result = None
  for _ in range(num_iters):
    start_time = perf_counter()
    result = func(*args, **kwargs)
    end_time = perf_counter()
    sort_times.append(end_time - start_time)
  return sum(sort_times)/num_iters, result


def swap(mylist, i, j):
  temp = mylist[j]
  mylist[j] = mylist[i]
  mylist[i] = temp


def isSorted(mylist):
  for i in range(len(mylist)-1):
    if mylist[i] > mylist[i+1]:
      return False
  return True

  
def bubble_sort(mylist):
  while not isSorted(mylist):
    for i in range(len(mylist)-1):
      if mylist[i] > mylist[i+1]:
        swap(mylist, i, i+1)

def insertion_sort(mylist):
  for i in range(len(mylist)-1):
    p = i+1
    while mylist[p] < mylist[p-1] and p > 0:
      swap(mylist, p, p-1)
      p -= 1

def merge(A, B):
  mylist = []
  while len(A) > 0 and len(B) > 0:
    if A[0] > B[0]:
      mylist.append(B[0])
      del B[0]
    else:
      mylist.append(A[0])
      del A[0]
  if len(A) != 0:
    mylist += A
  if len(B) != 0:
    mylist += B
  return mylist
  
def merge_sort(mylist):
  if len(mylist) == 1:
    return mylist
  else:
    n = len(mylist)
    A = mylist[0:n//2]
    B = mylist[n//2:]
    A = merge_sort(A)
    B = merge_sort(B)
    mylist = merge(A,B)
    return mylist
      
    
      
  

if __name__ == '__main__':
  main()