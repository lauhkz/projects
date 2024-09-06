# Assignment
<!--
Complete the bottom half of the main() function using two for-loops.

    1. In the first for-loop, describe() all of the dragons, starting with the first dragon in the
    list and ending with the last dragon in the list.

    2. In the next for-loop, have each dragon breathe_fire at coordinate x=3, y=3. Pass in all of the
    *other* dragons (not the one breathing fire) as the units parameters so we can see if they get hit.

Pass in the dragons in /ascending/ index order. For example, when Blue Dragon breathes fire, it should
breathe fire on the other dragons in this order:

    - Green Dragon
    - Red Dragon
    - Black Dragon
-->

    * The Dragon's position (pos_x, pos_y) represents the center of the dragon
    * The width and the height represents the total size of the dragon

Given this, how should we calculate the corners of the hitbox?

Consider these questions:

1. If the dragon is at position (0,0) with a width of 4 and height of 2, where
   would the top-left corner be?
        -4, 2

2. Where would the bottom-right corner be in this case?
        4,-2

If i only have the center of my rectangle, how would i calculate the corners of this?

