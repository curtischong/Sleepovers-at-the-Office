# A Metric to Replace Test Coverage

Knight Capital lost $440 Million in an hour because they didn't write tests for their software. Fortunately, mistakes like these made a lot more people care about testing.

But caring is not enough. When people write tests these days, people only care about the number of tests, not the quality.

This is because the industry uses a flawed metric known as "test coverage" to set team goals.

Let's take a look at how engineers calculate this metric to explain why it's flawed. The formula for test coverage is:
<br><br>
the number of lines of code ran by your tests

divided by

the number of lines of code in your program
<br><br>
Pretty straightforward, right?

But this percentage is a surface-level measurement of the number of tests you have, not the quality. That's the problem.

One basic test could have the same coverage as a comprehensive test database because it runs the same number of lines of code.

Even if you have 100% test coverage, your tests might only cover the most general cases.

That's why we need a new test coverage metric that considers:

- The number of services that call this function
- Function complexity (e.g. loops, state machines, asynchronous calls, etc.)
- Delicate code (Dereferencing pointers, division by zero, segment faults, etc.)

Moreover, this metric should also consider environmental factors:

- How quickly was the code written?
- How familiar is the author with this code?
- Have neighbouring functions been changed since we wrote these tests?

Having a dynamic metric like this can help teams prioritize their testing efforts, especially if tight deadlines keep people up at night.

Startups are the perfect users for this because after they "moved fast and broke things," they'll need to "fix things" by adding tests on a maturing codebase. This metric helps startups understand which functions to test first.

If we're incredibly ambitious, we can write an algorithm to use this metric and generate test cases for us to implement. This is useful because people in a hurry are biased to think of best-case scenarios rather than weird edge cases.

Here's to having tests taking over our entire lives, and I hope you have a wonderful week!

\- Curtis

<!--START OF FOOTER-->
<hr style="margin-top:9px;height:1px;border: 0;background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0), rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.0));">
<!--START OF ISSUE NAVIGATION LINKS-->
<p align="center"><a href='038_a_new_art_style_particle_effects.md'>#38: A New Art Style: Particle Effects</a></p>
<!--START OF ISSUE NAVIGATION LINKS-->
<!--END OF FOOTER-->
