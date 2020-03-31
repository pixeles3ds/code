
from edtools import *

from edtools.Tools import EdTree

t = EdTree.Tree()

t.setTree( t.getExampleTree() )


t.printTree()




print("-"*100)

#t.rename( "free","pago" ).rename("tiempo","tiempoLluvioso").rename("folder","path")

print("-"*100)


t.getFullPath()
