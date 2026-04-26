def sorting(arr):
    
    for i in range(len(arr)):
        curr=arr[i]
        j=i-1
        while j>=0 and arr[j]>curr:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=curr
    return arr  
if __name__=="__main__":
    arr=[12,11,13]
    print(sorting(arr))
    
