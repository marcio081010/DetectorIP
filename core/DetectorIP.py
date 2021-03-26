class DetectorIP:
    """Represents an DetectorIP information object"""
    
    def __init__(self, query, jsonData = None):
        self.Query = query
        self.ASN = '-'
        self.City = '-'
        self.Country = '-'
        self.CountryCode = '-'
        self.ISP = '-'
        self.Latitude = 0.0
        self.Longtitude = 0.0
        self.Organization = '-'
        self.IP = '0.0.0.0'
        self.Region = '-'
        self.RegionName = '-'
        self.Status = '-'
        self.Timezone = '-'
        self.Zip = '-'
        self.GoogleMapsLink = ''
        
        if jsonData != None:
            if type(jsonData) is dict:
                if 'as' in jsonData: 
                    self.ASN = jsonData['as']
                
                if 'city' in jsonData:
                    self.City = jsonData['city']
                 
                if 'country' in jsonData:
                    self.Country = jsonData['country']
                   
                if 'countryCode' in jsonData:
                    self.CountryCode = jsonData['countryCode']
                   
                if 'isp' in jsonData:
                    self.ISP = jsonData['isp']
                   
                if 'lat' in jsonData:
                    self.Latitude = jsonData['lat']
                  
                if 'lon' in jsonData:
                    self.Longtitude = jsonData['lon']
                  
                if 'org' in jsonData:
                    self.Organization = jsonData['org']
                   
                if 'query' in jsonData:
                    self.IP = jsonData['query']
                  
                if 'region' in jsonData:
                    self.Region = jsonData['region']
                  
                if 'regionName' in jsonData:
                    self.RegionName = jsonData['regionName']
                  
                if 'status' in jsonData:
                    self.Status = jsonData['status']
                   
                if 'timezone' in jsonData:
                    self.Timezone = jsonData['timezone']
                   
                if 'zip' in jsonData:
                    self.Zip = jsonData['zip']
                
                if type(self.Latitude) == float and type(self.Longtitude) == float: 
                    self.GoogleMapsLink = 'http://www.google.com/maps/place/{0},{1}/@{0},{1},16z'.format(self.Latitude, self.Longtitude)
                    
                    
    def ToDict(self):
        #self.__dict__.
        return {'Target':self.Query, 'IP':self.IP, 'ASN':self.ASN, 'City':self.City, 
                    'Country':self.Country, 'Country Code':self.CountryCode, 'ISP':self.ISP, 
                    'Latitude':str(self.Latitude), 'Longtitude':str(self.Longtitude), 
                    'Organization':self.Organization, 'Region':self.Region, 
                    'Region Name':self.RegionName, 'Timezone':self.Timezone, 
                    'Zip':self.Zip, 'Google Maps':self.GoogleMapsLink
                } 
