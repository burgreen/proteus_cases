from proteus import *
from proteus.default_p import *
from proteus.mprans import Dissipation
from main_param import *
from user_param import user_param

LevelModelType = Dissipation.LevelModel
RD_model = None
LS_model = None
ME_model = 2
#kappa_model = 1
#should not include this dissipation_model = 3

dissipation_model_flag = 1
if useRANS == 2:
    dissipation_model_flag=2
elif useRANS == 3:
    dissipation_model_flag=3


coefficients = Dissipation.Coefficients(V_model=int(movingDomain)+0,
                                        ME_model=ME_model,
                                        LS_model=LS_model,
                                        RD_model=RD_model,
#                                        kappa_model=kappa_model,
                                        dissipation_model_flag=dissipation_model_flag,#1 -- K-epsilon, 2 -- K-omega 1998, 3 -- K-omega 1988
                                        useMetrics=user_param.useMetrics,
                                        rho_0=user_param.rho_water,nu_0=user_param.nu_water,
                                        rho_1=user_param.rho_air,nu_1=user_param.nu_air,
                                        #g=user_param.gravity,
                                        g=numpy.array([user_param.gravity[0],
                                                       user_param.gravity[1],
                                                       user_param.gravity[2]], dtype='d'),
                                        c_mu=0.09,sigma_e=1.0,
                                        sc_uref=user_param.dissipation_sc_uref,
                                        sc_beta=user_param.dissipation_sc_beta)

dirichletConditions = {0: lambda x, flag: domain.bc[flag].dissipation_dirichlet.init_cython()}
advectiveFluxBoundaryConditions = {0: lambda x, flag: domain.bc[flag].dissipation_advective.init_cython()}
diffusiveFluxBoundaryConditions = {0: {0: lambda x, flag: domain.bc[flag].dissipation_diffusive.init_cython()}}



class ConstantIC:
    def __init__(self, cval=0.):
        self.cval = cval
    def uOfXT(self, x, t):
        return self.cval

kInflow = 0.
#xw hardwired
dissipationInflow =0.0
#dissipationInflow = coefficients.c_mu*kInflow**(1.5)/(0.03*tank_dim[nd-1])
if useRANS >= 2:
    dissipationInflow = dissipationInflow/(kInflow+1.0e-12)

initialConditions = {0: ConstantIC(cval=dissipationInflow*0.001)}
