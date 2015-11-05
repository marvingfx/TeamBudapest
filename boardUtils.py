class Car:
    def __init__(self, id, direction, length):
        self.id = id
        self.direction = direction
        self.length = length

    def __eq__(self, other):
        return self.id == other

    def __str__(self):
        return self.id + ' ' + str(self.length) + ' ' + self.direction

    def canMove(self, board):
        # checks horizontally orientated cars
        if self.direction == 'h':
            for line in board:
                try:
                    left = line.index(self.id)
                    right = left + self.length - 1
                    if not line [left-1] == '.' and not line[right + 1] == '.':
                        return False
                    else:
                        return True
                except:
                    continue

        # checks vertically orientated cars
        elif self.direction == 'v':
            for block in range(len(board)):
                col = [row[block] for row in board]
                try:
                    top = col.index(self.id)
                    bottom = top + self.length - 1
                    if not col[top - 1] == '.' and not col[bottom + 1] == '.':
                        return False
                    else:
                        return True
                    break
                except:
                    continue

        return False

    def move(self, number, board):
        return board

# gets the cars from the board
def getCars(board):

    # count occurances of letters
    occurances = []
    for line in board:
        for block in line:
            if not block == '.':
                occurances.append(block)
    lengths = {car:occurances.count(car) for car in occurances}

    # get horizontal cars
    hor = []
    currentCar = line[0][0]
    for line in board:
        for block in line:
            if not block == '.' and currentCar == block:
                if block not in hor:
                    hor.append(Car(block,'h', lengths[block]))
            currentCar = block

    # get vertical cars
    ver = []
    for block in occurances:
        if block not in hor and block not in ver:
            ver.append(Car(block, 'v', lengths[block]))

    # combine lists
    return hor + ver