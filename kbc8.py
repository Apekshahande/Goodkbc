Question_list = ["1.what is your name","2.what is your school name","3.what is your best frind name","4.what is your sister name"]
#main Question naam ke list banaye hai usmai kuch Question dale hai
First_option = ["1.Pooja","1.shri mahalaxmi vidiyal","1.Aishwary","1.Rani"]
#main first option naam ke list banaye hai usmai sub Question ke first option dale hai
Secound_option =["2.Apeksha","2.Choclat","2.Arya","2.kajal"]
#main secound option naam ke list banaye hai usmai sub Question ke secound option dale hai
Third_option =["3.Komal","3.z.p.primary","3.anjali","3.Pratiksha"]
#main Third option naam ke list banaye hai usmai sub Question ke third option dale hai
Fourth_option =["4.Punam","4.Snehalaya","4.Deepa","4.muskan"]
#main Fourth option naam ke list banaye hai usmai sub Question ke fourth option dale hai
All_option = ["First_option","Secound_option","Third_option","Fourth_option"]
#All_option list mai sub option dale hai 
Ans_key = [2,4,1,3]
#Ans_key mai sub Questhion ke sahi answer dale hai
Prize = [2000,1000,500,100]
#prize list mai hum Question jette hai to prize melega
first_option = ["1.Apeksha","1.shri mahalaxmi vidiyal","1.Aishwary","1.Rani"]
#humai 50-50 life line ka use karna tha isse liya humani ye list banaye usmai kuch sahi or kuch galat javab dale
secound_option = ["2.Komal","2.Snehalaya","2.Deepa","2.Pratiksha"]
#humai 50-50 life line ka use karna tha isse liya humani ye list banaye usmai kuch sahi or kuch galat javab dale
ans_key =[1,2,1,2] 
#humani in do option mai saisahi ans key dale       
i = 0#index value
while i <len(Question_list): #hamara loop len of Question tak chalaga.
    if i <=len(Question_list):
        print Question_list[i]#queshan_list ke aage i jo hai o Queshion list ke len se chalaga
        print First_option[i]
        print Secound_option[i]
        print Third_option[i]
        print Fourth_option[i]     
        x = int(raw_input("enter your choice"))#user se input lena hai
        if Ans_key[i] == x:#ager condition true ho gaiye to he vah print karega nahi to elif ke condition cheak karega
            print "you win amount"
            print Prize[i]
        elif (Ans_key!=x):
            print "Can you use life_line"
            c = input("your choice")#user se input lena hai
            if c == 50-50:#user input == 50-50 ke to he print kerega other wise print else
                print Question_list[i]
                print first_option[i]
                print secound_option[i]
            else:
                print "life_line 50-50 par chalaga"
                break#ager aap ne dono chanch ka option galat deya to break ker dega
            a = input("enter your choise")#user se input lena hai
            if ans_key[i] == a:#jo humare ans_key[i]==a ke barabar hai ke nahi chak karega
                print "Congrats!you are win"
                print Prize[i]
            else:
                print  "sorry you los Game is over"
                break
        i = i + 1#incrment



