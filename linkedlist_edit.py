class node : 

    def __init__(self , data = None , link = None) : 

        self.data = data 

        self.link = link

class circularlinkedlist :

    def __init__(self) :

        self.first = node()

        self.first.link = self.first # being circular

        self.last = self.first # secondary linkedlist

        

    def Add(self , item) :

        self.next = self.first.link # related to the findprime method 

        self.backward = self.first # related to the findprime method

        p = node()

        p.data = int(item) 

        p.link = self.first

        self.last.link = p

        self.last = p 

    def Print(self) :

        self.forward = self.first.link # a pointer that points to first node

        while self.forward != self.first :

            print(self.forward.data,end = "\t")

            self.forward = self.forward.link
        
        print()

    def FindPrime(self) :

        while self.next != self.first :

            countF = 0 # if count == 0 -> prime  else : not prime

            i = 2

            if self.next.data == 1 or self.next.data == 0 :

                countF = 1 

            while(i <= self.next.data / 2) :

                if self.next.data % i == 0 :

                    countF += 1

                i += 1

            if countF == 0 :

                self.backward.link = self.next.link # delete the prime value 
            
            else :

                self.backward = self.next

            self.next = self.next.link

    def merge(self , obj2 , obj3) :

        C_checker = self.first 
        
        A_checker = obj2.first.link

        B_checker = obj3.first.link

        while A_checker != obj2.first and B_checker != obj3.first :

            if A_checker.data <= B_checker.data :

                C_checker.link = A_checker

                C_checker = A_checker

                A_checker = A_checker.link

            else :

                C_checker.link = B_checker

                C_checker = B_checker

                B_checker = B_checker.link


        while A_checker != obj2.first : # if linkedlist(A) is not pointed to the first yet

                C_checker.link = A_checker 

                C_checker = A_checker

                A_checker = A_checker.link

      

        while B_checker != obj3.first : # if linkedlist(B) is not pointed to the first yet

                C_checker.link = B_checker 

                C_checker = B_checker

                B_checker = B_checker.link

        C_checker.link = self.first


#----------------------------------------

class Stack :

    def __init__(self) :

        self.top = node()

        self.top.link = None 

    def Push(self,item_stack) :

        new_stack = node()

        new_stack.data = int(item_stack)

        new_stack.link = self.top.link

        self.top.link = new_stack

    def Pop(self) :

        if  self.top.link : # check if any value is exist in stack

            data = self.top.link.data

            self.top.link = self.top.link.link # delete the current value and return it

            return data
        
        else :
            
            return None 
        
    def PrintStack(self) :
        
        self.forward = self.top.link # a pointer that points to first node

        while self.forward != None :

            print(self.forward.data,end = "\t")

            self.forward = self.forward.link
        
        print()

        
        



class Queue :

    def __init__(self) :

        self.front = node()

        self.front.link = None

        self.rear = self.front

    def Add(self,queue_item) :

        new_queue = node() 

        new_queue.data = int(queue_item)

        self.rear.link = new_queue

        self.rear = self.rear.link

    def Delete(self) :

        if self.front.link == self.rear : # check to not lose the rear

            self.rear = self.front 

        if self.front.link :

            data = self.front.link.data

            self.front.link = self.front.link.link

            return data

        else :

            return None
    
    def PrintQueue(self) :

        self.forward = self.front.link # a pointer that points to first node

        while self.forward != None :

            print(self.forward.data,end = "\t")

            self.forward = self.forward.link
        
        print()






number = 0 

while number != -1 :


    print("Enter the task's number you want to do :")

    print("press (1) if you want to add a node and print the linkedlist that was made : ")

    print("press (2) if you want to find primes on your last or new linkedlist and delete them : ")

    print("press (3) if yoou want to create two linkedlists and merge them : ")

    print("press (4) if you want to create a stack with the linkedlist and have push and pop functions : ")

    print("press (5) if you want to create a queue with the linkedlist and have add and delete functions : ")

    print("press (-1) to exit : ")


    number = int(input())

    if number == 1 :

        print(" Enter (-1) to exit ")

        obj1 = circularlinkedlist()

        i = 1

        while 1 : 

            item = int(input(f"item {i}:"))

            if item == -1 :

                print("Enter 'YES' if it is just an item : ")

                print("Enter 'NO' if you want to exit : ")

                answer = input()

                if answer == "NO" :

                    break
                    
            obj1.Add(item)

            i+=1

        obj1.Print()


    elif number == 2 :

        print("Enter 'YES' if you want to find your last linkedlist's prime number : ")

        print("Enter 'NO' if you want to create new linkedlist and find its prime number : ")

        print(" Enter (-1) to exit ")

        ask = input()

        if ask == "YES" :

            print("Linkedlist afer deleting the primes : ")

            obj1.FindPrime() 

            obj1.Print()

        else :

            obj1 = circularlinkedlist()

            i = 1

            while 1 : 

                item = int(input(f"item {i}:"))

                if item == -1 :

                    print("Enter 'YES' if it is just an item : ")

                    print("Enter 'NO' if you want to exit : ")

                    answer = input()

                    if answer == "NO" :

                        break

                obj1.Add(item)

                i+=1

            print("Linkedlist afer deleting the primes : ")

            obj1.FindPrime()

            obj1.Print()


    elif number == 3 :

        print(" Enter (-1) to exit ")

        obj2 = circularlinkedlist()

        obj3 = circularlinkedlist()

        obj4 = circularlinkedlist()

        print("enter the first linklist's number : ")

        n = int(input())

        for i in range(n) : 

            print("linkedlist" , i , "of A :")

            item1 = int(input())

            if item1 == -1 :

                print("Enter 'YES' if it is just an item : ")

                print("Enter 'NO' if you want to exit : ")

                answer = input()

                if answer == "NO" :

                    break

            obj2.Add(item1)

        print("enter the second linklist's number : ")

        n = int(input())

        for i in range(n) : 

            print("linkedlist" , i , "of B :")

            item2 = int(input())

            if item2 == -1 :

                print("Enter 'YES' if it is just an item : ")

                print("Enter 'NO' if you want to exit : ")

                answer = input()

                if answer == "NO" :

                    break

            obj3.Add(item2)

        obj4.merge(obj2,obj3)

        obj4.Print()


    elif number == 4 :

        num = 0 

        obj5 = Stack()

        while num != -1 :

            print("Press (1) to add a number to the stack : ")

            print("Press (2) to delete a number to the stack : ")

            print("Enter (-1) to exit : ")

            num = int(input())

            if num == 1 :
                
                print("Enter the data : ")
                
                data = int(input())

                obj5.Push(data)

            elif num == 2 :

                print("pop the last item of stack :",obj5.Pop())
        
        print("poping all things left in the stack")

        obj5.PrintStack()

        
    elif number == 5 :

        num = 0 

        obj6 = Queue()

        while num != -1 :

            print("Press (1) to add a number to the Queue : ")

            print("Press (2) to delete a number to the Queue : ")

            print("Enter (-1) to exit : ")

            num = int(input())

            if num == 1 :
                
                print("Enter the data : ")
                
                data = int(input())

                obj6.Add(data)

            elif num == 2 :

                print("Delete the item from queue :",obj6.Delete())

        print("poping all things left in the queue")

        obj6.PrintQueue()



    else :

        print("The entered number is not valid !")













