# target = 70
def rotate_array(arr, direction, rotation):
    """
    Rotates the array to the left by one position efficiently.
    """
    if len(arr) < 2:
        return arr
    # Slicing create a new list shifted by 1. 
    # This is O(N) but Pythonic and clean for standard lists.
    elif direction == "right":
        return arr[-rotation:] + arr[:-rotation]
    return arr[rotation:] + arr[:rotation]

try:
    arr = list(map(int, input("Enter the integer numbers with space: ").split()))
    if len(arr) < 2:
        print("Numbers without space are treated as a single number!")
        print()
    direction = input("Rotate to: ").lower()
    rotation = int(input("Rotate by: "))
    if rotation < 1:
        print("Invalid input. Please enter valid number.")
    elif direction == "left" or direction == "right":
        print(rotate_array(arr, direction, rotation))
    else:
        print("Invalid direction. Please enter 'left' or 'right'.")
except ValueError:
    print("Invalid input. Please enter valid integers.")

 

# def find_pair(b, target):
#     for item in range(len(b)-1, 0, -1):
#          sum = b[item] + b[item-1]
#          if sum == target:
#           return True
#     return False

# print(f"Result: {find_pair(b, target)}")





           

     


         



   

   
   

