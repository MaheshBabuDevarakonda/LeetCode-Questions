class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[]

        start=intervals[0][0]
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            curr_start=intervals[i][0]
            curr_end=intervals[i][1]

            #overlap condition

            if end>=curr_start:
                end=max(end,curr_end)


                #no overlap condition
            else:
                ans.append([start,end])
                start=curr_start
                end=curr_end

        ans.append([start,end])
        return ans



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna