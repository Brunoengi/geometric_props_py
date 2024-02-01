class GeometricProps:

    def __init__(self, arr):
        
        self.A, self.Sx, self.Sy, self.Ix, self.Iy, self.Ixy  = 0, 0, 0, 0, 0, 0 
        self.Xmax, self.Ymax, self.Xmin, self.Ymin, self.Xg, self.Yg, self.Ixg, self.Iyg, self.Ixyg, self.Y1, self.Y2, self.W1, self.W2, self.h = None, None, None, None, None, None, None, None, None, None, None, None, None, None
    
        for i in range(len(arr) - 1):

            x0, x1 = arr[i]['x'], arr[i + 1]['x']
            y0, y1 = arr[i]['y'], arr[i + 1]['y']

            dx, dy = x1 - x0, y1 - y0

            self.set_area(x0, dx, dy)
            self.set_Sx(x0, y0, dx, dy)
            self.set_Sy(x0, dx, dy)
            self.set_Ix(x0, y0, dx, dy)
            self.set_Iy(x0, dx, dy)
            self.set_Ixy(x0, y0, dx, dy)
            
        
        self.set_Xg()
        self.set_Yg()
        self.set_Ixg()
        self.set_Iyg()
        self.set_Ixyg()
       

        for j in range(len(arr)):
            self.set_XMax(arr[j]['x'])
            self.set_XMin(arr[j]['x'])

            self.set_YMax(arr[j]['y'])
            self.set_YMin(arr[j]['y'])

        self.set_h()
        self.set_Y1()
        self.set_Y2()
        self.set_W1()
        self.set_W2()

        self.sumSignCorrection()

    def set_area(self, x0, dx, dy):
        self.A += (x0 + dx / 2) * dy
    
    def set_Sx(self, x0, y0, dx, dy):
        self.Sx += (x0 * (y0 + dy / 2) + dx * (y0 / 2 + dy / 3)) * dy

    def set_Sy(self, x0, dx, dy):
        self.Sy += (x0 * (x0 + dx) + dx ** 2 / 3) * dy / 2

    def set_Ix(self, x0, y0, dx, dy):
        self.Ix += (
            x0 * (y0 * (dy + y0) + dy ** 2 / 3)
            + dx * (y0 * (y0 / 2 + 2 * dy / 3) + dy ** 2 / 4)
        ) * dy
        
    def set_Iy(self, x0, dx, dy):
        self.Iy += (dx ** 3 / 4 + x0 * (dx ** 2 + x0 * (3 * dx / 2 + x0))) * dy / 3

    def set_Ixy(self, x0, y0, dx, dy):
        self.Ixy += (
            x0 * (x0 * (y0 + dy / 2) + dx * (y0 + 2 * dy / 3))
            + dx ** 2 * (y0 / 3 + dy / 4)
        ) * dy / 2

    def set_Xg(self):
        self.Xg = self.Sy / self.A

    def set_Yg(self):
        self.Yg = self.Sx / self.A

    def set_Ixg(self):
        self.Ixg = self.Ix - self.Yg ** 2 * self.A

    def set_Iyg(self):
        self.Iyg = self.Iy - self.Xg ** 2 * self.A

    def set_Ixyg(self):
        self.Ixyg = self.Ixy - self.Xg * self.Yg * self.A

    def set_Y1(self):
        self.Y1 = abs(self.Yg - self.Ymin)

    def set_Y2(self):
        self.Y2 = abs(self.Ymax - self.Yg)

    def set_W1(self):
        self.W1 = self.Ixg / self.Y1

    def set_W2(self):
        self.W2 = self.Ixg / self.Y2

    def set_h(self):
        self.h = abs(self.Ymax - self.Ymin)

    def set_XMax(self, arrPositionx):
        if(self.Xmax is None or arrPositionx >= self.Xmax):
            self.Xmax = arrPositionx

    def set_XMin(self, arrPositionx):
        if(self.Xmin is None or arrPositionx <= self.Xmin):
            self.Xmin = arrPositionx

    def set_YMax(self, arrPositiony):
        if(self.Ymax is None or arrPositiony >= self.Ymax):
            self.Ymax = arrPositiony

    def set_YMin(self, arrPositiony):
        if(self.Ymin is None or arrPositiony <= self.Xmin):
            self.Ymin = arrPositiony

    def sumSignCorrection(self):
        self.Y1 *= - 1
        self.W1 *= -1

