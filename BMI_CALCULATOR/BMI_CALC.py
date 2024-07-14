#BMI CALCULATOR using command line
def calculate_bmi(weight, height):
         """Calculate the Body Mass Index (BMI) given a weight in kilograms and height in meters."""
         return weight / (height ** 2) 


def classify_BMI(bmi):
        #classify BMI in different categories..

        if (bmi < 18.5):
                return "Underweight", bmi
        elif (bmi >= 18.5 and bmi < 24.9):
                return "Normal weight", bmi
        elif (bmi >= 24.9 and bmi < 29.9):
                return "Overweight", bmi
        
        else:
                return "obesity" , bmi
        
def main():#this is used to run the bmi function
        height = float(input("Enter the height in meters: "))
        weight = float(input(" Enter the weight in kilograms: "))
         
        bmi = calculate_bmi(weight, height)
        category, bmi_value =  classify_BMI(bmi)
        print("your bmi is : {} and you are : {}".format(bmi_value,category))       
if __name__ == "__main__":
    main()