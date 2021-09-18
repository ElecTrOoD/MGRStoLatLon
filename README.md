# MGRS to Latitude/Longitude
The script converts the MGRS coordinates to latitude/longitude using [pymgrs](https://github.com/aydink/pymgrs) initialy created by aydink<br/>
Especially for Digital Combat Simulator.

**37TDK9999999999** converts to **45°09′12.48N 38°59′59.95E**<br/>
You can also add elevation data in the same line separated by a space. It will look like this: **37TDK9999999999 500ft**<br/>

The script takes data from the clipboard and replaces it with the converted one.<br/>
To convert multiple values at once, each value must start on a new line.

### Like this:
**37TDK9999999999 45°09′12.48N 38°59′59.95E<br/>**
**37TDK8888888888 45°03′12.10N 38°51′31.97E<br/>**
**37TDK7777777777 44°57′11.09N 38°43′05.76E<br/>**
**37TDK6666666666 44°51′09.46N 38°34′41.31E<br/>**

# How to install
You can download [executable file](https://github.com/ElecTrOoD/MGRStoLatLon/releases/tag/v1.0) and skip the next steps.

Or use source code:
1. Clone repository
2. Install python 3 from [python.org](https://www.python.org/)
3. Open PowerShell in project folder and run command
 ```
 pip install -r requirements.txt
 ```

# How to use it
1. Write down the coordinates you want and copy them using the keyboard shortcut CTRL + C
```
37TDK9999999999 999ft
37TDK8888888888 888ft
37TDK7777777777 777ft
37TDK6666666666 666ft
```
2. Run executable file.
   - If you are using the source code, open PowerShell in the project folder and run this command
 ```
 python main.py
 ```
4. Paste the result wherever you want using the keyboard shortcut CTRL + V
5. Done

To record the coordinates recommend using a [dcs-scratchpad](https://github.com/rkusa/dcs-scratchpad)

[Video example](https://youtu.be/hB0QEtUL6IQ)
