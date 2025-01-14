import omasjl
import omas

ods = omasjl.ODS()

# simple scalars, no MDS+
omas.omas_machine.d3d.gas_injection_hardware(ods, 133221)

# MDS+
omas.omas_machine.d3d.interferometer_hardware(ods, 170325)
omas.omas_machine.d3d.interferometer_data(ods, 170325)

# MDS+ with CodeParameters
omas.omas_machine.d3d.ec_launcher_active_hardware(ods, 170325)

# MDS+ with omfit_classes
omas.omas_machine.d3d.core_profiles_global_quantities_data(ods, 133221)
