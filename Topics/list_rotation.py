def rotate_array(arr):
    
           
    direction = input("Rotate to (left/right): ").lower()
    if direction != "left" and direction != "right":
        print("Invalid direction. Please enter 'left' or 'right'.")
    else:
        rotation = int(input("Rotate by: "))
        if rotation < 1:
            print("Invalid rotation. Please enter valid number.")
        else:
            if len(arr) < 2:
                return arr
            elif direction == "right":
                return arr[-rotation:] + arr[:-rotation]
            return arr[rotation:] + arr[:rotation]   

    
while True:  
    try:
        arr = list(map(int, input("Enter integer numbers with space: ").split()))
        if len(arr) < 2:
            print("Numbers without space are treated as a single number!")
            print()
        print(rotate_array(arr))
        break
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        continue
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break
    
