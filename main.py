from choosing import choose_from_base, choose_to_base, choose_input_number
from converting import convert_base

bases = [2, 8, 10, 16]

from_base = choose_from_base(bases)

to_base = choose_to_base(from_base, bases)

input_number = choose_input_number(from_base)

output_number = convert_base(from_base, to_base, input_number)

print(f'Your result is {output_number}, a base {to_base} number.')