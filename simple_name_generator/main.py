from tools.logger import Logger

class BandNameGenerator:
    def __init__(self):
        self.log = Logger(__name__)

    def get_city(self):
        return input("Where were you born?\n")

    def get_pet_name(self):
        return input("What is your first pets name?\n")

    def generate_name(self):
        city = self.get_city()
        pet = self.get_pet_name()
        answer = f"{city} {pet}"

        print(f"Band name: {answer}")


if __name__ == "__main__":
    generator = BandNameGenerator()
    generator.generate_name()

