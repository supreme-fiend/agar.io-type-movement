# agar.io-type-movement
Moving in a game in an agar.io pattern, where character appears to be in the centre while the display moves around it


Make sure you have pygame installed before you attempt executing this

```
pip3 install pygame

```
in cmd/terminal should do the trick

This is basically done by maintaining blitting co-ordinates, where you decide to display the background grid image. When the character moves, our reference blit co-ordinates move the other way. The position of the player is recorded in case it has interactions with other players along the way.

The overall terrain position is fixed, but only the part which the user can see moves around so as to make the user feel as if the avatar is moving across the screen.

Naturally, if you press the right arrow key, the background image appears to move left.

![sideways movement](https://raw.githubusercontent.com/pranay-venkatesh/agar.io-type-movement/master/gifs/sideways.gif)

Similarly, moving down moves the reference background up, but the avatar will appear to move down

![vertical movement](https://raw.githubusercontent.com/pranay-venkatesh/agar.io-type-movement/master/gifs/vertical.gif)

Diagonal movement is simply a combination of keypresses. So if you press UP-RIGHT, the background will appear to move downwards and to the left, but the avatar will tread in the direction that we press.

![diagonal movement](https://raw.githubusercontent.com/pranay-venkatesh/agar.io-type-movement/master/gifs/diagonal.gif)


There are strict borders in the grid, so the character is contained.
