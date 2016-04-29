

def load_card (load1,load5,load10,load20):

	load1 = 1.00 * load1
	load5 = 5.00 * load5
	load10 = 10.00 * load10
	load20 = 20.00 * load20

	return load1 + load5 + load10 + load20

print load_card(0,0,0,0)

print load_card (0,0,0,9)

print load_card (2,3,0,0)

print load_card (3,1,1,3)







