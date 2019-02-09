from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree as ET
import locale
from xml.dom import minidom
from lxml import etree
import os.path
from datetime import datetime
from datetime import timedelta
import math

locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_ALL, 'swedish')

class XmlCreator:

    def __init__(self, dictionary, file):
        self.mydictionary = dictionary
        self.file = file
        self.path = os.path.dirname(file)

    def prettify(self, elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t", encoding="utf-8")


    def halfpaceadjust(self, string):
        halfdict = {'Heltid': 'Halvtid', 'heltid': 'halvtid', '100%': '50%', '100 %': '50 %'}
        for k, v in halfdict.items():
            string = string.replace(k, v)
        return string

    def quartpaceadjust(self, string):
        quartdict = {'Heltid': 'Kvartstid', 'heltid': 'kvartstid', '100%': '25%', '100 %': '25 %'}
        for k, v in quartdict.items():
            string = string.replace(k, v)
        return string

    '''Denna funktion anropas för varje fil som ska skapas, antal starter * studietakter'''
    def makecoursestarts(self, start, pace, customer):
        workdictionary = {}
        if pace == 50:
            for k, v in self.mydictionary.items():
                if type(v) is str:
                    workdictionary[k] = self.halfpaceadjust(v)
                else:
                    workdictionary[k] = v
        elif pace == 25:
            for k, v in self.mydictionary.items():
                if type(v) is str:
                    workdictionary[k] = self.quartpaceadjust(v)
                else:
                    workdictionary[k] = v
        else:
            workdictionary = self.mydictionary
        coursesfile = './Courses.xml'
        if customer == 'Nacka':
            coursesfile = './Courses_na.xml'
        elif customer == 'Botkyrka':
            coursesfile = './Courses_bo.xml'
        elif customer == 'Stockholm':
            coursesfile = './Courses_st.xml'
        self.coursetree = ET.parse(coursesfile)
        self.root = self.coursetree.getroot()
        self.top = Element("CourseStarts")
        self.startdatestr = ""
        self.pointsperweek = 0
        if start == 2:
            self.startdatestr = workdictionary['start2']
        elif start == 3:
            self.startdatestr = workdictionary['start3']
        else:
            self.startdatestr = workdictionary['start1']
        if pace == 25:
            self.pointsperweek = 5
        elif pace == 50:
            self.pointsperweek = 10
        elif pace == 100:
            self.pointsperweek = 20
        for course in self.root.findall('Course'):
            if course.find(workdictionary['customer']).text == 'true':
                self.days = (math.floor(int(course.find('StudyPoints').text)/self.pointsperweek)*7)-3
                self.coursestart = SubElement(self.top, 'CourseStart')
                self.courseperiod = SubElement(self.coursestart, 'Period')
                self.courseperiod.text = workdictionary['periodformat']
                self.coursename = SubElement(self.coursestart, 'Name')
                self.coursename.text = course.find('Name').text
                self.schoolname = SubElement(self.coursestart, 'School')
                self.schoolname.text = workdictionary['schoolformat']
                self.extensexportday = SubElement(self.coursestart, 'ExtensExportDay')
                self.extensexportday.text = workdictionary['studyformat']
                self.flex = SubElement(self.coursestart, 'Flex')
                self.flex.text = str(workdictionary['flex'])
                self.distance = SubElement(self.coursestart, 'Distance')
                self.distance.text = str(workdictionary['distance'])
                self.coursegroup = SubElement(self.coursestart, 'CourseGroup')
                self.ccabbr = course.find('CourseCodeAbbr').text
                self.coursegroup.text = workdictionary['coursegroup'].replace('*ccabb*', self.ccabbr)
                self.startdate = SubElement(self.coursestart, 'StartDate')
                self.startdate.text = self.startdatestr
                self.enddate = SubElement(self.coursestart, 'EndDate')
                format = "%Y-%m-%d"
                start = datetime.strptime(self.startdate.text, format)
                end = start + timedelta(days=self.days)
                self.enddate.text = datetime.strftime(end, format)
                self.weeks = SubElement(self.coursestart, 'Weeks')
                points = course.find('StudyPoints').text
                self.points = SubElement(self.coursestart, 'Points')
                self.points.text = points
                pointweeks = math.floor(int(points)/self.pointsperweek)
                if pointweeks < 3:
                    self.top.remove(self.coursestart)
                else:
                    self.weeks.text = str(pointweeks)
                self.comment = SubElement(self.coursestart, 'Comment')
                if course.find('WorkExperience').text == 'true':
                    self.comment.text = workdictionary['workexperience']
                elif course.find('CPR').text == 'true':
                    self.comment.text = workdictionary['cprcomment']
                elif course.find('LAB').text == 'true':
                    self.comment.text = workdictionary['labcomment']
                else:
                    self.comment.text = workdictionary['standardcomment']
                self.header = SubElement(self.coursestart, 'Header')
                if 'header' in workdictionary:
                    if course.find('WorkExperience').text == 'true':
                        self.header.text = workdictionary['weheader']
                    elif course.find('CPR').text == 'true':
                        self.header.text = workdictionary['cprheader']
                    elif course.find('LAB').text == 'true':
                        self.header.text = workdictionary['labheader']
                    else:
                        self.header.text = workdictionary['header']
                self.startinfo = SubElement(self.coursestart, 'Startinfo')
                if 'startinfo' in workdictionary:
                    self.startinfo.text = workdictionary['startinfo']
                self.studyhours = SubElement(self.coursestart, 'Studyhours')
                if 'studyhours' in workdictionary:
                    self.studyhours.text = workdictionary['studyhours']
                self.fed = SubElement(self.coursestart, 'Fed')
                self.fed.text = 'false'

    def mergeToOne(self, files):
        first = None
        for filename in files:
            data = ET.parse(filename).getroot()
            if first is None:
                first = data
            else:
                first.extend(data)
        if first is not None:
            parser = etree.XMLParser(remove_blank_text=True)
            self.top = etree.XML(ET.tostring(first), parser=parser)

    def writetofile(self):
        self.finalxmlstring = self.prettify(self.top)
        self.finalxml = ET.ElementTree(ET.fromstring(self.finalxmlstring))
        self.root = self.finalxml.getroot()
        self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.finalxml.write(self.file, encoding="utf-8", method="xml")
        line = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        with open(self.file, 'r+') as f:
            file_data = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + file_data)