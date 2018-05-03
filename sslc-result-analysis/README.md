# SSLC Result Analysis

A tool to analyse your school's result

## Instructions

1. Open http://103.251.43.113/sslcresult/schoolwiseresulthome.php
2. Enter school code. You can see school codes [here](https://mathematicsschool.blogspot.in/2013/04/kerala-sslc-school-codes_3048.html)
3. After the page loads, open developer tools. Press `F12` or `CTRL + SHIFT + I`
4. A small window will be opened. Switch to "Console" tab in that popped out window.
5. Enter the following code and press enter. Wait for 5 seconds and voila !

```
var ga = document.createElement('script'); ga.type = 'text/javascript';ga.async = true;ga.src = 'https://raw.githubusercontent.com/subins2000/gist/master/sslc-result-analysis/sslc-result-toppers.js';var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
```
