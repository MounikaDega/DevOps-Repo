class Bank:
    
    def details(self,acno,bal):
        self.acno=acno;
        self.bal=bal;
    def chkbal(self):
        if (bal<=500):
            raise ValueError("withdrawl is not possible!!");
        else:
            self.amnt=int(input("enter the amount to withdraw:"))
            self.withdrawl(bal,self.amnt);
    def withdrawl(self,bal,amnt):
        self.amt=bal-self.amnt;
        if (self.amt<500):
            raise ValueError("Withdrawl is not possible!!");
        else:
            print ("withdrawl is possible for",self.amt)
            print ("The remaining bal is:",self.bal)
b=Bank()
try:
    acno=int(input("enter ur id:"))
    bal=int(input("enter ur bal:"))
    b.details(acno,bal);
    b.chkbal();
except ValueError:
    print("Withdrawl is not possible!!");
    
