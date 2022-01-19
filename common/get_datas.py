import xlrd
import configparser


# 字典方式
def test_ddt_excel1(filename, sheetname):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_name(sheetname)
    # print(sheet.ncols, sheet.nrows)
    # print(sheet.cell(0, 0))
    # print(sheet.cell_value(0, 0))
    datas = []
    for row in range(1, sheet.nrows):
        line_data = {}
        for col in range(sheet.ncols):
            key = sheet.cell_value(0, col)
            value = sheet.cell_value(row, col)
            line_data[key] = value
        print(line_data)
        datas.append(line_data)
        pass
    print(datas)
    return datas


def get_data_from_conf(filename, section, option):
    conf = configparser.ConfigParser()
    conf.read(filename)
    conf.sections()
    return conf.get(section, option)


if __name__ == '__main__':
    test_data = test_ddt_excel1(r'C:\Users\UFO\Desktop\test_login.xls', 'login')