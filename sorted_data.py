from sys import argv

script, filename = argv

f = open(filename)

# for line in f:
# 	split = f.readline()
# f_read = f.read()
# f.close()

# strip = f_read.strip("\n")
# print strip

# split = strip.
# while linenumber <= len(f):
# 	print f.readline()
restaurant_ratings = {}

for line in f:
	stripped = line.strip("\n")
	split = stripped.split(":")
	num = int(split[1])
	restaurant_ratings[split[0]] = num

for restaurant, rating in restaurant_ratings.iteritems():
	print "Restaurant %s is rated at %d." % (restaurant, rating)


