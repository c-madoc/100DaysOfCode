class BMICalc:

    def get_height(self):
        return input("Enter your height (m)\n")

    def get_weight(self):
        return input("Enter your weight (kg)\n")

    def bmi_indexing(self, bmi):

        if bmi <= 18.5:
            return "Underweight"

        if bmi <= 24.9:
            return "Normal"

        if bmi <= 29.9:
            return "Overweight"

        if bmi > 29.9:
            return "Obese"

    def calculate_bmi(self):

        # Using the exponent operator **
        bmi = int(self.get_weight()) / float(self.get_height()) ** 2

        round_bmi = round(bmi, 1)

        # # Using PEMDAS
        # bmi = int(self.get_weight()) / (float(self.get_height()) * float(self.get_height()))

        index = self.bmi_indexing(round_bmi)

        print(f"You are {index} ({round_bmi})")


if __name__ == "__main__":
    print(6 + 4 / 2 - (1 * 2))
    calc = BMICalc()
    calc.calculate_bmi()
