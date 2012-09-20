import web,os,sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

app_root = os.path.dirname(__file__)
sys.path.append(app_root)
templates_root = os.path.join(app_root, 'template')
render = web.template.render(templates_root)

import controller.NotFound
import controller.Index

class route:
    def run(self,path):
        if not path:
            arrPath = []
        else:
            arrPath = path.split('/')
        controller = self.createController(arrPath)
        controller.setVariable('urlPath',path)
        return controller.run(render)
        
    def GET(self,path):
        return self.run(path)
        
    def POST(self,path):
        return self.run(path)
        
    def createController(self,arrPath):
        if not arrPath :
            controller = self.createIndexController()
        else:
            controllerClass = self.importModule(arrPath)
            if controllerClass != None:
                controller = controllerClass()
            else:
                controller = self.createNotFoundController(arrPath)
        return controller
        
    def importModule(self,arrPath):
        modPath = 'app.controller.' + ".".join(arrPath)
        try:
            mod = __import__(modPath,fromlist=["*"])
        except ImportError as e:
            print 'ImportError'
            return None
        
        className = arrPath[-1]
        try:
            c = getattr(mod,className)
        except AttributeError as e:
            print 'AttributeError',e
            return None
        return c
        
    def createNotFoundController(self,arrPath):
        c = controller.NotFound.NotFound()
        return c
        
    def createIndexController(self):
        return controller.Index.Index()
