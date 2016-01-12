# your code goes here
def restaurant_ratings(filename):
    """Read a file, print restaurants in alphabetical order with ratings."""

    #open the file
    the_file = open(filename)

    #create an empty dictionary
    restaurants_with_ratings = {}

    #for every line in the file, split by ":"
    for line in the_file:
        line = line.rstrip()
        info = line.split(":")       
        #store restaurant name and rating in dictionary
        restaurants_with_ratings[info[0]] = info[1]

    #sort dictionary alphabetically by key
    for restaurant in sorted(restaurants_with_ratings):
        print "%s is rated at %s." % (restaurant, restaurants_with_ratings[restaurant])

    #loop over sorted dictionary and print formatted output
restaurant_ratings("scores.txt")

