def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr) - 1):
    if i > 0 and arr[i] == arr[i-1]:
      continue 
    search_pairs(arr, -arr[i], i+1, triplets)
  return triplets

def search_pairs(arr, t_s, l, triplets): 
  r = len(arr) - 1 
  while l < r:
    c_s = arr[l] + arr[r] 
    if t_s == c_s:
      triplets.append([-t_s, arr[l], arr[r]])
      l, r = l + 1, r - 1

      while l<r and arr[l] == arr[l-1]:
          l += 1
      while l<r and arr[r] == arr[r+1]:
          r -= 1
    elif t_s > c_s:
      l += 1 
    else:
      r -= 1

      

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()

