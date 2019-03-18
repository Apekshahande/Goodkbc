question_list= ["what is your school name","how many class room in your school","how many teacher in this school","what is your class teacher name ","how many student in your school"]
question_list.pop()
print question_list
print len(question_list)
question_list.append("what is your school place ?")
first_option = ["shri","178","58","dumbary A.B","Mumbai","300"]
print first_option[4]
second_option = ["mahalaxmi","32","350","hande a.b","Pune","400"]
third_option = ["subhasha vidymandir","33","790","jadhave","Umbraj","800"]
fourth_option = ["z.p.primary","65","34","gayakwad","nager","500"]

all_option = ["first_option","second_option","third_option","fourth_option"]
all_option.pop()
all_option.append(5)

print all_option
ans_key = [2,3,4,1,3,2]


i = 0
while i <len(question_list):
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
			break
	i = i + 1
