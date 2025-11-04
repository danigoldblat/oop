# class Book:
#     def __init__(self,title:str,author:str,content:str):
#         self.title=title
#         self.author=author
#         self.content=content
#     def __str__(self):
#         return f"title: {self.title} ,author: {self.author} ,content: { self.content}"    

# class Saving_list:
#     def __init__(self):
#         self.book_list=[]
#     def saving_to_list(self,content):
#         self.book_list.append(content)
#     def print_list(self):
#         for book in self.book_list:
#             print (book)    
# book = Book("title","author","content")
# saving_list =Saving_list()
# saving_list.saving_to_list(book)         
# saving_list.print_list()   



# class Student:
#     def __init__(self,name:str,grades:list[int]):
#         self.name=name
#         self.grades=grades
    
# class Average_computer:
#     def __init__(self):
#         pass
#     @staticmethod
#     def verage_calculator(grades):
#         return sum(grades) / len(grades)
# student1=Student("fgh",[99,87,69])  
 
# print(student1.name,Average_computer.verage_calculator(student1.grades))


# class Order:
#     def __init__(self,items:list[str],total_price:float):
#         self.items=items
#         self.total_price=total_price

# class InvoicePrinter(Order):
#     def print_invoice(self):
#         print(f"shopping list {self.items} sells {self.total_price}")
        
# order=Order(["a","s","d","f"],522.36) 
# InvoicePrinter.print_invoice(order)      