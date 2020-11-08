# Measuring Emotional Weight

Morning everyone,

Everybody loves a resonating speech or a moving film. But what makes a piece of writing more emotional than another? What even makes text sensitive? I think it boils down to 1 metric:

How much you agree/disagree with it.

1. Shock: Something so outrageous you can't believe it at all.
2. Agreement: Thoughts you had for months distilled into the perfect set of words.

To measure shock/agreement, we can use a binary classifier to predict if a text is shocking or agreeable. The closer the prediction is to 1, the more agreeable that statement is.

Fortunately, training a classifier is quite straightforward, but the prep work isn't. Let's set our eyes on some data gathering techniques.


### Shock
"He suspects the groom loves someone else... Do you love someone else? Do you, Charles?... I do."

    - Four Weddings and a Funeral
I think that there are an endless series of values people agree with. Confessing to another love on the alter is shocking because it violates marital values. So to detect shock, we have to test if a statement violates societal values. If it does, then we can mark it as shocking and add it to our training set.

Perhaps we can find a set of these values in the books of law. To determine if a statement violates the spirit of the law, we can use natural language processing techniques such as word embeddings or n-grams to identify statements that contradict societal values (e.g. NOT a visitor = trespassing).

However, many cultural values aren't on paper. In this case, we can find shocking headlines in news articles and YouTube videos with thumbnails of jaws hitting the floor.


### Agreement
This is hard to quantify because everybody agrees on different things. Moreover, an agreeable statement can fall flat on its own without context that backs it up, such as the score at the climax of a film.

An "I love you" after a lifetime of silence is far more emotional than screaming it at a Taylor Swift concert.

You can't program context because what's agreeable today may change tomorrow. Programmatically identifying a sole target audience is also hard because I think there are many ideas to agree with, far more than the number of different ideas to disagree with.

Unless you're a big tech company that knows the shows we watch and the comments we make, I think it's impossible to compile a dataset of things that people agree with, and that's tough.
 

    - Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='021_metrics_for_novelty.md'>#21: Metrics for Novelty</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href='023_grammarly_on_the_apple_glass.md'>#23: Grammarly on the Apple Glass</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
