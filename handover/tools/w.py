from faster_whisper import WhisperModel
import json
m=WhisperModel("small",compute_type="int8",cpu_threads=4)
import wave,numpy as np;wf=wave.open("a.wav");A=np.frombuffer(wf.readframes(wf.getnframes()),np.int16).astype(np.float32)/32768
seg,_=m.transcribe(A,word_timestamps=True,language="en")
W=[{"w":w.word.strip(),"s":w.start,"e":w.end} for s in seg for w in s.words]
json.dump(W,open("words.json","w"),indent=0)
