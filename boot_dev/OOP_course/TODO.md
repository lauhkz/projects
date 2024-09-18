# Assignment
Complete the `Card` class.

  1. Define a constructor that takes `rank` and `suit` as parameters and sets `rank`, `suit`,
  `rank_index`, and `suit_index` instance variables.

You will need the indexes of `ranks`, and `suits` to help you compare them against each other.
Keep in mind that a `rank` and a `suit` are just strings within a list.

  2. Overload the comparison operators:

Overload the following comparison operators:

  * `==`: **eq**
  * `>`: **gt**
  * `<`: **it**

## Ranking the cards

A card is "greather than" another card if it has a higher rank. However, if the ranks are the same,
the card with the higher suit is "greather than" the other card. This same logic applies to the "less
than" operator. The "equal to" operator should check that the rank AND suit are equal.

The suits and ranks are defined as global variables. *The lower the index, the lower the rank or suit*.


