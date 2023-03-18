# python3

def heaping(data, size, j, swaps):
  small = j 
  left = 2*j+1 
  right = 2*j+2 

  if left < size and data[left] < data[small]: 
    small = left 
  if right < size and data[right]<data[small]: 
    small = right 
  if j != small: 
    swaps.append((j,small)) 
    data[j],data[small] = data[small],data[j] 
    heaping(data, size, small, swaps)
    

def build_heap(data):
  swaps = []
  size = len(data)
  i = size // 2 - 1
  for i in range(size//2,-1,-1):
    heaping(data, size, i, swaps)
    i = i - 1       
  return swaps


def main():    
  text = input()
  if "F" in text:
    fileName = input()
    if "a" in fileName:
      return
    with open("./tests/"+fileName, mode="r") as file:
      n = int(file.readline())
      data = list(map(int, file.readline().split())) 
  elif "I" in text:
    n = int(input())
    data = list(map(int, input().split())) 

  swaps = build_heap(data)
  assert len(data) == n
    
  print(len(swaps))
  for i, j in swaps:
    print(i, j)

if __name__ == "__main__":
  main()
