Question_list = ["how many student in navgurukul","who is co-founder of navgurukul","who is facileti incharge in navgurukul","what is meaning of navgurukul","what is place of navgurukul","how many councel member in navgurukul","how many laptop in navgurukul","who is food&higin codeneter in navgurukul","who is disko","what is learn navgurukul","what is navgurukul","what work in trazerer","who is founder of navgurukul","who is Gensek in navgurukul","how many room in navgurukul"]
#meni Question list naam ke list banaye hai usmai mani 15 Question dale hai
print len(Question_list)
#meni question ke len print ke hai (ketne question hai unka number)
print Question_list
#puri Question list print ke hai
first_options =["39","Abhishek Gupta","Nilam","newthing","pune","4","46","priya mishra","Komal bhat","skil","learningplace","monybujet","Rishabh Verma","kajal","10"]
#jete bhi Question dale hai unke first optionlekhane hai
secound_option =["40","Vandana Pandey","pooja","navnermit","mumbai","5","45","bindu","kajal kumari","softwere","fames place","rul","Abhishek Gupta","Nilam","23"]
#manlo 15 question dale hai un sub ka secound option lekhana hai
third_option =["58","Rishabh Verma","komal","nayagurukul","banglor","6","30","Rani","Nilam","code","NGO","GBU post","Vandana Pandey","bindu","14"]
#sub Question ke third option lekhne hai
fourth_option =["50","anuradha","Vandana Pandey","Newleaning","nager","7","50","megah","khushbu","enjoy","market","give a vijetable","anuradha","megah","11"]
#sub Question ke fourth option lekhne hai
all_option = [first_options,secound_option,third_option,fourth_option]
#all_option list mai sub option ko dale hai 
print len(all_option)
print all_option
answer_key = [3,1,4,2,3,4,4,2,1,2,3,1,1,4,3]
ans_list=[]
print len(answer_key)
print answer_key
prize = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
print len(prize)
leanth = len(Question_list)
i = 0
while i <=leanth:
	if i <= leanth:
		print Question_list[i]
		print first_options[i]
		print secound_option[i]
		print third_option[i]
		print fourth_option[i]
		x = int(raw_input("enter your choice"))
		ans_list.append(x)
		print ans_list
		if answer_key[i] == x:
			print "you win amount"
			print prize[i]
		else:
			print "sorry try again"
			break
		if i ==4:
			print "Congrats! Aapka padaav pura ho gaya hai."
		if (i ==9):
			print "Congrats! Aapka doosra padaav pura ho gaya hai"
		if(i == 14): 
			print "Congrats! Aap ek crore rupye jeet gaya hai"	
			break		
		i = i + 1


		
	
	

