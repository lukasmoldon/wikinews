import statistics
import datetime

def getFirstDateFromIsoWeek(p_year,p_week):
    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    return firstdayofweek

class Timepoint:
    def __init__(self,countPerWeek):
        self.isoweek = countPerWeek[0]
        self.year = countPerWeek[0][0]
        self.date = getFirstDateFromIsoWeek(countPerWeek[0][0],countPerWeek[0][1])
        self.count = countPerWeek[1]

class Timeseries:
    def getCounts(self):
        return [x.count for x in self.timepoints]
    def __init__(self,word,countsPerWeek):
        self.timepoints = []
        for i in range(len(countsPerWeek)):
            self.timepoints.append(Timepoint(countsPerWeek[i]))
        self.word = word
        self.outliers = statistics.findOutliers(self.getCounts())
        self.variance = statistics.getVariance(self.getCounts())
    
x = ('year',[((2019,1),38),((2019,2),10),((2019,3),1)])
ts = Timeseries(x[0],x[1])
p = 5