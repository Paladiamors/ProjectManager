'''
Created on Aug 18, 2013

@author: justin
'''

import wx
import datetime


def py2wxDatetime(date):
    """
    Takes in a python datetime object and converts it to a wx.DateTime Object
    """
    wxDt = wx.DateTime()
    day, month, year = date.day, date.month - 1, date.year #wow, the month parameter is needs to be subtracted by one! 
    hour, minute, second, millisec = date.hour, date.minute, date.second, int(date.microsecond/1000)
     
    wxDt.Set(day, month, year, hour, minute, second, millisec)
    return wxDt

def wx2pyDatetime(date):
    """
    takes a wx DateTime object and converts it to a python date time object
    """
    
    day, month, year = date.Day, date.Month + 1, date.Year
    hour, minute, second, microsecond = date.Hour, date.Minute, date.Second, date.Millisecond*1000
    
    return datetime.datetime(year, month, day, hour, minute, second, microsecond)

if __name__ == "__main__":
    
    today = datetime.datetime.today()
    
    wxDate = py2wxDatetime(today)
    pyDate = wx2pyDatetime(wxDate)
    
    print today
    print wxDate
    print pyDate