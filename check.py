f = open("/root/mldev/new_code.py", "r")
check_code = f.read()

if 'keras' and 'Convolution2D' and 'MaxPooling2D' and 'Sequential' in check_code:				
	print('CNN_code')
elif 'sklearn' and 'numpy' in check_code:
	print('traditional')
else:
	print("not Machine learning")
