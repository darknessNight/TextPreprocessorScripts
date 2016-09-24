import re

class IncrementTemplateVars(object):
    
    def __init__(self):
        self.source = ""
        self.outTemplate = ""
        self.outProduct = ""
        self.nameIndex = 0
        self.valueIndex = 1

    def setSource(self, source):
        self.source = source

    def build(self):
        outTemplate,outProduct = self.source,self.source
        for match in self.__getMatchesIterator():
            outProduct, outTemplate = self.__incrementVars(match.group(0), outProduct, outTemplate)
        self.outTemplate,self.outProduct = outTemplate,outProduct
        
    def __getMatchesIterator(self):
        return re.finditer("\{.+?:[0-9]+?\}",self.source)

    def __incrementVars(self, el, outProduct, outTemplate):
        var,value = self.__getVarNameAndValue(el)
        number = self.__getIncrementVal(value)
        return self.__replaceOldVar(el, var, number, outProduct, outTemplate)

    def __getVarNameAndValue(self, string):
        out=string.replace('{','').replace('}','').split(':')
        return out[0],out[1]

    def __getIncrementVal(self, value):
        return int(value) + 1
    
    def __replaceOldVar(self, el, var, number, outProduct, outTemplate):
        outTemplate = self.__changeTemplate(el, var, number, outTemplate)
        outProduct = self.__changeProduct(el, number, outProduct)
        return outProduct, outTemplate

    def __changeTemplate(self, el, var, number, outTemplate):
        outStr = self.__prepareTemplateReplaceString(var, number)
        outTemplate = outTemplate.replace(el,outStr)
        return outTemplate

    def __prepareTemplateReplaceString(self, var, number):
        outStr = "{" + var + ":" + str(number) + "}"
        return outStr

    def __changeProduct(self, el, number, outProduct):
        return outProduct.replace(el,str(number))

    def getTemplate(self):
        return self.outTemplate

    def getProduct(self):
        return self.outProduct
