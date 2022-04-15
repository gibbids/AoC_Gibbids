import aocd
import beautifulsoup as bs


input_list = [int(n) for n in aocd.get_data(day=1, year=2021).splitlines()]

increase = 0
previous_number = input_list[0]
for i in input_list[1:]:
    if i > previous_number:
        increase += 1
    previous_number = i

print(increase)

increase = 0

previous_number = sum(input_list[0:3])

for i in range(1, len(input_list) - 2):
    current_number = sum(input_list[i:i+3])
    if current_number > previous_number:
      increase += 1
    previous_number = current_number

print(increase)