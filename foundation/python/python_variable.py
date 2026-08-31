'''
    variable:
     - có 2 loại là biến global và local
     - biến là 1 container lưu trữ giá trị của biến
     - các trường hợp của biến:
        +) có thể khai báo nhiều biến trên 1 dòng, note: số lương biến phải bằng số lượng của giá trị trong biến
         EX:x, y, z = "Orange", "Banana", "Cherry"
            print(x)
            print(y)
            print(z)
        +) có thể khai báo nhiều biến với cùng 1 giá trị:
         EX: x = y = z = "Orange"
            print(x)
            print(y)
            print(z)
        +) với các kiểu dữ liệu là list và tuple thì có thể tách các giá trị trong các kiểu dữ liệu đó:
        EX: fruits = ["apple", "banana", "cherry"]
            x, y, z = fruits
            print(x)
            print(y)
            print(z)
    - biến global: là biến được khai báo ngoài function và được sử dụng cả bên trong và bên ngoài function
        EX:x = "awesome"
            def myfunc():
            print("Python is " + x)
            myfunc()
        +) 
'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)