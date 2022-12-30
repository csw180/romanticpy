def solution(citations):
	citations.sort(reverse=True)
	max_value = 0
	for i in range(len(citations)) :
		if  citations[i] >= i+1 :
			max_value = max(max_value,i+1)
		else :
			break
	return max_value

citations = [3, 0, 6, 1, 5]
print(solution(citations))



