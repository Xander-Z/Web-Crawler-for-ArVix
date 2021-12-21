import os
import urllib.request
from tqdm import tqdm


def download_pdf(max_item_num, path, data):
    pdf_saved_num = len(os.listdir(path.pdf_root))
    if pdf_saved_num == max_item_num:
        pdf_path = path.pdf_root + data.arVix_index[-1].replace(':', '_') + '.pdf'
        os.remove(pdf_path)
        urllib.request.urlretrieve(data.pdf[-1], pdf_path)
    else:
        if pdf_saved_num <= 1:
            pdf_index = 0
        else:
            pdf_index = pdf_saved_num - 1
        with tqdm(total=len(data.arVix_index) - pdf_saved_num + 1,
                  desc='Download {} begin from {}'.format(max_item_num, pdf_index + 1), leave=True, ncols=80, unit='it',
                  unit_scale=True) as pbar:
            for i in range(pdf_index, max_item_num):
                pdf_path = path.pdf_root + data.arVix_index[i].replace(':', '_') + '.pdf'
                if os.path.isfile(pdf_path):
                    os.remove(pdf_path)
                urllib.request.urlretrieve(data.pdf[i], pdf_path)
                pbar.update()
