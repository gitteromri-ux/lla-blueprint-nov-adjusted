# Ad 17 VIP, November version — editor report

Source: /home/user/lla-blueprint-nov-adjusted/final/claude/ad17_VIP_regen_9x16.mp4 (79.1 s, 24 fps, burned-in captions). Repo HEAD 0b9a85b.
Outputs: /home/user/kit/out/Ad17/Ad17_VIP_Nov_9x16_1080x1920.mp4, Ad17_VIP_Nov_4x5_1080x1350.mp4, Ad17_VIP_Nov_1x1_1080x1080.mp4 (80.25 s each: original 76.5 s of footage/cards + approved end card 3.75 s).
Evidence strips (6 fps, read with the Read tool): /home/user/kit/out/Ad17/evidence/*.jpg. QA harness output: bottom of this file.

Method (what was done to the burned-in captions): every burned caption in the talking-head shots was removed per frame by a text mask (white/blue text + shadow, pooled over +/-8 frames so fading captions are caught too) filled with sweater texture copied from the rows above/below (no blur, no box); captions on the dark cards were filled with the local card background. New captions were re-rendered with the approved capfx style (Playfair SemiBold 65 px, white / blue italic for emphasis, soft shadow) on a dark rounded backing (5,13,34,150, 8 px blur) at y 1022-1123, 2-4 words per caption, synced to word timings (Cloudinary auto_transcription of the cut, transcript_mixed.json). Footage, cut points and timing are unchanged except: a slow 1.00->1.03 push-in on the static cards (required by qa.py), two short push-ins to hide the hands, and the end card (approved animated card from film2 61.04-64.0 s + 0.5 s hold) replacing the old static end card + black tail.

## Lead verification (frame strips in evidence/, QA harness /home/user/kit/qa/qa.py)
1 Music: pop removed (vocal stem pauses -77 dB, no tonal content); calm licensed piano bed ("Leave", Mattia Vlad Morleo, Artlist) 16 dB under voice, -18 LUFS under cards/end. DONE.
2 Captions re-synced to word timings, 2-4 words, nothing frozen (qa: no frozen stretches). DONE.
3 Dark backing on all captions (strips 1-78). DONE.
4 "Julie proved it." now at 20.15-21.8 s when Julie is named (sheet, strip_20). DONE.
5 Duplicate "Ten years pass. She ages six." big caption removed at 22-26 s; the small header inside the chart graphic remains as the single instance. DONE.
6 "In 2023," joined: "In 2023, she out-aged" / "Bryan Johnson" / "and his $2 million a year" / "on about $100 a month." (strip_27, 28.5). DONE.
7 USA Today at 0:28: whole and centred in this cut, no change needed (strip_28.5). DONE.
8 Hands: push-in 1.22x at 38.95-40.35 and 1.38x at 45.9-47.85; a hand is still visible for ~0.3 s at 38.7-38.9 before the push-in starts. PARTIAL.
9 Spoken CTA "Tap Learn More to claim your $79 November spot." in her cloned voice at 76.3 s into the approved animated end card. DONE.
10 Offer on screen exactly: "Start for $79. / Then $169 a month, four months. / 14-day full refund." + "VIP seat at Julie's live masterclass, Nov 14" (69.7-74.75 s); VIP also spoken/captioned at 61-66 s. DONE.
11 Sizes 9:16, 4:5 (crop y=285), 1:1 (crop y=330, 1x1 end card); -14.0 LUFS, -1.3 dBTP; H.264 High / AAC 192k; qa.py RESULT PASS on all three; no text in top 14% / bottom 35% of the 9:16. DONE.
