import inspect, os, os.path, shutil, subprocess, tempfile, time
from pxr import Usd

def getDataFolder():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    scriptPath = os.path.dirname(os.path.abspath(filename))
    return os.path.abspath(os.path.join(os.path.dirname(scriptPath), "data"))

def getDataFilePath(dataFilename):
    return os.path.join(getDataFolder(), dataFilename)

def viewUsdFile(dataFilePath):
    process = subprocess.Popen(['usdview.cmd', dataFilePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        pipes = process.communicate()
        if pipes[0]: print pipes[0]
        if pipes[1]: print pipes[1]
        if process.poll(): time.sleep(0.1)
        else: break

def createWorkStage(dataFilename):
    stage = Usd.Stage.CreateInMemory()
    appendLayer(stage, dataFilename)
    stage.SetEditTarget(stage.GetSessionLayer())
    return stage

def appendLayer(stage, dataFilename):
    stage.GetRootLayer().subLayerPaths.append(getDataFilePath(dataFilename))
    
def printWorkStage(stage):
    print stage.GetSessionLayer().ExportToString()

def viewUsdStage(stage):
    td = tempfile.mkdtemp()
    stageFilePath = os.path.join(td, "stage.usda")
    stage.Export(stageFilePath)
    viewUsdFile(stageFilePath)
    shutil.rmtree(td)
