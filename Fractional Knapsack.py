'''
🧠 Solution Technique (Quick Recap)
	•	Compute value/weight ratio
	•	Sort descending
	•	Pick:
	•	Full item if possible
	•	Else fraction → break

'''


class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        
        items = []
        n = len(val)
        for i in range(n):
            items.append((val[i],wt[i],val[i]/wt[i]))
    
        
        items.sort(key=lambda x:x[2], reverse=True)
        
        max_val = 0.0
        
        for v, w, r in items:
            if capacity >= w:
                max_val += v
                capacity -= w
            else:
                max_val += (r* capacity)
                break
        return round(max_val,6)
                
        