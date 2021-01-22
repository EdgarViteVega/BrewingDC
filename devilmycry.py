var="[[0, 4, 0, 0, 0, 0, 0, 8, 0],[4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0],[0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7],[0, 0, 2, 0, 0, 0, 6, 7, 0] ]"

def getdata(dim,string):
	var=string
	vec=[]
	aux=""
	for i in range(len(var)):
		if((var[i]!='[') and (var[i]!=']') and (var[i]!='')):
			aux=aux+var[i]
	array=aux.split(",")
	aux2=[]
	for y in range(dim**2):
		aux2.append(int(array[y]))
	for x in range(dim):
		vec.append(aux2[dim*x:dim*x+dim])
	return vec	
pitotee=getdata(9,var)
print(pitotee[1][2]+35)
