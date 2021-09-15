# Test code

list_of_accepted_values = [1, 2]
print(list_of_accepted_values)
shape_choice = 1

if shape_choice in list_of_accepted_values:
    print('shape_choice true')
else:
    print('shape_choice false')

shapes = ('cube', 'tetrahedron') # Tuples of shape user can select
print(shapes)
print(type(shapes))
print(shapes[0])
print(shapes[0])

shape = 'cube'
if shape in shapes:
    print('in shape in shapes')

print('cm\u00b3')

range_of_number = range(1, 4)
print('range_of_number')
print(range_of_number)
print(type(range_of_number))

if 2 in range_of_number:
    print('2 in range_of_number')
