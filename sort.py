arr=[]
n=int(input("enter the number of array:"))
for i in range(0, n):
    ele=int(input("enter the element:"))
    arr.append(ele)
print(arr)
temp=0
for i in range(0,len(arr)):
    print(arr[i], end=" ")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
          temp=arr[i]
          arr[i]=arr[j]
          arr[j]=temp
print()
print("element of an array in sorted array:")
for i in range(0, len(arr)):
      print(arr[i],end=" ")
