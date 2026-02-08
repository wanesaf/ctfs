import angr
import claripy

p = angr.Project('../stackstrings_hard', auto_load_libs=False)

BASE_ADDR = p.loader.main_object.mapped_base

FLAG_LEN = 41

flag_chars = [claripy.BVS(f'char_{i}', 8) for i in range(FLAG_LEN)]
flag_combined = claripy.Concat(*flag_chars)

state = p.factory.entry_state(stdin=flag_combined)


find_offset = 0x1593  # Offset where the "Success" write loop starts
avoid_offset = 0x14d0 # Offset where the "Failure" write (LABEL_15) starts

target_addr = BASE_ADDR + find_offset
avoid_addr = BASE_ADDR + avoid_offset

simgr = p.factory.simulation_manager(state)


simgr.explore(find=target_addr, avoid=avoid_addr)

if simgr.found:
    solution_state = simgr.found[0]
    flag = solution_state.solver.eval(flag_combined, cast_to=bytes)
    print(f"\n[+] Success! Flag: {flag.decode(errors='ignore')}")
else:
    print("\n[-] Path not found. Check if the avoid address is cutting off the correct path.")
