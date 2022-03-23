from bs4 import BeautifulSoup
import requests


## Used to create a new numbers.txt folder with the data scraped.
# URL = "https://www.lottonumbers.com/lotto-max-results-2009"
# r = requests.get(URL)
# yc_webpage = r.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
#
# results = soup.find_all(name="ul", class_="balls -cn")
#
# for x in results[::-1]:
#     numbers = x.get_text()
#     numbers = numbers.strip().replace("\n", ", ")
#
#     with open("numbers.txt", "a") as f:
#         f.write(numbers + "\n")
# print("done")



def calculate_number_frequency(filename):
    """
    This function takes in a filename and calculates the frequency of
    numbers appearing in that file. It returns a dictionary where the
    keys are the numbers and the values are the percentages of their
    occurrence in the file.
    """
    with open(filename) as f:
        lines = f.readlines()

        result_dict = {x: 0 for x in range(1, 51)}

        for line in lines:
            numbers = line.strip().split(", ")
            for number in numbers:
                if int(number) in result_dict:
                    result_dict[int(number)] += 1

        d = {k: v for k, v in sorted(result_dict.items(), key=lambda item: item[1])}

        for k, v in d.items():
            print(f"{k} = {round((v / len(lines)) * 100, 1)}%")

