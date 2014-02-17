pb_servings = 6
jelly_servings = 4
bread_slices = 9
sandwich_num = 0

while pb_servings and jelly_servings >=1 and bread_slices >=2:
	pb_servings= pb_servings-1
	jelly_servings = jelly_servings-1
	bread_slices = bread_slices-2
	sandwich_num = sandwich_num+1
	print "You've made {0} sandwiches, you now have {1} servings of peanut butter {2} servings of jelly and {3} slices of bread\n".format (sandwich_num, pb_servings, jelly_servings,bread_slices)

if jelly_servings==0:
	print "You need some jelly because you're all out!!\n"
elif pb_servings ==0:
	print "You need some peanut butter because you're all out!!\n"
elif bread ==0:
	print "You need some bread because you're all out!!\n"
if bread_slices ==1:	
	print "You don't have enough bread to make a full on sandwich and I know how you hate open-face sandwiches, you better get to the store!!\n"
