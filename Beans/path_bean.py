def cheak_root(root):
    if root[-1] == '\\':
        root = root[:-1] + '/'
    elif root[-1] == '/':
        pass
    else:
        root = root + '/'
    return root


class PathBean():
    def __init__(self, root, date):
        self.path = cheak_root(root) + 'arVix_data/' + date + '/'
        self.excel_content = self.path + date + "_arVix_cs" + ".xlsx"
        self.excel_subject = self.path + date + "_arVix_cs_subject" + ".xlsx"
        self.excel_wordcloud = self.path + date + "_arVix_cs_wordcloud" + ".png"
        self.pdf_root = self.path + 'pdf/'
