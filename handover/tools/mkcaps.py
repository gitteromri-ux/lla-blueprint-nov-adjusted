# usage: mkcaps.py words.json W H fontscale bottom_margin outdir t_start t_end
import json,sys,os
from PIL import Image,ImageDraw,ImageFont
W=json.load(open(sys.argv[1])); FW,FH=int(sys.argv[2]),int(sys.argv[3]); sc=float(sys.argv[4]); bm=int(sys.argv[5]); od=sys.argv[6]
T0,T1=float(sys.argv[7]),float(sys.argv[8])
FIX={"so,":"SO","northrup":"NORTHROP"}
os.makedirs(od,exist_ok=True)
S=round(72*sc); OUT=max(3,round(6.5*sc)); PITCH=round(112*sc); BOXH=round(104*sc); PADX=round(12*sc); R=round(13*sc)
font=ImageFont.truetype("/usr/share/fonts/truetype/sand-box/google/Poppins/Poppins-ExtraBold.ttf",S)
HL=(110,166,254,255); MAXC=16
words=[dict(w,t=FIX.get(w['w'].lower(),w['w'].upper())) for w in W if w['e']>T0 and w['s']<T1]
# chunk into <=2 lines of <=MAXC chars, break on sentence end / pause
chunks=[];cur=[];lines=[[]]
def flush():
    global lines
    if lines[0]: chunks.append(lines)
    lines=[[]]
for i,w in enumerate(words):
    L=lines[-1]; txt=" ".join(x['t'] for x in L+[w])
    if L and len(txt)>MAXC:
        if len(lines)==2: flush()
        else: lines.append([])
    lines[-1].append(w)
    nxt=words[i+1] if i+1<len(words) else None
    if w['t'][-1] in ".?!" or (nxt and nxt['s']-w['e']>0.6): flush()
flush()
sp=font.getlength(" ")
def render(ch,act,path):
    im=Image.new("RGBA",(FW,FH),(0,0,0,0)); d=ImageDraw.Draw(im)
    n=len(ch); cy_last=FH-bm
    for li,L in enumerate(ch):
        cy=cy_last-(n-1-li)*PITCH
        ws=[font.getlength(x['t']) for x in L]; tot=sum(ws)+sp*(len(L)-1); x=(FW-tot)/2
        for x_w,wd in zip(L,ws):
            if x_w is act: d.rounded_rectangle([x-PADX,cy-BOXH/2,x+wd+PADX,cy+BOXH/2],R,fill=HL)
            x+=wd+sp
        x=(FW-tot)/2
        for x_w,wd in zip(L,ws):
            d.text((x,cy),x_w['t'],font=font,fill="white",anchor="lm",stroke_width=OUT,stroke_fill="black"); x+=wd+sp
    im.save(path)
blank=os.path.join(od,"blank.png"); Image.new("RGBA",(FW,FH),(0,0,0,0)).save(blank)
seq=[];k=0
allw=[w for ch in chunks for L in ch for w in L]
for ci,ch in enumerate(chunks):
    cw=[w for L in ch for w in L]
    nxt=chunks[ci+1][0][0]['s'] if ci+1<len(chunks) else T1
    end=min(nxt, cw[-1]['e']+0.5, T1)
    for j,w in enumerate(cw):
        s=max(w['s'],T0); e=cw[j+1]['s'] if j+1<len(cw) else end
        p=os.path.join(od,f"c{k:04d}.png"); render(ch,w,p); k+=1; seq.append((s,e,p))
# build concat list covering 0..T1 exactly
t=0;out=[]
for s,e,p in seq:
    if s>t+1e-3: out.append((blank,s-t)); t=s
    out.append((p,e-t)); t=e
out.append((blank,0.04))
with open(os.path.join(od,"list.txt"),"w") as f:
    for p,dur in out: f.write(f"file '{os.path.abspath(p)}'\nduration {dur:.4f}\n")
    f.write(f"file '{os.path.abspath(blank)}'\n")
print(len(chunks),"chunks",k,"frames; ends",t)
