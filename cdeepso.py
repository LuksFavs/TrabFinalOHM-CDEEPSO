import math
import numpy as np


def rastrigin(x):
    aux = 10*len(x)
    soma = 0
    for i in range(len(x)):
       soma += x[i]*x[i] - 10 * math.cos(2*math.pi*x[i])
    return aux + soma

def rosen(x):
  """Generalized n-dimensional version of the Rosenbrock function"""
  return sum(100*(x[1:]-x[:-1]**2.0)**2.0 +(1-x[:-1])**2.0)

def Extract(lista, n=0):
    listac = lista.copy()
    return [item[n] for item in listac]

def DEEPSO(func,tau,mode = 1, LS = False, Niter = 30, Npar = 30, dim = 2, w = []):
  ## mode:
  ##  1 = personal best , 2 = aleaorio da pop,
  ##  3 = aleatorio da pop passada, 4 = media de 2 e 3
  ## LS = local Search

  x = np.random.uniform(-5.,5.,(Npar, dim+1))
  p = math.floor(0.1 * Npar)
  percent = math.floor(0.1 * Npar)
  xbef = np.zeros((percent, dim+1))
  v = np.zeros((Npar,dim+1))
  hist = np.zeros((Niter,dim+1))
  part = range(Npar)
  histsumW = []
  melhorei = []
  for i in part:
    value = func(x[i][:dim])
    x[i][-1] = value
  melhorIdx = np.argmin(Extract(x, -1))
  if w == []:
    w=np.random.uniform(size=3)
  for i in range(Niter):
    for j in part:
      #w=w/w[1]+w[2]+w[0]
      histsumW.append(sum(w))
      #print(histsumW)
      C = np.random.binomial(1,tau,size=dim+1)
      if mode == 1 or mode == 2:
        xnow = x.copy()
        num = np.random.randint(0,Npar) if mode == 2 else j
        xr = xnow[num]
      elif mode == 3:
        num = np.random.randint(0,percent)
        xr = xbef[num]
      else:
        xnow = x.copy()
        num1 = np.random.randint(0,Npar)
        num2 = np.random.randint(0,percent)
        xr=(xnow[num1] + xbef[num2])/2

      tv = w[0] * v[j] + w[1] * (xr - x[j]) + w[2] * C * (x[melhorIdx]-x[j])
      tx = x[j] + tv
      tx[-1] = func(tx[:dim])
      if tx[-1]<x[j][-1]:
        x[j] = tx.copy()
        v[j] = tv.copy()
      if x[j][-1] < xr[-1] and type == 1:
        xnow[j] = x[j].copy()
      if x[j][-1] < x[melhorIdx][-1]:
        melhorIdx = j
    if LS and ((i % 19) == 0) :
      vel = v[melhorIdx].copy()
      candidato = x[melhorIdx].copy()
      for local in range(10):
        vel1 = vel + np.random.uniform(-0.1,0.1, dim+1)
        vel2 = vel + np.random.uniform(-0.1,0.1, dim+1)
        a, b, c = func((candidato + vel)[:dim]), func((candidato + vel1)[:dim]), func((candidato + vel2)[:dim])
        tentativa = [a, b, c]
        if tentativa[0] < candidato[-1]:
          candidato = (candidato + vel).copy()
          candidato[-1] = tentativa[0]
          melhorei.append([i,local,'a', candidato[-1]])
        elif tentativa[1] < candidato[-1]:
          candidato = (candidato + vel1).copy()
          vel = vel1
          candidato[-1] = tentativa[1]
          melhorei.append([i,local,'b',tentativa[1]])
        elif tentativa[2] < candidato[-1]:
          candidato = (candidato + vel2).copy()
          vel = vel2
          candidato[-1] = tentativa[2]
          melhorei.append([i,local,'c',tentativa[2]])
        x[melhorIdx] = candidato.copy()
        v[melhorIdx] = vel.copy()

    idx = np.argpartition(Extract(x,-1), percent)
    for n in range(percent):
      xbef[n] = x[idx[n]].copy()
    hist[i]+=x[melhorIdx]

  return(x, hist, histsumW, melhorei, w)



def CDEEPSO(func,tau,mode = 1, LS = False, Niter = 30, Npar = 30, dim = 2, pert = 0.0, w=[], verbose=False, limites = [-5.,5.]):
  ## mode:
  ##  1 = personal best , 2 = aleaorio da pop,
  ##  3 = aleatorio da pop passada, 4 = media de 2 e 3
  ## LS = local Search

  x = np.random.uniform(limites[0], limites[1],(Npar, dim+1))
  p = math.floor(0.1 * Npar)
  percent = math.floor(0.1 * Npar)
  xbef = np.zeros((percent, dim+1))
  v = np.zeros((Npar,dim+1))
  hist = np.zeros((Niter,dim+1))
  part = range(Npar)
  histsumW = []
  melhorei = []
  for i in part:
    value = func(x[i][:dim])
    x[i][-1] = value
  melhorIdx = np.argmin(Extract(x, -1))
  if pert == 0: 
    pert=np.random.uniform(0,1)
  if w == []:
    w=np.random.uniform(size=3)
  for i in range(Niter):
    for j in part:
      #w=w/w[1]+w[2]+w[0]
      histsumW.append(sum(w))
      #print(histsumW)
      C = np.random.binomial(1,tau,size=dim+1)
      if mode == 1 or mode == 2:
        xnow = x.copy()
        num = np.random.randint(0,Npar) if mode == 2 else j
        xr = xnow[num]
      elif mode == 3:
        num = np.random.randint(0,percent)
        xr = xbef[num]
      else:
        xnow = x.copy()
        num1 = np.random.randint(0,Npar)
        num2 = np.random.randint(0,percent)
        xr=(xnow[num1] + xbef[num2])/2
      
      xst = xr + pert * (x[melhorIdx] - xr) + pert * (x[np.random.randint(0,Npar)]-x[np.random.randint(0,Npar)])

      tv = w[0] * v[j] + w[1] * (xst - x[j]) + w[2] * C * (x[melhorIdx]-x[j])
      tx = x[j] + tv
      tx[-1] = func(tx[:dim])
      if tx[-1]<x[j][-1]:
        x[j] = tx.copy()
        v[j] = tv.copy()
      if x[j][-1] < xr[-1] and type == 1:
        xnow[j] = x[j].copy()
      if x[j][-1] < x[melhorIdx][-1]:
        melhorIdx = j
    if LS and ((i % 19) == 0) :
      vel = v[melhorIdx].copy()
      candidato = x[melhorIdx].copy()
      for local in range(10):
        vel1 = vel + np.random.uniform(-0.1,0.1, dim+1)
        vel2 = vel + np.random.uniform(-0.1,0.1, dim+1)
        a, b, c = func((candidato + vel)[:dim]), func((candidato + vel1)[:dim]), func((candidato + vel2)[:dim])
        tentativa = [a, b, c]
        if tentativa[0] < candidato[-1]:
          candidato = (candidato + vel).copy()
          candidato[-1] = tentativa[0]
          melhorei.append([i,local,'a', candidato[-1]])
        elif tentativa[1] < candidato[-1]:
          candidato = (candidato + vel1).copy()
          vel = vel1
          candidato[-1] = tentativa[1]
          melhorei.append([i,local,'b',tentativa[1]])
        elif tentativa[2] < candidato[-1]:
          candidato = (candidato + vel2).copy()
          vel = vel2
          candidato[-1] = tentativa[2]
          melhorei.append([i,local,'c',tentativa[2]])
        x[melhorIdx] = candidato.copy()
        v[melhorIdx] = vel.copy()

    idx = np.argpartition(Extract(x,-1), percent)
    for n in range(percent):
      xbef[n] = x[idx[n]].copy()
    hist[i]+=x[melhorIdx]
  
  if verbose: 
    print(pert, w, hist[-1][-1])
  params = [pert, w]
  return(x, hist, histsumW, melhorei, params)

def buscaParametros(func, tau, dim, nIter, nPar, md, c=False):
    result = []
    for i in range(100):
        if c :
            _, hist, _, _, para = CDEEPSO(func, tau, mode=md, Niter=nIter, Npar=nPar, dim=dim)
        else:
            _,hist,_,_, para = DEEPSO(func,tau,mode = md, LS = False, Niter = nIter, Npar = nPar, dim = dim)
        result.append([hist[-1], para])

    result.sort(key=lambda x: x[0][-1])

    return result[0]
