Question=["Q.which country is Delhi located in?","Q.what is the capital of india?"]
fist_option=["india","Delhi"]
second_option=["France","Chandigarh"]
third_option =["Czech Republic","Jaipur"]
forth_option=["USA","Bhopal"]

all_option =["fist_option","second_option","third_option","forth_option"]
ans_key =[0,3]
i = 0
while i < 2:
	print Question[i]
	print fist_option[i]
	print second_option[i]
	print third_option[i]
	print forth_option[i]
	user_input= int(raw_input("enter your choise"))
	if ans_key[i] == user_input:
			print "you are win"
	else:
			print "try again you are answer is wrong"
	i = i + 1