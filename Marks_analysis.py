def merge_sort(arr,sum,length):
    if len(arr) > 1:#as well as sorting here ,the sum and length of array is also obtained  using sum and length variables
        mid = len(arr) // 2
        left_half = arr[:mid] # obtaining an array of elements less than mid
        right_half = arr[mid:] # array of mid to last element in array
        merge_sort(left_half,sum,length)#recursive calling
        merge_sort(right_half,sum,length)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):#conquering logic
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            sum=sum+arr[k]
            length+=1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            sum=sum+arr[k]
            length+=1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            sum=sum+arr[k]
            length+=1
            k += 1
        return sum,length #returning sum&length
marks=[100,80,25,20]
sum,length=merge_sort(marks,0,0) #marks get sorted
pass_marks=40
failed=bonus=0
arr_set=set(marks)
for i in marks:
    if i>=pass_marks:
        break
    failed+=1
passed=length-failed
passed_per=(passed/length)*100
failed_per=100- passed_per
mean=sum/length 
meadian=0
if length%2==1:
    meadian=marks[length//2]
else:
    meadian=((marks[length//2]+marks[(length-1)//2])/2)
if marks[0] < pass_marks:
    bonus=pass_marks- marks[0]  #minimum marks be added to least marks scored in exam to pass is passmarks-least marks
print("no of students passed: ",passed)
print("no of students failed: ",failed)
print("pass percentage: ",passed_per)
print("fail percentage: ",failed_per)
print("mean marks ",mean)
print("meadian ",meadian)
print("Bonus points to award in oredr to obtain 100% pass is ",bonus)
