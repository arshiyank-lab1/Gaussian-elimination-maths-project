"""Generate the six-scene storyboard PDF and timestamped recording script."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from lesson import LESSON, STORYBOARD, END

ROOT = Path(__file__).resolve().parent.parent

def mmss(t):
    return f"{t//60:02}:{t%60:02}"

lines = ["# Gaussian elimination — voice-over script",
         "", "Mohammad Arshiyan Ali Imran Ali Khan · E25B070750",
         "", "Read the paragraphs aloud. Use the timestamp ranges as cue points. "
             "The clip runs exactly 5:00. Leave short pauses for viewers to follow the highlighted values.",
         "", "**Pronunciation:** Read R₂ as ‘row two,’ z as ‘zed’ or ‘zee,’ and (1, 2, 3) "
             "as ‘one, two, three.’", ""]
for i,(start,title,visual,voice) in enumerate(LESSON):
    end = LESSON[i+1][0] if i+1 < len(LESSON) else END
    lines += [f"## {mmss(start)}–{mmss(end)} · {title}", "", voice, ""]
(ROOT/"Narration_Script.md").write_text("\n".join(lines),encoding="utf-8")

math_plan = [
    "Guiding question: how can three equations identify one point in space?",
    "Use the system x + y + z = 6, 2x + 3y + z = 11, and 3x + 4y + 4z = 23. Define the augmented matrix and its constant column.",
    "The first two planes intersect in a line. The third plane cuts the line in one point. Colour each plane to match its equation.",
    "Apply R2 := R2 - 2R1, R3 := R3 - 3R1, then R3 := R3 - R2. The last row becomes (0, 0, 2 | 6). Back-substitute to find z = 3, y = 2, x = 1.",
    "Substitute (1, 2, 3) into the original equations and obtain 6, 11, and 23. Identify the triple as the point shared by all three planes.",
    "Recap the augmented matrix, clearing below pivots, and back-substitution. Credit the M3 project brief and disclose ChatGPT use.",
]
voice_plan = [
    "Ask where three planes meet and introduce elimination as a way to find the point.",
    "Explain that a solution satisfies all three equations and show what each matrix column stores.",
    "Describe the overlap of two planes and the third plane's intersection with their line.",
    "Explain why each operation is reversible. Read the pivot, subtract each row multiple, and solve from the bottom upward.",
    "Read the substitution checks and connect one pivot per variable to a unique solution.",
    "End with the three steps and the reason elimination works. Leave the credits on screen.",
]
navy=colors.HexColor("#112747")
teal=colors.HexColor("#176e61")
gray=colors.HexColor("#43556a")
title=ParagraphStyle("Title",fontName="Helvetica-Bold",fontSize=26,leading=31,textColor=navy,spaceAfter=13)
sub=ParagraphStyle("Sub",fontName="Helvetica",fontSize=11,leading=16,textColor=gray,spaceAfter=15)
head=ParagraphStyle("Head",fontName="Helvetica-Bold",fontSize=14,leading=20,textColor=teal,spaceAfter=7)
body=ParagraphStyle("Body",fontName="Helvetica",fontSize=11,leading=16,textColor=navy,spaceAfter=5)
doc = SimpleDocTemplate(str(ROOT/"Storyboard.pdf"),pagesize=A4,leftMargin=51,rightMargin=51,topMargin=58,bottomMargin=58,
                         title="Gaussian Elimination Storyboard",author="Mohammad Arshiyan Ali Imran Ali Khan")
story=[]
def p(text, style):
    story.append(Paragraph(text,style))
for i,((name,start,end,visual),math,voice) in enumerate(zip(STORYBOARD,math_plan,voice_plan)):
    if i in (0,3):
        if i:
            story.append(PageBreak())
        p("Gaussian elimination storyboard",title)
        p("Mohammad Arshiyan Ali Imran Ali Khan | E25B070750 | M3 Internal Assessment",sub)
        if i==0:
            p("<b>Learning objective</b> By the end, the viewer can solve a 3 × 3 system using reversible row operations and back-substitution, then interpret its solution as the common point of three planes.",body)
            story.append(Spacer(1,20))
    p(f"{i+1}. {escape(name)} &nbsp; <font color='#43556a'>{mmss(start)}–{mmss(end)}</font>",head)
    for key,value in [("Visual",visual),("Narration",voice),("Math",math)]:
        p(f"<b>{key}</b> &nbsp; {escape(value)}",body)
    story.append(Spacer(1,22))
doc.build(story)
