# 프로그래머스 > 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시

class Cache :

	def __init__(self,size) :
		self.size = size
		self.cache = []
	
	def read(self,v) :
		hit = False
		if self.size == 0 : return hit
		if not v.lower() in self.cache:
			hit=False
			if len(self.cache) < self.size:
				self.cache.append(v.lower())
			else:
				self.cache.pop(0)
				self.cache.append(v.lower())
		else:
			hit =True
			self.cache.pop(self.cache.index(v.lower()))
			self.cache.append(v.lower())
		return hit

def solution(cacheSize, cities):
	cache = Cache(cacheSize)
	times = 0
	for v in cities :
		if cache.read(v) :
			times += 1
		else :
			times += 5
	return times

cacheSize1 = 3
cities1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(f'[cacheSize1,cities1] solution={solution(cacheSize1,cities1)}')

cacheSize2 = 3
cities2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(f'[cacheSize2,cities2] solution={solution(cacheSize2,cities2)}')

cacheSize3 = 2
cities3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(f'[cacheSize3,cities3] solution={solution(cacheSize3,cities3)}')

cacheSize4 = 2
cities4 =["Jeju", "Pangyo", "NewYork", "newyork"]
print(f'[cacheSize4,cities4] solution={solution(cacheSize4,cities4)}')

cacheSize5 = 0
cities5 =["Jeju", "Pangyo", "NewYork", "newyork"]
print(f'[cacheSize5,cities5] solution={solution(cacheSize5,cities5)}')