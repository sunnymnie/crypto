import os
import requests
import glob
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import shutil
import pypandoc
from datetime import datetime, timedelta
import sys
import time

def title_class(c):
    return is_class(c, "MuiContainer-root MuiContainer-maxWidthLg")

def author_class(c):
    return is_class(c, "MuiTypography-root MuiTypography-body1")

def is_class(c, key):
    return c is not None and c[:len(key)] == key


def parse(text):
    text = text.replace('\n', ' ', -1) + '\n\n'
    text = text.replace('\\tightlist', '', -1)
    return text

def parse_title(title):
    title = title.lower()
    title = title.replace(":", "-", -1)
    title = title.replace(" ", "-", -1)
    title = title.replace("\n", "", -1)
    return title

def parse_figure(fig, img_name):
    try: 
        if fig.name == "img":
            link = fig['src']
        else:
            link = fig.find('a')['href']
        img = requests.get(link, stream=True)
        img.raw.decode_content = True
        extension = link[link.rfind('.'):]
        if extension.find("?") != -1: extension = extension[:extension.find("?")]
        if extension.find("&") != -1: extension = extension[:extension.find("&")]
        with open(img_name + extension,'wb') as f:
            shutil.copyfileobj(img.raw, f)

        return "\includegraphics[width=0.9\linewidth]{"+img_name+"}"
    except:
        link = fig.find('div').next['src'].replace('_', '\_', -1)
        return f"Video: {link}"

# def parse_img(img, name):
#     print(f"Finding: ---------- {img['src']}")
#     raise ValueError

def html_parse(text):
    return pypandoc.convert_text("<p>" + text + "</p>", 'latex', format='html')

def parse_header(header, rank):
    text = html_parse(header.text)
    text = "section*{" + text + "}"
    if rank == "h3": text = "sub" + text
    elif rank != "h2": text = "subsub" + text
    return f"\\{text}"

def get_date(html_soup):
    date = html_soup.find_all('p', class_=author_class)[1].text
    date = date[:date.find('\xa0')]
    if 'hour' in date:
        date = datetime.today().strftime("%b %-d, %Y")
    elif 'day' in date:
        date = (datetime.today() - timedelta(days=1)).strftime("%b %-d, %Y")
    return date
    

def cleanup(fignum, temp):
    for i in range(fignum):
        for filename in glob.glob(f"./{i}*"):
            os.remove(filename) 
    for filename in glob.glob(f"./{temp}*"):
            os.remove(filename) 
            

def main():

    try:
        url = str(sys.argv[1])
    except:
        url = str(input("Input Messari article URL:\n"))
        
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    while True:
        html_soup: BeautifulSoup = BeautifulSoup(driver.page_source, 'html.parser')
        try:
            main = html_soup.find('div', attrs={'class': 'Messari-paywall'}).next()
            break
        except: 
            print("Waiting for website to load...")
            time.sleep(1)
    texdoc = []
    fignum = 0
    temp = 'test'



    # print(html_soup.find('div', class_=title_class))
    # print("="*60)

    title = html_parse(html_soup.find('div', class_=title_class).find('h1').text)
    # title = html_parse(html_soup.find('div', class_= 'MuiContainer-root MuiContainer-maxWidthLg').find('h1').text)
    # title = html_parse(html_soup.find('div', attrs={'class': 'MuiContainer-root MuiContainer-maxWidthLg'}).find('h1').text)

    filename = str(parse_title(title))
    author = html_parse(html_soup.find('p', class_=author_class).find('a').text)
    # author = html_parse(html_soup.find('p', attrs={'class': 'MuiTypography-root MuiTypography-body1'}).find('a').text)
    # author = html_parse(html_soup.find('p', class_='MuiTypography-root MuiTypography-body1').find('a').text)
    texdoc.append("\documentclass{messari}\n")
    texdoc.append("\\usepackage{hyperref}\n")
    texdoc.append("\hypersetup{colorlinks=true,linkcolor=black,filecolor=magenta,urlcolor=blue,pdftitle={Overleaf Example},pdfpagemode=FullScreen}\n")
    texdoc.append("\\title{" + title + "}\n")
    texdoc.append("\\author{" + author + "}\n")
    texdoc.append("\\date{" + get_date(html_soup) + "}\n")

    texdoc.append("\\begin{document}\n")
    texdoc.append("\\maketitle\n")
    texdoc.append("\\author\n")


    for i in range(len(main)):
        if main[i].name in ['p','ol', 'ul']:
            texdoc.append(parse(pypandoc.convert_text(str(main[i]), 'latex', format='html')))
        elif main[i].name in ["figure", "img"]:
            texdoc.append(parse(parse_figure(main[i], str(fignum))))
            fignum += 1
        elif main[i].name in ['h2', 'h3', 'h4', 'h5', 'h6', 'h7']:
            texdoc.append(parse_header(main[i], main[i].name)+"\n")

    texdoc.append("\end{document}")

    with open(f"{temp}.tex", 'w') as fout:
        for i in range(len(texdoc)):
            fout.write(texdoc[i])

    os.system(f"xelatex {temp}.tex")
    os.replace(f"{temp}.pdf", f"{filename}.pdf")
    driver.quit()


    cleanup(fignum, temp)
    os.system(f"open {filename}.pdf")


if __name__ == "__main__":
    main()
