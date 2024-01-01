def pageFaults(pages, n, capacity):
	indexes = {}
	s=set()
	page_faults = 0
	for i in range(n):
		if len(s) < capacity:
			if pages[i] not in s:
				s.add(pages[i])
				page_faults += 1
			indexes[pages[i]] = i
		else:
			if pages[i] not in s:
				lru = float('inf')
				for page in s:
					if indexes[page] < lru:
						lru = indexes[page]
						val = page
				s.remove(val)
				s.add(pages[i])
				page_faults += 1
			indexes[pages[i]] = i
	return page_faults
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
n = len(pages)
capacity = 4
print(pageFaults(pages, n, capacity))