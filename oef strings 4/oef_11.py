text = input('Enter a text: ')
if 'x' in text and 'y' in text:
    reverse = text[-1:]
    position_x = reverse.find("x")
    position_y = text.find("y")
    if position_x > position_y:
        print('In this text not every x is followed by a y.')
    else:
        print('in this text every x is followed by a y.')
else:
    print("There isn't an x or y in the text")
