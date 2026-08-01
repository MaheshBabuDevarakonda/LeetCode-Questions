class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Coach: Your current logic is almost perfect, but there is a critical bug!
        # Root Cause: You are using a Two-Pointer approach on an UNSORTED array.
        # For the two-pointer logic (j++ / k--) to work, the array MUST be sorted first.
        # Also, you need to handle duplicate values for 'j' and 'k' to avoid duplicate triplets in the result.
        
        # Step 1: Add 'nums.sort()' at the beginning of the function.
        # Step 2: Inside the 'else' block, after finding a triplet, add a while loop 
        # to skip duplicate values of nums[j] and nums[k].
        
        # Complexity Analysis:
        # Current Time Complexity: O(n^2) - but incorrect due to lack of sorting.
        # Ideal Time Complexity: O(n^2) with sorting O(n log n).
        # Space Complexity: O(1) or O(n) depending on sorting implementation.
        
        # Hint: If you're stuck on the duplicate skipping logic, check the "Video Solutions" 
        # tab in the LeetHub editor's left pane for a visual walkthrough!
        nums.sort()
        result=[]
        n=len(nums)
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    # Coach: Optimization Alert! 
                    # Using 'if temp not in result' makes the search O(result_size), 
                    # increasing overall complexity. Since the array is sorted, 
                    # you should skip duplicates using while loops instead.
                    temp=[nums[i],nums[j],nums[k]]
                    result.append(temp)
                    
                    # To fix the duplicate issue optimally:
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1
        # Current Time Complexity: O(n^2) - Logic is now correct thanks to sorting.
        # Current Space Complexity: O(1) excluding output array.
        # This is the optimal approach. Now that you've implemented the while-loop duplicate skipping, 
        # you can confidently click the Git icon to push this to your GitHub repo!
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna