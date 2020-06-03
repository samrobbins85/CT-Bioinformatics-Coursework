import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
G=nx.Graph()
count=0
def WPGMA(filename):
	start=time.time()
	# Open the file
	file = open(filename, "r")
	# Initialize the table
	table = []
	# Loop through all the rows of the matrix
	for line in file:
		# If it's the header, print it
		if line[0] == "-":
			names = line.rstrip().split(" ")[1:]
			names1=line.rstrip().split(" ")[1:]
			names2=line.rstrip().split(" ")[1:]
			print(names)
		# Otherwise, remove the first character and split by dashed
		else:
			lister = line.rstrip().split(" ")[1:]
			# Convert it into an integer list rather than char list
			lister = [int(x) for x in lister]
			# Add it as a row to the table
			table.append(lister)
	# Convert through to a numpy datatype
	table = np.array(table, dtype=float)
	print(table)
	# This is because we stop when its a 2 by 2 matrix
	while table.shape != (2, 2):
		# Find the minimum value
		minval = np.min(table[np.nonzero(table)])
		# Find its coordinates
		itemindex = np.where(table == minval)
		# Merge the two species corresponding to those coordinates
		table = mergespecies(table, itemindex[0][0], itemindex[0][1], names, names2)
		nametable=[str(name) for name in names2]
		stack1=np.array(nametable)
		stacktotal=np.vstack((stack1,table))
		print(stacktotal)

	graphmerge(names[0],names[1])
# 	Here we need to tidy up the labels
	pos = nx.get_node_attributes(G, 'pos')
	nx.draw(G, pos=pos, with_labels=False)
	labels1 = {}
	for item in names1:
		labels1[item]=item


	nx.draw_networkx_labels(G, pos=pos, labels=labels1)
	plt.savefig(filename.split(".")[0]+"_tree.png")
	stop = time.time()
	time_taken = stop - start
	print('Time taken: ' + str(time_taken))


def graphmerge(a,b):
	# This counter indicates the x position of the last species inserted
	global count
	if isinstance(a,str) and isinstance(b,str):
		# print("a is "+a+" b is "+b)
		G.add_node(a, pos=(count, 0))
		G.add_node(b,pos=(count+1,0))
		G.add_node(str([a,b]),pos=(count+0.5,1))
		G.add_edge(a, str([a,b]))
		G.add_edge(b, str([a,b]))
		count += 2
	if isinstance(a,list) and isinstance(b,list):
		a_str=str(a)
		b_str=str(b)
		pos = nx.get_node_attributes(G, 'pos')
		highest=max(pos[a_str][1],pos[b_str][1])
		midpoint=(pos[a_str][0]+pos[b_str][0])/2
		G.add_node(str([a,b]),pos=(midpoint,highest+1))
		G.add_edge(str(a),str([a,b]))
		G.add_edge(str(b),str([a,b]))
		# print("Both list")
	if isinstance(a,list) and isinstance(b,str):
		a_str=str(a)
		G.add_node(b,pos=(count,0))
		pos = nx.get_node_attributes(G, 'pos')
		highest = max(pos[a_str][1], pos[b][1])
		midpoint = (pos[a_str][0] + pos[b][0]) / 2
		G.add_node(str([a, b]), pos=(midpoint, highest + 1))
		G.add_edge(str(a), str([a, b]))
		G.add_edge(str(b), str([a, b]))
		count+=1
	return


def mergespecies(table, a, b, names, names2):
	depth = lambda L: (isinstance(L, list) and (max(map(depth, L)) + 1) if L else 1) or 0
	if depth(names[a])<depth(names[b]):
		names[a],names[b]=names[b],names[a]
	# print("Merge:" + str(names[a]) + " and " + str(names[b]))
	graphmerge(names[a],names[b])
	names2[a]=names2[a]+names2[b]
	names2.remove(names2[b])
	sublist = [names[a], names[b]]
	names.remove(names[b])
	names.remove(names[a])
	names.insert(a, sublist)
	column1 = table[:, a:a + 1]
	column2 = table[:, b:b + 1]
	# Combine the two columns
	combine = np.hstack((column1, column2))
	# Get the mean of all the rows
	combine = combine.reshape(-1, 2).mean(axis=1).reshape(combine.shape[0], -1)
	# Delete the rows corresponding to the two species
	combine = np.delete(combine, [a, b], 0)
	# Delete the rows/columns corresponding to the two species from the main table
	table = np.delete(table, [a, b], 0)
	table = np.delete(table, [a, b], 1)
	# Append the amended column to the main table
	combine = np.transpose(combine)
	table = np.insert(table, min(a, b), combine, axis=1)
	# Add a zero the the column and transpose it
	combine = np.insert(combine, min(a, b), [0], axis=1)
	# Add this row to the bottom of the main table
	table = np.insert(table, min(a, b), combine, axis=0)
	# Return the table back to the main function
	return table


WPGMA("matrix1.txt")
