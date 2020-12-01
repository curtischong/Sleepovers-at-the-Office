# Technical Interviews for Writing Pull Requests
Pull requests consumes hours of an engineer's time, which is why the best engineers are those that manage their pull requests well.

I believe that making your code easily reviewable can significantly improve cohesion in a software engineering team. However, recruiters never consider this when hiring.

So I'll propose a new type of interview that directly evaluates how well an engineer works with others.

Instead of coding algorithms from scratch, candidates should modify existing code by submitting PRs.

This can help us answer questions like:
- Do they put Github Comments to explain where they moved functions? Which objects have gained/lost access due to this change, and why?
- Do they refactor code in a separate PR BEFORE adding logic?
    - It's quite hard to understand what's happening if your PR refactors a lot of logic and adds new logic at the same time.
- Do they explain design decisions with easy-to-notice comments?
- Do they show examples when explaining abstract concepts in code comments?

There are two problems with this approach:

1) To evaluate how well someone manages PRs, you need them to submit a relatively large PR.
2) The engineer needs a solid understanding of the codebase before they can submit a thoughtful PR for reviewers.

I don't think we can solve 1) in a technical interview, there's just not much time.

To solve 2), we can ask them to make additions to famous algorithms. For example:

- Update 0-1 knapsack for unlimited items.
    - They'll get a lot of bonus points if they can explain their changes well (especially with examples).
- Update Dijkstra's to account for edges with multiple weights (and more restrictions).

I like this kind of technical interview more since the underlying algorithm is already provided.

What we have now is an interview that tests their ability to:
	1) Adapt code for our use case.
	2) Communicate their work with other team members.

One of my dreams is to have an intern of my own one day. So if you're reading this, I hope you brushed up on writing PRs!

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='034_drawing_routes_with_what_3_words.md'>#34: Drawing Routes with What 3 Words</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
