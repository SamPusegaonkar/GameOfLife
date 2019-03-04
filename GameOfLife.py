from tkinter import *
import json

def checkNeighbours(i, j, cells, labels): #Check for the nearest neighbours
	alive_nodes=0
	if(labels[(i+1)%cells][j].cget("bg")=="white"):	
		alive_nodes+=1
	if(labels[i][(j+1)%cells].cget("bg")=="white"):	
		alive_nodes+=1
	if(labels[(i-1+cells)%cells][j].cget("bg")=="white"):	
		alive_nodes+=1
	if(labels[i][(j-1+cells)%cells].cget("bg")=="white"):	
		alive_nodes+=1
	if(labels[(i+1)%cells][(j+1)%cells].cget("bg")=="white"):	
		alive_nodes+=1
	if(labels[(i-1+cells)%cells][(j-1+cells)%cells].cget("bg")=="white"):	
		alive_nodes+=1
	if(labels[(i+1)%cells][(j-1+cells)%cells].cget("bg")=="white"):	
		alive_nodes+=1
	if(labels[(i-1+cells)%cells][(j+1)%cells].cget("bg")=="white"):	
		alive_nodes+=1
	return alive_nodes

def setup(pattern_number):
	my_window=Tk() #Main window	

	json_file=open("Pattern.json","r")
	data=json.load(json_file)
	json_file.close()

	cells=data[pattern_number]['cells']
	labels=[[0 for x in range(cells)] for y in range(cells)] #Stores all the cells

	for i in range(cells):
		for j in range(cells):
			labels[i][j]=Label(my_window, relief=RIDGE,width=3,height=2,bg="black")
			labels[i][j].grid(row=i, column=j) #Grid layout

	for i,j in zip( data[pattern_number]['i'] , data[pattern_number]['j'] ):
		labels[i][j].config(bg="white")
	
	run(cells,labels,my_window,pattern_number)

def run(cells,labels, my_window,pattern_number):
	for i in range(cells):
		for j in range(cells):
			if ((checkNeighbours(i,j,cells,labels)<2 or checkNeighbours(i, j, cells, labels)>3) and labels[i][j].cget("bg")=="white"):
				labels[i][j].config(bg="black")
			elif checkNeighbours(i,j,cells, labels)==3 and labels[i][j].cget("bg")=="black":
				labels[i][j].config(bg="white")	
	
	my_window.after(500, run,cells,labels,my_window,pattern_number) #Delay in milliseconds
	my_window.mainloop()
while(True):
	choice=int(input(" Enter 1 for Pattern 1\n Enter 2 for Pattern 2\n Enter 3 for Pattern 3\n Enter 4 for exit\n"))
	if choice==4:
		quit()
	else:	
		if choice==1:
			setup('Pattern1')
		if choice==2:
			setup('Pattern2')
		if choice==3:
			setup('Pattern3')
		






