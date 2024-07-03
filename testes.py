import cdeepso as cd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

d = np.zeros(shape=(100,11))
c = np.zeros(shape=(100,11))
bests = []
bestsc = []
for i in range(30):
    hist = cd.DEEPSO(cd.rosen,0.6,Npar=100, Niter = 100, mode = 3, LS= False, dim = 10, w = [0.321, 0.094, 0.895])[1]
    histc = cd.CDEEPSO(cd.rosen,0.6,Npar=100, Niter = 100, mode = 3, LS= False, dim = 10,pert =0.853 , w = [0.054, 0.842, 0.098])[1]
    bests.append(hist[-1][-1].copy())
    bestsc.append(histc[-1][-1].copy())
    c+=histc
    d+=hist

c=c/30
d=d/30
figure, axis = plt.subplots(1, 2)
axis[0].boxplot([bests, bestsc], labels=["DEEPSO", "CDEEPSO"])
axis[0].set_title("DEEPSO - rosen d=10")
axis[1].boxplot([bests, bestsc], labels=["DEEPSO", "CDEEPSO"])
axis[1].set_yscale('log')
axis[1].set_title(" DEEPSO - rosen d=10 - log")
plt.tight_layout()
plt.savefig("DEEPSOVSCRosen10-bests.png")
print("DEEPSO: ", np.mean(bests), np.std(bests), np.max(bests), np.min(bests) )
print("C-DEEPSO: ", np.mean(bestsc), np.std(bestsc), np.max(bestsc), np.min(bestsc) )
print(stats.ttest_ind(bests, bestsc))
plt.show()

# rosenTen = cd.buscaParametros(cd.rosen, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=True)
# print(rosenTen)
# rosenTird = cd.buscaParametros(cd.rosen, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=True)
# print(rosenTird)
# rosenFifty = cd.buscaParametros(cd.rosen, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=True)
# print(rosenFifty)
# rasTen = cd.buscaParametros(cd.rastrigin, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=True)
# print(rasTen)
# rasTird = cd.buscaParametros(cd.rastrigin, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=True)
# print(rasTird)
# rasFifty = cd.buscaParametros(cd.rastrigin, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=True)
# print(rasFifty)
# rosenTen = cd.buscaParametros(cd.rosen, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=False)
# print(rosenTen)
# rosenTird = cd.buscaParametros(cd.rosen, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=False)
# print(rosenTird)
# rosenFifty = cd.buscaParametros(cd.rosen, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=False)
# print(rosenFifty)
# rasTen = cd.buscaParametros(cd.rastrigin, 0.6,dim = 10, nIter = 100, nPar=100, md = 3, c=False)
# print(rasTen)
# rasTird = cd.buscaParametros(cd.rastrigin, 0.6,dim = 30, nIter = 100, nPar=100, md = 3, c=False)
# print(rasTird)
# rasFifty = cd.buscaParametros(cd.rastrigin, 0.6,dim = 50, nIter = 100, nPar=100, md = 3, c=False)
# print(rasFifty)
