# Cross-service Debuggers

###### First posted on June 6, 2022
What if debuggers worked across processes? Across computers? Would that even be useful?

We could do this locally by spinning up each service you're trying to test in debug mode. You'll debug normally, except you'll have to alt-tab between multiple IDEs to see which breakpoint was tripped.

But there are many challenges to getting this to work well:

- You may not have all the services you want to debug cloned locally.
    - We can solve this by setting up a "debug" environment in the cloud.
        - This would be similar to a dev/staging environment, but we'd start each service in debug mode.
        - You'll need some way to connect each process to a UI so you can set/see the breakpoints.
- If you can debug locally, you have to alt-tab between services to see which breakpoint tripped.
- If a service uses multiple threads, it can be hard to track the specific thread you're debugging in.
    - We can solve this by limiting the thread pool to one, but that could eliminate the bug.
- Did service A or B call service C?
    - Maybe we'll need a "stack trace" to tell us who the parent callers are between services.

I think an excellent multi-service debugger is hard to build because we'll probably need some program to track every breakpoint and explain how we reached it.

Who knows, maybe we don't need something like this because it's probably a better use of time to write more tests. Anyway, that's all I have this week, and I hope you have a great week!

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='089_spreadsheeting_friendships.md'>#89: Spreadsheeting Friendships</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href='091_a_unit_for_fun.md'>#91: A Unit for Fun</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
