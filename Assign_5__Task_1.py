# Assignment 5  # Task 1

# Create a Dictionary Of Student Marks  

def Dic(name):
    data = {"Rohit" : 82,"Krishh": 92,"Rahul": 72,"Gurpreet": 71,"Sidhu":92}
    try:
        print(f"The {name} marks is : {data[name]}")
    except KeyError:
        print(f"The {name} not Found in the Dictionary")   
Dic(input("Enetr The Student\'s Name : "))
print(type(Dic))
