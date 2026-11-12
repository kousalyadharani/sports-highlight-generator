# Automated Sports Highlight Generator & Event Detector

Clean-room reconstruction of the documented YOLOv8/OpenCV/NumPy workflow. The portfolio reports 30+ FPS, 40% lower inference latency, and 10-second event clips on its tested setup. Those measurements are not reproduced or claimed here.

## Run

`python3 detect_events.py sample_detections.json --fps 30 --clip-seconds 10`

The detector consumes timestamped ball and goal bounding boxes, filters candidates using rectangle intersection, and outputs clip windows. This separates event logic from model inference; connect YOLOv8 detections as a preprocessing step to use real footage. OpenCV clip rendering is available in the CourtVision repository.

## Verify

`python3 -m unittest -v`
