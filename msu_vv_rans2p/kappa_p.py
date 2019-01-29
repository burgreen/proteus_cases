from proteus.default_p import *
from proteus.mprans import Kappa
from main_param	import *
from user_param import * 

LevelModelType = Kappa.LevelModel

dissipation_model_flag = 1
if user_param.useRANS == 2:
    dissipation_model_flag = 2
elif user_param.useRANS == 3:
    dissipation_model_flag = 3

RD_model = None
LS_model = None
ME_model = 1
dissipation_model = 2

coefficients = Kappa.Coefficients(V_model=int(movingDomain)+0,
                                  ME_model=ME_model,
                                  LS_model=LS_model,
                                  RD_model=RD_model,
                                  dissipation_model=dissipation_model,
#1 -- K-epsilon, 2 -- K-omega 1998, 3 -- K-omega 1988
                                  dissipation_model_flag=dissipation_model_flag,
                                  useMetrics=user_param.useMetrics,
                                  rho_0=user_param.rho_water,
                                  nu_0=user_param.nu_water,
                                  rho_1=user_param.rho_air,
                                  nu_1=user_param.nu_air,
                                  #g=user_param.gravity,
                                  g=numpy.array([user_param.gravity[0],
                                                 user_param.gravity[1],
                                                 user_param.gravity[2]], dtype='d'),
                                  nd=user_param.nd,
                                  c_mu=0.09,
                                  sigma_k=1.0,
                                  sc_uref=user_param.kappa_sc_uref,
                                  sc_beta=user_param.kappa_sc_beta)

dirichletConditions = {0: lambda x, flag: domain.bc[flag].k_dirichlet.init_cython()}
advectiveFluxBoundaryConditions = {0: lambda x, flag: domain.bc[flag].k_advective.init_cython()}
diffusiveFluxBoundaryConditions = {0: {0: lambda x, flag: domain.bc[flag].k_diffusive.init_cython()}}



class ConstantIC:
    def __init__(self, cval=0.):
        self.cval = cval
    def uOfXT(self, x, t):
        return self.cval

initialConditions = {0: ConstantIC(cval=0)}
