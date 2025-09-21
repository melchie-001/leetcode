def sortArray(nums):
    def merge_sort(start, end):
        if end - start <= 1:
            return
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid, end)
        merge(start, mid, end)

    def merge(start, mid, end):
        left = nums[start:mid]
        right = nums[mid:end]
        i = j = 0
        for k in range(start, end):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1

    merge_sort(0, len(nums))
    return nums


### ✅ Example Usage

print(sortArray([5,2,3,1]))        # Output: [1,2,3,5]
print(sortArray([5,1,1,2,0,0]))    # Output: [0,0,1,1,2,5]
