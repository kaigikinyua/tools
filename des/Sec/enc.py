class Security:
	def __init__(self,data):
		print(data)
		x=open('keys.txt','r')
		keys=x.readlines()
		x.close()
		newData=""
		for j in range(len(data)-1):
			for i in range(len(keys[0])-1):
				if data[j]==keys[0][i]:
					newData+=keys[1][i]
		print(newData)
s=Security("My name is Antony")
