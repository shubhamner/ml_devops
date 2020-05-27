f = open("/root/mldev/cnn.py", "r")
contents = f.readlines()
f.close()


conv_count =0
for x in contents:
	if x == "model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu')) \n":
		conv_count = conv_count+1 
			
print(conv_count)

hidden_count =0
for x in contents:
	if x == "model.add(Dense(units=128, activation='relu'))\n":
		hidden_count = hidden_count+1 

print(hidden_count)
		

if conv_count < 2:
	print("Add a Convolutional layer")	
	contents.insert(12, "model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu')) \n")
	contents.insert(13, "model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu')) \n")
	contents.insert(14, "model.add(MaxPooling2D(pool_size=(2, 2))) \n")
	num = int(contents[34][9])
	num = num + 2
	str_num = str(num)
	contents[34] = "epochs = "+str_num+"\n"
	print(contents[34])
	f = open("/root/mldev/cnn.py", "w")
	contents = "".join(contents)
	f.write(contents)
	f.close()
elif conv_count == 2:
	print("Convolution layers are correct")
	if hidden_count < 2:
		print("Add a Hidden layer")
		contents.insert(19, "model.add(Dense(units=128, activation='relu'))\n")
		contents.insert(20, "model.add(Dense(units=64, activation='relu'))\n")
		num = int(contents[36][9])
		num = num + 2
		str_num = str(num)
		contents[36] = "epochs = "+str_num+"\n"
		print(contents[36])
		f = open("/root/mldev/cnn.py", "w")
		contents = "".join(contents)
		f.write(contents)
		f.close()
	elif hidden_count == 2:
		print("Hidden layers are correct")
		print("Increase Epochs")
		num = int(contents[36][9])
		num = num + 2
		str_num = str(num)
		contents[36] = "epochs = "+str_num+"\n"
		print(contents[36])
		f = open("/root/mldev/cnn.py", "w")
		contents = "".join(contents)
		f.write(contents)
		f.close()
else:
	print("Close the program")

