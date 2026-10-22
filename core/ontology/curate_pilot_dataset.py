"""
Curator for 100 Anchor Physical & Technological Concepts across 4 Domains.
Uses a curated high-purity offline encyclopedic corpus of definitions + DOM-12 extraction.
Zero rate limits, deterministic, instant.
"""
import json
from ontology_extractor import extract_dom12_vector

# Ground-truth encyclopedic definitions for 100 key physical & technological concepts
DEFINITIONS = {
    # --- DOMAIN: BIOLOGICAL (25) ---
    "Apple": "The round, edible pomaceous fruit of an apple tree, with crisp flesh, thin skin, seeds, and sweet taste.",
    "Oak": "A large deciduous hardwood tree of genus Quercus with deeply lobed leaves, acorns, and durable dense wood.",
    "Wolf": "A carnivorous wild canine mammal living in social packs, possessing sharp teeth, fur, and predatory instincts.",
    "Mushroom": "The fleshy, spore-bearing fruiting body of a fungus, typically produced above ground on soil or its food source.",
    "Wheat": "A cereal grain grass cultivated globally for its edible starchy seeds, milled into flour for human food.",
    "Honeybee": "A social flying insect that produces honey and beeswax, pollinating flowering plants with winged flight.",
    "Salmon": "An anadromous migratory fish with pink flesh, swimming upstream to spawn in freshwater rivers.",
    "Rose": "A woody perennial flowering plant of genus Rosa, with thorny stems, fragrant red petals, and ornamental flowers.",
    "Whale": "A massive aquatic marine mammal breathing air through a blowhole, swimming through ocean depths.",
    "Bacteria": "Microscopic single-celled prokaryotic microorganisms lacking a nucleus, reproducing rapidly by cell division.",
    "Pine": "An evergreen coniferous tree with needle-shaped leaves, cones containing seeds, and aromatic resinous wood.",
    "Spider": "An eight-legged predatory arthropod producing silk threads to spin webs for capturing insect prey.",
    "Eagle": "A large bird of prey with keen eyesight, hooked beak, and powerful talons hunting small animals.",
    "Carrot": "A biennial root vegetable, typically orange, crisp, and fibrous, rich in beta-carotene and dietary nutrients.",
    "Potato": "A starchy tuberous root vegetable of Solanum tuberosum, growing underground as a major human carbohydrate food.",
    "Yeast": "Eukaryotic single-celled fungi capable of fermenting sugars into alcohol and carbon dioxide in baking and brewing.",
    "Grass": "Monocotyledonous herbaceous plants with narrow leaves growing from the base, forming ground pastures and lawns.",
    "Horse": "A large domesticated four-legged herbivorous mammal with hooves, used for transport, riding, and draft work.",
    "Shark": "A predatory cartilaginous fish with multiple gill slits, triangular sharp teeth, and streamlined hydrodynamic body.",
    "Tomato": "The glossy red edible berry of Solanum lycopersicum, containing juicy pulp and seeds, used in cuisine.",
    "Orange": "A round citrus fruit with a fragrant textured rind, segmented juicy pulp, and sweet-acidic vitamin C juice.",
    "Bamboo": "A fast-growing woody perennial evergreen grass with hollow stems, immense tensile strength, and fibrous stalks.",
    "Ant": "A colonial eusocial insect living in underground mounds with complex division of labor and high collective organization.",
    "Elephant": "The largest terrestrial mammal, possessing a long prehensile muscular trunk, large ears, and ivory tusks.",
    "Coral": "Marine invertebrate animals living in compact colonies of polyps, secreting calcium carbonate hard exoskeletons.",

    # --- DOMAIN: TECHNOLOGICAL & TOOLS (25) ---
    "Hammer": "A handheld manual striking tool consisting of a heavy metal head mounted perpendicularly on a rigid handle.",
    "Knife": "A cutting tool or handheld weapon with an exposed sharp edged blade affixed to an ergonomic handle.",
    "Lever": "A rigid beam pivoted at a fixed fulcrum used to amplify mechanical force and lift heavy loads.",
    "Wheel": "A circular mechanical component rotating on an axle, reducing friction to transport vehicles or transfer torque.",
    "Anvil": "A heavy forged steel block with a flat working surface upon which hot metals are hammered and shaped.",
    "Telescope": "An optical instrument using lenses or curved mirrors to magnify distant astronomical celestial bodies.",
    "Microscope": "An optical device with compound lenses to produce magnified visual images of microscopic specimens.",
    "Engine": "A machine designed to convert thermal, chemical, or electrical energy into mechanical work and motion.",
    "Battery": "An electrochemical storage device that converts stored chemical potential energy into electrical current.",
    "Transistor": "A solid-state semiconductor electronic device used to amplify or switch electrical signals and power.",
    "Compass": "A navigational instrument with a magnetized needle pointing toward the Earth's magnetic north pole.",
    "Clock": "A mechanical or electronic timekeeping instrument measuring, displaying, and synchronizing hours and minutes.",
    "Laser": "A device that emits a coherent, monochromatic, collimated beam of electromagnetic light radiation.",
    "Turbine": "A rotary mechanical machine that extracts kinetic energy from a fluid flow (gas, steam, water) into shaft work.",
    "Computer": "A programmable digital electronic machine that executes algorithmic instructions, processing data and code.",
    "Resistor": "A passive two-terminal electronic component that implements electrical resistance as a circuit element.",
    "Capacitor": "A passive electrical component consisting of two conducting plates storing energy in an electrostatic field.",
    "Antenna": "An electrical transducer device that converts radio frequency electromagnetic currents into radiating radio waves.",
    "Pump": "A mechanical apparatus used to move fluids (liquids or gases) by positive displacement or centrifugal mechanical action.",
    "Gear": "A toothed wheel that meshes with another to transmit torque, change speed, or alter rotational direction.",
    "Screwdriver": "A handheld tool with a shaped tip fitting into a screw head to turn, drive, or remove threaded fasteners.",
    "Mirror": "A reflective planar or curved glass surface with a metallic backing reflecting visible light rays specularly.",
    "Lens": "A transparent optical glass element with curved surfaces that refracts light beams to converge or diverge.",
    "Transformer": "A passive electrical device transferring alternating electrical power between circuits through electromagnetic induction.",
    "Dynamo": "An electrical generator that converts mechanical shaft rotation into direct current electricity using magnetic coils.",

    # --- DOMAIN: PHENOMENA & PROCESSES (25) ---
    "Lightning": "A high-voltage electrostatic discharge phenomenon between clouds or ground, producing plasma and thunder.",
    "Thunder": "The loud acoustic acoustic shockwave produced by the rapid thermal expansion of air heated by lightning plasma.",
    "Rain": "Liquid water droplets condensing from atmospheric water vapor and falling under gravity onto Earth's surface.",
    "Fire": "The visible exothermic chemical oxidation process of combustion, releasing heat, light, flames, and smoke.",
    "Earthquake": "A sudden violent seismic shaking of the ground caused by the release of kinetic energy along geological faults.",
    "Tornado": "A violently rotating column of air in contact with both the earth surface and a cumulonimbus cloud.",
    "Glacier": "A persistent massive body of dense ice moving slowly downhill under its own gravitational weight.",
    "Aurora": "A natural light display in high-latitude skies caused by solar wind particles colliding with magnetospheric gases.",
    "Rainbow": "An optical meteorological phenomenon displaying a spectrum of light in the sky caused by reflection and refraction in rain.",
    "Tsunami": "A series of immense water ocean waves caused by underwater earthquakes, volcanic eruptions, or landslides.",
    "Volcano": "A geological rupture in the planetary crust through which molten lava, volcanic ash, and hot gases erupt.",
    "Fog": "A dense low-lying cloud of water droplets suspended in the air near the ground, reducing visual visibility.",
    "Wind": "The perceptible natural movement of air currents flowing from areas of high atmospheric pressure to low pressure.",
    "Combustion": "A high-temperature exothermic chemical reaction between a fuel and an oxidant producing heat and flue gas.",
    "Evaporation": "The thermodynamic phase transition process by which liquid molecules gain kinetic energy and escape into gas.",
    "Condensation": "The physical change of state where a gas or vapor transitions into a liquid upon cooling.",
    "Geyser": "A natural hot spring that intermittently discharges boiling hot water and steam violently into the atmosphere.",
    "Eclipse": "An astronomical alignment phenomenon where one celestial body passes into the shadow cast by another.",
    "Avalanche": "A rapid downhill flow of a massive volume of snow, ice, and rock debris tumbling down a steep mountain slope.",
    "Rust": "The reddish-brown iron oxide compound formed by the electrochemical oxidation of iron in moisture and oxygen.",
    "Decay": "The biological breakdown and organic decomposition of dead matter by bacteria and fungi into simple minerals.",
    "Freezing": "The phase transition where a liquid cools below its freezing point and crystallizes into a solid state.",
    "Boiling": "The rapid thermodynamic vaporization of a liquid occurring when vapor pressure equals surrounding ambient pressure.",
    "Magnetism": "A physical fundamental force mediated by magnetic fields produced by electric currents and magnetic dipoles.",
    "Gravitation": "The universal fundamental physical interaction where all masses and energy attract one another in spacetime."
    ,
    # --- DOMAIN: SUBSTANCES & MATERIALS (25) ---
    "Water": "A transparent odorless liquid chemical substance of formula H2O forming streams, lakes, oceans, and living fluid.",
    "Iron": "A dense, silvery-grey ferromagnetic transition metal element (Fe), easily forged and vital in industrial steel.",
    "Gold": "A precious dense, malleable, and ductile yellow metallic element (Au), resistant to chemical corrosion and tarnish.",
    "Diamond": "A solid metastable allotrope of pure carbon with atoms arranged in a crystal lattice, possessing extreme hardness.",
    "Oxygen": "A colorless odorless gaseous chemical element (O2) essential for aerobic cellular respiration and combustion.",
    "Hydrogen": "The lightest, most abundant chemical element in the universe, a colorless flammable diatomic gas (H2).",
    "Carbon": "A nonmetallic tetravalent chemical element forming the chemical basis of all known organic life forms.",
    "Quartz": "A hard crystalline mineral composed of silicon and oxygen atoms in a continuous SiO4 framework.",
    "Granite": "A coarse-grained intrusive felsic igneous rock composed predominantly of quartz, feldspar, and mica minerals.",
    "Basalt": "A dense dark extrusive igneous volcanic rock formed by the rapid cooling of basaltic lava on oceanic crust.",
    "Copper": "A soft, malleable reddish-orange transition metal element with extremely high electrical and thermal conductivity.",
    "Silver": "A lustrous white precious transition metal element exhibiting the highest electrical conductivity of any metal.",
    "Silicon": "A hard, brittle crystalline semiconductor metalloid element used as the foundation for modern microchips.",
    "Salt": "A crystalline mineral composed primarily of sodium chloride (NaCl), an essential biological nutrient and seasoning.",
    "Sulfur": "A bright yellow nonmetallic crystalline chemical element forming sulfide minerals, gunpowder, and sulfuric acid.",
    "Nitrogen": "A colorless odorless inert diatomic chemical gas (N2) comprising seventy-eight percent of Earth's atmosphere.",
    "Helium": "A colorless, odorless, non-toxic, inert noble gas, the second lightest element, glowing pale yellow in plasma.",
    "Lead": "A heavy, dense, soft, malleable grey toxic metal element with a low melting point and high radiation shielding.",
    "Mercury": "A heavy, silvery liquid transition metal element that remains liquid at standard ambient temperature and pressure.",
    "Petroleum": "A naturally occurring yellowish-black viscous liquid mixture of hydrocarbons found in geological formations.",
    "Methane": "A colorless, odorless, flammable hydrocarbon gas (CH4), the primary constituent of natural fossil fuel gas.",
    "Ozone": "An inorganic molecule composed of three oxygen atoms (O3), forming a protective layer blocking UV rays in the stratosphere.",
    "Graphite": "A soft, slippery crystalline allotrope of carbon with layered planar sheets conducting electricity well.",
    "Ammonia": "A pungent, colorless alkaline gas compound of nitrogen and hydrogen (NH3), used in industrial fertilizers.",
    "Calcium": "A reactive alkaline earth metal element (Ca), an essential chemical constituent of animal bones, teeth, and shells."
}

def build_dataset():
    pilot_data = []
    print(f"Vectorizing 100 anchor concepts into DOM-12 coordinates...")
    
    count = 0
    domains = [
        ("Domain_Biological", list(DEFINITIONS.keys())[0:25]),
        ("Domain_Technological", list(DEFINITIONS.keys())[25:50]),
        ("Domain_Phenomena", list(DEFINITIONS.keys())[50:75]),
        ("Domain_Substances", list(DEFINITIONS.keys())[75:100])
    ]
    
    for domain_name, concepts in domains:
        print(f"\nProcessing {domain_name} ({len(concepts)} concepts)...")
        for concept in concepts:
            count += 1
            definition = DEFINITIONS[concept]
            vec = extract_dom12_vector(concept, definition)
            record = {
                "id": count,
                "name": concept,
                "domain": domain_name,
                "extract": definition,
                "vector": vec
            }
            pilot_data.append(record)
            print(f"  [{count:02d}/100] {concept:12s} -> C1:{vec['C1_state']['name']:8s} | C2:{vec['C2_genesis']['name']:13s} | C6:{vec['C6_teleology']['name']:10s}")
            
    out_file = "/Users/afilum/Mycelium_project/mycelium_core/ontology/pilot_100.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(pilot_data, f, indent=2, ensure_ascii=False)
        
    print(f"\n Successfully compiled {len(pilot_data)} concepts into {out_file}")

if __name__ == "__main__":
    build_dataset()
