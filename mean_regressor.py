class MeanRegressor:

    # # commenting out for now since this is throwing errors    
    # def __init__(self, X, y):
    #     self.X = X
    #     self.y = y
        
    def fit(self, X, y):
        self.y_mean = sum(y)/len(y)
        return None

    def predict(self, X):
        self.yy = []
        i = 0
        while i < len(X):
            self.yy.append(self.y_mean)
            i+=1
        return self.yy

    def score(self,X,y):
        rreslist = (y-self.predict(X))**2
        rtotlist = []
        i = 0
        for n in y:
            rtotlist.append((n-sum(y)/len(y))**2)
        self.rsquared = 1 - sum(rreslist)/sum(rtotlist)
        return self.rsquared

