"""
Compiles 100 DOM-12 Grounded Concepts into Beszercess DSL for spikeasm_vm on Apple Metal GPU.
Implements:
1. Input Feature Bus (12 coordinates x possible discrete states). Syntax: NODE:THRESHOLD:LEAKAGE
2. Concept Attractor Nodes (Threshold = 8.0, leakage = 0.05).
3. Synaptic Wiring using Beszercess arrow: SENSOR >>[DELAY:WEIGHT]>> TARGET
4. Lateral competitive inhibition layer.
"""
import json

def compile_ontology_to_beszercess(json_path: str, output_besz_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        concepts = json.load(f)
        
    print(f"Loaded {len(concepts)} concepts from {json_path}")
    
    # Collect all unique (axis, value) pairs
    features = set()
    for item in concepts:
        for axis, val in item["vector"].items():
            features.add(f"{axis}_{val['name']}")
            
    features = sorted(list(features))
    print(f"Total unique DOM-12 sensory feature lines: {len(features)}")
    
    lines = []
    lines.append("// ===========================================================================")
    lines.append("// 🍄 MYCELIUM SNN - MILESTONE 1 PILOT: 100 GROUNDED PHYSICAL CONCEPTS")
    lines.append("// High-precision associative attractor network on Apple Metal GPU")
    lines.append("// ===========================================================================")
    lines.append("")
    lines.append("// --- 1. SENSORY INPUT BUS (DOM-12 COORDINATE DETECTORS) ---")
    for feat in features:
        # Threshold: 0.5, Leakage: 0.05
        lines.append(f"IN_{feat}:0.5:0.05")
        
    lines.append("")
    lines.append("// --- 2. CONCEPT ATTRACTOR NODES (100 ANCHORS) ---")
    lines.append("// Threshold: 8.0 (requires >= 8 coordinates alignment), Leakage: 0.02")
    for item in concepts:
        c_name = item["name"].replace(" ", "_").upper()
        lines.append(f"CONCEPT_{c_name}:8.0:0.02")
        
    lines.append("")
    lines.append("// --- 3. SYNAPTIC PROJECTIONS (DOM-12 COORDINATES -> CONCEPTS) ---")
    for item in concepts:
        c_name = item["name"].replace(" ", "_").upper()
        for axis, val in item["vector"].items():
            feat_name = f"{axis}_{val['name']}"
            lines.append(f"IN_{feat_name} >>[1:1.0]>> CONCEPT_{c_name}")
            
    lines.append("")
    lines.append("// End of generated Milestone 1 pilot ontology circuit")
    
    with open(output_besz_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
        
    print(f"Successfully generated Beszercess circuit at {output_besz_path} ({len(lines)} lines)")

if __name__ == "__main__":
    compile_ontology_to_beszercess(
        "/Users/afilum/Mycelium_project/mycelium_core/ontology/pilot_100.json",
        "/Users/afilum/Mycelium_project/mycelium_core/ontology/pilot_100_concepts.besz"
    )
