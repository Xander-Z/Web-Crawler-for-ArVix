import jieba
from wordcloud import WordCloud


def draw_wordcloud(path, data):
    filter_list = ['Learning', 'learning', 'based', 'Network', 'Neural Network',
                   'Data', 'using', 'via', 'Using', 'Neural', 'neural',
                   'Networks', 'Systems', 'networks']
    cloud_text = ' '.join(data.title)
    cut_text = jieba.cut(cloud_text)
    filtered_text = []
    for w in cut_text:
        if w not in filter_list:
            filtered_text.append(w)
    result = " ".join(filtered_text)
    wc = WordCloud(
        background_color='white',
        width=600,
        height=400,
        max_font_size=50,
        min_font_size=10,
        mode='RGBA'

    )
    wc.generate(result)
    wc.to_file(path.excel_wordcloud)
