from bs4 import BeautifulSoup
import urllib.request
import re


def check_url(opt):
    url_org = opt.url
    html_org = urllib.request.urlopen(url_org).read().decode()
    soup_org = BeautifulSoup(html_org, 'lxml')
    item_num = soup_org.find('small')
    item_num_text = item_num.text
    max_item_num = int(re.search('total of (\d+) entries', item_num_text).group(1))
    date_text = soup_org.find('h3').text
    date = re.search('New submissions for (.*)', date_text).group(1)
    return max_item_num, date


def crawl_object(num, opt):
    url = opt.url + '?show=' + str(num)
    html = urllib.request.urlopen(url)
    return html
