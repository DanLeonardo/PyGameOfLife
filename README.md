# PyGameOfLife
1. [Summary](#summary)
2. [Controls](#controls)  
3. [Arguments](#arguments)
    * [Grid Size](#grid-size)
    * [Cell Size](#cell-size)
    * [Update Rate](#update-rate)

## Summary
PyGameOfLife is Conway's Game of Life built in Python3 using [PyGame](https://wwwpygame.org). Enjoy everybodies favorite cellular automaton from the comfort of your own monitor. Easily create new starting states and experiment with different patterns.  
  
With special command line arguments (to be added) you can easily customize the size of the grid, size of each cell, and updates per second to match whatever it is you have in mind.  
  
You can start the game from the command line by moving to the directory and running `python3 game.py`.

## Controls
`Left Mouse Click`: Toggle a cell.  
You can hold the mouse button and drag to set additional cells to the first cell.  
  
`Right Mouse Click`: Clear a cell.  
You can hold the mouse button and drag to clear additional cells.  

`Middle Mouse Click`: Start/Stop the game.  
Click the middle button again to stop the game.

## Arguments
In Progress  
	Arguments are added from the command line. If an argument is not provided then the default value will be used.  
For Grid Size and Cell Size arguments the window will automatically resize to fit the entire grid.  
To run with a square grid of 24 cells with each cell being 8x8 pixels and updating ~3 times per second use the command `python3 game.py --grid-size 24 --cell-size 8 --update-rate 0.33`

### Grid Size
|Argument|Action|
|:---|:---|
|`--grid-size 12`| The horizontal and vertical capacity of the grid.|
|`--grid-height 8`| The vertical capacity of the grid.|
|`--grid-width 18`| Torizontal capacity of the grid.|

### Cell Size
|Argument|Action|
|:---|:---|
|`--cell-size 8`| The number of pixels to render each cells as. A cell is square.|

### Update Rate
|Argument|Action|
|:---|:---|
|`--update-rate`| The number of times per second to update the grid.|
