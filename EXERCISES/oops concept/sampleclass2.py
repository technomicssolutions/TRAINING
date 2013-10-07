class point:
    def _init_( self, x=0, y=0):
        self.x = x
        self.y = y
    def _del_(self):
        class_name = self._class_._name_
        print class_name,"destroyed"
pt1 = point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)
del pt1
del pt2
del pt3
   
