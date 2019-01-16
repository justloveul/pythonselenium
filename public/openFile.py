import yaml, os, time
def open_yaml(name):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    filepath = os.path.join(path, name)
    f = open(filepath, "rb")
    content = f.read()
    data = yaml.load(content)
    f.close()
    return data

def open_report_file(path):
    path = os.path.join(path, 'report')
    reportDate = time.strftime("%Y-%m-%d", time.localtime())
    reportTime = time.strftime("%H-%M-%S", time.localtime())
    reportBashPath = os.path.join(path, reportDate)
    if  not os.path.exists(reportBashPath):
        os.mkdir(reportBashPath)
    reportPath = os.path.join(reportBashPath, "report {}.html".format(reportTime))
    # with open(reportPath, 'wb') as f:
    #     return f
    f = open(reportPath, 'wb')
    return f

