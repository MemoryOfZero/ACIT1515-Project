'''Exception handling  when programming, you would need to account for errors that occur during
 run-time For example, one inputs a wrong type of a file that doesn't exist and you are trying to open it. In fact there are three different main types of
 malfunctioning in software reliability

 1- bug: an abnormaly due to wrong implementation of logical misunderstandings


 2 - Error: intermitted misehavior of the system due to missing impleentation of corer ques


 3.Failure : an absolute clash of a system  due to a completion wrong-doing . A failure is a
 foe example: A bluescreen



 try :


 except
 '''
a = False
while not a:
    try:
        f_n = input("enter")
        i_f = open(f_n , 'r')
    except:
        print("input file not found")
    else:
        print("not done")