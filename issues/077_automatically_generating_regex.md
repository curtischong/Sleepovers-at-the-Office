# Automatically Generating Regex

###### First posted on December 14, 2021

Regex can be confusing. So what if we had a program that could automatically generate regex for us?

Here's how it would work:

1) You paste a bunch of strings that you want the regex to match (e.g. sell, bells, shell).
2) The code will generate a regex that matches all of those strings: `[a-z]+ells?`
	- `[a-z]` matches the "s" in sells, the "b" in bells, and the "sh" in shell.
	- `ell` matches the "ell."
	- `s?` matches the "s" in bells.

But why have such a tool in the first place?

1) Because the tool can help us write regex expressions faster.
2) Developers will need to find more examples before feeding the examples into the algorithm. More examples means:
	1) Better generated regex.
	2) More documentation for the regex.

After attempting to write this algorithm, I ran into a problem. Since the algorithm doesn't understand the significance of the characters, it doesn't know the right blocks of text to group together across the examples. Because there are many different ways to match a string, the regex won't be tailored to your use case.

So instead of generating one regex, we could generate 20, but that might not be useful since there are millions of different ways to match your examples.

What if we moved away from a fully-automated approach and asked users to help the algorithm by highlighting the common "blocks" of characters we want the regex to match?

Here's how it'll look like (Note: the over/underlines represent the different "blocks" the user selects.):

- s̅<ins>ell</ins>
- b̅<ins>ell</ins>s̅
- s̅h̅<ins>ell</ins>

These annotations help the algorithm create our intended regex `[a-z]+ells? since we explicitly tell the algorithm to group "s," "b," and "sh" into the first block, "ell" into the second block, and "s" into the third block.

The downside with this approach is that it requires a lot of manual highlighting, so I'm not sure if the tool is worth building. But it's alright. I already had a lot of fun.

Anyway, that's about it, let me know what you think, and I wish you the best of luck this week!

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='076_preventing_500_gcp_bills.md'>#76: Preventing $500 GCP Bills</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href='078_wikipediafying_books_to_make_reading_fun.md'>#78: Wikipediafying Books to Make Reading Fun</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
