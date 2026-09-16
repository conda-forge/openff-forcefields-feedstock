from openff.toolkit import ForceField
from packaging.version import Version

from openforcefields import __version__

print(f"Version in memory is {__version__=}")
assert Version(__version__) > Version("0.0.0")

ForceField("openff-1.0.0.offxml")
ForceField("openff_unconstrained-1.3.1.offxml")
ForceField("openff-2.1.0.offxml")
ForceField("openff-2.2.0-rc1.offxml")
ForceField("openff-2.2.1.offxml")
ForceField("openff_unconstrained-2.2.0-rc1.offxml")
ForceField("tip3p.offxml")
ForceField("tip4p_fb-1.0.1.offxml")
ForceField("tip5p.offxml")
ForceField("opc3.offxml")
ForceField("opc.offxml")
ForceField("spce-1.0.0.offxml")
ForceField("openff-2.3.0.offxml")
ForceField("openff_no_water-3.0.0-alpha0.offxml")
ForceField("openff_no_water-3.0.0-alpha2b.offxml")
