# Windows get CPU usage command

Searched high and low for a command to get CPU usage on the internet to no
avail. From a DOS command prompt (Windows server 2003) CPU usage for all
nodes:

    
    
    WMIC CPU GET LoadPercentage
    

SNMP was my other alternative, but not all deployments would have this
service.

This does not aggregate the values, nor does it easily feed into a batch file.
For that I use a ` FOR ` loop.

    
    
    FOR /F "delims= " %%i in ('WMIC CPU GET LoadPercentage') do @echo %%i
    

Posted in DOS | Tagged CPU , DOS CPU usage , utilization | Leave a comment 


Original post date: November 16, 2010

Category: DOS