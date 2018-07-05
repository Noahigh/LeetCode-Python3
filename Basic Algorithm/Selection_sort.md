
# Selection_sort

**Conditions:**


**Time complexity:**
+ $1$~$O(n^2)$


---

```python
def findSmallest(nums):
    smallest = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
    if nums[i] < smallest:
    	smallest = nums[i]
	smallest_index = i
    return smallest_index

def selection_sort(nums):
    newNums = []
    for i in range(len(nums)):
        smallest = finSmallest(nums)
	newNums.append(nums.pop(smallest))
    return newNums

my_list = [5, 2, 9, 6, 8]
print(selection_sort(my_list))

```
