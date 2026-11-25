"""Render the silent 1080p lesson using Python, Pillow, NumPy, and FFmpeg."""
import argparse
from functools import lru_cache
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from lesson import END, LESSON

W, H = 1920, 1080
BG, PANEL, INK, MUTED, MINT = "#0b1321", "#14243a", "#f3f7ff", "#a5bdd0", "#76e7c9"
COLORS = ["#76e7c9", "#7cb8ff", "#ffc477"]
ORIGINAL = ((1, 1, 1, 6), (2, 3, 1, 11), (3, 4, 4, 23))
MATRICES = [ORIGINAL, (ORIGINAL[0], (0, 1, -1, -1), ORIGINAL[2]),
            (ORIGINAL[0], (0, 1, -1, -1), (0, 1, 1, 5)),
            (ORIGINAL[0], (0, 1, -1, -1), (0, 0, 2, 6))]
OPERATIONS = [
    (114, 0, 1, 0, 2, "R₂ ← R₂ − 2R₁"),
    (127, 1, 2, 0, 3, "R₃ ← R₃ − 3R₁"),
    (147, 2, 2, 1, 1, "R₃ ← R₃ − R₂"),
]
SOLUTION = np.array([1, 2, 3])
NORMALS = np.array([row[:3] for row in ORIGINAL])

@lru_cache
def font(size, bold):
    return ImageFont.truetype("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", size)

def label(draw, xy, value, size=40, color=INK, bold=False, anchor="lm"):
    draw.text(xy, str(value), font=font(size, bold), fill=color, anchor=anchor)

def clock(seconds):
    return f"{seconds // 60:02}:{seconds % 60:02}"

def geometry(im, elapsed, recap):
    draw = ImageDraw.Draw(im)
    theta = -0.55 + 0.63 * min(max(elapsed - 2, 0) / 7, 1)
    if recap:
        theta = 0.08 - 0.53 * min(elapsed / 6, 1)
    horizontal = np.array([np.cos(theta), -np.sin(theta), 0])
    vertical = np.array([0.46*np.sin(theta), 0.46*np.cos(theta), 0.89])

    def project(v):
        shifted = v - SOLUTION
        return (700 + 92 * shifted @ horizontal, 554 - 92 * shifted @ vertical)

    grid_origin = np.array([0., 0., 0.])
    for i, axis in enumerate("xyz"):
        endpoint = np.eye(3)[i] * 4.6
        draw.line([project(grid_origin), project(endpoint)], fill="#68849b", width=3)
        x, y = project(endpoint)
        label(draw, (x+17, y-12), axis, 27, MUTED, True)
    reveal = [0, 3.5, 14]
    for i, normal in enumerate(NORMALS):
        amount = 1 if recap else min(max((elapsed-reveal[i])/2, 0), 1)
        if amount <= 0:
            continue
        normal = normal / np.linalg.norm(normal)
        u = np.cross(normal, [0, 0, 1])
        u /= np.linalg.norm(u)
        v = np.cross(normal, u)
        vertices = [project(SOLUTION + amount*2.53*(a*u+b*v))
                    for a,b in [(-1,-1),(1,-1),(1,1),(-1,1)]]
        overlay = Image.new("RGBA", im.size)
        layer = ImageDraw.Draw(overlay)
        from PIL import ImageColor
        rgb = ImageColor.getrgb(COLORS[i])
        layer.polygon(vertices, fill=(*rgb, 52), outline=(*rgb, 220), width=3)
        im.paste(overlay, mask=overlay.getchannel("A"))

    draw = ImageDraw.Draw(im)
    if recap or elapsed >= 7:
        direction = np.cross(NORMALS[0], NORMALS[1])
        direction = direction / np.linalg.norm(direction)
        draw.line([project(SOLUTION - 2.7*direction), project(SOLUTION + 2.7*direction)],
                  fill="#ffffff", width=6)
        label(draw, (1232, 618), "White line: first two planes", 28, MUTED)
    if recap or elapsed >= 18:
        x,y = project(SOLUTION)
        draw.ellipse((x-11,y-11,x+11,y+11), fill="#ffffff", outline=BG, width=3)
        draw.line([(x+12,y-10),(x+88,y-80),(x+146,y-80)], fill="#ffffff", width=3)
        label(draw, (x+157,y-80), "(1, 2, 3)" if recap else "Shared point", 31, INK, True)
    for i, equation in enumerate(LESSON[1][2]):
        if recap or elapsed >= reveal[i]:
            y = 367 + 71*i
            draw.rounded_rectangle((1232,y-9,1252,y+11),5,fill=COLORS[i])
            label(draw,(1273,y),equation,31,INK)

def matrix(draw, rows, x, y, width, pivot=None, target=None, progress=1, previous=None, source=None):
    cols = [x + width*i for i in (0.26, 0.43, 0.60, 0.82)]
    step = 108
    for i, name in enumerate(("x", "y", "z", "constant")):
        label(draw, (cols[i],y-84), name, 26, MUTED, True, "mm")
    left,right = x+width*.14,x+width*.94
    draw.line([(left+20,y-45),(left,y-45),(left,y+2*step+45),(left+20,y+2*step+45)], fill=MUTED,width=4)
    draw.line([(right-20,y-45),(right,y-45),(right,y+2*step+45),(right-20,y+2*step+45)], fill=MUTED,width=4)
    separator=x+width*.71
    draw.line((separator,y-45,separator,y+2*step+45),fill=MUTED,width=3)
    for r,row in enumerate(rows):
        cy=y+r*step
        if r in (target, source):
            draw.rounded_rectangle((left+8,cy-40,right-8,cy+40),15,
                                   fill="#193d41" if r==target else "#223653")
        label(draw,(x+width*.08,cy),f"R{r+1}",27,MUTED,True,"mm")
        for c,val in enumerate(row):
            is_pivot = pivot is not None and (r,c) in pivot
            if is_pivot:
                draw.rounded_rectangle((cols[c]-40,cy-40,cols[c]+40,cy+40),12,fill="#26605a")
            offset = 0
            if previous and r == target:
                # Replace the target row one entry at a time, including the constant.
                reveal = np.clip(progress*5 - c, 0, 1)
                if reveal < .5:
                    val = previous[r][c]
                    offset = -19*float(reveal)
                else:
                    offset = 19*(1-float(reveal))
            label(draw,(cols[c],cy+offset),str(val).replace("-","−"),49,MINT if is_pivot else INK,True,"mm")

def row_work(draw, t):
    active = None
    state = 0
    for op in OPERATIONS:
        if t >= op[0]:
            active = op
            state = op[1]+1
    second = t >= 140
    pivots = [(0,0), (1,1), (2,2)] if t >= 160 else ([(1,1)] if second else [(0,0)])
    if active and 0 <= t-active[0] < 11:
        start, old, target, source, factor, operation = active
        elapsed = t-start
        progress = min(max((elapsed-3)/3, 0),1)
        matrix(draw,MATRICES[old+1],116,464,1000,pivots,target,progress,MATRICES[old],source)
        label(draw,(1170,390),operation,53,MINT,True)
        original = MATRICES[old][target]
        scaled = tuple(factor*v for v in MATRICES[old][source])
        result = MATRICES[old+1][target]
        row_text = lambda a: f"({a[0]}, {a[1]}, {a[2]} | {a[3]})".replace("-","−")
        label(draw,(1170,480),row_text(original),35)
        label(draw,(1170,542),"− " + row_text(scaled),35)
        if elapsed >= 3:
            label(draw,(1170,628),"= " + row_text(result),38,MINT,True)
    else:
        matrix(draw,MATRICES[state],116,464,1000,pivots)
        msg = ("Row echelon form", "Zeros below each pivot.") if t>=160 else (
              ("Next pivot", "Clear the y-entry below it.") if second else
              (("First pivot", "Clear the x-entries below it.") if state==0 else
              ("Updated matrix","Apply the operation to the constant too.")))
        label(draw,(1170,450),msg[0],44,MINT,True)
        label(draw,(1170,530),msg[1],28)

def frame(t):
    im = Image.new("RGB",(W,H),BG)
    draw = ImageDraw.Draw(im)
    index = max(i for i,row in enumerate(LESSON) if row[0] <= t)
    start, title, lines, _ = LESSON[index]
    elapsed = t-start
    draw.rounded_rectangle((96,51,441,102),24,fill="#193d41")
    label(draw,(118,76),"M3  /  LINEAR ALGEBRA",24,MINT,True)
    label(draw,(1824,76),clock(start),25,MUTED,True,"rm")
    label(draw,(96,167),title,72 if index else 92,INK,True)
    draw.rounded_rectangle((96,254,1824,940),36,fill=PANEL,outline="#28415b",width=3)

    if index in (2,8):
        geometry(im,elapsed,index==8)
    elif index in (4,5):
        row_work(draw,t)
    elif index == 1 and elapsed >= 12:
        matrix(draw,ORIGINAL,122,467,1000)
        for i,line in enumerate(lines):
            label(draw,(1190,452+112*i),line,37)
    elif index == 6:
        visible = min(3,1+int(elapsed >= 9)+int(elapsed >= 21))
        matrix(draw,MATRICES[-1],119,467,1000,[(3-visible,3-visible)])
        steps = ["2z = 6  →  z = 3", "y − 3 = −1  →  y = 2", "x + 2 + 3 = 6  →  x = 1"]
        for i in range(visible):
            label(draw,(1170,459+i*97),steps[i],40,MINT if i==visible-1 else INK,True)
    else:
        visible = len(lines)
        if index in (1,3,7):
            visible = min(visible,1+int(elapsed>=4)+int(elapsed>=8))
        for i,line in enumerate(lines[:visible]):
            y=(409+i*125) if index!=9 else (379+i*101)
            size = 34 if index==9 and i>=3 else (48 if index==0 else 51)
            label(draw,(960,y),line,size,MINT if i==0 else INK,i==0,"mm")
        if index==7 and elapsed>=12:
            label(draw,(960,816),"(x, y, z) = (1, 2, 3)",50,MINT,True,"mm")
    draw.rounded_rectangle((96,1004,1824,1013),4,fill="#2a435c")
    draw.rounded_rectangle((96,1004,96+max(8,int(1728*t/END)),1013),4,fill=MINT)
    return im

def timeline():
    # Full frame-rate output with short animated sections and held reading frames.
    ranges = [(50,59),(64,66),(233,239)] + [(s+3,s+6) for s,*_ in OPERATIONS]
    for second in range(END):
        moving = any(a<=second<b for a,b in ranges)
        step = 2 if moving else 24
        for f in range(0,24,step):
            yield second+f/24, step/24

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path("_Video.mp4"))
    parser.add_argument("--preview",type=float,help="Render a single frame to --output.")
    args=parser.parse_args()
    if args.preview is not None:
        frame(args.preview).save(args.output)
        return
    with TemporaryDirectory() as temp:
        directory=Path(temp)
        sequence=[]
        for i,(time,duration) in enumerate(timeline()):
            image=directory/f"{i:05}.jpg"
            frame(time).save(image,quality=94,subsampling=0)
            sequence += [f"file '{image.name}'","option framerate 24",f"duration {duration:.9f}"]
        sequence += [f"file '{image.name}'","option framerate 24"]
        manifest=directory/"frames.txt"
        manifest.write_text("\n".join(sequence)+"\n")
        subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0",
                        "-i",str(manifest),"-vf","tpad=stop_mode=clone:stop_duration=0.25","-t",str(END),"-r","24","-an","-c:v","libx264",
                        "-threads","4","-preset","veryfast","-crf","20","-pix_fmt","yuv420p",
                        "-movflags","+faststart",str(args.output.resolve())],check=True)

if __name__=="__main__":
    main()
