nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_list):
	external_counter = 0
	external_counter_max = len(nested_list)
	counter_internal = -1
	counter_internal_max = len(nested_list[external_counter])

	while external_counter != external_counter_max:
		counter_internal += 1
		if counter_internal == counter_internal_max:
			external_counter += 1
			if external_counter == external_counter_max:
				return
			counter_internal = 0
			counter_internal_max = len(nested_list[external_counter])
			print(nested_list[external_counter][counter_internal])
		yield nested_list[external_counter][counter_internal]


for item in flat_generator(nested_list):
	print(item)
