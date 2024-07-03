import cdeepso as cd
import numpy as np
import matplotlib.pyplot as plt
# c = np.zeros(shape=(100,51))
# bests = []
# for i in range(30):
#     aux = cd.CDEEPSO(cd.rastrigin,0.6,Npar=100, Niter = 100, mode = 3, LS= True, dim = 50, pert = 0.027 ,w = [0.079, 0.9, 0.9],verbose=False)[1][-1]
#     bests.append(aux[-1].copy())
#
# plt.boxplot(bests)
# plt.show()
# hist = cd.CDEEPSO(cd.rastrigin,0.6, Niter = 100, mode = 3, LS= False, dim = 50, pert = 0.027 ,w = [0.079, 0.9, 0.9], verbose=False)[1]
# print(hist[-1])

rosenTen = cd.buscaParametros(cd.rosen, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=True)
print(rosenTen)
rosenTird = cd.buscaParametros(cd.rosen, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=True)
print(rosenTird)
rosenFifty = cd.buscaParametros(cd.rosen, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=True)
print(rosenFifty)
rasTen = cd.buscaParametros(cd.rastrigin, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=True)
print(rasTen)
rasTird = cd.buscaParametros(cd.rastrigin, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=True)
print(rasTird)
rasFifty = cd.buscaParametros(cd.rastrigin, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=True)
print(rasFifty)
rosenTen = cd.buscaParametros(cd.rosen, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=False)
print(rosenTen)
rosenTird = cd.buscaParametros(cd.rosen, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=False)
print(rosenTird)
rosenFifty = cd.buscaParametros(cd.rosen, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=False)
print(rosenFifty)
rasTen = cd.buscaParametros(cd.rastrigin, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=False)
print(rasTen)
rasTird = cd.buscaParametros(cd.rastrigin, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=True)
print(rasTird)
rasFifty = cd.buscaParametros(cd.rastrigin, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=True)
print(rasFifty)
