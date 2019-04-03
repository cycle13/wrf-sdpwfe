#!/usr/bin/python
# -*- coding: UTF-8 -*-
#   Fetch GFS realtime forecast data from HKUST ENVR Server
#   executed every day at 00:30
#       L_Zealot
#       Jan 06, 2018
#
#

import datetime
import requests 
import os



# Main function

def main():
    
    # Optional URL when data not available from HKUST
    #url='ftp://ftpprd.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.2018010512/'
    
    # Fetch url
    url0='http://envf.ust.hk/dataop/data/model_input/gfs_1.00deg_realtime/'
    
    # Archive path
    arpath='/home/disk1/zhpfu/disk2/gfs_fcst/'

    date_lastday=datetime.datetime.now()+datetime.timedelta(days=-2)
    date_str=date_lastday.strftime('%Y%m%d')
    
    arpath=arpath+date_str
    os.system('mkdir '+arpath)
    for ii in range(0,168,6):
        url=url0+'gfs.'+date_str+'12/'+'gfs.t12z.pgrb2.1p00.f%03d' % ii
        print('fetching '+url)
        r = requests.get(url)
        with open(arpath+'/'+'gfs.t12z.pgrb2.1p00.f%03d' % ii, 'wb') as code:
            code.write(r.content)
if __name__=='__main__':
    main()
