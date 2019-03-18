question_list= ["what is your school name","how many class room in your school","how many teacher in this school","how many student in your school","what is your class teacher name ",]
first_option = ["shri","178","58","400","dumary A.B"]
second_option = ["mahalaxmi","32","54","350","hande a.b."]
third_option = ["subhasha vidymandir","33","212","790","jadhave"]
fourth_option = ["z.p.primary","65","34","500","gayakwad"]
all_option = ["first_option","second_option","third_option","fourth_option","five_option"]
ans_key = [2,3,4,4,1,]
i = 0
while i <=5:
	print question_list[i]
	print first_option[i]
	print second_option[i]
	print third_option[i]
	print fourth_option[i]
	x =int(raw_input('enter your choice'))
	if  ans_key[i] == x:
			print ("you are win")
	else:
 			print ("you are los try again")
			
	i = i + 1
