target = 70


 

def find_pair(b, target):
    for item in range(len(b)-1, 0, -1):
         sum = b[item] + b[item-1]
         if sum == target:
          return True
    return False

print(f"Result: {find_pair(b, target)}")





           

     


         



   

   
   

