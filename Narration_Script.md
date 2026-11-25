# Gaussian elimination — voice-over script

Mohammad Arshiyan Ali Imran Ali Khan · E25B070750

Read the paragraphs aloud. Use the timestamp ranges as cue points. The clip runs exactly 5:00. Leave short pauses for viewers to follow the highlighted values.

**Pronunciation:** Read R₂ as ‘row two,’ z as ‘zed’ or ‘zee,’ and (1, 2, 3) as ‘one, two, three.’

## 00:00–00:22 · Gaussian elimination

How can three equations with three unknowns tell us exactly where three planes meet? In this video, we’ll use Gaussian elimination to turn a crowded system into a simpler one and find that point step by step.

## 00:22–00:50 · From equations to rows

Our goal is to solve this three-by-three system using row operations and back-substitution. A solution must satisfy all three equations at once. In the augmented matrix, each row is one equation. The first three columns hold the coefficients of x, y, and z. The rightmost column holds the constants.

## 00:50–01:22 · Three planes, one common point

Each equation describes a plane in three-dimensional space. Watch as the first two planes appear. Their overlap is a line, because many points satisfy those two equations. The third plane cuts that line at one point. Every coordinate of that point must satisfy all three equations. Elimination gives us a way to find those coordinates exactly.

## 01:22–01:48 · Why row operations work

These row operations preserve the solution set because each can be undone. Swapping changes the order. Scaling by a nonzero number keeps the equality equivalent. Adding a multiple of another equation keeps every shared solution valid, and subtracting it again restores the original equation. Apply every operation to the constants as well.

## 01:48–02:20 · First pivot · Clear the x-column

The first pivot is the leading one in row one. R two means row two. Subtract twice row one from row two. Two minus two becomes zero, and eleven minus twelve becomes negative one. Next, subtract three times row one from row three. Three minus three becomes zero, and twenty-three minus eighteen becomes five.

## 02:20–02:51 · Second pivot · Reach echelon form

Now use the leading one in row two as the second pivot. Subtract row two from row three to clear the entry below it. For z, one minus negative one is two. For the constant, five minus negative one is six. The leading entries make a staircase, with zeros below them. This is row echelon form.

## 02:51–03:28 · Back-substitute from the bottom

Read the bottom row first. Two z equals six, so z is three. The middle row says y minus z equals negative one. Substitute three for z and add three to get y equals two. Finally, the first row says x plus y plus z equals six. Substitute two and three, then subtract five. That leaves x equals one.

## 03:28–03:53 · Check the original equations

Let’s verify the ordered triple one, two, three in the original equations. The left-hand sides evaluate to six, eleven, and twenty-three. They match all three constants. And with one pivot for each variable, the back-substitution steps give exactly one possible value for each coordinate.

## 03:53–04:24 · Interpret the result

Back on the graph, the point is at x equals one, y equals two, and z equals three. It lies on the intersection line of the first two planes and on the third plane. That is the geometric meaning of the solution. The row operations changed the equations we worked with while preserving their shared solution.

## 04:24–05:00 · Summary and credits

To recap, write the augmented matrix, use pivots to clear the entries below them, then back-substitute and check the original equations. The key idea is that reversible row operations simplify the system while keeping its solutions. That is what lets us turn the three-plane problem into a sequence of one-variable steps.
