import statistics
import datetime
import manage_articles as mng

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
    def getDates(self):
        return [x.date for x in self.timepoints]
    def __init__(self,countsPerWeek):
        #countsPerWeek:   [((2019, 1), 38), ((2019, 2), 10), ...
        self.timepoints = []
        for i in range(len(countsPerWeek)):
            self.timepoints.append(Timepoint(countsPerWeek[i]))
        self.outliers = statistics.findOutliers(self.getCounts())
        self.variance = statistics.getVariance(self.getCounts())
    def getStartDate(self):
        return sorted(self.getDates())[0]
    def getEndDate(self):
        return sorted(self.getDates())[-1]

def parseWikipediaCounts(wiki):
    d = {}
    for i in range(len(wiki[0])):
        year = wiki[0][i].isocalendar()[0]
        week = wiki[0][i].isocalendar()[1]
        count = wiki[1][i]
        if (year,week) not in d:
            d[(year,week)] = count
        else:
            d[(year,week)] = d[(year,week)]+count
    
    l = []
    for k in d:
        l.append((k,d[k]))
    return Timeseries(l)