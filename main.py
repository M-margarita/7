from collections import Counter

def merge(*lists):
    cnt = Counter()
    
    for i in lists:
        cnt += Counter(i)
        
    return(sorted(cnt.elements()))
