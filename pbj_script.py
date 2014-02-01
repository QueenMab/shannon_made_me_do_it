pb_servings = 6
jelly_servings = 4
bread_slices = 9
full_on_pbj = bread_slices/2
open_face_pbj = bread_slices%2
bread_enabled_pbjs = full_on_pbj + open_face_pbj
pbs = bread_enabled_pbjs - jelly_servings

if pb_servings >= 1 and jelly_servings >=1 and bread_slices >=2:
	print "Congratulations! You can make a peanut butter and jelly Sandwich!!!!"

else:
	print "Sucks to be you! You should get your ass to the grocery store!!"

if bread_slices >=1:
	print "You can make", full_on_pbj, "peanut butter and jelly sandwiches"

if open_face_pbj >= 1:
	print "Yo! Btws, you can tots make", open_face_pbj, "open face peanut butter and jellies!!! Rock that!"

if jelly_servings < bread_enabled_pbjs:
	print "Hold the phone, Houston we've got a problem, you only have ", jelly_servings, "servings of jelly---that ain't gonna make", bread_enabled_pbjs, "sandwiches!"

if pb_servings < bread_enabled_pbjs:
	print "I gots to have my peanut butter!Only", pb_servings, "servings of pb makes Mackensey not enough pbjs! :("

if jelly_servings < bread_enabled_pbjs and pb_servings >= bread_enabled_pbjs:
	print "Well you don't have enough jelly to make all of the sandwiches in this best of all possible worlds, either travel to another world where the jelly supply is plentiful and people will let you eat jelly sandwiches or eat", full_on_pbj, "PBJs and", pbs, "PBSs"
