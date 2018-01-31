# This program takes the website retrieved by the scraper and extracts data with regex

import re

with open('espnrankings.txt', 'r') as espn_file:
    data = espn_file.read()
    result1 = re.findall('<p><b>(.*?)</b><br />(.*?)</p><p><inline.*?-wide></p><p>(.*?)<em>(.*?)</em>', data, re.DOTALL)
    result2 = re.findall('<p><b>(.*?)</b><br />.*?</p><p><inline.*?-wide></p><p>.*?<em>.*?</em>', data, re.DOTALL)
    result3 = re.findall('<p><b>.*?</b><br />(.*?)</p><p><inline.*?-wide></p><p>.*?<em>.*?</em>', data, re.DOTALL)
    result4 = re.findall('<p><b>.*?</b><br />.*?</p><p><inline.*?-wide></p><p>(.*?)<em>.*?</em>', data, re.DOTALL)
    result5 = re.findall('<p><b>.*?</b><br />.*?</p><p><inline.*?-wide></p><p>.*?<em>(.*?)</em>', data, re.DOTALL)

with open('espnrankings_parsed.txt', 'w') as final_espn:
	print(result1, file=final_espn)
        
with open('espnrankings_parsed.txt', 'a') as final_espn:
    print(result2, file=final_espn)
    print(result3, file=final_espn)
    print(result4, file=final_espn)
    print(result5, file=final_espn)

print()
