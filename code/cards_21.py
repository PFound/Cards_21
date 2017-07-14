class Song(object):
 
  def __init__(self, lyrics):
    self.lyrics = lyrics
  
  def singMeASong(self):
    for line in self.lyrics:
      print line

test = Song(["Test and athings in dfahldsfjkh a"])

test.singMeASong()
  