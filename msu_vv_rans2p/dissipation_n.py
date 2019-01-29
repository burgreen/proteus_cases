from proteus.default_n import *
import dissipation_p as physics
from proteus import (StepControl,
                     TimeIntegration,
                     NonlinearSolvers,
                     LinearSolvers,
                     LinearAlgebraTools)
from proteus.mprans import Dissipation
from proteus import Context
from main_param import *
from user_param import user_param

if timeIntegration == "VBDF":
    timeIntegration = TimeIntegration.VBDF
    timeOrder = 2
else:
    timeIntegration = TimeIntegration.BackwardEuler_cfl
stepController  = StepControl.Min_dt_controller

femSpaces = {0: basis}
elementQuadrature = elementQuadrature
elementBoundaryQuadrature = elementBoundaryQuadrature

massLumping       = False
numericalFluxType = Dissipation.NumericalFlux
conservativeFlux  = None
subgridError      = Dissipation.SubgridError(coefficients=physics.coefficients,
                                             nd=nd)
shockCapturing    = Dissipation.ShockCapturing(coefficients=physics.coefficients,
                                               nd=nd,
                                               shockCapturingFactor=user_param.dissipation_shockCapturingFactor,
                                               lag=user_param.dissipation_lag_shockCapturing)

fullNewtonFlag  = True
multilevelNonlinearSolver = NonlinearSolvers.Newton
levelNonlinearSolver      = NonlinearSolvers.Newton

nonlinearSmoother = None
linearSmoother    = None

matrix = LinearAlgebraTools.SparseMatrix

if not useSuperlu:
    multilevelLinearSolver = LinearSolvers.KSP_petsc4py
    levelLinearSolver      = LinearSolvers.KSP_petsc4py
else:
    multilevelLinearSolver = LinearSolvers.LU
    levelLinearSolver      = LinearSolvers.LU

linear_solver_options_prefix = 'dissipation_'
levelNonlinearSolverConvergenceTest = 'rits'
linearSolverConvergenceTest         = 'rits'

tolFac = 0.0
linTolFac =0.0
l_atol_res = 0.001*dissipation_nl_atol_res
nl_atol_res = dissipation_nl_atol_res
useEisenstatWalker = False

maxNonlinearIts = 50
maxLineSearches = 0
