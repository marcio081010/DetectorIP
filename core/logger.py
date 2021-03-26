from datetime import datetime
import os
from termcolor import colored
from sys import platform as _platform


if _platform == 'win32':
    import colorama
    colorama.init()

def Red(value):
        return colored(value, 'red', attrs=['bold'])
    
def Green(value):
    return colored(value, 'green', attrs=['bold'])
    
          
class Logger:
    
    def __init__(self, nolog=False, verbose=False):
        self.NoLog = nolog
        self.Verbose = verbose
        
        
    def WriteLog(self, messagetype, message):
        filename = '{}.log'.format(datetime.strftime(datetime.now(), "%Y%m%d"))
        path = os.path.join('.', 'logs', filename)
        with open(path, 'a') as logFile:
            logFile.write('[{}] {} - {}\n'.format(messagetype, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), message))
              
              
    def PrintError(self, message):
        """Print/Log error message"""
        if not self.NoLog:
            self.WriteLog('ERROR', message)
        
        print('[{}] {}'.format(Red('ERROR'), message))
    
    
    def PrintResult(self, title, value):
        """print result to terminal"""
        print('{}: {}'.format(title, Green(value)))
    
    
    def Print(self, message):
        """print/log info message"""
        if not self.NoLog:
            self.WriteLog('INFO', message)
            
        if self.Verbose:
            print('[{}] {}'.format(Green('**'), message))
    
    
    def PrintIPGeoLocation(self, ipGeoLocation):
        """print IP Geolocation information to terminal"""
        self.PrintResult('\nTarget', DetectorIP.Query)
        self.PrintResult('IP', DetectorIP.IP)
        self.PrintResult('ASN', DetectorIP.ASN)
        self.PrintResult('City', DetectorIP.City)
        self.PrintResult('Country', DetectorIP.Country)
        self.PrintResult('Country Code', DetectorIP.CountryCode)
        self.PrintResult('ISP', DetectorIP.ISP)
        self.PrintResult('Latitude', str(DetectorIP.Latitude))
        self.PrintResult('Longtitude', str(DetectorIP.Longtitude))
        self.PrintResult('Organization', DetectorIP.Organization)
        self.PrintResult('Region Code', DetectorIP.Region)
        self.PrintResult('Region Name', DetectorIP.RegionName)
        self.PrintResult('Timezone', DetectorIP.Timezone)
        self.PrintResult('Zip Code', DetectorIP.Zip)
        self.PrintResult('Google Maps', DetectorIP.GoogleMapsLink)
        print()
        #.encode('cp737', errors='replace').decode('cp737')
    
