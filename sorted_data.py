# from sys import argv

# script, filename = argv

# f = open(filename)

f = open("scores.txt")

restaurant_ratings = {}

for line in f:
	stripped = line.strip("\n")
	split = stripped.split(":")
	num = int(split[1])
	restaurant_ratings[split[0]] = num

# for restaurant, rating in restaurant_ratings.iteritems():
# 	print "Restaurant %s is rated at %d." % (restaurant, rating)

def rest_rate():
	restaurant = raw_input("\vWhich restaurant would you like to know about?\n> ")
	print "The rating for %s is %d" % (restaurant, restaurant_ratings[restaurant])

	while True:
		print "\vWhat other restaurant are you interested in?"
		next = raw_input("> ")
		
		if next == "hungry":
			print "om nom nom :D"
			break
		elif restaurant_ratings.get(next) == None:
			print "Still trying to get a reservation. Maybe try Urbun Burger?"
			continue
		else:
			print "The rating for %s is %d" % (next, restaurant_ratings[restaurant])
			continue

rest_rate()