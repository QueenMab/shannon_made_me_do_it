for number in range(99, 0, -1):
	
	if number >2:
		print "{0} bottles of beer on the wall! {0} bottles of beer! Take one down, pass it around, {1} bottles of beer on the wall" .format(number, number-1)
	
	elif number ==2:
		print "{0} bottles of beer on the wall! {0} bottles of beer! Take one down, pass it around, {1} bottle of beer on the wall" .format(number, number-1)
	
	else:
		print "{0} bottle of beer on the wall! {0} bottle of beer! Take one down, pass it around, {1} bottles of beer on the wall" .format(number, number-1)	
