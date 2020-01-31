def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline low"
    else: 
        return "Low" 

def cholesterol_analysis():
    print("Cholesterol Analysis") 
    HDLinput = input("Enter test_result: ") 
    test_info = HDLinput.split("=") 
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))
def new_feature():
    pass #python keyword that allows python to pass over this line

def interface():
    while True: 
        print("Cholesterol Calculator")
        print("Options: ")
        print( "1 - Cholesterol Analysis") 
        print( "9 - Quit") 
        choice = input("enter your option: ")
        if choice == '9': 
            return 
        elif choice == "1":
            cholesterol_analysis()

if __name__ == "__main__":
    interface() 