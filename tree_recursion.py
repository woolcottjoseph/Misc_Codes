class Leaf:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def print(self):
        return str(self.data)

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def setchildren(self,left,right):
        self.left = left
        self.right = right

def Treesearch(root, searchitem, leftitem, rightitem):
    leftitem = root.getleft()
    rightitem = root.getright()
    print(root.print())
    if leftitem:
        Treesearch(leftitem, searchitem, None, None)
    if rightitem:
        Treesearch(rightitem, searchitem, None, None)
    if root.print() == searchitem:
        print ("Item found! :{}".format(root.print ()))




leaf_a = Leaf("A",None,None)
leaf_b = Leaf("B",None,None)
leaf_h = Leaf("H",None,None)
leaf_g = Leaf("G",None,None)
leaf_f = Leaf("F",leaf_h,None)
leaf_e = Leaf("E",leaf_f,leaf_g)
leaf_c = Leaf("C",leaf_a,leaf_b)
leaf_d = Leaf("D",leaf_e,leaf_c)

Treesearch(leaf_d,"C",None,None)