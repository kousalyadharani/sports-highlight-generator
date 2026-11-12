import unittest
from detect_events import detect
class DetectorTests(unittest.TestCase):
 def test_intersection_creates_clamped_ten_second_clip(self):
  e=detect([{"frame":30,"ball":[1,1,4,4],"goals":[[0,0,5,5]]}],10,30)[0]; self.assertEqual(e["start"],0); self.assertEqual(e["end"],10)
 def test_nonintersection_ignored(self): self.assertEqual(detect([{"frame":30,"ball":[8,8,9,9],"goals":[[0,0,2,2]]}]),[])
if __name__=="__main__":unittest.main()
