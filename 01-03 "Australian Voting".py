cases = 1
candidates = ['Jon Doe', 'Batman', 'George Washington']
num = len(candidates)
ballots = [
    [1,2,3],
    [2,1,3],
    [3,2,1],
    [1,3,2],
    [3,1,2],
    [1,2,3],
    [2,3,1],
    [2,1,3],
    [2,3,1],
    [3,2,1],
    [1,2,3],
    [1,2,3],
    [1,2,3],
]

"""
Tally up the first choice in each ballot
    Create a dictionary for each candidate number
    Count the total number of votes
If a candidate wins by > 50% then they win
    Find winner and divide their votes by total votes
Else remove candidate(s) in last place from each ballot
"""

def elect(ballots):
    
    # Count first place votes for each candidate
    d = {}
    for ballot in ballots:
        first = ballot[0]
        if first in d.keys():
            d[first] += 1
        else:
            d[first] = 1
    
    # Find most votes
    maxv = max(d.values())
    maxk = []
    for k, v in d.items():
        if v == maxv:
            maxk.append(k)
    
    # Find total number of votes
    totv = 0
    for v in d.values():
        totv += v
    
    # Find total number of candidates
    totk = len(d.keys())
    
    # Clear winner?
    if maxv/totv > .5 or len(maxk) == totk:
        return maxk
        
    # If no clear winner, remove losers and repeat
    else:
        minv = min(d.values())
        mink = []
        for k, v in d.items():
            if v == minv:
                mink.append(k)
        for ballot in ballots:
            for k in mink:
                ballot.remove(k)
        return elect(ballots)



# Test
print(elect(ballots))
