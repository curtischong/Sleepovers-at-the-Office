# Drawing Routes with What 3 Words

It's Haiti - The year 2010.

There's a rumble, then a crash. In an instant, the world has fallen. Buildings merge with streets, and landmarks levelled. Nothing is recognizable.

Emergency response teams scramble, but how can you send help when you don't even know where to go?

Enter What 3 Words, a website that locates where you are on the world with a three-word identifier.

Think geo-coordinates, but instead of latitude and longitude, you use three words to identify a 3m by 3m square on Earth. For people living in slums, where street names aren't paid for yet, these three words tell couriers where to go and Cholera vaccinators where you live.

Now imagine you're in Haiti. Sure the emergency teams know where you are, but how do they know which route to take? Rubble renders maps useless, and you can't see everything with satellites.


What 3 Words is a location, not a step-by-step route to get to you.

What if we could use What 3 Words to form a route to guide emergency response teams?

To do this, we need to express a path simply. To start this route, we can first read off the three words locating our current position.

Next, walk along your path. When your phone detects that you've turned a corner, you add the coordinate's first word (at the point where you turned) to your first three words.

For example, let's say that you start on "Apple, Train, Swam." You walk to "Monitor, Tree, Chopsticks." You could describe the path connecting those two points as "Apple, Train, Swam, Monitor." To extend the trail, keep on adding the first word on the next point to your list of words. When there are no more words in the list, you have reached the end of the path.

Now emergency teams can efficiently get to locations unambiguously.

To help remember these paths, we can use mnemonics. To remember our "Apple, Train, Swam, Monitor" path, we can represent this as a sentence: An apple rode a train then swam and dried itself on a monitor.

I really like this idea because it transforms points on Earth into an easily encodable route, something that you share with another person on the phone. Perhaps the next step would be to encode these points across time to coordinate vaccination teams or drone flight routes.

Have a great week!

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='033_using_knowledge_graphs_to_prioritize_learning.md'>#33: Using Knowledge Graphs to Prioritize Learning</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href='035_technical_interviews_to_evaluate_pr_management.md'>#35: Technical Interviews to Evaluate PR Management</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
