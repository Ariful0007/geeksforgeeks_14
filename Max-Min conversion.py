for _ in range(int(input())):
   n=input()
   s=""
   for i in n:
     if(i=='5'):
      s=s+'6'
     elif(i=='6'):
       s=s+'5'
     else:
        s=s+i
   print(int(n)+int(s))



   if __name__ == '__main__':
       pass
   
