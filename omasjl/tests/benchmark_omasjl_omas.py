import omasjl
import omas

import time
def benchmark(ods, n=100):
    for k in range(n):
        omas.omas_machine.d3d.gas_injection_hardware(ods, 133221)
    return None

start_time = time.time()
ods = omasjl.ODS()
benchmark(ods)
end_time = time.time()
print(f"Execution time in omasjl: {end_time - start_time:.6f} seconds")

start_time = time.time()
ods = omas.ODS()
benchmark(ods)
end_time = time.time()
print(f"Execution time in omas: {end_time - start_time:.6f} seconds")
