'define sample tree and pattern'
tree = ('a', [('b', [('d', []), ('e', [])]), ('c', [('f', []), ('g', [])])])
pattern = ('a', [('b', [('d', []), ('e', [])]), ('c', [('f', []), ('g', [])])]) 
def pattern_match(pattern, tree):
    '''Return True if the pattern matches the tree.'''