def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
    
def reverse_str(str):
    n = len(str)
     
    # initialising a empty
    # string 'str1'
    str1 = ''
    i = n - 1
    while i >= 0:
         
        # copy str
        # to str1
        str1 += str[i]
        i -= 1
    print(str1)    

#concats list of strings to string
" ".join(string[::-1])