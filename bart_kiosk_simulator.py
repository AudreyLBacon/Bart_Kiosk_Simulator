

DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60


def load_card (load1,load5,load10,load20):

	load1 = 1.00 * load1
	load5 = 5.00 * load5
	load10 = 10.00 * load10
	load20 = 20.00 * load20

	return load1 + load5 + load10 + load20

'''print load_card(6,0,1,9)

print load_card (0,0,0,9)

print load_card (2,3,0,9)

print load_card (3,0,0,9)'''


def travel_to_destination(fare_price, card_value):
	if card_value >= fare_price:
		print "welcome aboard, enjoy your trip"
	else:
		print "you need more money"

clipper_card = load_card(1,1,0,1)
travel_to_destination(FREMONT_TO_COLMA, clipper_card)



