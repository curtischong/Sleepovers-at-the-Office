# Search via Dynamic File Trees

Morning everyone,


Personal documents archive the notes, thoughts, and jokes you've heard throughout the day. Let's assume that there is a tool that easily allows you to append fresh ideas to personal documents.


For example, if you conceived a new way to compliment someone, the tool helps you append your idea to your "compliments" document.


Over time you'll have a host of unorganized loose documents. Which is fine, your thoughts don't come to you assembled in a file structure.


How would you search through these thoughts without a file tree?


Solution: Generate a useful file tree for every search.

  1) Identify relevant documents and ideas.

  2) Categorize all of these documents into different "folders."

  3) Organize these folders into a tree hierarchy on a toolbar on the left-hand side (So you can see the file structure).


The main advantages:

- This solution brings organization and hierarchy to an unorganized set of documents.
- Every search tailors the file structure to your needs.
    - Every search is different! A static file structure won't be optimal for most searches.
- If you want to write to multiple related documents, they will appear in the same folder.
    - There's no need to traverse up a file tree to append ideas to multiple documents in your "school" and "work" folders.

Why should we dynamically organize these documents into a tree instead of a list (like how Google presents search results?)

- A file tree-like hierarchy helps us quickly identify which series of pages would be useful.
    - So we don't have to try again with five different searches hoping that the next one would return better results.
- We will visit fewer documents overall.
    - On Google, you don't know if your search is good enough until you've visited around three different websites.
    - The file tree categories each document, you won't have to visit those pages to understand what they're about.
    - Moreover, you were the curator for these documents, so you'll have an impression of each document's contents before opening them.
- We don't have to guess your search intent.
    - Google shows you a bit of every category in its results, spamming the top 5 results with irrelevant pages.
    - With documents clustered in a file tree, you only have to click into the topics you're interested in.

But isn't generating a file structure for every search slow?
- Right, but your set of documents is quite a small compared to the amount of text in Academic Journals or libaries.
- We can use some heuristics to speed up the search.
    1. Caching.
    2. Pre-identify document clusters and index each document.
        - Since these documents are smaller than the entire internet, we can index each document much more thoroughly.
        - Indexing will also be much faster because there are fewer documents.
    3. We can start searching as you are typing your query.
        - This narrows down the number of possible pages to consider.
        - Search engines probably do this to tout a 0.01ms response time.

The Pitfalls
- It might take longer to understand the file structure than to scan the top 2 results on Google.
- The file structure might confuse you since you didn't organize the documents in that way.
- The categorization and clustering algorithms will have to be excellent.
    - I definitely think it's possible, but it'll take a lot of work.

I hope you find that song to obsess over this week!

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='018_the_shortcomings_of_google_drives_search.md'>#18:  The Shortcomings of Google Drive's Search</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href='020_cybersecurity_for_consumers.md'>#20: Cybersecurity for Consumers</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
