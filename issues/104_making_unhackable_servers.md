# Making Unhackable Servers

###### First posted on Feb 2, 2024

If you shop online, you trust Stripe with your credit card. When you send an email, you trust that Gmail isn’t reading your emails.

Our internet is built on trust between us and third parties. And it works.

But sometimes, we need a higher level of trust. For example, assume two healthcare providers need to know the patients they have in common, but due to regulation, they cannot reveal their unique patients.

This seems impossible! Cause to find the shared patients, both sets of patients have to be on the same computer.

<br/>
<br/>
But what if there’s another way? Many computers have a secure enclave chip, which is a component that says:

<br/>
“I only run code you told me to run. Here is a proof that shows you I am only running your code”.

<br/>
<br/>


With this proof, you can verify that no extra code is running that steals all your private data. This technology is cool, and it’s used. But it has a gaping flaw: we assumed that AWS didn’t install a backdoor into the enclave.

Cryptographers are trying really hard to eliminate this flaw. They are building protocols to allow parties to collaborate without trusting each other or AWS.

However, enclaves will always be faster than cryptography. And since we already trust AWS to host the internet, I think enclaves will power most privacy-centric applications.

But who cares? Because we’re ok with trusting strangers with our data. How important is privacy tech if we don’t care about privacy? Nonetheless, I think society should still research cryptography because it could help in the future, maybe with trusting aliens.

I hope you have a wonderful week!

\- Curtis

P.S. I made a demo that runs a Minecraft server inside an AWS enclave [here.](https://github.com/tenetxyz/minecraft-tee)

P.P.S. I’m only talking about 2PC/MPC technologies here. ZK research is still incredibly useful because it is the only tool that can retroactively prove that a computation happened.

Note: My friend Eesha mentioned that you can just hash a user's private info and compare the hashes instead. This is so true (and is what hashmaps already do)! I guess you're still revealing extra info (like how many patients you have). So it's not perfect. But I would count this as using custom cryptography to solve this specific problem.

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='103_phds_are_replacing_formulas_with_neural_nets.md'>#103: PhDs Are Replacing Formulas with Neural Nets</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
