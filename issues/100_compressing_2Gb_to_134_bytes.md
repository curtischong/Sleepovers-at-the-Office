# Compressing 2Gb ➜ 134 Bytes

###### First posted on Jul 17, 2023

Last month, Photoshop released an AI feature to:

1) Generate an image from a prompt
2) Edit the image by:
    1) Drawing a box
    2) Asking it to “Add <an object> here”

Wait… isn’t this a compression algorithm? If you send your friend the prompts you used to:

1) Generate the image: (e.g. “NYC street”)
2) Edit the image (e.g. “Add a fire truck at coordinates (0,0) to (200, 500)”)

Then they can generate the same image (as long as both your models are the same and deterministic).

We only needed to send 2-3 sentences! To save even more space, we can compress our text (using bzip2) before sending it.

But who cares? Our current compression algorithms work fine.

I think this algorithm would work well when storing and transmitting data is expensive (i.e. in blockchains):

- Rather than storing images on-chain, store the prompts to generate them.
- For blockchain games, don’t store how the world looks, just the prompts to create it.

Like all compression, there is a tradeoff between data preservation and file size, so we probably won’t use this algorithm for mission-critical communications. But I think this algorithm would benefit blockchain-based programs until Moore’s Law renders it obsolete.

Anyway, that’s about it. Maybe this idea is purely theoretical, but I think it’s still cool. Also hey! I can’t believe we’re at 100 sleepovers. I hope you’re doing well. Thanks for sticking by me all this time. You can’t see it, but I always smile when I receive a reply to a Sleepover. So I want to write more. A lot more. Because for the first time in 5 years, I’m finally getting back in the tech scene, and there are just so many ideas.

Anyway, you’re stellar, and thanks for reading this. I hope you have a fantastic week!
 

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='099_grammarly_for_cold_emails.md'>#99: Grammarly for Cold Emails</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
