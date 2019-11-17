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
]

"""
Tally up the first choice in each ballot
    Create a dictionary for each candidate number
    Count the total number of votes
If a candidate wins by > 50% then they win
    Find winner and divide their votes by total votes
Else remove candidate(s) in last place from each ballot
"""

def aussie_vote(ballots):

    print('\n\nLOOP START')
    print('Ballots: ' + str(ballots))
    
    votes = {}
    vote_count = 0
    
    # Count first place votes
    for ballot in ballots:
        first = ballot[0]
        if first not in votes.keys():
            votes[first] = 1
        else:
            votes[first] += 1
        vote_count += 1
    print('Votes: ' + str(votes))
    print('Vote Count: ' + str(vote_count))
    
    # Find first place
    max_val = max(votes.values())
    max_key = []
    for k, v in votes.items():
        if v == max_val:
            max_key.append(k)
    print('Max Val: ' + str(max_val))
    print('Max Key: ' + str(max_key))
    
    # Clear winner?
    if max_val/vote_count > .5 or len(votes) == 1:
        print('TRUE')
        return max_key
    else:
        # If no clear winner, remove last place and repeat
        min_val = min(votes.values())
        min_key = []
        for k, v in votes.items():
            if v == min_val:
                min_key.append(k)
        for m in min_key:
            for ballot in ballots:
                ballot.remove(m)
        aussie_vote(ballots)


# Test function
winner = aussie_vote(ballots)
print(winner)
