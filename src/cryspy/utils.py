import cryspy.numbers as nb
import cryspy.geo as geo

class Karussell:
   def __init__(self, metric, zerodirection, positivedirection):
       
       self.zerodir = zerodirection * (1/metric.length(zerodirection))
       self.positivedir = positivedirection - self.zerodir * metric.dot(positivedirection, self.zerodir)
       self.positivedir *= 1/metric.length(self.positivedir)
       self.metric = metric

   def direction(self, angle):
       x = nb.cos(angle)
       y = nb.sin(angle)
       return self.zerodir * x + self.positivedir * y
