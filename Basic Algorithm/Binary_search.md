
# Binary_search

**Conditions:**
+ `Ordered list`

**Time complexity:**
+ `1~O(logn)`

---

```python
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high: # Recursive case
        mid = int((low + high) / 2)
	guess = nums[mid]

	if guess == target: # Base case
	    return mid
	if guess > target:
	    low = mid + 1
	else:
	    high = mid - 1

    return None

my_list = [1, 2, 5, 6, 3, 7, 4]
print(binary_search(my_list, 5))
print(binary_search(my_list, 0))

```
