# Reframe recipe v2: Red Wine 4:5 (passed self-audit Nov 3, 10:45 Israel time). 1:1 cannot pass (see end).
Inputs: FINAL = red_wine_4k_final.mp4 (opening, end card, AUDIO); WIDE = riverside_raw/red_wine_nocap_wide.mp4 (body, no captions/hook; 1804 frames, same cut points as the final, audio lag 5 ms).
Frames @24fps: opening 0-94 | body 95-1634 | end card 1635-1802 (1803 total = final).

1. Measure on WIDE (ruler frames: drawgrid h=100/500 every shot): head top ~330 native px (early) to ~430 (late); chin ~2250 (early) to ~2480 (late, t>62s). The date label is at y>=3420, x>=1700, so keep the crop bottom < 3400.
   Shot cuts (scene>0.3): 13.33 18.42 28.54 33.58 49.04 54.08 58.29 62.25 68.17.
2. Per-shot crop y (2160x2700): t<13.33: 180 | <54.08: 230 | <62.25: 260 | else 350. Body push-in 1.00->1.02 linear (scale eval=frame, then centre crop).
3. Captions: python3 /workspace/mkcaps.py words.json 1080 1350 0.8 64 cap45w 3.95 68.125   (words.json from /workspace/w.py whisper)
4. Hook (frames 95-140 in the final, i.e. 3.96-5.88s): python3 /workspace/mkhook.py 1080 1350 hook45.png 200
   Style measured from the final: Inter Bold, white, line 1 = 84.5% of width, dark drop shadow offset 3px with light blur, 2 lines "YOUR WINE IS MAKING / HOT FLASHES WORSE".
5. End card (fills the frame, no box): crop the inside of the panel and scale it up; extend the top and bottom by stretching the card's own edge rows (seamless):
   ffmpeg -i FINAL -vf "trim=start_frame=1635,setpts=PTS-STARTPTS,crop=1240:1112:330:1396,scale=1080:972:flags=lanczos,setsar=1,split=3[em][et][eb];[et]crop=1080:2:0:0,scale=1080:190:flags=neighbor[t1];[eb]crop=1080:2:0:970,scale=1080:188:flags=neighbor[b1];[t1][em][b1]vstack=3,setsar=1,format=yuv420p" -an -c:v libx264 -crf 10 -preset fast ec45.mp4
6. Main render (/workspace/r45.sh):
ffmpeg -i FINAL -i WIDE -f concat -safe 0 -i cap45w/list.txt -loop 1 -i hook45.png -i ec45.mp4 -filter_complex "[0:v]trim=end_frame=95,setpts=PTS-STARTPTS,crop=2160:2700:0:0,scale=1080:1350:flags=lanczos,setsar=1[O];[1:v]trim=start_frame=95:end_frame=1635,crop=2160:2700:0:'if(lt(t,13.33),180,if(lt(t,54.08),230,if(lt(t,62.25),260,350)))',scale=w='max(1080,2*trunc(540*(1+0.02*(t-3.958)/64.167)))':h=-2:eval=frame:flags=lanczos,crop=1080:1350,setsar=1,setpts=PTS-STARTPTS[B];[4:v]setsar=1[E];[O][B][E]concat=n=3:v=1:a=0[v0];[2:v]format=rgba,fps=24[c];[v0][c]overlay=0:0:eof_action=pass[v1];[3:v]format=rgba[h];[v1][h]overlay=0:0:shortest=1:enable='between(n,95,140)',format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -preset medium -crf 18 -threads 6 -c:a copy -movflags +faststart -y red_wine_4x5.mp4
   Gotchas: scale w must be max(1080,...) because at init t=0 the height would be <1350; 1-px crops fail in yuv420 (use 2); an inline end-card split segfaulted, so pre-render it.
7. Audit: nb_frames 1803; freezedetect n=0.002 d=1 (0); cropdetect = full 1080x1350 (no bars); sheet = frames 24,72,100,135 + every 96 frames with a pts label; ruler frames per shot for head-top / chin / caption-top.

## 1:1 is not feasible from WIDE
Face span (hair top to chin) is ~1920-2050 native px at 2160 width. With headroom (>=60) and a 2-line caption block fully below the chin (~330 native), you need ~2350-2450 > 2160. Any square crop cuts the head or chin, or puts captions over the chin. A 1.1-zoom export (w11) is worse.
