import YuanXian.Core

structure TCSR_Field

def T_μν_TCSR : Tensor := ...

def ρ_net := spatial_average (expectation T_00_TCSR)
def p_net := (1/3) * spatial_average (expectation (T_ii_TCSR))
