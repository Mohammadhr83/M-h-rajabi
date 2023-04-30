ranandegi = int(input('chand kilometr ranandegi kardid:'))
mile = ranandegi * 0.62137
print ('shoma',mile,'mile ranandegi kardid')
if mile  < 15 :
	print ('shoma kamtar az 15 mile ranandegi kardid !')
else : 
	print('shoma bishtar az 15 mile ranandegi kardid !')
	
	
weight = int(input('vazn shoma chand kg ast:'))
gram = 1000 * weight
print ('vazn shoma',gram,'gram ast')
if gram < 100000 :
	print('vazn shoma kamtar az 100000 gram ast')
elif gram > 100000 :
	print('vaz shoma bishtar az 100000 gram ast')