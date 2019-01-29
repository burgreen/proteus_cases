from proteus.default_n import *
from proteus import (StepControl,
                     TimeIntegration,
                     NonlinearSolvers,
                     LinearSolvers,
                     LinearAlgebraTools)
from proteus.mprans import Kappa
import kappa_p as physics
from main_param import *
from user_param import user_param

if timeIntegration == "VBDF":
    timeIntegration = TimeIntegration.VBDF
    timeOrder = 2
else:
    timeIntegration = TimeIntegration.BackwardEuler_cfl
stepController = StepControl.Min_dt_controller

femSpaces = {0: basis}

massLumping       = False
numericalFluxType = Kappa.NumericalFlux
conservativeFlux  = None
subgridError      = Kappa.SubgridError(coefficients=physics.coefficients,
                                       nd=nd)
shockCapturing    = Kappa.ShockCapturing(coefficients=physics.coefficients,
                                         nd=nd,
                                         shockCapturingFactor=user_param.kappa_shockCapturingFactor,
                                         lag=user_param.kappa_lag_shockCapturing)

fullNewtonFlag  = True
multilevelNonlinearSolver = NonlinearSolvers.Newton
levelNonlinearSolver      = NonlinearSolvers.Newton

nonlinearSmoother = None
linearSmoother    = None
#printNonlinearSolverInfo = True

matrix = LinearAlgebraTools.SparseMatrix

if not useOldPETSc and not useSuperlu:
    multilevelLinearSolver = LinearSolvers.KSP_petsc4py
    levelLinearSolver      = LinearSolvers.KSP_petsc4py
else:
    multilevelLinearSolver = LinearSolvers.LU
    levelLinearSolver      = LinearSolvers.LU

linear_solver_options_prefix = 'kappa_'
levelNonlinearSolverConvergenceTest = 'rits'
linearSolverConvergenceTest         = 'rits'

tolFac = 0.
linTolFac = 0.
l_atol_res = 0.001*kappa_nl_atol_res
nl_atol_res = kappa_nl_atol_res
useEisenstatWalker = False

maxNonlinearIts = 50
maxLineSearches = 0
