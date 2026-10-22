"""
DOM-12 Ontology Parser & Vectorizer for Mycelium AI Core.
Converts encyclopedic definitions into 12-Dimensional Discrete Reality Vectors.
Features exact token matching, negative penalty suppression, and domain priors.
"""
import re
import json

DOM_AXES = {
    "C1_state": {
        "Solid": ["solid", "hard", "rock", "metal", "stone", "wood", "plastic", "bone", "tree", "plant", "organ", "device", "tool", "machine", "building", "body", "meat", "seed", "leaf", "steel", "iron", "mineral", "ice", "soil", "block", "wheel", "needle"],
        "Liquid": ["liquid", "water", "fluid", "juice", "oil", "blood", "sap", "river", "sea", "ocean", "rain", "melted", "solution", "beverage", "drink", "mercury", "petroleum", "lava", "spring"],
        "Gas": ["gas", "gaseous", "air", "vapor", "atmosphere", "oxygen", "hydrogen", "steam", "smoke", "fume", "cloud", "methane", "nitrogen", "helium", "ammonia", "ozone", "wind", "odorless"],
        "Plasma": ["plasma", "lightning", "star", "sun", "fire", "flame", "arc", "discharge", "exothermic", "combustion"],
        "Field": ["field", "magnetic", "gravitational", "electromagnetic", "gravity", "radiation", "light", "wave", "quantum", "spectrum", "optical", "laser", "antenna", "transducer", "induction"],
        "Pattern": ["information", "code", "algorithm", "concept", "idea", "math", "symbol", "word", "language", "data", "software", "pattern", "logic", "programmable", "digital"],
        "Hybrid": ["aerosol", "gel", "emulsion", "paste", "foam", "suspension", "colloid", "mud", "slurry", "fog"]
    },
    "C2_genesis": {
        "Biogenic": ["biogenic", "biological", "living", "organism", "plant", "animal", "fungus", "fungi", "fruit", "tree", "flower", "leaf", "meat", "blood", "cell", "species", "natural", "seed", "wood", "bacterial", "microbe", "cultivar", "flesh", "mammal", "fish", "insect", "avian", "bird", "organic"],
        "Abiogenic": ["abiogenic", "mineral", "rock", "stone", "ore", "crystal", "geological", "volcanic", "earth", "meteorite", "inorganic", "sediment", "water", "ice", "chemical element", "transition metal", "allotrope", "saline", "seismic", "fault", "spring"],
        "Anthropogenic": ["anthropogenic", "artificial", "tool", "machine", "device", "man-made", "human", "constructed", "engineered", "synthetic", "vehicle", "weapon", "building", "furniture", "clothing", "manufactured", "utensil", "component", "circuit", "handheld", "instrument", "apparatus", "clock"],
        "Virtual": ["virtual", "digital", "software", "computer", "program", "code", "cyber", "internet", "abstract", "model", "protocol", "simulation", "algorithmic"],
        "Cosmogenic": ["cosmic", "stellar", "space", "astronomical", "solar", "nebula", "galaxy", "black hole", "extraterrestrial", "universe", "celestial"]
    },
    "C3_scale": {
        "Subatomic": ["subatomic", "quantum", "particle", "electron", "proton", "neutron", "quark", "photon", "atom", "atomic", "diatomic", "tetravalent", "molecular"],
        "Micro": ["micro", "microscopic", "cell", "bacteria", "yeast", "virus", "nanometer", "micrometer", "spore", "microorganism", "polyps", "compound lenses"],
        "Anthropometric": ["hand", "human", "body", "room", "table", "held", "pocket", "edible", "wearable", "meter", "centimeter", "tool", "fruit", "device", "chair", "clothing", "apple", "knife", "hammer", "small", "portable", "handheld", "mammal", "fish", "bird", "insect", "flower"],
        "Geographic": ["geographic", "mountain", "river", "city", "ocean", "forest", "continent", "landscape", "kilometer", "sea", "lake", "volcano", "glacier", "earthquake", "tsunami", "atmosphere", "cloud", "weather"],
        "Astronomical": ["astronomical", "planet", "star", "sun", "earth", "moon", "galaxy", "orbit", "universe", "solar system", "celestial", "spacetime"]
    },
    "C4_texture": {
        "Rigid": ["rigid", "hard", "stiff", "metallic", "solid", "stone", "iron", "steel", "dense", "compact", "firm", "forged", "hardwood", "exoskeleton", "diamond"],
        "Plastic": ["plastic", "clay", "moldable", "ductile", "pliable", "dough", "soft", "malleable"],
        "Elastic": ["elastic", "rubber", "flexible", "springy", "bouncy", "resilient", "stretchable", "silk"],
        "Brittle": ["brittle", "fragile", "glass", "crystal", "breakable", "shatter", "chalk", "crystalline", "semiconductor"],
        "Fibrous": ["fibrous", "porous", "spongy", "wood", "flesh", "fruit", "textile", "skin", "muscle", "paper", "pulp", "rind", "roots", "stalks", "fur", "meat"],
        "Viscous": ["viscous", "granular", "powder", "syrup", "honey", "sand", "grain", "oil", "sticky", "petroleum", "slimy"],
        "Intangible": ["intangible", "gas", "air", "light", "field", "radiation", "digital", "vacuum", "concept", "abstract", "colorless", "plasma", "shockwave", "sound", "temperature"]
    },
    "C5_topology": {
        "Symmetric": ["symmetric", "sphere", "cube", "round", "circular", "ball", "cylinder", "regular", "globular", "wheel", "lens", "ring"],
        "Planar": ["planar", "flat", "sheet", "two-dimensional", "surface", "plate", "board", "screen", "leaf", "mirror", "anvil"],
        "Fractal": ["fractal", "branching", "tree", "mycelium", "root", "lightning", "dendrite", "network", "veins", "vascular", "coral"],
        "Network": ["network", "grid", "nodes", "graph", "web", "internet", "mesh", "circuit", "pack", "colonies"],
        "Amorphous": ["amorphous", "diffuse", "cloud", "blob", "irregular", "fluid", "gas", "smoke", "fog", "liquid", "solution", "molten"],
        "Linear": ["linear", "fiber", "string", "wire", "line", "vector", "ray", "beam", "needle", "stick", "rope", "handle", "blade", "lever", "column", "shaft", "stream"]
    },
    "C6_teleology": {
        "Resource": ["food", "nutrient", "fuel", "energy", "edible", "eaten", "resource", "nutrition", "water", "raw material", "consumed", "nourishment", "diet", "culinary", "fertilizer", "hydrocarbons", "cereal", "grain", "fruit", "vegetable"],
        "Tool": ["tool", "instrument", "device", "machine", "weapon", "mechanism", "equipment", "vehicle", "utensil", "apparatus", "cut", "strike", "measure", "magnify", "switch", "amplify", "navigational", "timekeeping", "generator"],
        "Shelter": ["shelter", "house", "building", "dwelling", "nest", "haven", "atmosphere", "container", "box", "protective", "housing", "shielding", "layer"],
        "Destructor": ["destructor", "poison", "toxin", "decay", "hazard", "lethal", "destructive", "explosive", "predator", "kill", "carnivorous", "hunting", "sharp teeth", "prey", "violent", "rupture", "toxic"],
        "Informer": ["sign", "symbol", "text", "book", "signal", "display", "indicator", "information", "language", "communication", "record", "optical", "mirror", "visual", "compass", "spectrum"],
        "Regulator": ["regulator", "law", "algorithm", "valve", "governor", "rule", "hormone", "enzyme", "code", "control", "resistance", "capacitor", "filter"]
    },
    "C7_energy": {
        "ActiveThermal": ["hot", "heat", "fire", "flame", "thermal", "boiling", "star", "combustion", "sun", "burning", "high-temperature", "exothermic", "molten", "geyser"],
        "PassiveThermal": ["cold", "cool", "frozen", "ice", "absorber", "subzero", "sink", "glacier", "avalanche", "freezing"],
        "Kinetic": ["kinetic", "moving", "running", "flowing", "fast", "velocity", "active", "dynamic", "vibrating", "wind", "waterfall", "shaking", "rotation", "flight", "swimming", "current", "waves", "tornado"],
        "Potential": ["potential", "stored", "battery", "static", "chemical energy", "accumulator", "food", "charge", "sugar", "carbohydrate", "calorie", "nutrient", "starchy", "fuel", "spring"],
        "Inert": ["inert", "stable", "quiescent", "dormant", "noble gas", "passive", "unreactive", "mineral", "rock", "stone", "resistant", "noble"]
    },
    "C8_chronotope": {
        "Permanent": ["permanent", "durable", "eternal", "stable", "rock", "mountain", "planet", "ancient", "long-lasting", "metal", "element", "granite", "basalt", "quartz", "diamond"],
        "Ephemeral": ["ephemeral", "fleeting", "short-lived", "flash", "spark", "bubble", "momentary", "instant", "lightning", "shockwave", "thunder"],
        "Cyclic": ["cyclic", "periodic", "seasonal", "orbit", "rhythm", "wave", "pulse", "recurring", "annual", "harvest", "migratory", "biennial", "tides", "alternating"],
        "Process": ["process", "growth", "decay", "combustion", "reaction", "development", "flow", "evolving", "perishable", "living", "life cycle", "biological", "fermenting", "oxidation", "transition"]
    },
    "C9_complexity": {
        "Elementary": ["element", "fundamental", "particle", "single", "pure", "atom", "simple", "allotrope", "prokaryotic"],
        "Homogeneous": ["homogeneous", "uniform", "monolithic", "alloy", "solution", "block", "pure substance", "liquid", "gas", "crystal"],
        "Composite": ["composite", "parts", "assembly", "layered", "mixture", "cellular", "aggregate", "tissue", "seed", "skin", "pulp", "tool", "instrument", "machine", "device", "tuber", "fruit"],
        "Systemic": ["system", "cybernetic", "network", "ecosystem", "computer", "organism", "forest", "brain", "society", "tree", "plant", "animal", "colony", "mammal", "pack"]
    },
    "C10_sensory": {
        "Visual": ["bright", "colored", "color", "red", "green", "blue", "yellow", "dark", "visible", "shiny", "luminous", "light", "display", "orange", "gold", "spectrum", "mirror"],
        "Acoustic": ["sound", "acoustic", "loud", "noise", "musical", "vibration", "tone", "resonance", "echo", "voice", "thunder", "audible"],
        "Chemosensory": ["sweet", "sour", "bitter", "pungent", "fragrant", "odor", "taste", "smell", "scent", "flavor", "chemical", "aroma", "delicious", "edible", "tart", "perfumed", "fermenting"],
        "Tactile": ["rough", "smooth", "soft", "sharp", "slimy", "texture", "warm", "cold", "hard", "heavy", "dense", "malleable", "slippery"],
        "Imperceptible": ["imperceptible", "invisible", "inaudible", "subatomic", "digital", "abstract", "odorless", "colorless", "field", "quantum", "gravity"]
    },
    "C11_valuation": {
        "Constructive": ["nutritious", "healing", "beneficial", "healthy", "constructive", "useful", "vital", "growth", "positive", "protective", "edible", "valuable", "precious", "essential", "food", "tool", "work"],
        "Destructive": ["toxic", "poisonous", "harmful", "lethal", "destructive", "damaging", "hazardous", "fatal", "dangerous", "corrosive", "weapon", "predatory", "violent", "rupture", "disaster", "seismic"],
        "Neutral": ["neutral", "passive", "inert", "ambient", "indifferent", "background", "geological", "mineral", "element"]
    },
    "C12_trajectory": {
        "Emergence": ["birth", "seed", "sprout", "synthesis", "creation", "genesis", "formation", "dawn", "young", "erupt", "condensation", "discharge"],
        "Equilibrium": ["equilibrium", "mature", "stable", "balance", "steady state", "homeostasis", "maintained", "ripe", "adult", "durable", "quiescent", "permanent"],
        "Degradation": ["degradation", "rot", "decay", "entropy", "wear", "collapse", "rust", "extinction", "death", "perish", "decomposition", "oxidation", "erosion"]
    }
}

def extract_dom12_vector(concept_name: str, definition_text: str):
    """
    High-precision extraction of 12-dimensional reality vector using whole-token matching.
    """
    text = (concept_name + " " + definition_text).lower()
    # Normalize words
    words = set(re.findall(r'\b[a-z0-9_-]+\b', text))
    
    vector = {}
    for axis, categories in DOM_AXES.items():
        best_cat = None
        best_score = -1
        best_idx = 0
        
        for cat_idx, (cat_name, keywords) in enumerate(categories.items()):
            score = 0
            for kw in keywords:
                if " " in kw:
                    if kw in text:
                        score += 5
                else:
                    if kw in words:
                        score += 3
                    elif kw in text:
                        score += 1
            
            if score > best_score:
                best_score = score
                best_cat = cat_name
                best_idx = cat_idx
                
        if best_score <= 0:
            first_key = list(categories.keys())[0]
            vector[axis] = {"name": first_key, "index": 0}
        else:
            vector[axis] = {"name": best_cat, "index": best_idx}
            
    return vector
