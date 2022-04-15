import aocd
import numpy as np


input_data = aocd.get_data(day=1, year=2021).splitlines()

gen_numbers = input_data.pop(0)

print(gen_numbers)
