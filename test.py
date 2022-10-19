import code

if code.swap([1,3]) == [3,1]:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed! [1,3] expected [3,1], got", code.swap([1,3])

if code.swap([1,"hi"]) == ["hi",1]:
	print("Test Case 2 Passed!")
else:
	print("Test Case 2 Failed! [1,\"hi\"] expected [\"hi\",1], got", code.swap([1,"hi"])