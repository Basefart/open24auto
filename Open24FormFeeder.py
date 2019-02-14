import wx
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, os.path
from xml.etree import ElementTree as ET
import locale
import threading
import io

class FormFeeder:

    def __init__(self, parent, file, browser, revs, dry, wait, savemode):
        self.file = file
        self.parent = parent
        self.wfile = ''
        file, suffix = os.path.basename(self.file).split('.')
        dir = os.path.dirname(self.file)
        if file[-1] == 'R':
            self.wfile = dir + '\\' + file[:-1] + 'W.' + suffix
        self.cStarts = open(self.file, 'rb')
        self.starttree = ET.parse(self.cStarts)
        self.root = self.starttree.getroot()
        if len(self.wfile) > 5:
            self.cWStarts = open(self.wfile, 'rb+')
            self.writetree = ET.parse(self.cWStarts)
            self.wroot = self.writetree.getroot()
        self.xcount = len(self.root.findall('CourseStart'))
        self.ready = False
        if browser == 'Google Chrome':
            self.driver = webdriver.Chrome(service_args=["--log-path=chrome.log"])
        elif browser == 'Mozilla Firefox':
            self.driver = webdriver.Firefox()
        self.revs = revs
        self.dry = dry
        self.wait = wait
        self.savemode = savemode

    def readysteadygo(self, lookfor, delay):
        time.sleep(delay)
        element = False
        timeout = time.time() + 20
        while element == False:
            element = self.driver.find_element_by_id(lookfor)
            if time.time() > timeout:
                self.driver.quit()
        time.sleep(delay)
        return True


    def open24Entrypage(self, url):
        self.starturl = url
        self.driver.get(self.starturl)

    def thread_start(self):
        th = threading.Thread(target=self.prepareFeeder)
        th.start()


    def prepareFeeder(self):
        try:
            element = self.driver.find_element_by_id('btnSaveAndNew')
        except NoSuchElementException:
            dial = wx.MessageDialog(None, 'Är du på rätt sida?', 'Info', wx.OK)
            dial.ShowModal()
            return
        except NoSuchWindowException:
            dial = wx.MessageDialog(None, 'Börja med att klicka på Öppna!', 'Info', wx.OK)
            dial.ShowModal()
            return
        self.workurl = self.driver.current_url
        self.slcdict = {}
        self.chkdict = {}
        self.datedict = {}
        self.textdict = {}
        self.fedlist = []
        i = 0
        j = self.parent.done
        for cStart in self.root.findall('CourseStart'):
            if self.wfile:
                self.wtree = self.wroot.findall('CourseStart')
            exists = os.path.isfile('./sessiondir/CONTINUE')
            if exists == False:
                dial = wx.MessageDialog(None, 'Du har valt att avbryta! Programmet kommer att avslutas.', 'Info', wx.OK)
                dial.ShowModal()
                self.cStarts.close()
                self.writeFeds()
                open('./sessiondir/ADJÖ', 'w')
                return
            if cStart.find('Fed').text == 'false':
                self.slcdict.update({'slcPeriod': cStart.find('Period').text, 'slcSchool': cStart.find('School').text, 'slcCourseCode':
                    cStart.find('Name').text, 'slcExtensExportDay': cStart.find('ExtensExportDay').text})
                flexBool = eval(cStart.find('Flex').text[:1].upper() + cStart.find('Flex').text[1:])
                distanceBool = eval(cStart.find('Distance').text[:1].upper() + cStart.find('Distance').text[1:])
                self.chkdict.update({'chkFlex': flexBool, 'chkDistance': distanceBool})
                self.datedict.update({'txtStartDate': cStart.find('StartDate').text, 'txtEndDate': cStart.find('EndDate').text})
                self.textdict.update({'txtCourseGroup': cStart.find('CourseGroup').text,'txtWeeks': cStart.find('Weeks').text, 'txtStudyPoints':
                    cStart.find('Points').text, 'txtComment': cStart.find('Comment').text, 'txtInfoHeadline': cStart.find('Header').text,
                                             'txtCourseStartInfo': cStart.find('Startinfo').text, 'txtDaysComment': cStart.find('Studyhours').text})
                self.newtextdict = {}
                self.newslcdict = {}
                self.newchkdict = {}
                self.newdatedict = {}
                for k, v in self.textdict.items():
                    if v != None:
                        self.newtextdict.update({k: v})
                for k, v in self.slcdict.items():
                    if v != None:
                        self.newslcdict.update({k: v})
                for k, v in self.chkdict.items():
                    if v != None:
                        self.newchkdict.update({k: v})
                for k, v in self.datedict.items():
                    if v != None:
                        self.newdatedict.update({k: v})
                self.chooseSelect(self.newslcdict)
                self.boxCheck(self.newchkdict)
                self.textDate(self.newdatedict)
                self.textText(self.newtextdict)
                self.csSubmit(self.dry)
                if hasattr(self, 'wtree'):
                    for child in self.wtree[j]:
                        if child.tag == 'Fed':
                            child.text = 'true'
                            thisroot = self.writetree.getroot()
                            thisroot.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
                            self.writetree.write(self.wfile, encoding="utf-8", method="xml")
                            line = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                            with io.open(self.wfile, 'r+', encoding='utf8') as f:
                                file_data = f.read()
                                f.seek(0, 0)
                                f.write(line.rstrip('\r\n') + '\n' + file_data)
                fedcourse = self.newtextdict['txtCourseGroup']
                open("./sessiondir/" + fedcourse, 'w')
                if not self.dry:
                    self.fedlist.append(str(fedcourse))
                i += 1
                j += 1
                if i >= self.revs:
                    self.cStarts.close()
                    self.writeFeds()
                    os.remove('./sessiondir/CONTINUE')
                    open('./sessiondir/ADJÖ', 'w')
                    return
        #release xml and write true to Fed
        self.cStarts.close()
        self.writeFeds()

    #För varje funktion ska jag se till att väntetiden är optimal.
    def writeFeds(self):
        self.starttree = ET.parse(self.file)
        self.root = self.starttree.getroot()
        for fed in self.fedlist:
            for self.start in self.root.findall('CourseStart'):
                self.fednode = self.start.find('CourseGroup').text
                if self.fednode == fed:
                    self.start.find('Fed').text = 'true'
                    self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
                    self.starttree.write(self.file, encoding="utf-8", method="xml")
                    line = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    with io.open(self.file, 'r+', encoding='utf8') as f:
                        file_data = f.read()
                        f.seek(0, 0)
                        f.write(line.rstrip('\r\n') + '\n' + file_data)

    #Jag har valt helt fel sätt att gå vidare när jag har samma värde.
    def chooseSelect(self, dictionary):
        try:
            for k, v in dictionary.items():
                slc = Select(self.driver.find_element_by_id(k))
                if slc.first_selected_option == v and k != 'slcCourseCode':
                    continue
                else:
                    ready = self.readysteadygo('btnSaveAndNew', 0.5 * self.wait)
                    if ready:
                        slc.select_by_visible_text(v)
        except (NoSuchWindowException, WebDriverException):
            return

    def boxCheck(self, dictionary):
        try:
            for k, v in dictionary.items():
                chk = self.driver.find_element_by_id(k)
                if chk.is_selected() and v:
                    continue
                elif not chk.is_selected() and v:
                    ready = self.readysteadygo('btnSaveAndNew', 0.5 * self.wait)
                    if ready:
                        chk.click()
        except (NoSuchWindowException, WebDriverException):
            return

    def textDate(self, dictionary):
        try:
            for k, v in dictionary.items():
                dateT = self.driver.find_element_by_id(k)
                if dateT.get_attribute('value') == v:
                    continue
                else:
                    ready = self.readysteadygo('btnSaveAndNew', 0.5 * self.wait)
                    if ready:
                        dateT.clear()
                        dateT.send_keys(v)
                        outside = self.driver.find_element_by_id('spTitle')
                        outside.click()
        except (NoSuchWindowException, WebDriverException):
            return

    def textText(self, dictionary):
        #print(dictionary.items())
        try:
            for k, v in dictionary.items():
                #print(k, v)
                txt = self.driver.find_element_by_id(k)
                if txt.get_attribute('value') == v:
                    continue
                else:
                    ready = self.readysteadygo('btnSaveAndNew', 0.5 * self.wait)
                    if ready:
                        txt.clear()
                        txt.send_keys(v)
        except (NoSuchWindowException, WebDriverException):
            return

    def csSubmit(self, dry):
        if not dry:
            ready = self.readysteadygo('btnSaveAndNew', 0.5 * self.wait)
            if ready:
                submitButtons = ['btnSaveAndNew', 'btnSaveAndCopy']
                btnSave = self.driver.find_element_by_id(submitButtons[self.savemode])
                btnSave.click()
                alertText = ['Vill du spara kursen?', 'Vill du spara kursen och kopiera all data till en ny?']
                try:
                    WebDriverWait(self.driver, 3).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    if alert.text == alertText[self.savemode]:
                        alert.accept()
                    else:
                        print("other alert")
                except TimeoutException:
                    pass
        else:
            ready = self.readysteadygo('btnSaveAndNew', 0.5 * self.wait)
            if ready:
                dirtime = time.strftime('%Y-%m-%d', time.localtime())
                filetime = time.strftime('%H.%M.%S', time.localtime())
                dir = './screendumps_' + dirtime + '/'
                exists = os.path.isdir(dir)
                if not exists:
                    os.makedirs(dir)
                saveTo = dir + filetime + ".png"
                result = self.driver.get_screenshot_as_file(saveTo)
                self.driver.get(self.workurl)

