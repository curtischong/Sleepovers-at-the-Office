# Using Knowledge Graphs to Learn from Others
Morning everyone,

My favourite conversations are those where I learn something new. But these conversations are hard to stumble into because of "What You See is All There Is" syndrome; how can you ask to learn something if you didn't know that topic in the first place?

What if a program told you what someone else knew? This way, you can guide more conversations into territory where you can apprentice their mind.

To start, we would need a list of topics people know and how familiar/passionate they are about each topic.

- We can gather this list via their Google / YouTube results (if they're willing to share it).
- Or we can collect information from journaling apps such as Roam Research.
We now have two lists, A and B, representing what I know and what they know, respectively. Our goal is to see if there are items in B that aren't in A. The extra items in B are ideas that we can learn from.

Since each idea/concept is related to other concepts, we should cluster each concept into categories to simplify our search for extra items in B.

We can perform this clustering using a knowledge graph (I.e. a graph where (1) ideas are nodes and (2) related ideas are connected with edges).
- Wikipedia can be the knowledge graph.
    - Each page represents a node, and the links are the edges.
- We can also use existing knowledge graphs like WordNet.

In brief, running clustering algorithms (e.g. Spectral/Louvain) on the knowledge graph can tell us how similar two nodes are.

For example, if I know a lot about MacOS and they know a lot about Linux, then these concepts would be clustered into a general "Unix OS" topic that we both know. However, if they know a lot about horseback riding, whereas I don't, then they would have nodes in the horseback riding cluster, whereas I don't.

By finding clusters of information that I don't know about, I can prepare conversations beforehand and find transitions to segway into learning more about public speaking.

To further this idea, a keynote speaker can tailor their talk with topics few people in the audience know.

Or the speaker can use recommendation algorithms on the knowledge graph to identify the topics the audience would want to learn next.
- Ex: If the audience took intro psych courses, a recommendation system might suggest the keynote to be about Experienced Utility.

I don't believe that technology will make learning from others easier, but I find this idea really cool because it can frack knowledge all the way to the surface.

And I can't stop dreaming of a future where I can learn something spectacular with every conversation I have.

I hope you call a friend this week and have great conversations.

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='031_pop_quizes_to_learn_from_books.md'>#31: Pop Quizzes to Learn From Books</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
