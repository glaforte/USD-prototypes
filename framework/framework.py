import inspect, os, os.path, subprocess

def getDataFolder():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    scriptPath = os.path.dirname(os.path.abspath(filename))
    return os.path.abspath(os.path.join(os.path.dirname(scriptPath), "data"))

def getDataFilePath(dataFilename):
    return os.path.join(getDataFolder(), dataFilename)

def viewUsdFile(dataFilePath):
    subprocess.call("usdview.cmd %s" % dataFilePath)
