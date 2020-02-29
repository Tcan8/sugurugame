from SuguruSolver import *

class MySolver(SuguruSolver):
  def __init__(self, problem, maxTime, visualizer):
    SuguruSolver.__init__(self, problem, maxTime, visualizer)

  # You should improve these functions to improve performance
  def selectUnassignedLocation(self, state):
    # Find the first location on the board has more than one possibility
    # then return it.  In class we talked about heuristics that might
    # perform better than this.
    for row in range(self._problem.getSize()[0]):
      for col in range(self._problem.getSize()[1]):

        if len(state.getPossibleValues((row,col))) > 1:
          return (row,col)

  def isConsistent(self, state, location, value):

    cell = state.getCellId(location)
    cell_size = state.cellSize(cell)
    cell_contents = state.getCell(cell)

    for locate in cell_contents:
      if locate == location:
          continue
      elif state.isValueKnown(locate) and (state.getPossibleValues(locate)[0] == value):
          return False

  ### Check surrounding cells of location for consistency ###
    y,x = location
    rows, cols = state.getSize()

    # check the left cell
    if x-1 >= 0:
        if state.isValueKnown((y,x-1)) and state.getPossibleValues((y,x-1))[0] == value:
            return False
    # check the left up cell
    if y-1 >= 0 and x-1 >= 0:
        if state.isValueKnown((y-1,x-1)) and state.getPossibleValues((y-1,x-1))[0] == value:
            return False
    # check the cell on the top
    if y-1 >= 0:
        if state.isValueKnown((y-1,x)) and state.getPossibleValues((y-1,x))[0] == value:
            return False
    # check the right up cell
    if y-1 >= 0 and x+1 < cols:
        if state.isValueKnown((y-1,x+1)) and state.getPossibleValues((y-1,x+1))[0] == value:
            return False
    # check the right cell
    if x+1 < cols:
        if state.isValueKnown((y,x+1)) and state.getPossibleValues((y,x+1))[0] == value:
            return False
    # check the right bottom cell
    if y+1 < rows and x+1 < cols:
        if state.isValueKnown((y+1,x+1)) and state.getPossibleValues((y+1,x+1))[0] == value:
            return False
    # check the cell below
    if y+1 < rows:
        if state.isValueKnown((y+1,x)) and state.getPossibleValues((y+1,x))[0] == value:
            return False
    # check the left bottom cell
    if y+1 < rows and x-1 >= 0:
        if state.isValueKnown((y+1,x-1)) and state.getPossibleValues((y+1,x-1))[0] == value:
            return False

    return True

  def infer(self, state, changedLocations, initial=False):
       #while len(changedLocations) > 0:
        #   location = changedLocations.pop()
         #  for value in range(1,6):
        #        print (changedLocations)
      return state


    #while one of the cells have no option due to inconcistency, then remove the possible values from the surrounding cells
    #don't forget to append
    #while len(changedLocations) > 0:
    #    location = changedLocations.pop()
    #    for value in range(1,6):
    #        print (changedLocations)


        #    if self.isConsistent(state, location, value) :
        #        return False
                #location = changedLocations.append(value)
