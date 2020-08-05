import sys
def repeating(arr,n):
    first=second=third=-sys.maxsize
    for i in range(0,n):
        if (arr[i]>first):
            third=second
            second=first
            first=arr[i]
        elif (arr[i]>second):
            third=second
            second=arr[i]
        elif (arr[i]>third):
            third=arr[i]
    
    print(first,second,third)
arr=[10,4,3,90,50,90]
n=len(arr)
repeating(arr,n)