# How to Frame Your Photo at the Sydney Opera House

Morning guys!

Who doesn't love to have a photo with the Opera House? I hope to one day. But I never know where to stand to get the best shot.

Fortunately, hundreds of other tourists have already clinched their snapshots. So all you'll need is a bit of code to discover the best spots. Here's how I would do it:

1.  Go on Instagram and download 10,000 photos of The Opera House.
2.  Get the location of these 10,000 photos (latitude, longitude).
3.  Run a clustering algorithm to group different clusters of photos.
    - This helps you see where people are taking pictures.
    - The best angles may only exist from hidden vantage points.
4. Use an algorithm to determine the best shots at each cluster.
    - You can use the number of likes.
    - Only consider photos that are 1.5 standard deviations above their average like count.
5. Browse the top 5 pictures from each cluster and pick the viewpoints you like best.

Other considerations:

1. If you know the time of day you'll arrive, you should filter for photos taken at that hour to match the lighting conditions.
2. You should only consider pictures with one person.
    - Since 2+ ppl will influence the number of likes it has.
    - You can use the Viola-Jones algorithm to count the number of faces.
3. The app should also help you decide where the subject and your photographer should stand by considering the size of the landmark and subject relative to the frame.

Seize some great shots this week.

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='011_gossip_thats_stronger_than_liquor.md'>#11: Gossip That's Stronger than Liquor</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href='013_a_tool_that_helps_you_write_better.md'>#13: A Tool That Helps You Write Better</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
