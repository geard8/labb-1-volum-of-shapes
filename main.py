import math

"""
To add new shape it needs to add string of shape name in to the tuple called shapes.
A new fuction called volume_of_(shape name) that take float or int edge_length as a parameter
and return the volume of the cube based on edge_length.
Need to add new if statmeant after existing if statmeant checking for for with shape uses have chosen in main_run and call
volume_of_(shape name) for that shape.
"""
shapes = ('cube', 'tetrahedron') # tuple of shapes

def volume_of_cube(edge_length):
    '''
    Returns volum for cube based on its edge length

    Parameters:
        edge_length (float or int): edge lenght of a cube   
    
    Returns:
        cube_volume (float): volume of cube
    '''

    cube_volume = float(pow(edge_length, 3))
    return cube_volume

def volume_of_tetrahedron(edge_length):
    '''
    Returns volum for tetrahedron based on its edge length

    Parameters:
        edge_length (float or int): edge lenght of a tetrahedron   
    
    Returns:
        tetrahedron_volume (float): volume of tetrahedron
    '''

    tetrahedron_volume = float(pow(edge_length, 3) / (6 * math.sqrt(2)))
    return tetrahedron_volume

def get_edge_length_from_user():
    '''
    retruns edge length that come from asking user to input edge length in cm

    Returns:
        edge_length (float): edge length in cm
    '''

    edge_length = 0.0

    try:
        edge_length = float(input('How long is one edge in cm: '))
        if edge_length <= 0:
            raise ValueError('value can only be positive')
    except ValueError:
        while True:
            try:
                edge_length = float(input('You can only write a positive number, ex 17.55: '))
                if edge_length <= 0:
                    raise ValueError('value can only be positive')
            except ValueError:
                pass
            else:
                break
    return edge_length

def get_user_choice_of_shape():
    '''
    Returns shape user want to use to calculate volume for based on edge length.
    Chose available is based of tuples shapes.

    Returns:
        shape (str): string name of user chosen shape
    '''

    shape_choice = 0 # used to track user chosen shape 
    shape_choices_text = "" # str with text of shape choices
    range_of_accepted_numbers = range(1, len(shapes)+1) # range of 

    # build up str shape_choices_text based on shapes
    i = 0
    while i < len(shapes):
        shape_choices_text += f'\n{i+1}: {shapes[i]}'
        i = i + 1

    # Make user chose which shape they want to calculate the volume of
    try:
        shape_choice = int(input(f'Do you want to calculate the volume of{shape_choices_text}\n'))
        if shape_choice not in range_of_accepted_numbers:
            raise ValueError(f'value can only be int in of {range_of_accepted_numbers}')
    except ValueError:
        while True:
            try:
                shape_choice = int(input(f'You can only select{shape_choices_text}\n'))
                if shape_choice not in range_of_accepted_numbers:
                    raise ValueError(f'value can only be int in of {range_of_accepted_numbers}')
            except ValueError:
                pass
            else:
                break
    
    shape = shapes[shape_choice-1]
    return shape

def main_run():
    shape = get_user_choice_of_shape()
    edge_lenght = get_edge_length_from_user()

    shape_volum = 0 # shape volum in cm

    if shape in shapes:
        if shape == 'cube':
            shape_volum = volume_of_cube(edge_lenght)
        if shape == 'tetrahedron':
            shape_volum = volume_of_tetrahedron(edge_lenght)
    else:
        raise Exception(f'shape is \"{shape}\" but have to be in \"{shapes}\"')

    print(f'Volume of a {shape} with edge length of {edge_lenght} cm is {shape_volum} cm\u00b3')

main_run()
