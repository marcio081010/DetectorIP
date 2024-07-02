# 🚀📤DetectorIP📤🚀

    ....................................................................................................
    ....................................................................................................
    .............................................................:::^^^^^^^^^^:::.......................
    .........................................................::^^^^^^^^::^^^^^^~^^^::...................
    .......................................................:^^^::::::::::::::::::^^~~^:.................
    .....................................................:^^::::::::::::::::::::::::^~~^:...............
    ....................................................^^::::::::::::::::::::::::::::^~~^..............
    ...................................................^^:::::::::::::::::::::::::::::::~~^.............
    ..................................................^^:::::::::::::::::::::::::::::::::~~^............
    .................................................:^:::::::::ooooo ooooooooo.::::::::::~~:...........
    .................................................^^:::::::::`888' `888   `Y88.::::::::~~^...........
    .................................................^:::::::::::888   888   .d88'::::::::^~^...........
    .................................................^^::::::::::888   888ooo88P' ::::::::~~^...........
    .................................................:^.:::::::::888   888::::::::::::::::~^:...........
    ..................................................^~.::::::::888   888:::::::::::::::^~:............
    ..................................................:J~.::::::o888o o888o:::::::::::::^~:.............
    ...................................................^J!:.:::::::::::::::::::::::::::^^:..............
    .............::^::::::^^^^^^^^^^^^^^^^^::......:::!JJ??~:.:::::::::::::::::::::::^^^:...............
    ............:^^^:::::^^^^^^^^^^^^^^^~~~~^:::^::!77?!^::~!!::::..:::::::::::::::^^^:.................
    .........::^^^::::^^^^^^^^^^~~~~!!!!~^^::^^^^~JJ!~^......::::::::::::::::::^^^::....................
    .......:^^^^:::::^^^^^^^^~!~~!!7?!~^^^^^~!!!~~Y7..............::::::::::::::........................
    .....:^^^^::::^^^^^^^^^~~~7777!~^^^^^~~~!77!~!^:....................................................
    ...:^^^^:::^^^^^^^^~~~~~!!!7~^^^^^^~~~!!7!~~!!:.....................................................
    ::^^^^^^^^^^^^~~~!!!!!!!~~^^^^^~~~!!!!77!!7?7^......................................................
    ^~^^^^^^^^~~~!!!!!!~~^^^^^^~~~~~~!!77!!!?YY?~:......................................................
    ~^^~~~~~~~~~~~~^^^^^^~~~~~~~~~~~~~~!!!?YPYJ!:.......................................................
    ~~~~~~!!!!!!~~~~~~^^~~~~~^^~~~~~~~~7JY?!!!~:........................................................
    ~!!!!!!!777777!!~~~~~~~~~~~~~~~~!7????7~............................................................
    !777777??????77!!!!!~~~~~~~~~~!7JJ??77~.............................................................
    777?????????77777777!!!!!!~~!JYJ??77!^..............................................................
    ??????????777777777777!!!~~!JJJ?!^..................................................................
    ?????????777777777?777!!~~~!??!^:...................................................................
    ????????????????????77!!~~~!!^:.....................................................................
    ????????77????JJ???77!!~~~:.........................................................................
    ??????????????JJ??77!!!~^:..........................................................................

## 🎇What is

 📌A tool for retrieving IP geolocation information

 📌Powered by ip-api

## 🎇Requirements

 🔹Python version 3.x

 🔹colorama

 🔹termcolor

## 🎇Features

  ✔️Select random proxy from file. Each proxy URL in new line. 

  ✔️Export results to csv, xml and txt format.

  ✔️Select random User-Agent strings from file. Each User Agent string in new line.

  ✔️Retrieve IP or Domain Geolocation.

  ✔️Retrieve Geolocation for IPs or Domains loaded from file. Each target in new line.

  ✔️Retrieve your own IP Geolocation.

  ✔️Define your own custom User Agent string.

  ✔️Proxy support.

  ✔️Open IP geolocation in Google Maps using the default browser.

## 🎇information obtained

 🌟Longtitude

 🌟Latitude

 🌟Organization

 🌟Zip Code

 🌟Region Name

 🌟Timezone

 🌟Region Code

 🌟ISP

 🌟Country Code

 🌟Country

 🌟City

 🌟ASN

## 🎇Examples

+ Retrieve your IP Geolocation

🔸 ./ip2geolocation.py -m

+ Retrieve IP Geolocation

🔸 ./ip2geolocation.py -t x.x.x.x

+ Retrieve Domain Geolocation

🔸 ./ip2geolocation.py -t example.com

+ Do not save .log files

🔸 ./ip2geolocation.py -t example.com --nolog

+ Custom User Agent string

🔸 ./ip2geolocation.py -t x.x.x.x -u "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko"

+ Using Proxy

🔸 ./ip2geolocation.py -t x.x.x.x -x http://127.0.0.1:8080

+ Using random Proxy

🔸 ./ip2geolocation.py -t x.x.x.x -X /path/to/proxies/filename.txt

+ Pick User-Agent string randomly

🔸 ./ip2geolocation.py -t x.x.x.x -U /path/to/user/agent/strings/filename.txt

+ Retrieve IP geolocation and open location in Google maps with default browser

🔸 ./ip2geolocation.py -t x.x.x.x -g

+ Export results to CSV file

🔸 ./ip2geolocation.py -t x.x.x.x --csv /path/to/results.csv

+ Export results to XML file

🔸 ./ip2geolocation.py -t x.x.x.x --xml /path/to/results.xml

+ Export results to TXT file

🔸 ./ip2geolocation.py -t x.x.x.x -e /path/to/results.txt

+ Retrieve IP Geolocation for many targets

🔸 ./ip2geolocation.py -T /path/to/targets/targets.txt

+ Retrieve IP Geolocation for many targets and export results to xml

🔸 ./ip2geolocation.py -T /path/to/targets/targets.txt --xml /path/to/results.xml

+ Do not print results to terminal

🔸 ./ip2geolocation.py -m -e /path/to/results.txt --noprint

## 🎇Download/Installation

🎯 git clone https://github.com/marcio081010/DetectorIP

🎯pip3 install -r requirements.txt --user

🎯 if pip3 is missing:

🎯apt-get install python3-setuptools

🎯easy_install3 pip

🎯pip3 install -r requirements.txt

## ⚠️Attention⚠️

⚠️🚧 this script was made for the purpose of improving your learning about python programming!! 🚧⚠️

🚧then Use at your own risk and take responsibility for your acts.🚧

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
By: ⚡Marcio Vinicius⚡
💸💲help keep this project from sponsoring!!💲💰
😊❤️🏆my contact if you want to sponsor me: marcio081010@outlook.com

🔆"don't let others limit your success, success only depends on your choices!!"🔆
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






