# -*-coding:Utf-8 -*
from mplotlab.utils.abctypes import GetSubTypes,AType
from plotmodels import APlotModel
from sources import ASource
from variables import AVariable
from projections import AProjection
from slides import ASlide
import xml.etree.cElementTree as ET  


class Container():
    modelCategories = \
    [ASource,AVariable,APlotModel,AProjection,ASlide]
    categoryLabels = \
    ["source","variable","plotmodel","projection","slide"]

    def __init__(self):
        self.__modelsByClassById = {}
        self.__context = None
        self.flush()

    def flush(self):
        self.__modelsByClassById = {
            #class: [(id,mdl)]
        }

    def getMdlType(self,cls):
        mdls=[]
        for _,mdl in self.__modelsByClassById.get(cls,[]):
            mdls.append(mdl)
        return mdls

    def getMdlSubTypes(self,cls):
        mdls=[]
        for c in GetSubTypes(cls):
            mdls.extend(self.getMdlType(c))
        return mdls

    def toxml(self,filename):
        root = ET.Element("models")
        for label,mdlCat in zip(self.categoryLabels,\
                                self.modelCategories):
            for mdl in self.getMdlSubTypes(mdlCat):
                mdl.toxml(label,
                          root,
                          populateModel=True)
        tree = ET.ElementTree(root)
        tree.write(filename)

    def fromxml(self,filename):        
        tree = ET.ElementTree(file=filename)
        root = tree.getroot()
        self.__context={}
        for et in root:
            AType.fromxml(et,self)
        del self.__context
        self.__context=None
    
    def __register(self,m_id,model,context):
        m_cls = model.__class__
        if not context.has_key(m_cls):
            context[m_cls]=[]
        if not self.__hasModel(m_id, m_cls, context):
            context[m_cls].append((m_id,model))
        else:
            raise Exception(\
                "Id already used. Cannot register '%s'"%\
                                        model.get_name())

    def register(self,model):
        m_id = int(model.get_id())
        self.__register(m_id,model,self.__modelsByClassById)

    def registerContext(self,c_id,model):
        if not self.__context is None:
            self.__register(c_id,model,self.__context)
            
    def __hasModel(self,m_id,m_cls,context):
        st=False
        for _id,_ in context.get(m_cls,[]):
            if _id==m_id:
                st=True
                break
        return st

    def hasModel(self,m_id,m_cls,useContext=False):
        if useContext and not self.__context is None:
            return self.__hasModel(m_id,m_cls,self.__context)
        return self.__hasModel(m_id,m_cls,self.__modelsByClassById)

    def __getModel(self,m_id,m_cls,context):
        mdl=None
        for _id,_mdl in context.get(m_cls,[]):
            if _id==m_id:
                mdl=_mdl
                break
        return mdl

    def getModel(self,m_id,m_cls,useContext=False):
        if useContext and not self.__context is None:
            return self.__getModel(m_id,m_cls,self.__context)
        return self.__getModel(m_id,m_cls,self.__modelsByClassById)

    def delete(self,model):
        m_id = model.get_id()
        m_cls = model.__class__
        if self.hasModel(m_id,m_cls):
            del self.__modelsByClassById[m_cls][m_id]

    def getSources(self):
        return self.getMdlSubTypes(ASource)

    def getVariables(self):
        return self.getMdlSubTypes(AVariable)

    def getPlotModels(self):
        return self.getMdlSubTypes(APlotModel)

    def getProjections(self):
        return self.getMdlSubTypes(AProjection)

    def getSlides(self):
        return self.getMdlSubTypes(ASlide)

