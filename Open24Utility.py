import webbrowser
from xml.etree import ElementTree as ET
import wx
import wx.xrc
import wx.adv
import wx.locale
from Open24XMLCreator import XmlCreator
import subprocess
import locale

locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_ALL, 'swedish')

class Open24Utility:

    @classmethod
    def getcourselist(cls, cust):
        if cust == 'Välj kund':
            dial = wx.MessageDialog(None, 'Du måste välja kund!', 'Info', wx.OK)
            dial.ShowModal()
            return
        coursefile = "Courses.xml"
        if cust == "Nacka":
            coursefile = "Courses_na.xml"
        elif cust == "Botkyrka":
            coursefile = "Courses_bo.xml"
        elif cust == "Stockholm":
            coursefile = "Courses_st.xml"
        tree = ET.parse(coursefile)
        coursenames = tree.findall('.//Name')
        ccabb = tree.findall('.//CourseCodeAbbr')
        return coursenames, ccabb

    def __init__(self):
        self.urls = open('urls.txt','r')
        self.urldict = eval(self.urls.read())

    def opencustomersite(self, customer):
        url = self.urldict[customer]
        webbrowser.open(url)

    def buildcoursegroup(self, obj, ccabb, pace, sm, order):
        NTI = obj.textCtrlNTI.GetValue() or ''
        CGYear = obj.textCtrlCGYear.GetValue() or ''
        CGPeriod = obj.textCtrlCGPeriod.GetValue() or ''
        StudyForm = obj.textCtrlStudyForm.GetValue() or ''
        if sm == 1:
            SM = obj.textCtrlStartMarker1.GetValue() or ''
        elif sm == 2:
            SM = obj.textCtrlStartMarker2.GetValue() or ''
        elif sm == 3:
            SM = obj.textCtrlStartMarker3.GetValue() or ''
        else:
            SM = ''
        if pace == 'full':
            P = obj.textCtrl100.GetValue() or ''
        elif pace == 'half':
            P = obj.textCtrl50.GetValue() or ''
        else:
            P = obj.textCtrl25.GetValue() or ''
        CG = ''
        strswitcher = {0: NTI, 1: CGYear, 2: CGPeriod, 3: ccabb, 4: StudyForm, 5: SM, 6: P}
        for place in order:
            if place >= 0:
                CG += strswitcher[place]
        return CG

    def preparesave(self, obj):
        self.c = obj.customerSelect.GetValue()
        if self.c == "Välj kund":
            dial = wx.MessageDialog(None, 'Du måste välja kund!', 'Info', wx.OK)
            dial.ShowModal()
            return
        if obj.headerChk.IsChecked() and obj.headerText.IsEmpty():
            dial = wx.MessageDialog(None, 'Ska kunden ha rubrik, måste du skriva något.', 'Info', wx.OK)
            dial.ShowModal()
            return
        if obj.startInfoChk.IsChecked() and obj.startInfoText.IsEmpty():
            dial = wx.MessageDialog(None, 'Ska kursstartsinfo vara med måste du skriva text.', 'Info', wx.OK)
            dial.ShowModal()
            return
        if obj.studyHoursChk.IsChecked() and obj.studyHoursText.IsEmpty():
            dial = wx.MessageDialog(None, 'Ska dagar och tider vara med måste du skriva text.', 'Info', wx.OK)
            dial.ShowModal()
            return
        else:
            with wx.DirDialog(obj, message="Var ska XML-filerna sparas?", defaultPath="",
              style=wx.DD_DEFAULT_STYLE, pos=wx.DefaultPosition, size=wx.DefaultSize) as dirDialog:

                if dirDialog.ShowModal() == wx.ID_CANCEL:
                    return

                self.pathname = dirDialog.GetPath()
                self.hassecond = False
                self.hasthird = False
                self.p = obj.textCtrlCGPeriod.GetValue()
                self.c = obj.customerSelect.GetValue()
                self.startmarker1 = obj.textCtrlStartMarker1.GetValue()
                #Fixa hanteringen av andra starten
                if obj.start2Check.IsChecked():
                    self.hassecond = True
                    startDate2DT = obj.start2Date.GetValue()
                    self.startDate2str = startDate2DT.FormatDate()
                    self.startmarker2 = obj.textCtrlStartMarker2.GetValue()
                if obj.start3Check.IsChecked():
                    self.hasthird = True
                    startDate3DT = obj.start3Date.GetValue()
                    self.startDate3str = startDate3DT.FormatDate()
                    self.startmarker3 = obj.textCtrlStartMarker3.GetValue()
                now = wx.DateTime.Now()
                self.file100_1 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker1 + "_100.xml"
                self.file50_1 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker1 + "_50.xml"
                self.file25_1 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker1 + "_25.xml"
                if self.hassecond:
                    self.file100_2 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker2 + "_100.xml"
                    self.file50_2 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker2 + "_50.xml"
                    self.file25_2 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker2 + "_25.xml"
                if self.hasthird:
                    self.file100_3 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker3 + "_100.xml"
                    self.file50_3 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker3 + "_50.xml"
                    self.file25_3 = self.pathname + "\\" + self.c + '_P' + self.p + '_' + now.Format("%Y%m%d") + self.startmarker3 + "_25.xml"
                self.processProfile(obj)

    def processProfile(self, obj):
        self.customer = obj.customerSelect.GetValue()
        self.di = {'customer': self.customer}
        self.yearAndPeriod = obj.yearAndPeriodInput.GetValue()
        self.di.update({'periodformat': self.yearAndPeriod})
        self.schoolFormatVal = obj.schoolNameInput.GetValue()
        self.di.update({'schoolformat': self.schoolFormatVal})
        self.studyFormatVal = obj.studyFormInput.GetValue()
        self.di.update({'studyformat': self.studyFormatVal})
        self.start1DateVal = obj.start1Date.GetValue()
        self.di.update({'start1': self.start1DateVal.FormatDate()})
        if obj.headerChk.IsChecked():
            self.headerVal = obj.headerText.GetValue()
            self.di.update({'header': self.headerVal})
        if obj.startInfoChk.IsChecked():
            self.startInfoVal = obj.startInfoText.GetValue()
            self.di.update({'startinfo': self.startInfoVal})
        if obj.studyHoursChk.IsChecked():
            self.studyHoursVal = obj.startInfoText.GetValue()
            self.di.update({'studyhours': self.studyHoursVal})
        if obj.start2Check.IsChecked():
            self.startDate2Val = obj.start2Date.GetValue()
            self.di.update({'start2': self.startDate2Val.FormatDate()})
        if obj.start3Check.IsChecked():
            self.startDate3Val = obj.start3Date.GetValue()
            self.di.update({'start3': self.startDate3Val.FormatDate()})
        self.flexRadioVal = obj.flexRadio.GetValue()
        self.di.update({'flex': self.flexRadioVal})
        self.distanceRadioVal = obj.distanceRadio.GetValue()
        self.di.update({'distance': self.distanceRadioVal})
        self.standardCommentVal = obj.standardComment.GetValue()
        self.di.update({'standardcomment': self.standardCommentVal})
        self.workExperienceVal = obj.workexpComment.GetValue()
        self.di.update({'workexperience': self.workExperienceVal})
        self.cprcommentVal = obj.cprComment.GetValue()
        self.di.update({'cprcomment': self.cprcommentVal})
        self.labcommentVal = obj.labComment.GetValue()
        self.di.update({'labcomment': self.labcommentVal})
        if obj.headerChk.IsChecked():
            self.headerTextVal = obj.headerText.GetValue()
            self.di.update({'header': self.headerTextVal})
            self.header = True
            self.headerWETextVal = obj.headerWEText.GetValue()
            self.di.update({'weheader': self.headerWETextVal})
            self.headerCPRTextVal = obj.headerCPRText.GetValue()
            self.di.update({'cprheader': self.headerCPRTextVal})
            self.headerLabTextVal = obj.headerLabText.GetValue()
            self.di.update({'labheader': self.headerLabTextVal})
        if obj.startInfoChk.IsChecked():
            self.startInfoTextVal = obj.startInfoText.GetValue()
            self.di.update({'startinfo': self.startInfoTextVal})
            self.startInfo = True
        if obj.studyHoursChk.IsChecked():
            self.studyHoursTextVal = obj.studyHoursText.GetValue()
            self.di.update({'studyhours': self.studyHoursTextVal})
            self.studyHours = True
        listobj = obj.coursegroupSort.GetList()
        self.order = listobj.GetCurrentOrder()
        self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'full', 1, self.order)
        self.di.update({'coursegroup' : self._coursegroup})
        xc100_1 = XmlCreator(self.di, self.file100_1)
        xc100_1.makecoursestarts(1, 100, self.customer)
        xc100_1.writetofile()
        self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'half', 1, self.order)
        self.di.update({'coursegroup' : self._coursegroup})
        xc50_1 = XmlCreator(self.di, self.file50_1)
        xc50_1.makecoursestarts(1, 50, self.customer)
        xc50_1.writetofile()
        self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'quart', 1, self.order)
        self.di.update({'coursegroup' : self._coursegroup})
        xc25_1 = XmlCreator(self.di, self.file25_1)
        xc25_1.makecoursestarts(1, 25, self.customer)
        xc25_1.writetofile()
        if self.hassecond:
            self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'full', 2, self.order)
            self.di.update({'coursegroup': self._coursegroup})
            xc100_2 = XmlCreator(self.di, self.file100_2)
            xc100_2.makecoursestarts(2, 100, self.customer)
            xc100_2.writetofile()
            self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'half', 2, self.order)
            self.di.update({'coursegroup': self._coursegroup})
            xc50_2 = XmlCreator(self.di, self.file50_2)
            xc50_2.makecoursestarts(2, 50, self.customer)
            xc50_2.writetofile()
            self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'quart', 2, self.order)
            self.di.update({'coursegroup': self._coursegroup})
            xc25_2 = XmlCreator(self.di, self.file25_2)
            xc25_2.makecoursestarts(2, 25, self.customer)
            xc25_2.writetofile()
        if self.hasthird:
            self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'full', 3, self.order)
            self.di.update({'coursegroup': self._coursegroup})
            xc100_3 = XmlCreator(self.di, self.file100_3)
            xc100_3.makecoursestarts(3, 100, self.customer)
            xc100_3.writetofile()
            self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'half', 3, self.order)
            self.di.update({'coursegroup': self._coursegroup})
            xc50_3 = XmlCreator(self.di, self.file50_3)
            xc50_3.makecoursestarts(3, 50, self.customer)
            xc50_3.writetofile()
            self._coursegroup = self.buildcoursegroup(obj, '*ccabb*', 'quart', 3, self.order)
            self.di.update({'coursegroup': self._coursegroup})
            xc25_3 = XmlCreator(self.di, self.file25_3)
            xc25_3.makecoursestarts(3, 25, self.customer)
            xc25_3.writetofile()
        subprocess.Popen('explorer ' + self.pathname)


