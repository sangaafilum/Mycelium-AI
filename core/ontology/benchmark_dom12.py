"""
Pilot Benchmark & Association Engine for DOM-12 Ontological Reasoning on Metal GPU.
Tests accurate recall, classification latency, and disambiguation dynamics.
"""
import subprocess
import time
import json

def test_concept_recall(concept_name: str, threshold: float = 11.5):
    with open("/Users/afilum/Mycelium_project/mycelium_core/ontology/pilot_100.json") as f:
        concepts = json.load(f)
        
    target = None
    for c in concepts:
        if c["name"].lower() == concept_name.lower():
            target = c
            break
            
    if not target:
        print(f"Concept {concept_name} not found!")
        return
        
    cmd = [
        "/Users/afilum/Mycelium_project/spikeasm_vm_engine/target/release/spikeasm_vm",
        "/Users/afilum/Mycelium_project/mycelium_core/ontology/pilot_100_concepts.besz"
    ]
    
    for axis, val in target["vector"].items():
        cmd.extend(["--spike", f"IN_{axis}_{val['name']}", "1.0", "0"])
        
    t0 = time.perf_counter()
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    t_elapsed = (time.perf_counter() - t0) * 1000.0
    
    fired = []
    for line in res.stdout.splitlines():
        if "ВЫХОДНОЙ ИМПУЛЬС" in line:
            name = line.split("Узел 'CONCEPT_")[1].split("'")[0]
            fired.append(name)
            
    print(f"\n==================================================")
    print(f"🎯 Query Concept: {target['name']} (Domain: {target['domain']})")
    print(f"⚡ Latency: {t_elapsed:.2f} ms")
    print(f"💥 Active Resonators (Threshold={threshold}): {fired}")
    if target["name"].upper() in fired:
        print(f"✅ EXACT RECALL CONFIRMED!")
    else:
        print(f"❌ MISSED TARGET!")
    print(f"==================================================")

if __name__ == "__main__":
    for test_target in ["Apple", "Hammer", "Lightning", "Diamond"]:
        test_concept_recall(test_target)
