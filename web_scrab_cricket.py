from bs4 import BeautifulSoup
import requests ,openpyxl
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="LIVE SCORE"
sheet.append(["TEAM 1 NAME","TEAM 1 SCORE","TEAM 2 NAME","TEAM 2 SCORE"])

html_text = requests.get('https://www.cricbuzz.com/cricket-match/live-scores').text
soup = BeautifulSoup(html_text, "html.parser")
#print(soup)
sect = soup.find_all('div', class_='sp-scr_wrp')
section = sect[1]
description = section.find('span', class_='description').text
location = section.find('span', class_='location').text
current = section.find('div', class_='scr_dt-red').text
link = "https://sports.ndtv.com/" + section.find(
    'a', class_='scr_ful-sbr-txt').get('href')

try:
    status = section.find_all('div', class_="scr_dt-red")[1].text
    block = section.find_all('div', class_='scr_tm-wrp')
    team1_block = block[0]
    team1_name = team1_block.find('div', class_='scr_tm-nm').text
    team1_score = team1_block.find('span', class_='scr_tm-run').text
    team2_block = block[1]
    team2_name = team2_block.find('div', class_='scr_tm-nm').text
    team2_score = team2_block.find('span', class_='scr_tm-run').text
    print(description)
    print(location)
    print(status)
    print(current)
    print(team1_name.strip())
    print(team1_score.strip())
    print(team2_name.strip())
    print(team2_score.strip())
    print(link)
    sheet.append([team1_name,team1_score,team2_name,team2_score])
except Exception as e:
     print(e)

excel.save("Cricket.xlsx")