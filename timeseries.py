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
    def getIsoWeeks(self):
        return [x.isoweek for x in self.timepoints]
    def __init__(self,countsPerWeek):
        self.timepoints = []
        for i in range(len(countsPerWeek)):
            self.timepoints.append(Timepoint(countsPerWeek[i]))
    def getStartDate(self):
        return sorted(self.getDates())[0]
    def getEndDate(self):
        return sorted(self.getDates())[-1]
    def getOutliers(self):
        return statistics.findOutliers(self.getCounts())
    def getVariance(self):
        return statistics.getVariance(self.getCounts())

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

def alignTimeseries(seriesA, seriesB):
    #function to remove timepoints ((year,week),count) from Timeseries seriesA and seriesB if timepoint not in both
    timepointsBoth = [list(set(seriesA.getIsoWeeks()) & set(seriesB.getIsoWeeks()))][0]
    delA = [x for x in seriesA.timepoints if x.isoweek not in timepointsBoth]
    while(len(delA)>0):
        x = delA[0]
        delA.remove(x)
        seriesA.timepoints.remove(x)
    delB = [x for x in seriesB.timepoints if x.isoweek not in timepointsBoth]
    while(len(delB)>0):
        x = delB[0]
        delB.remove(x)
        seriesB.timepoints.remove(x)
    return seriesA,seriesB