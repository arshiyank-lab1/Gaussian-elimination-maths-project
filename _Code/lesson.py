"""Timing, on-screen content, and narration for the Gaussian elimination lesson."""
# Start time (seconds), heading, display lines, voice-over.
LESSON = [
(0, "Gaussian elimination", ["One system. Three equations. One shared point.",
"Student: Mohammad Arshiyan Ali Imran Ali Khan", "Student ID: E25B070750"],
"How can three equations with three unknowns tell us exactly where three planes meet? In this video, we’ll use Gaussian elimination to turn a crowded system into a simpler one and find that point step by step."),
(22, "From equations to rows", ["x + y + z = 6", "2x + 3y + z = 11", "3x + 4y + 4z = 23"],
"Our goal is to solve this three-by-three system using row operations and back-substitution. A solution must satisfy all three equations at once. In the augmented matrix, each row is one equation. The first three columns hold the coefficients of x, y, and z. The rightmost column holds the constants."),
(50, "Three planes, one common point", [],
"Each equation describes a plane in three-dimensional space. Watch as the first two planes appear. Their overlap is a line, because many points satisfy those two equations. The third plane cuts that line at one point. Every coordinate of that point must satisfy all three equations. Elimination gives us a way to find those coordinates exactly."),
(82, "Why row operations work", ["Swap two rows → swap them back.", "Scale a row by k ≠ 0 → divide by k.", "Add k times another row → subtract k times that row."],
"These row operations preserve the solution set because each can be undone. Swapping changes the order. Scaling by a nonzero number keeps the equality equivalent. Adding a multiple of another equation keeps every shared solution valid, and subtracting it again restores the original equation. Apply every operation to the constants as well."),
(108, "First pivot · Clear the x-column", ["R₂ ← R₂ − 2R₁", "R₃ ← R₃ − 3R₁"],
"The first pivot is the leading one in row one. R two means row two. Subtract twice row one from row two. Two minus two becomes zero, and eleven minus twelve becomes negative one. Next, subtract three times row one from row three. Three minus three becomes zero, and twenty-three minus eighteen becomes five."),
(140, "Second pivot · Reach echelon form", ["R₃ ← R₃ − R₂", "The pivots form a staircase."],
"Now use the leading one in row two as the second pivot. Subtract row two from row three to clear the entry below it. For z, one minus negative one is two. For the constant, five minus negative one is six. The leading entries make a staircase, with zeros below them. This is row echelon form."),
(171, "Back-substitute from the bottom", ["2z = 6  →  z = 3", "y − 3 = −1  →  y = 2", "x + 2 + 3 = 6  →  x = 1"],
"Read the bottom row first. Two z equals six, so z is three. The middle row says y minus z equals negative one. Substitute three for z and add three to get y equals two. Finally, the first row says x plus y plus z equals six. Substitute two and three, then subtract five. That leaves x equals one."),
(208, "Check the original equations", ["1 + 2 + 3 = 6", "2(1) + 3(2) + 3 = 11", "3(1) + 4(2) + 4(3) = 23"],
"Let’s verify the ordered triple one, two, three in the original equations. The left-hand sides evaluate to six, eleven, and twenty-three. They match all three constants. And with one pivot for each variable, the back-substitution steps give exactly one possible value for each coordinate."),
(233, "Interpret the result", [],
"Back on the graph, the point is at x equals one, y equals two, and z equals three. It lies on the intersection line of the first two planes and on the third plane. That is the geometric meaning of the solution. The row operations changed the equations we worked with while preserving their shared solution."),
(264, "Summary and credits", ["Write the augmented matrix.", "Use pivots to clear entries below them.", "Back-substitute and check the original equations.",
"Reference: M3 Internal Assessment brief (topic and project structure).",
"AI disclosure: ChatGPT assisted with scripting, visuals, and animation code."],
"To recap, write the augmented matrix, use pivots to clear the entries below them, then back-substitute and check the original equations. The key idea is that reversible row operations simplify the system while keeping its solutions. That is what lets us turn the three-plane problem into a sequence of one-variable steps."),
]
END = 300
STORYBOARD = [
("Hook / Context", 0, 22, "Ask where three planes meet. Introduce the project and presenter."),
("Concept Introduction", 22, 50, "Introduce the equations and map x, y, z and the constants to matrix columns."),
("Visual Intuition", 50, 82, "Reveal two planes, their intersection line, then the third plane and shared point."),
("Worked Example", 82, 208, "Justify reversible row operations. Animate the scalar multiples and new rows, highlight the pivot staircase, and reveal z, y, then x."),
("Interpretation", 208, 264, "Check the triple in all three equations. Return to the planes and label their shared point."),
("Summary & Credits", 264, 300, "Recap the three steps and display the reference and AI disclosure."),
]
