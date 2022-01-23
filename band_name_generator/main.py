import sys


class BandNameGenerator:
    def __init__(self):
        self.log_file = sys.path[0] + "/band_names.txt"

    # Log all the band names
    def _write(self, entry):
        with open(self.log_file, "a") as log:
            log.write(entry + "\n")

    # Simple greeting when starting program
    def greeting(self):
        print("Welcome to the Band Name Generator\n\n")

    # Input for the city name field
    def get_city(self):
        return input("What city were you born in?\n")

    # Input for the pet name field
    def get_pet_name(self):
        return input("What is your first pets name?\n")

    # Generates the name, adding the city and pets name, then adding the result to a log
    def generate_name(self):
        self.greeting()

        answer = f"{self.get_city()} {self.get_pet_name()}"

        print(f"Band name: {answer}")
        self._write(answer)


if __name__ == "__main__":
    generator = BandNameGenerator()
    generator.generate_name()

