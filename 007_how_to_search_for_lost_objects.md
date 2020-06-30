# How to Search for Lost Objects
Morning guys!
<br>
<br>
Wouldn't it be great if the security cameras in your house also told you where your keys were? This way, you wouldn't have to comb through dozens of hours of video to learn that they slid underneath your McDonalds receipt.


To broaden the horizon, can we turn security cameras into item-searching machines?


But training a neural network to recognize 20 million different objects is hard, you need a LOT of data.
 

A feasible solution would be to train multiple networks to recognize object descriptions. Instead of teaching a network to recognize all circular objects known to Wikipedia, we can teach it what circular objects are.


These networks should identify:
- Items of different shapes.
- Items of different colours.
- Items of different sizes.
- Items of different materials.

The cherry on top would be a "confirmation object" from Google Images that helps us verify the accuracy of our item description.
<br>
<br>
I hope you do some housekeeping this week!

\- Curtis
<br>
<br>
<br>
P.S. This idea came to mind after watching this Ted Talk: [youtube.com/watch?v=IQkj4CF_ha4](https://www.youtube.com/watch?v=IQkj4CF_ha4). It's worth a viewing :)

# Author's Amendments
For those of you who wonder, "but if the object is covered, how will our cameras find it?"

The solution to this problem is to comb through recordings of our video. This means that we don't have to see an object to know where it is presently. We can retroactively search through hours of footage with our networks to see where the item last was.