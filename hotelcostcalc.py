class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):
        print ("\n\n*****WELCOME TO DESOL HOTEL*****\n")
        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")
    def roomrent(self):
        print ("We have the following rooms for you:-")
        print ("1.  type A---->rs 6000 PN\-")
        print ("2.  type B---->rs 5000 PN\-")
        print ("3.  type C---->rs 4000 PN\-")
        print ("4.  type D---->rs 3000 PN\-")
        x=int(input("Enter Your Choice Please->"))
        n=int(input("For How Many Nights Did You Stay:"))
        if(x==1):
            print ("you have opted room type A")
            self.s=6000*n
        elif (x==2):
            print ("you have opted room type B")
            self.s=5000*n
        elif (x==3):
            print ("you have opted room type C")
            self.s=4000*n
        elif (x==4):
            print ("you have opted room type D")
            self.s=3000*n
        else:
            print ("please choose a room")
        print ("your room rent is =",self.s,"\n")
