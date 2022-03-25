from .z3 import *
from collections.abc import Generator
from typing import Any

def vset(seq, idfun: Any | None = ..., as_list: bool = ...) -> Generator[None, None, Any]: ...
def get_z3_version(as_str: bool = ...): ...
def ehash(v): ...
def is_expr_var(v): ...
def is_expr_val(v): ...
def get_vars(f, rs: Any | None = ...): ...
def mk_var(name, vsort): ...
def prove(claim, assume: Any | None = ..., verbose: int = ...): ...
def get_models(f, k): ...
def is_tautology(claim, verbose: int = ...): ...
def is_contradiction(claim, verbose: int = ...): ...
def exact_one_model(f): ...
def myBinOp(op, *L): ...
def myAnd(*L): ...
def myOr(*L): ...
def myImplies(a, b): ...
def Iff(f): ...
def model_str(m, as_str: bool = ...): ...