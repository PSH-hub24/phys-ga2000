import matplotlib.pyplot as plt
import numpy as np
import jax
import jax.numpy as jnp
import scipy.optimize as optimize

xpath = []
def squirrel(xk):
    global xpath
    xpath.append(np.array(xk))

def f1(x):
	return jnp.exp(x)

def f2(x):
	return jnp.log(1+x)

def f3(x):
	return f2(f1(x))

def Negloglike(params, *args):
	beta0 = params[0]
	beta1 = params[1]
	age = args[0]
	respond = args[1]
	exponent = beta0 + beta1*age
	l = (respond-1) * exponent - f3(-exponent)
	return -l.sum()
	
def Hessian(f):
  return jax.jacfwd(jax.grad(f))

surveyData = np.genfromtxt('survey.csv', delimiter=',')
surveyData = surveyData[1:]
age = surveyData[:,0]
respond = surveyData[:,1]

negloglikeGrad = jax.grad(Negloglike)
pst = np.array([1., 1.])
xpath = [pst]
r = optimize.minimize(Negloglike, pst, jac=negloglikeGrad, args=(age,respond), method='BFGS', tol=1e-6, callback=squirrel)
xpath = np.array(xpath)
print('Maximum likelihood values of beta0 and beta1:')
print(r.x)
print("Number of function evaluations: {n}".format(n=r.nfev))
print("Number of iterations: {n}".format(n=r.nit))

h = Hessian(Negloglike)
hmat = np.array(h(r.x, age, respond))
covar = np.linalg.inv(hmat)
print('Covariance matrix:')
print(covar)
print('Formal errors:')
print(np.sqrt(np.diag(covar)))

plt.scatter(age, respond, label='Survey data', color='black')
xArr = np.linspace(min(age), max(age), 500)
beta0 = r.x[0]
beta1 = r.x[1]
pArr = 1 / (1 + np.exp(-(beta0+beta1*xArr)))
plt.plot(xArr, pArr, label='Logistic Model', color='red')

plt.xlabel('Age')
plt.ylabel('Probability of Yes (1)')
plt.legend(loc='center right')
plt.savefig('ps8Figures/q1Plot.png')