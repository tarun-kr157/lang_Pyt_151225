# print(not True)
# print(not False)
# print(not 1)
# print(not 0)
# print(not "Rahul")
# print(not "")
# print()
# print(not None)
# print(not [])
# print(not ())
# print(not {})

def voter_eligibility(age, nationality):
    if not age >= 18 or nationality not in ["Indian", "Indian citizen", "India", "indian", "india", "Indian Citizen", "INDIAN", "INDIA", "INDIAN CITIZEN"]:
        return "Not eligible for voting."
    else:
        return "Eligible for voting."
while True:
    try:
        age = int(input("Age: "))
        citizenship = (input("Nationality: "))
        if not citizenship:
            print("Nationality is required.")
            continue
        if not citizenship.isalpha():
            print("Nationality must be alphabets only.")
            continue
        print(voter_eligibility(age, citizenship))
        break
    except ValueError:
        print("Invalid input. Please enter valid input.")
        continue
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break

