# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Mar 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.locale
import locale
from Open24Utility import Open24Utility
from Open24FormFeeder import FormFeeder
import os, shutil, time
import os.path
from xml.etree import ElementTree as ET
import threading

locale.setlocale(locale.LC_ALL, '')
locale.setlocale(locale.LC_ALL, 'swedish')

###########################################################################
## Class open24Frame
###########################################################################

class open24Frame(wx.Frame):


    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Open24 v.5", pos=wx.DefaultPosition, size=wx.Size(800, 750),
                          style=wx.DEFAULT_FRAME_STYLE | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)
        if os.path.isdir('sessiondir'):
            shutil.rmtree('sessiondir')
        os.makedirs('./sessiondir/')
        open('./sessiondir/CONTINUE', 'w')
        self.locale = wx.Locale(wx.LANGUAGE_SWEDISH)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menubar1.Append(self.m_menu1, u"&Arkiv")
        self.help = self.m_menu1.Append(wx.ID_ANY, '&Hjälp', 'HJälp', kind=wx.ITEM_NORMAL)
        self.exit = self.m_menu1.Append(wx.ID_ANY, 'Av&sluta', 'Avsluta', kind=wx.ITEM_NORMAL)

        self.SetMenuBar(self.m_menubar1)

        self.m_toolBar1 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.m_toolBar1.SetToolSeparation(20)
        self.m_toolBar1.AddSeparator()

        customerSelectChoices = [u"Välj kund", u"Botkyrka", u"Ekerö", u"Nacka", u"Stockholm"]
        self.customerSelect = wx.ComboBox(self.m_toolBar1, wx.ID_ANY, u"Välj kund", wx.DefaultPosition, wx.DefaultSize, customerSelectChoices, 0)
        self.customerSelect.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.customerSelect.SetToolTip(u'Botkyrka, Ekerö, Nacka, Stockholm')

        self.m_toolBar1.AddControl(self.customerSelect)
        self.m_toolBar1.AddSeparator()

        self.courseitemsTool = self.m_toolBar1.AddTool(wx.ID_ANY, u"xmlPageLink", wx.Bitmap(u"./xml.png", wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_RADIO, u"Vilka saker ska fyllas i?",
                                                            u"Här ska du ange vilka saker som ska fyllas i för denna kund. Allt utom kursgrupp som vi gör i nästa steg.",
                                                            None)


        self.coursegroupTool = self.m_toolBar1.AddTool(wx.ID_ANY, u"courseGroupLink", wx.Bitmap(u"./group.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_RADIO, u"Hur ska kursgrupp se ut?",
                                                            u"Här ska du ange vad kursgrupp ska innehålla och i vilken ordning delarna ska skrivas",
                                                            None)

        self.formfeedTool = self.m_toolBar1.AddTool(wx.ID_ANY, u"formFeedLink", wx.Bitmap(u"./form.png", wx.BITMAP_TYPE_ANY),
                                                         wx.NullBitmap, wx.ITEM_RADIO, u"Fyll i formulär!",
                                                         u"Här ska du välja den fil du har genererat, nu eller tidigare och sedan välja webbläsare, kund etc. Och sedan börja inmatningen.",
                                                         None)

        self.m_toolBar1.AddSeparator()

        self.start1Date = wx.adv.DatePickerCtrl(self.m_toolBar1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY)
        self.start1Date.SetToolTip(u'Första starten.')
        self.m_toolBar1.AddControl(self.start1Date)
        self.m_toolBar1.AddSeparator()

        self.m_toolBar1.AddSeparator()

        self.start2Check = wx.CheckBox(self.m_toolBar1, wx.ID_ANY, u"Start 2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.start2Check.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.start2Check.SetToolTip(u'Ska det vara en andra start?')

        self.m_toolBar1.AddControl(self.start2Check)
        self.start2Date = wx.adv.DatePickerCtrl(self.m_toolBar1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY)
        self.start2Date.Enable(False)
        self.start2Date.SetToolTip(u'Andra starten.')

        self.m_toolBar1.AddControl(self.start2Date)
        self.m_toolBar1.AddSeparator()

        self.start3Check = wx.CheckBox(self.m_toolBar1, wx.ID_ANY, u"Start 3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.start3Check.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.start3Check.Enable(False)
        self.start3Check.SetToolTip(u'Ska det vara en tredje start?')

        self.m_toolBar1.AddControl(self.start3Check)
        self.start3Date = wx.adv.DatePickerCtrl(self.m_toolBar1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY)
        self.start3Date.Enable(False)
        self.start3Date.SetToolTip(u'Tredje starten')

        self.m_toolBar1.AddControl(self.start3Date)

        self.m_toolBar1.AddSeparator()
        
        self.customerURL = self.m_toolBar1.AddTool(wx.ID_ANY, u"Kundens internetadress", wx.Bitmap(u"./web.png", wx.BITMAP_TYPE_ANY),
                                                        wx.NullBitmap, wx.ITEM_NORMAL, u"Kundens internetadress",
                                                        u"Öppnar kundens internetadress i datorns standardwebbläsare.", None)

        self.stopButton = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool", wx.Bitmap(u"./stop.png", wx.BITMAP_TYPE_ANY),
                                                 wx.NullBitmap,
                                                 wx.ITEM_NORMAL, u"STOPP!", wx.EmptyString, None)

        self.m_toolBar1.Realize()

        self.open24StatusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.mainSizer.SetMinSize(wx.Size(750, 550))
#
#       Här börjar kursdetaljer
#
        self.courseItemsSizer = wx.BoxSizer(wx.VERTICAL)

        self.courseItemsSizer.SetMinSize(wx.Size(750, 550))
        sbSizerCI = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Vilka värden vill kunden ha inmatade?"), wx.VERTICAL)

        sbSizerCI.SetMinSize(wx.Size(750, 550))
        self.courseItemsLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY,
                                              u"Här ska du skriva in generella värden kunden vill ha för denna inmatning. Viktigt att det blir rätt. Kursgrupp tar vi i nästa steg.",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.courseItemsLabel.Wrap(-1)
        self.courseItemsLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        sbSizerCI.Add(self.courseItemsLabel, 0, wx.ALL, 5)

        fgSizerCI = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizerCI.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizerCI.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.selectInputLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Flervalslistor", wx.DefaultPosition, wx.DefaultSize, 0)
        self.selectInputLabel.Wrap(-1)
        self.selectInputLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.selectInputLabel, 0, wx.ALIGN_TOP | wx.ALL, 5)

        self.placeHolder0 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder0.Wrap(-1)
        fgSizerCI.Add(self.placeHolder0, 0, wx.ALL, 5)

        self.placeHolder1 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder1.Wrap(-1)
        fgSizerCI.Add(self.placeHolder1, 0, wx.ALL, 5)

        self.placeHolder2 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder2.Wrap(-1)
        fgSizerCI.Add(self.placeHolder2, 0, wx.ALL, 5)

        self.yearAndPeriodLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Hur anger kunden år, period och start?", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.yearAndPeriodLabel.Wrap(-1)
        self.yearAndPeriodLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.yearAndPeriodLabel, 0, wx.ALL, 5)

        self.yearAndPeriodInput = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), 0)
        self.yearAndPeriodInput.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.yearAndPeriodInput.SetToolTip(u'En flervalslista. Högt upp på sidan. Skrivs lite olika; 2018_3, 2018_3:2')

        fgSizerCI.Add(self.yearAndPeriodInput, 0, wx.ALL, 5)

        self.schoolNameLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Hur benämns NTI-skolan?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.schoolNameLabel.Wrap(-1)
        self.schoolNameLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.schoolNameLabel, 0, wx.ALL, 5)

        self.schoolNameInput = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1), 0)
        self.schoolNameInput.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.schoolNameInput.SetToolTip(u'En flervalslista med olika namn för NTI-skolan. Vanligast är "NTI-skolan AB".')

        fgSizerCI.Add(self.schoolNameInput, 0, wx.ALL, 5)

        self.studyFormLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Hur anges dessa kursers studieform?", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.studyFormLabel.Wrap(-1)
        self.studyFormLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.studyFormLabel, 0, wx.ALL, 5)

        self.studyFormInput = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(75, -1), 0)
        self.studyFormInput.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.studyFormInput.SetToolTip(u'En flervalslista. Distans, Flex eller något annat')

        fgSizerCI.Add(self.studyFormInput, 0, wx.ALL, 5)

        self.placeHolder3 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder3.Wrap(-1)
        fgSizerCI.Add(self.placeHolder3, 0, wx.ALL, 5)

        self.placeHolder4 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder4.Wrap(-1)
        fgSizerCI.Add(self.placeHolder4, 0, wx.ALL, 5)

        self.checkBoxInputLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Kryssrutor", wx.DefaultPosition, wx.DefaultSize, 0)
        self.checkBoxInputLabel.Wrap(-1)
        self.checkBoxInputLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.checkBoxInputLabel, 0, wx.ALL, 5)

        self.placeHolder5 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder5.Wrap(-1)
        fgSizerCI.Add(self.placeHolder5, 0, wx.ALL, 5)

        self.placeHolder6 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder6.Wrap(-1)
        fgSizerCI.Add(self.placeHolder6, 0, wx.ALL, 5)

        self.placeHolder7 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder7.Wrap(-1)
        fgSizerCI.Add(self.placeHolder7, 0, wx.ALL, 5)

        self.studyFormChkLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Vilken av dessa kryssrutor ska kryssas i?", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.studyFormChkLabel.Wrap(-1)
        self.studyFormChkLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.studyFormChkLabel, 0, wx.ALL, 5)

        self.flexRadio = wx.RadioButton(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Flexkurs", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        self.flexRadio.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.flexRadio, 0, wx.ALL, 5)

        self.distanceRadio = wx.RadioButton(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Distanskurs", wx.DefaultPosition, wx.DefaultSize, 0)
        self.distanceRadio.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCI.Add(self.distanceRadio, 0, wx.ALL, 5)

        self.placeHolder8 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder8.Wrap(-1)
        fgSizerCI.Add(self.placeHolder8, 0, wx.ALL, 5)

        sbSizerCI.Add(fgSizerCI, 1, wx.ALIGN_TOP | wx.ALL | wx.FIXED_MINSIZE, 5)

        fgSizerCIComment = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizerCIComment.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizerCIComment.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizerCIComment.SetMinSize(wx.Size(750, 100))
        self.commentInputLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Kommentarer (skriv Heltid)", wx.Point(0, 0), wx.DefaultSize, 0)
        self.commentInputLabel.Wrap(-1)
        self.commentInputLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.commentInputLabel, 0, wx.ALIGN_TOP | wx.ALL | wx.FIXED_MINSIZE, 5)

        self.placeHolder9 = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeHolder9.Wrap(-1)
        fgSizerCIComment.Add(self.placeHolder9, 0, wx.ALL, 5)

        self.standardCommentLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Standardkommentar: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.standardCommentLabel.Wrap(-1)
        self.standardCommentLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.standardCommentLabel, 0, wx.ALL, 5)

        self.standardComment = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(600, -1), 0)
        self.standardComment.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.standardComment.SetMinSize(wx.Size(520, -1))
        self.standardComment.SetMaxSize(wx.Size(520, -1))
        self.standardComment.SetToolTip(u'Den vanligast förekommande kommentaren. Skriv vid Heltid.')

        fgSizerCIComment.Add(self.standardComment, 0, wx.ALL, 5)

        self.workexpCommentLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Kommentar vid APL:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.workexpCommentLabel.Wrap(-1)
        self.workexpCommentLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.workexpCommentLabel, 0, wx.ALL, 5)

        self.workexpComment = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(600, -1), 0)
        self.workexpComment.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.workexpComment.SetMinSize(wx.Size(520, -1))
        self.workexpComment.SetMaxSize(wx.Size(520, -1))
        self.workexpComment.SetToolTip(u'Samma som standard med tillägget att kursen innehåller APL.')


        fgSizerCIComment.Add(self.workexpComment, 0, wx.ALL, 5)

        self.cprCommentLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Kommentar vid HLR:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.cprCommentLabel.Wrap(-1)
        self.cprCommentLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.cprCommentLabel, 0, wx.ALL, 5)

        self.cprComment = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(600, -1), 0)
        self.cprComment.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.cprComment.SetMinSize(wx.Size(520, -1))
        self.cprComment.SetMaxSize(wx.Size(520, -1))
        self.cprComment.SetToolTip(u'Samma som standard med tillägget att kursen kräver HLR.')

        fgSizerCIComment.Add(self.cprComment, 0, wx.ALL, 5)

        self.labCommentLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Kommentar vid Labb:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labCommentLabel.Wrap(-1)
        self.labCommentLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.labCommentLabel, 0, wx.ALL, 5)

        self.labComment = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(600, -1), 0)
        self.labComment.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.labComment.SetMinSize(wx.Size(520, -1))
        self.labComment.SetMaxSize(wx.Size(520, -1))
        self.labComment.SetToolTip(u'Samma som standard med tillägget att kursen kräver laboration på plats.')

        fgSizerCIComment.Add(self.labComment, 0, wx.ALL, 5)

        self.headerChk = wx.CheckBox(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Ska rubrik fyllas i?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.headerChk.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.headerChk, 0, wx.ALL, 5)

        self.headerText = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        self.headerText.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.headerText.Enable(False)
        self.headerText.SetMinSize(wx.Size(400, -1))
        self.headerText.SetMaxSize(wx.Size(400, -1))
        self.headerText.SetToolTip(u'Om kunden kräver denna ska du kryssa för och skriva vid Heltid eller 100%.')

        fgSizerCIComment.Add(self.headerText, 0, wx.ALL, 5)

        self.weTitleLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Rubrik vid APL:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weTitleLabel.Wrap(-1)
        self.weTitleLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.weTitleLabel, 0, wx.ALL, 5)

        self.headerWEText = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        self.headerWEText.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.headerWEText.Enable(False)
        self.headerWEText.SetMinSize(wx.Size(400, -1))
        self.headerWEText.SetMaxSize(wx.Size(400, -1))
        self.headerWEText.SetToolTip(u'Samma som ovan med APL som tillägg.')

        fgSizerCIComment.Add(self.headerWEText, 0, wx.ALL, 5)

        self.cprTitleLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Rubrik vid HLR:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.cprTitleLabel.Wrap(-1)
        self.cprTitleLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.cprTitleLabel, 0, wx.ALL, 5)

        self.headerCPRText = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        self.headerCPRText.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.headerCPRText.Enable(False)
        self.headerCPRText.SetMinSize(wx.Size(400, -1))
        self.headerCPRText.SetMaxSize(wx.Size(400, -1))
        self.headerCPRText.SetToolTip(u'Samma som ovan med HLR som tillägg.')

        fgSizerCIComment.Add(self.headerCPRText, 0, wx.ALL, 5)

        self.labTitleLabel = wx.StaticText(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Rubrik vid laboration:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labTitleLabel.Wrap(-1)
        self.labTitleLabel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.labTitleLabel, 0, wx.ALL, 5)

        self.headerLabText = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        self.headerLabText.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.headerLabText.Enable(False)
        self.headerLabText.SetMinSize(wx.Size(400, -1))
        self.headerLabText.SetMaxSize(wx.Size(400, -1))
        self.headerLabText.SetToolTip(u'Samma som ovan med laboration som tillägg.')

        fgSizerCIComment.Add(self.headerLabText, 0, wx.ALL, 5)

        self.startInfoChk = wx.CheckBox(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Kursstartsinformation?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.startInfoChk.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.startInfoChk, 0, wx.ALL, 5)

        self.startInfoText = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        self.startInfoText.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.startInfoText.Enable(False)
        self.startInfoText.SetMinSize(wx.Size(400, -1))
        self.startInfoText.SetMaxSize(wx.Size(400, -1))
        self.startInfoText.SetToolTip(u'Om kunden kräver denna ska du kryssa för och skriva om saker som berör kursstart. Inte så vanlig.')

        fgSizerCIComment.Add(self.startInfoText, 0, wx.ALL, 5)

        self.studyHoursChk = wx.CheckBox(sbSizerCI.GetStaticBox(), wx.ID_ANY, u"Dagar och Tider?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.studyHoursChk.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizerCIComment.Add(self.studyHoursChk, 0, wx.ALL, 5)

        self.studyHoursText = wx.TextCtrl(sbSizerCI.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        self.studyHoursText.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.studyHoursText.Enable(False)
        self.studyHoursText.SetMinSize(wx.Size(400, -1))
        self.studyHoursText.SetMaxSize(wx.Size(400, -1))
        self.startInfoText.SetToolTip(u'Om kunden kräver denna ska du kryssa för och skriva om saker som berör studietid. Inte alls vanlig och '
                                      u'framför allt inte vid Distans.')

        fgSizerCIComment.Add(self.studyHoursText, 0, wx.ALL, 5)

        sbSizerCI.Add(fgSizerCIComment, 1, wx.ALIGN_TOP | wx.FIXED_MINSIZE, 5)

        self.courseItemsSizer.Add(sbSizerCI, 1, wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL | wx.FIXED_MINSIZE, 5)

        self.mainSizer.Add(self.courseItemsSizer, 1, wx.EXPAND, 5)
#       Här slutar kursdetaljer
#
#       Här börjar kursgruppsredigering
        self.courseGroupSizer = wx.BoxSizer(wx.VERTICAL)

        self.courseGroupSizer.SetMinSize(wx.Size(750, 550))
        sbSizerCG = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Hur vill kunden att kursgrupp skrivs?"), wx.VERTICAL)

        sbSizerCG.SetMinSize(wx.Size(750, 550))
        self.courseItemsLabel1 = wx.StaticText(sbSizerCG.GetStaticBox(), wx.ID_ANY,
                                               u"Här ska du bestämma vilka värden som ska finnas med i kursgrupp och i vilken ordning de ska förekomma.",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.courseItemsLabel1.Wrap(-1)
        self.courseItemsLabel1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        sbSizerCG.Add(self.courseItemsLabel1, 0, wx.ALL, 5)

        fgSizerCG = wx.FlexGridSizer(0, 2, 15, 15)
        fgSizerCG.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizerCG.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizerCG.SetMinSize(wx.Size(750, 550))
        bSizerCGItems = wx.BoxSizer(wx.VERTICAL)

        sbSizerCGItems = wx.StaticBoxSizer(wx.StaticBox(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"År och period i kursgrupp"), wx.HORIZONTAL)

        self.staticTextCGYear = wx.StaticText(sbSizerCGItems.GetStaticBox(), wx.ID_ANY, u"År i kursgrupp: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextCGYear.Wrap(-1)
        self.staticTextCGYear.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerCGItems.Add(self.staticTextCGYear, 0, wx.ALL, 5)

        self.textCtrlCGYear = wx.TextCtrl(sbSizerCGItems.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, -1), 0)
        self.textCtrlCGYear.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerCGItems.Add(self.textCtrlCGYear, 0, wx.ALL, 5)

        self.staticTextCGPeriod = wx.StaticText(sbSizerCGItems.GetStaticBox(), wx.ID_ANY, u"Period i kursgrupp: ", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.staticTextCGPeriod.Wrap(-1)
        self.staticTextCGPeriod.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerCGItems.Add(self.staticTextCGPeriod, 0, wx.ALL, 5)

        self.textCtrlCGPeriod = wx.TextCtrl(sbSizerCGItems.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        self.textCtrlCGPeriod.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerCGItems.Add(self.textCtrlCGPeriod, 0, wx.ALL, 5)

        bSizerCGItems.Add(sbSizerCGItems, 1, wx.EXPAND, 5)

        sbSizerNTIChars = wx.StaticBoxSizer(wx.StaticBox(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"NTI:s namn i kursgrupp och studieform"),
                                            wx.HORIZONTAL)

        self.staticTextNTIChars = wx.StaticText(sbSizerNTIChars.GetStaticBox(), wx.ID_ANY, u"NTI i kursgrupp: ", wx.DefaultPosition, wx.DefaultSize,
                                                0)
        self.staticTextNTIChars.Wrap(-1)
        self.staticTextNTIChars.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerNTIChars.Add(self.staticTextNTIChars, 0, wx.ALL, 5)

        self.textCtrlNTI = wx.TextCtrl(sbSizerNTIChars.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1), 0)
        self.textCtrlNTI.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerNTIChars.Add(self.textCtrlNTI, 0, wx.ALL, 5)

        self.staticTextStudyForm = wx.StaticText(sbSizerNTIChars.GetStaticBox(), wx.ID_ANY, u"Studieform i kursgrupp: ", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.staticTextStudyForm.Wrap(-1)
        self.staticTextStudyForm.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerNTIChars.Add(self.staticTextStudyForm, 0, wx.ALL, 5)

        self.textCtrlStudyForm = wx.TextCtrl(sbSizerNTIChars.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        sbSizerNTIChars.Add(self.textCtrlStudyForm, 0, wx.ALL, 5)

        bSizerCGItems.Add(sbSizerNTIChars, 1, wx.EXPAND, 5)

        sbSizerPace = wx.StaticBoxSizer(wx.StaticBox(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"Så markeras de olika kurstakterna i kursgrupp"),
                                        wx.HORIZONTAL)

        self.staticText100 = wx.StaticText(sbSizerPace.GetStaticBox(), wx.ID_ANY, u"100 %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText100.Wrap(-1)
        self.staticText100.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerPace.Add(self.staticText100, 0, wx.ALL, 5)

        self.textCtrl100 = wx.TextCtrl(sbSizerPace.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        self.textCtrl100.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerPace.Add(self.textCtrl100, 0, wx.ALL, 5)

        self.staticText50 = wx.StaticText(sbSizerPace.GetStaticBox(), wx.ID_ANY, u"50 %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText50.Wrap(-1)
        self.staticText50.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerPace.Add(self.staticText50, 0, wx.ALL, 5)

        self.textCtrl50 = wx.TextCtrl(sbSizerPace.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        self.textCtrl50.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerPace.Add(self.textCtrl50, 0, wx.ALL, 5)

        self.staticText25 = wx.StaticText(sbSizerPace.GetStaticBox(), wx.ID_ANY, u"25 %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText25.Wrap(-1)
        self.staticText25.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerPace.Add(self.staticText25, 0, wx.ALL, 5)

        self.textCtrl25 = wx.TextCtrl(sbSizerPace.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        self.textCtrl25.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerPace.Add(self.textCtrl25, 0, wx.ALL, 5)

        bSizerCGItems.Add(sbSizerPace, 1, wx.EXPAND, 5)

        sbSizerStart = wx.StaticBoxSizer(wx.StaticBox(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"Så markeras start i kursgrupp"), wx.HORIZONTAL)

        self.staticTextStartMarker1 = wx.StaticText(sbSizerStart.GetStaticBox(), wx.ID_ANY, u"Start 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextStartMarker1.Wrap(-1)
        sbSizerStart.Add(self.staticTextStartMarker1, 0, wx.ALL, 5)

        self.textCtrlStartMarker1 = wx.TextCtrl(sbSizerStart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        self.textCtrlStartMarker1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        sbSizerStart.Add(self.textCtrlStartMarker1, 0, wx.ALL, 5)

        self.staticTextStartMarker2 = wx.StaticText(sbSizerStart.GetStaticBox(), wx.ID_ANY, u"Start 2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextStartMarker2.Wrap(-1)
        sbSizerStart.Add(self.staticTextStartMarker2, 0, wx.ALL, 5)

        self.textCtrlStartMarker2 = wx.TextCtrl(sbSizerStart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        self.textCtrlStartMarker2.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.textCtrlStartMarker2.Enable(False)

        sbSizerStart.Add(self.textCtrlStartMarker2, 0, wx.ALL, 5)

        self.staticTextStartMarker3 = wx.StaticText(sbSizerStart.GetStaticBox(), wx.ID_ANY, u"Start 3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextStartMarker3.Wrap(-1)
        sbSizerStart.Add(self.staticTextStartMarker3, 0, wx.ALL, 5)

        self.textCtrlStartMarker3 = wx.TextCtrl(sbSizerStart.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        self.textCtrlStartMarker3.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.textCtrlStartMarker3.Enable(False)

        sbSizerStart.Add(self.textCtrlStartMarker3, 0, wx.ALL, 5)

        bSizerCGItems.Add(sbSizerStart, 1, wx.EXPAND, 5)

        fgSizerCG.Add(bSizerCGItems, 1, wx.EXPAND, 5)

        bSizerCGOrder = wx.BoxSizer(wx.VERTICAL)

        sbSizerCGOrder = wx.StaticBoxSizer(wx.StaticBox(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"Förekomst och ordning i kursgrupp"), wx.VERTICAL)

        self.ORDER = [0, 1, 2, 3, 4, 5, 6]
        self.ITEMS = ["Skola", "År", "Period", "Kurskod (förkortad)", "Studieform", "Startmarkör", "Takt" ]

        self.coursegroupSort = wx.RearrangeCtrl(sbSizerCGOrder.GetStaticBox(), id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(300,-1),
                                                order=self.ORDER,
                                                items=self.ITEMS, validator=wx.DefaultValidator, name="Kursgruppens byggstenar")
        self.coursegroupSort.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.coursegroupSort.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))
        self.coursegroupSort.SetMinSize(wx.Size(300, -1))
        self.coursegroupSort.SetMaxSize(wx.Size(300, -1))

        sbSizerCGOrder.Add(self.coursegroupSort, 0, wx.ALIGN_TOP | wx.ALIGN_RIGHT | wx.ALL, 10)

        bSizerCGOrder.Add(sbSizerCGOrder, 1, wx.ALIGN_RIGHT | wx.EXPAND, 5)

        fgSizerCG.Add(bSizerCGOrder, 1, wx.EXPAND, 5)

        sbSizerCG.Add(fgSizerCG, 1, wx.EXPAND, 5)

        self.courseGroupSizer.Add(sbSizerCG, 1, wx.ALIGN_CENTER | wx.ALL | wx.FIXED_MINSIZE, 5)

        bSizerCGExample1 = wx.BoxSizer(wx.VERTICAL)

        bSizerCGExample1.SetMinSize(wx.Size(-1, 40))
        sbSizerCGExample1 = wx.StaticBoxSizer(wx.StaticBox(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"Välj kurs för att se exempel"), wx.VERTICAL)

        sbSizerCGExample1.SetMinSize(wx.Size(-1, 40))

        self.comboBoxCourseSelectChoices = ['Välj kurs!']
        self.comboBoxCourseSelect = wx.ComboBox(sbSizerCGExample1.GetStaticBox(), wx.ID_ANY, u"Välj kurs!", wx.DefaultPosition, wx.Size(220, -1),
                                                self.comboBoxCourseSelectChoices, 0)
        self.comboBoxCourseSelect.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.comboBoxCourseSelect.SetMinSize(wx.Size(220, -1))
        self.comboBoxCourseSelect.SetMaxSize(wx.Size(220, -1))

        sbSizerCGExample1.Add(self.comboBoxCourseSelect, 0, wx.ALL, 5)

        bSizerCGExample1.Add(sbSizerCGExample1, 1, wx.EXPAND | wx.FIXED_MINSIZE, 5)

        bSizerCGExample1.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizerCG.Add(bSizerCGExample1, 1, wx.EXPAND, 5)

        bSizerCGExample2 = wx.BoxSizer(wx.VERTICAL)

        bSizerCGExample2.SetMinSize(wx.Size(-1, 40))
        sbSizerCGExample2 = wx.StaticBoxSizer(wx.StaticBox(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"Exempel på kursgrupp"), wx.VERTICAL)

        self.textCtrlCGExample = wx.TextCtrl(sbSizerCGExample2.GetStaticBox(), wx.ID_ANY, u"NT184ADM01DA00", wx.DefaultPosition, wx.Size(280, 30), 0)
        self.textCtrlCGExample.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.textCtrlCGExample.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVEBORDER))
        self.textCtrlCGExample.Enable(False)
        self.textCtrlCGExample.SetMinSize(wx.Size(280, 30))
        self.textCtrlCGExample.SetMaxSize(wx.Size(280, 30))

        sbSizerCGExample2.Add(self.textCtrlCGExample, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        bSizerCGExample2.Add(sbSizerCGExample2, 1, wx.EXPAND, 5)

        bSizerCGExample2.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizerCG.Add(bSizerCGExample2, 1, wx.EXPAND, 5)
        self.buttonSaveXML = wx.Button(sbSizerCG.GetStaticBox(), wx.ID_ANY, u"Spara", wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonSaveXML.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        sbSizerCG.Add(self.buttonSaveXML, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.mainSizer.Add(self.courseGroupSizer, 1, wx.EXPAND, 5)
        self.mainSizer.Hide(self.courseGroupSizer, recursive=True)
#       Här slutar kursgruppredigering
#
#       Här börjar inmatningssidan
        self.formFeedSizer = wx.BoxSizer(wx.VERTICAL)

        sbSizerFF = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Inmatning i Open24"), wx.VERTICAL)

        sbSizerFF.SetMinSize(wx.Size(750, 550))
        gbSizerFF = wx.GridBagSizer(2, 2)
        gbSizerFF.SetFlexibleDirection(wx.BOTH)
        gbSizerFF.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        browserSelectChoices = [u"Välj webbläsare!", u"Google Chrome", u"Mozilla Firefox"]
        self.browserSelect = wx.ComboBox(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Välj webbläsare!", wx.DefaultPosition, wx.Size(160, -1),
                                         browserSelectChoices, 0)
        self.browserSelect.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.browserSelect.SetMinSize(wx.Size(140, -1))
        self.browserSelect.SetMaxSize(wx.Size(140, -1))

        gbSizerFF.Add(self.browserSelect, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.shrinkBox = wx.BoxSizer(wx.HORIZONTAL)

        self.filePickerXML = wx.FilePickerCtrl(sbSizerFF.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Välj fil!", u"*.xml", wx.DefaultPosition,
                                               wx.Size(60, -1))
        self.filePickerXML.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.filePickerXML.SetMinSize(wx.Size(70, -1))
        self.filePickerXML.SetMaxSize(wx.Size(70, -1))

        self.shrinkBox.Add(self.filePickerXML, 0, wx.ALL, 5)

        self.selectedFile = wx.TextCtrl(sbSizerFF.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), 0)
        self.selectedFile.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.selectedFile.SetBackgroundColour((255, 204, 51))
        self.selectedFile.Enable(False)
        self.selectedFile.SetMinSize(wx.Size(230, -1))
        self.selectedFile.SetMaxSize(wx.Size(230, -1))

        gbSizerFF.Add(self.selectedFile, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.chkTestSite = wx.CheckBox(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Testsajt", wx.DefaultPosition, wx.DefaultSize, 0)
        self.chkTestSite.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        self.shrinkBox.Add(self.chkTestSite, 0, wx.ALL, 5)

        self.chkDryRun = wx.CheckBox(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Testkörning", wx.DefaultPosition, wx.DefaultSize, 0)
        self.chkDryRun.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        self.shrinkBox.Add(self.chkDryRun, 0, wx.ALL, 5)

        gbSizerFF.Add(self.shrinkBox, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.placeholder102 = wx.StaticText(sbSizerFF.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.placeholder102.Wrap(-1)
        gbSizerFF.Add(self.placeholder102, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.textCtrlCURL = wx.TextCtrl(sbSizerFF.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(750, 60), wx.TE_MULTILINE)
        self.textCtrlCURL.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.textCtrlCURL.SetBackgroundColour((255, 204, 51))
        self.textCtrlCURL.SetMinSize(wx.Size(750, 60))
        self.textCtrlCURL.SetMaxSize(wx.Size(750, 60))

        gbSizerFF.Add(self.textCtrlCURL, wx.GBPosition(1, 0), wx.GBSpan(1, 4), wx.ALL, 5)

        self.btnStartFF = wx.Button(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Öppna", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizerFF.Add(self.btnStartFF, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        squaresizer = wx.BoxSizer(wx.VERTICAL)

        saveNewCopy = wx.BoxSizer(wx.HORIZONTAL)

        newOrCopyChoices = [u"Spara / Ny", u"Spara / Kopiera"]
        self.newOrCopy = wx.RadioBox(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Val av spara-knapp", wx.DefaultPosition, wx.DefaultSize,
                                     newOrCopyChoices, 2,
                                     wx.RA_SPECIFY_COLS)
        self.newOrCopy.SetSelection(0)
        saveNewCopy.Add(self.newOrCopy, 0, wx.ALL, 5)
        squaresizer.Add(saveNewCopy, 0, wx.ALL, 5)

        startAndSpeed = wx.BoxSizer(wx.HORIZONTAL)

        self.speedSlider = wx.Slider(sbSizerFF.GetStaticBox(), wx.ID_ANY, 10, 1, 10, wx.DefaultPosition, wx.DefaultSize,
                                     wx.SL_HORIZONTAL | wx.SL_INVERSE | wx.SL_LABELS)
        self.speedSlider.SetToolTip(u'Här ställer du in fördröjningen')
        startAndSpeed.Add(self.speedSlider, 0, wx.ALL, 5)
        self.btnStartProcess = wx.Button(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Börja", wx.DefaultPosition, wx.DefaultSize, 0)
        startAndSpeed.Add(self.btnStartProcess, 0, wx.ALL, 5)

        squaresizer.Add(startAndSpeed, 0, wx.ALL, 5)
        gbSizerFF.Add(squaresizer, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.fedCourses = wx.TextCtrl(sbSizerFF.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200,200), wx.TE_MULTILINE)
        self.fedCourses.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.fedCourses.Enable(True)
        self.fedCourses.SetMinSize(wx.Size(200, 200))
        self.fedCourses.SetMaxSize(wx.Size(200, 200))

        gbSizerFF.Add(self.fedCourses, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        progressBox = wx.BoxSizer(wx.VERTICAL)

        progressBox.SetMinSize(wx.Size(50, 80))
        undoneStatBox = wx.StaticBoxSizer(wx.StaticBox(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Att mata in"),
                                          wx.VERTICAL)

        undoneStatBox.SetMinSize(wx.Size(60, 40))
        self.revolutionCtrl = wx.SpinCtrl(undoneStatBox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(75, 30), wx.SP_ARROW_KEYS, 0, 1500, 0)
        self.revolutionCtrl.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.revolutionCtrl.SetMinSize(wx.Size(75, 30))
        self.revolutionCtrl.SetMaxSize(wx.Size(75, 30))

        undoneStatBox.Add(self.revolutionCtrl, 0, wx.ALL, 5)

        progressBox.Add(undoneStatBox, 1, wx.FIXED_MINSIZE, 5)

        doneStatBox = wx.StaticBoxSizer(wx.StaticBox(sbSizerFF.GetStaticBox(), wx.ID_ANY, u"Färdiga"), wx.VERTICAL)

        self.doneTxtCtrl = wx.TextCtrl(doneStatBox.GetStaticBox(), wx.ID_ANY, u'0', wx.DefaultPosition,
                                       wx.Size(75, 30), 0)
        self.doneTxtCtrl.SetFont(
            wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.doneTxtCtrl.Enable(False)
        self.doneTxtCtrl.SetMinSize(wx.Size(75, 30))
        self.doneTxtCtrl.SetMaxSize(wx.Size(75, 30))
        doneStatBox.Add(self.doneTxtCtrl, 0, wx.ALL, 5)

        progressBox.Add(doneStatBox, 1, wx.EXPAND, 5)

        gbSizerFF.Add(progressBox, wx.GBPosition(2, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        gbSizerFF.Add((700, 800), wx.GBPosition(4, 0), wx.GBSpan(1, 4), wx.EXPAND, 5)

        gbSizerFF.AddGrowableCol(4)
        gbSizerFF.AddGrowableRow(1)

        sbSizerFF.Add(gbSizerFF, 1, 0, 5)

        self.formFeedSizer.Add(sbSizerFF, 1, wx.ALIGN_CENTER | wx.ALL | wx.FIXED_MINSIZE, 5)

        self.mainSizer.Add(self.formFeedSizer, 1, wx.EXPAND, 5)
        self.mainSizer.Hide(self.formFeedSizer, recursive=True)

        self.SetSizer(self.mainSizer)
        self.Layout()

        self.Centre(wx.BOTH)
        self.Show(True)

        # Connect Events
        self.customerSelect.Bind(wx.EVT_COMBOBOX, self.setCustomer)
        self.Bind(wx.EVT_MENU, self.OnClicked, self.exit)
        self.Bind(wx.EVT_MENU, self.OnHelp, self.help)
        self.Bind(wx.EVT_TOOL, self.showCourseItemsPage, id=self.courseitemsTool.GetId())
        self.Bind(wx.EVT_TOOL, self.showCourseGroupPage, id=self.coursegroupTool.GetId())
        self.Bind(wx.EVT_TOOL, self.showFormFeedPage, id=self.formfeedTool.GetId())
        self.Bind(wx.EVT_TOOL, self.openCustomerUrl, id=self.customerURL.GetId())
        self.Bind(wx.EVT_TOOL, self.stopExecution, id=self.stopButton.GetId())
        self.start2Check.Bind(wx.EVT_CHECKBOX, self.enablestart2)
        self.start3Check.Bind(wx.EVT_CHECKBOX, self.enablestart3)
        self.headerChk.Bind(wx.EVT_CHECKBOX, self.enableHeaderText)
        self.startInfoChk.Bind(wx.EVT_CHECKBOX, self.enableStartInfo)
        self.studyHoursChk.Bind(wx.EVT_CHECKBOX, self.enableStudyHours)
        self.comboBoxCourseSelect.Bind(wx.EVT_COMBOBOX, self.DisplayCGExample)
        self.buttonSaveXML.Bind(wx.EVT_BUTTON, self.onsaveas)
        self.filePickerXML.Bind(wx.EVT_FILEPICKER_CHANGED, self.stackFile)
        self.btnStartFF.Bind(wx.EVT_BUTTON, self.startFF)
        self.btnStartProcess.Bind(wx.EVT_BUTTON, self.startProcess)
        self.speedSlider.Bind(wx.EVT_SCROLL, self.setSpeed)
        self.newOrCopy.Bind(wx.EVT_RADIOBOX, self.chooseButton)

    def __del__(self):
        pass

    def OnClicked(self, e):
        self.Close()

    def OnHelp(self, e):
        os.system("start Help.pdf")

    def stopExecution(self, event):
        os.remove('./sessiondir/CONTINUE')

    def checkForCSThread(self):
        thr = threading.Thread(target=self.checkForCS)
        thr.start()

    def checkForCS(self):
        path_to_watch = "./sessiondir"
        before = dict([(f, None) for f in os.listdir(path_to_watch)])
        while self:
            time.sleep(1)
            after = dict([(f, None) for f in os.listdir(path_to_watch)])
            added = [f for f in after if not f in before]
            if added:
                for cs in added:
                    if cs == 'ADJÖ':
                        self.softClose()
                    elif cs != 'CONTINUE':
                        self.fedCourses.WriteText(cs + "\n")
                        todo = self.revolutionCtrl.GetValue()
                        self.revolutionCtrl.SetValue(todo - 1)
                        done = self.doneTxtCtrl.GetValue()
                        newdone = int(done) + 1
                        self.doneTxtCtrl.SetValue(str(newdone))
            before = after

    def softClose(self):
        time.sleep(1)
        self.Close()

    def DisplayCGExample(self, event):
        val = self.comboBoxCourseSelect.GetSelection()
        ccabb = self.ccabb[val].text
        listobj = self.coursegroupSort.GetList()
        order = listobj.GetCurrentOrder()
        self.testSite = False
        if self.chkTestSite.IsChecked():
            self.testSite = True
        util = Open24Utility(self.testSite)
        cgx = util.buildcoursegroup(self, ccabb, 'full', 1, order)
        self.textCtrlCGExample.SetValue(cgx)

    def setCustomer(self, event):
        self.testSite = False
        if self.chkTestSite.IsChecked():
            self.testSite = True
        c = self.customerSelect.GetValue()
        if c == "Välj kund":
            self.textCtrlCURL.SetValue('')
            self.comboBoxCourseSelect.Clear()
            self.comboBoxCourseSelect.SetValue('Välj kurs')
        else:
            ut = Open24Utility(self.testSite)
            self.textCtrlCURL.SetValue(ut.urldict[c])
            self.coursenames, self.ccabb = Open24Utility.getcourselist(c)
            self.comboBoxCourseSelect.Clear()
            self.comboBoxCourseSelect.SetValue('Välj kurs')
            courseChoices = []
            for coursename in self.coursenames:
                courseChoices.append(coursename.text)
            self.comboBoxCourseSelect.AppendItems(courseChoices)

    def onsaveas(self, event):
        self.testSite = False
        if self.chkTestSite.IsChecked():
            self.testSite = True
        utili = Open24Utility(self.testSite)
        utili.preparesave(self)

    def startProcess(self, event):
        try:
            self.ff.thread_start()
        except AttributeError:
            dial = wx.MessageDialog(None, 'Du måste trycka på Öppna först!', 'Info', wx.OK)
            dial.ShowModal()
            return
        self.ff.ready = True
        self.checkForCSThread()

    def setSpeed(self, event):
        self.wait = self.speedSlider.GetValue()

    def chooseButton(self, event):
        self.submitButtonIndex = self.newOrCopy.GetSelection() or 0

    def stackFile(self, event):
        self.openXMLPath = self.filePickerXML.GetPath()
        file, suffix = os.path.basename(self.openXMLPath).split('.')
        self.selectedFile.SetValue(file)
        self.cStarts = open(self.openXMLPath, 'rb')
        self.starttree = ET.parse(self.cStarts)
        self.root = self.starttree.getroot()
        self.coursestarts = self.root.findall('CourseStart')
        self.waiting = 0
        self.done = 0
        for coursestart in self.coursestarts:
            self.fed = coursestart.find('Fed').text
            if self.fed == 'false':
                self.waiting += 1
            else:
                self.done +=1
        self.revolutionCtrl.SetValue(self.waiting)
        self.doneTxtCtrl.SetValue(str(self.done))

    def startFF(self, event):
        self.c = self.customerSelect.GetValue()
        if self.c == "Välj kund":
            dial = wx.MessageDialog(None, 'Du måste välja kund!', 'Info', wx.OK)
            dial.ShowModal()
            return
        self.b = self.browserSelect.GetValue()
        if self.b == "Välj webbläsare!":
            dial = wx.MessageDialog(None, 'Du måste välja webbläsare!', 'Info', wx.OK)
            dial.ShowModal()
            return
        self.f = self.selectedFile.GetValue()
        if len(self.f) == 0:
            dial = wx.MessageDialog(None, 'Du måste välja källfil!', 'Info', wx.OK)
            dial.ShowModal()
            return
        confirmtext= """
        När du väljer Öppna måste alla val vara klara. Du ska ha bestämt antal kurser som ska 
        matas in. Du ska också ha bestämt med vilken hastighet inmatningen ska ske. Du ska också
        ha bestämt om data i gränssnittet ska sparas; 'Spara / Kopiera' eller tas bort; 'Spara / Ny'. 
        Om allt detta är klart kan du klicka på Ja, annars klicka på Nej.
        """
        confirm = wx.MessageDialog(None, confirmtext, 'Är allt klart?', wx.YES_NO | wx.NO_DEFAULT)
        confirmanswer = confirm.ShowModal()
        if confirmanswer == wx.ID_YES:
            startURL = self.textCtrlCURL.GetValue()
            self.revs = self.revolutionCtrl.GetValue()
            self.dry = False
            if self.chkDryRun.IsChecked():
                self.dry = True
            self.wait = self.speedSlider.GetValue()
            self.savemode = self.newOrCopy.GetSelection()
            self.revolutionCtrl.Enable(False)
            self.ff = FormFeeder(self.openXMLPath, self.b, self.revs, self.dry, self.wait, self.savemode)
            self.ff.open24Entrypage(startURL)
        else:
            return

    def enablestart2(self, event):
        if self.start2Check.IsChecked():
            self.start2Date.Enable(True)
            self.start3Check.Enable(True)
            self.textCtrlStartMarker2.Enable(True)
        else:
            self.start2Date.Enable(False)
            self.start3Check.Enable(False)
            self.start3Date.Enable(False)
            self.textCtrlStartMarker2.Enable(False)
            if self.start3Check.IsChecked():
                self.start3Check.SetValue(False)
            self.textCtrlStartMarker3.Enable(False)

    def enablestart3(self, event):
        if self.start3Check.IsChecked():
            self.start3Date.Enable(True)
            self.textCtrlStartMarker3.Enable(True)
        else:
            self.start3Date.Enable(False)
            self.textCtrlStartMarker3.Enable(False)

    def enableHeaderText(self, event):
        if self.headerChk.IsChecked():
            self.headerText.Enable(True)
            self.headerWEText.Enable(True)
            self.headerCPRText.Enable(True)
            self.headerLabText.Enable(True)
        else:
            self.headerText.Enable(False)
            self.headerWEText.Enable(False)
            self.headerCPRText.Enable(False)
            self.headerLabText.Enable(False)

    def enableStartInfo(self, event):
        if self.startInfoChk.IsChecked():
            self.startInfoText.Enable(True)
        else:
            self.startInfoText.Enable(False)

    def enableStudyHours(self, event):
        if self.studyHoursChk.IsChecked():
            self.studyHoursText.Enable(True)
        else:
            self.studyHoursText.Enable(False)

    def openCustomerUrl(self, event):
        self.c = self.customerSelect.GetValue()
        if self.c == "Välj kund":
            dial = wx.MessageDialog(None, 'Du måste välja kund!', 'Info', wx.OK)
            dial.ShowModal()
            return
        self.testSite = False
        if self.chkTestSite.IsChecked():
            self.testSite = True
        util = Open24Utility(self.testSite)
        util.opencustomersite(self.c)

    # Virtual event handlers, overide them in your derived class
    def showCourseItemsPage(self, event):
        self.mainSizer.Hide(self.courseGroupSizer, recursive=True)
        self.mainSizer.Hide(self.formFeedSizer, recursive=True)
        self.mainSizer.Show(self.courseItemsSizer, show=True, recursive=True)
        self.mainSizer.Layout()

    def showCourseGroupPage(self, event):
        self.mainSizer.Hide(self.courseItemsSizer, recursive=True)
        self.mainSizer.Hide(self.formFeedSizer, recursive=True)
        self.mainSizer.Show(self.courseGroupSizer, show=True, recursive=True)
        self.mainSizer.Layout()


    def showFormFeedPage(self, event):
        self.mainSizer.Hide(self.courseItemsSizer, recursive=True)
        self.mainSizer.Hide(self.courseGroupSizer, recursive=True)
        self.mainSizer.Show(self.formFeedSizer, show=True, recursive=True)
        self.mainSizer.Layout()


def main():
    ex = wx.App()
    open24Frame(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()
