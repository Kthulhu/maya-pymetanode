

import pymel.core as pm
import pymel.api as api
import maya.OpenMaya as OpenMaya


__all__ = [
    'getMetaData',
    'getMObject',
    'getUUID',
    'hasAttr',
    'hasAttrFast',
]

META_ATTR = 'pymetadata'


def hasAttr(node, attrName):
    """
    Return True if the given node has the given attribute.
    
    Args:
        node: A MObject, PyMel node, or string representing a node
        attrName: A string name of an attribute to test
    """
    if isinstance(node, OpenMaya.MObject):
        return hasAttrFast(node, attrName)
    elif isinstance(node, pm.nt.DependNode):
        return hasAttrFast(node.__apimobject__(), attrName)
    else:
        return pm.cmds.objExists(node + '.' + attrName)

def hasAttrFast(mobject, attrName):
    """
    Return True if the given node has the given attribute.
    Performs no validation or type-checking.

    Args:
        mobject: A MObject node
    """
    try:
        api.MFnDependencyNode(mobject).attribute(attrName)
        return True
    except RuntimeError:
        return False

def getMObject(nodeName):
    """
    Return the MObject from the scene for the given node name

    Args:
        nodeName: A string node name
    """
    sel = api.MSelectionList()
    sel.add(nodeName)
    node = api.MObject()
    sel.getDependNode(0, node)
    return node

def getUUID(nodeName):
    """
    Return the UUID of the given node

    Args:
        nodeName: A string node name
    """
    sel = OpenMaya.MSelectionList()
    sel.add(nodeName)
    node = OpenMaya.MObject()
    sel.getDependNode(0, node)
    val = OpenMaya.MFnDependencyNode(node)
    return val.uuid().asString()


def getMetaData(node):
    """
    Return all meta data on the given node

    Args:
        node: A PyMel node or string node name
    """
    pass