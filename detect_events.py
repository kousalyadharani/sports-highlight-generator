#!/usr/bin/env python3
"""Detect candidate goal events from timestamped object detections."""
import argparse,json
from pathlib import Path

def intersects(a,b): return a[0]<b[2] and a[2]>b[0] and a[1]<b[3] and a[3]>b[1]
def detect(frames, clip_seconds=10.0, fps=30.0, frame_skip=1):
 """Input: [{frame, ball:[x1,y1,x2,y2] or null, goals:[[x1,y1,x2,y2], ...]}]."""
 candidates=[]; prev=None
 for row in sorted(frames,key=lambda x:int(x["frame"])):
  frame=int(row["frame"])
  if frame%max(1,int(frame_skip)): continue
  ball=row.get("ball"); goals=row.get("goals",[])
  if ball and any(intersects(ball,g) for g in goals):
   t=frame/fps; start=max(0,t-clip_seconds/2); candidates.append({"frame":frame,"time":round(t,3),"start":round(start,3),"end":round(start+clip_seconds,3),"event":"goal-region intersection"})
  prev=ball
 return candidates
def main():
 p=argparse.ArgumentParser(); p.add_argument("detections",type=Path); p.add_argument("--output",type=Path,default=Path("events.json")); p.add_argument("--fps",type=float,default=30); p.add_argument("--clip-seconds",type=float,default=10); p.add_argument("--frame-skip",type=int,default=1); a=p.parse_args()
 events=detect(json.loads(a.detections.read_text()),a.clip_seconds,a.fps,a.frame_skip); a.output.write_text(json.dumps(events,indent=2)+"\n"); print(f"Found {len(events)} candidate events")
if __name__=="__main__":main()
