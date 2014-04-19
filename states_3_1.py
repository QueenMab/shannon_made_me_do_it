


###states_list = "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District Of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","PALAU","Pennsylvania","PUERTO RICO","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"
###abbrevs_list= "AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PW","PA","PR","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"

with open ("states.csv", "r") as states_file:
	states = states_file.read().split("\n")


filename = "states3.html"

output = []

output.append ("<select>")

for index, state in enumerate(states):
	states[index] = state.split(",")
	output.append ("<option value='{0}'>{1} ({0})</option>".format(states[index][0], states[index][1]))
output.append ("</select>") 

output="".join(output)

#print output


with open (filename,"a") as states_file:
	states_file.write(output)
