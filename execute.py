from Beans.path_bean import PathBean
from Beans.data_bean import DataBean
from Utils.create_xlsx import write_xlsx
from Utils.download_pdf import download_pdf
from Utils.draw_wordcloud import draw_wordcloud
from Utils.crawl_util import check_url, crawl_object

import os
import logging
import coloredlogs
import jieba
import argparse

logger = logging.getLogger()
coloredlogs.install(level='DEBUG')
jieba.setLogLevel(logging.INFO)


def parse_opt():
    parser = argparse.ArgumentParser()

    parser.add_argument('--root', type=str, default='f:/', help='path of result saving')
    parser.add_argument('--url', type=str, default='https://arxiv.org/list/cs/new', help='the url crawled')
    parser.add_argument('--update', type=bool, default=False,
                        help='Whether crawling it again when the latest data has been crawled.')

    opt = parser.parse_args()
    return opt


def date_reshape(date):
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    port = date.replace(',','').split(' ')
    new = port[::-1]
    new[1] = str(month.index(new[1])+1)
    new[0] = '20'+new[0]
    return '_'.join(new[:-1])


if __name__ == '__main__':
    opt = parse_opt()
    logger.info('Crawl for the latest data.')

    max_item_num, date = check_url(opt)
    logger.info("{} papers were detected.".format(max_item_num))
    logger.info('It was last updated at ' + date + '.')
    date = date_reshape(date)
    path = PathBean(opt.root, date)
    data = DataBean(crawl_object(max_item_num, opt))

    try:
        os.makedirs(path.path, mode=0o770)
    except FileExistsError:
        logger.info(path.path + ' already exists.')
    else:
        logger.info(path.path + ' is created.')
    try:
        os.makedirs(path.pdf_root, mode=0o770)
    except FileExistsError:
        pass
    else:
        pass
    if os.path.exists(path.excel_content) and os.path.exists(path.excel_subject) and os.path.exists(
            path.excel_wordcloud):
        logger.info('The latest data has been crawled.')
        if opt.update:
            logger.info('Updating now.')
            write_xlsx(path, data)
            draw_wordcloud(path, data)
            download_pdf(max_item_num, path, data)
            logger.info('Update complete.')
        else:
            logger.info('Exit the program without updating data.')
    else:
        logger.info('Crawling now.')
        write_xlsx(path, data)
        draw_wordcloud(path, data)
        download_pdf(max_item_num, path, data)
        logger.info('Crawl to complete.')
