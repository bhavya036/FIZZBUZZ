for i in range(1,51):
    if (i%3==0 and i%5==0):
        print(str(i)+" FIZZBUZZ")
    else:
         if(i%3==0):
            print(str(i)+" FIZZ")
         else:
             if(i%5==0):
                print(str(i)+" BUZZ")
             else:
                 print(i)
                 