import statistics
import datetime

def getFirstDateFromIsoWeek(p_year,p_week):
    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    return firstdayofweek

class Timepoint:
    def __init__(self,week,count):
        self.isoweek = week
        self.year = week[0]
        self.date = getFirstDateFromIsoWeek(week[0],week[1])

class Timeseries:
    def __init__(self,word,weeks,counts):
        if len(weeks) == len(counts):
            self.timepoints = []
            for i in range(len(weeks)):
                self.timepoints.append(Timepoint(weeks[i],counts[i]))
            self.word = word
            self.outliers = statistics.findOutliers(counts)
            self.variance = statistics.getVariance(counts)