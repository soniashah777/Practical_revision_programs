class string_reverse:
     list_of_char=[]
     reversed_string=""
     def __init__(self):
          self.list_of_char=[]
          self.reversed_string=""
     def push(self, str_input):
          for i in str_input:
               self.list_of_char.append(i)
     def display(self):
          for i in range (len(self.list_of_char)-1,-1,-1):
               self.reversed_string += self.list_of_char[i]
          print (self.reversed_string)
    
obj=string_reverse()
obj.push("aryan")
obj2=string_reverse()
obj2.push("anant")
obj.push("shamil")
obj2.display()
obj.display()

          
