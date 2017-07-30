inventory = {}
inventory['Water'] = 120
inventory['Puffpuff'] = 390
inventory['Fanta'] = 203
inventory['Milk'] = 430

# print inventory
#
# del inventory['Puffpuff']
# print len(inventory)
# print inventory
# print inventory.keys()
# print inventory.values()
# print inventory.items()
# print inventory.has_key('Water')
#
# print
# print
# print

opposite = {'up':'down','white':'black','grace':'law','knowledge':'ignorance'}
opp = opposite.copy()
alias = opposite

opp['white'] = 'green'

print opposite
print alias
print opp
print opposite.get('grace',-1)