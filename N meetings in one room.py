#User function Template for python3

'''
Given N meetings with their start and end times. Your task is to find the maximum number of meetings that can be performed in a meeting room.
Example 1:
Input:
N = 6
start[] = {1, 3, 0, 5, 8, 5}
end[] = {2, 4, 6, 7, 9, 9}
Output: 4
Explanation: Four meetings can be performed with given start and end timings. One of the possible ways to perform maximum meetings is: (1, 2), (3, 4), (5, 7) and (8, 9).
Example 2:
Input:
N = 3
start[] = {10, 12, 20}
end[] = {20, 25, 30}
Output: 1
Explanation: Only one meeting can be performed with given start and end timings. One of the possible ways to perform maximum meetings is: (10, 20).
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximumMeetings() which takes the array start[] and end[] as input and returns the maximum number of meetings that can be performed in a meeting room.
Expected Time Complexity: O(N*Log(N))
Expected Auxiliary Space: O(N)  
Constraints:
1 ≤ N ≤ 105
1 ≤ start[i] < end[i] ≤ 105 

Solution approach:
1. Create a list of tuples where each tuple contains the start and end time of a meeting.
2. Sort the list of meetings based on their end times . If two meetings have the same end time, sort them based on their start times.
3. Initialize a counter to keep track of the number of meetings that can be performed and a variable to keep track of the end time of the last meeting that was added to the schedule.
4. Iterate through the sorted list of meetings and for each meeting, check if its start time is greater than the end time of the last meeting that was added to the schedule. If it is, increment the counter and update the end time of the last meeting to the end time of the current meeting.
5. Return the counter as the result, which represents the maximum number of meetings that can be performed in the meeting room. 

'''


class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        n = len(start)
        
        metting = [(start[i],end[i]) for i in range(n)]
        
        metting.sort(key=lambda x: (x[1],x[0]))
        
        cnt = 1
        
        last_end_time = metting[0][1]
        
        for i in range(1,n):
            if metting[i][0]>last_end_time:
                cnt+=1
                last_end_time = metting[i][1]
        return cnt
                
                