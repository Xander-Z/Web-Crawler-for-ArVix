import pandas as pd


def list2D_to_list1D(list):
    result = []
    for sublist in list:
        str = '; \n'.join(sublist)
        result.append(str)
    return result


def write_xlsx(path, data):
    df = pd.DataFrame({"title": data.title,
                       "abstract": data.abstract,
                       "authors": list2D_to_list1D(data.authors),
                       "subjects": list2D_to_list1D(data.subjects),
                       "comments": data.comments,
                       "index": data.arVix_index,
                       "pdf": data.pdf})
    writer = pd.ExcelWriter(path.excel_content, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column("A:A", 30)
    worksheet.set_column("B:B", 110)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 40)
    worksheet.set_column("E:E", 40)
    worksheet.set_column("F:F", 20)
    worksheet.set_column("G:G", 30)
    writer.save()

    dict_subjects = {}
    for i in data.subjects:
        for j in i:
            if j in dict_subjects:
                dict_subjects[j] += 1
            else:
                dict_subjects[j] = 1

    list_subjects_name = []
    list_subjects_num = []
    for i in dict_subjects:
        list_subjects_name.append(i)
        list_subjects_num.append(dict_subjects[i])

    dd = pd.DataFrame({"subject": list_subjects_name,
                       "num": list_subjects_num})
    dd.to_excel(path.excel_subject, index=False)
