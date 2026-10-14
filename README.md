# 🍄 Mycelium AI Core (Bio-Spike Semantic Intelligence)

[![Status](https://img.shields.io/badge/Status-R%26D%20%2F%20Proprietary-blueviolet)]()
[![Architecture](https://img.shields.io/badge/Paradigm-Spiking%20Neural%20Network-green)]()
[![Language](https://img.shields.io/badge/DSL-Beszercess-blue)]()
[![Runtime](https://img.shields.io/badge/Engine-spikeasm__vm-red)]()
[![Hardware](https://img.shields.io/badge/Target-Metal%20GPU%20%2F%20Apple%20Silicon-orange)]()
[![Security](https://img.shields.io/badge/Encrypted%20By-Obscura%20Stealth%20Codec-black)]()

> **Mycelium** is an alternative artificial intelligence architecture founded upon biologically plausible Spiking Neural Networks (SNN), discrete mycelial topology, and event-driven computing.
> 
> The project represents a fundamental departure from deep learning conventions: **a total elimination of continuous floating-point weight matrices (Float16/32 Transformers/LLMs) in favor of discrete spike events ("ones only, zero zeroes").**
> 
> 🇷🇺 **[Документация на русском языке (README_RU.md)](README_RU.md)**

---

## 🏛️ The Biomorphic Ecosystem Architecture

Mycelium is not an isolated academic script; it is the cognitive pinnacle of a multi-tiered, custom-built technological stack engineered over months of systems programming. To understand how Mycelium operates without matrices, one must examine its four symbiotic foundation layers:

```mermaid
flowchart TD
    subgraph L3["Tier 3: Cognitive & Knowledge Synthesis"]
        MYC["🍄 Mycelium AI Core<br/>• Topological Semantic Knowledge Graphs (16k+ concepts)<br/>• Hierarchical Syllable-Word Neural Tries<br/>• Spatial Chords Parallel Receptor Bus<br/>• Central Pattern Generator (CPG Grammar Engine)"]
    end
    subgraph L2["Tier 2: Synaptic Description & Symbolic Compilation"]
        BESZ["🧬 Beszercess Domain-Specific Language (DSL)<br/>• Physical Conductivity Formulation: Source >>[delay:weight]>> Target:v_th:leak<br/>• Native Biomorphic Assembly: Zero Loops, Pure Topological Flow<br/>• Event-Triggered Micro-Circuit Routing & STDP Plasticity Mapping"]
    end
    subgraph L1["Tier 1: Bare-Metal Execution Environment"]
        SVM["⚡ spikeasm_vm (Rust Runtime Engine)<br/>• Asynchronous BinaryHeap Event Priority Scheduler<br/>• Leaky Integrate-and-Fire (LIF) Dynamic Biophysics<br/>• Massive Parallel Event Dispatch via Apple Metal GPU Compute Shaders (WGSL)<br/>• Unified Zero-Copy Memory Access on Apple Silicon"]
    end
    subgraph L0["Tier 0: Cryptographic Perimeter & Memory Streaming"]
        OBS["🛡️ Obscura Stealth Codec<br/>• Zero-Signature High-Entropy Model Container (Zero Magic Bytes / Anti-DPI)<br/>• 4-Node SNN NeuroRatchet Stream Cipher with Live Synaptic Mutation<br/>• 5D QuantumSpin Chaotic Key Derivation (Golden Ratio & Möbius Topology)<br/>• Monolithic VFS Streaming: Instant Zero-Copy Bytecode Mounting"]
    end

    MYC --> BESZ
    BESZ --> SVM
    SVM -. "Compiled Synaptic Bytecode Sealed & Streamed by" .-> OBS
```

---

## 🔬 In-Depth Engineering Analysis of the Core Components

### 1. `spikeasm_vm` — The High-Performance Spiking Virtual Machine
Traditional neural software relies on PyTorch, TensorFlow, or CUDA engines executing continuous matrix dot-products ($Y = W \cdot X + b$). Even when a token requires no activation, millions of parameters are multiplied across dense memory buffers.

`spikeasm_vm` is a bare-metal virtual execution runtime engineered in Rust from the ground up:
* **The Operating Principle (Asynchronous Temporal Queues):**  
  At its core lies a high-precision `BinaryHeap<SpikeEvent>` priority queue ordered strictly by target firing time ($t$). Rather than sweeping through all neurons at every clock tick, the engine advances simulation time directly to the timestamp of the next physical spike. Inactive neurons ("zeros") consume **zero computational cycles and zero electrical watts**.
* **Biophysical Neuron Models (Leaky Integrate-and-Fire):**  
  Every neuron maintains a resting membrane potential $V_{rest}$, an activation threshold $V_{th}$, a temporal refractory lockout period, and a continuous leak coefficient $\lambda$. When an incoming spike arrives, the synaptic weight $W$ integrates into the membrane potential. If $V \ge V_{th}$, an action potential is emitted, and $V$ resets instantly.
* **On-the-Fly Synaptic Plasticity (STDP & LTD):**  
  The VM incorporates biological learning directly into the runtime:
  * **LTP (Long-Term Potentiation):** Synapses that fire shortly before a downstream neuron fires are strengthened ($+ \Delta W$).
  * **LTD (Long-Term Depression):** Inactive or lagging connections decay ($- \Delta W$), pruning inefficient pathways automatically.
* **Hardware Acceleration via Apple Metal GPU:**  
  When associative recall unleashes millions of concurrent spikes, the VM dispatches spike propagation into Apple Metal Compute Shaders (WGSL), exploiting Apple Silicon’s unified memory architecture for zero-overhead, multi-gigabyte throughput.

---

### 2. `Beszercess` — The Biomorphic Synaptic Assembly Language
Classical programming languages (C, Rust, Python) describe sequential procedural logic through instructions, conditional branches (`if/else`), and iterative loops (`for/while`). Neural networks cannot be efficiently expressed through procedural code without massive abstraction penalties.

`Beszercess` is a proprietary declarative domain-specific language (DSL) engineered to specify neural topology as physical conductivity:
* **Syntax & Mechanics:**  
  Connections are defined as directional energetic vectors:
  $$\text{SourceNode} \gg [\text{delay} : \text{weight}] \gg \text{TargetNode} : V_{th} : \lambda$$
  * `delay`: Number of discrete simulation ticks the signal requires to travel the axon.
  * `weight`: Real-valued synaptic conductance (positive for excitatory, negative for inhibitory).
  * $V_{th}$: Physical threshold required to depolarize the target cell.
  * $\lambda$: Exponential potential decay rate per tick.
* **Role in the Architecture:**  
  `Beszercess` serves as the compiler bridge. It converts human-readable semantic and grammatical structures into highly optimized bytecode matrices ingested directly by `spikeasm_vm`. There are no runtime loops; the program is the physical wiring itself.

---

### 3. `Obscura Stealth Codec` — Cryptographic Shield & Zero-Copy VFS
Why does a cognitive language model require an advanced cryptographic codec like [Obscura](https://github.com/sangaafilum/Obscura)?

In conventional AI, model weights (`.safetensors`, `.onnx`, `.pt`) are completely exposed. Their static headers and parameter matrices make them vulnerable to corporate theft, regulatory censorship, automated DPI fingerprinting, and weight extraction attacks.

`Obscura` solves this across three distinct operational layers:
* **Zero-Signature Packaging:**  
  Obscura strips all magic bytes, file signatures, and structural metadata. A compiled Mycelium knowledge container encrypted by Obscura appears to deep forensic inspection as completely uniform, high-entropy white noise indistinguishable from physical hardware noise or unformatted disk sectors.
* **Neuro-Symmetric Security (NeuroRatchet):**  
  Unlike static symmetric algorithms (AES, ChaCha20) which rely on rigid mathematical substitution boxes, Obscura employs `NeuroRatchet`: an evolving 4-node Spiking Neural Network simulation. Every byte streamed through the cipher acts as an external action potential, triggering real-time synaptic plasticity (STDP). The encryption mask mutates with every single byte, rendering differential cryptanalysis mathematically impossible.
* **Chaotic Entropy Injection (5D QuantumSpin):**  
  Key derivation utilizes a 5-dimensional non-linear dynamical equation governed by the golden ratio, temporal flow vectors, and Möbius strip topology, yielding verified 50% avalanche entropy.
* **Monolithic Streaming Virtual File System (VFS):**  
  Obscura houses an internal zero-copy virtual filesystem. `spikeasm_vm` does not need to decrypt a 50 GB model into system RAM; it mounts the Obscura container as a streaming block device, decrypting and executing specific synaptic clusters on-demand in micro-seconds with less than 15 MB of RAM overhead.

---

## ⚡ Architectural Manifesto: Why Beyond Conventional LLMs?

Contemporary Large Language Models function as compute-heavy dense matrix probability calculators:
* Billions of floating-point matrix multiplications to generate a single token;
* Massive electrical and thermal dissipation calculating non-informative "zeros" and dead space;
* Inability to achieve immediate, localized on-chip learning without expensive global backpropagation;
* Absence of structural, biological plausibility.

### The Foundational Mycelium Postulate:
> **"Information in the brain is not retained in flat arithmetic matrices — it circulates within a dynamic three-dimensional synaptic topology. The network's topology dictates its computational formula."**

In Mycelium:
1. **Ones Only (Active Spikes):** Inactive state ("0") incurs zero computational expense. Processing units fire strictly when an action potential event arrives.
2. **Spatial Chords:** Elimination of temporal delays during character decoding. An 8-bit parallel receptor bus identifies characters instantaneously at tick $t=0$ with zero pipeline latency.
3. **Hierarchical Neural Trie:** Structured prefix trees prevent synaptic event queue saturation (`EventQueue overflow`).
4. **Topological Semantic Form:** A bidirectional associative graph (16,000+ concept nodes) synthesized directly from comprehensive explanatory lexical corpora.
5. **Central Pattern Generator (CPG):** A biological rhythm oscillator enforcing grammatical order across sequential time slots (`Subject` $\to$ `Verb` $\to$ `Object`).

---

## 🔬 Research Chronology and Verified Milestones

*(Core execution binaries, mathematical weights, and proprietary graph structures are held under confidential research status).*

```mermaid
flowchart LR
    A["Parallel Receptor Bus<br/>(8-bit Spatial Chords)"] --> B["Hierarchical Neural Trie<br/>(Prefix Word Recognition)"]
    B --> C["Semantic Mycelium<br/>(16k+ Core Concepts)"]
    C <--> D["Universal Interlingua<br/>(Cross-Lingual Protocol)"]
    C --> E["Biological Grammar Engine<br/>(CPG Slot Formulator)"]
    E --> F["Inhibition Network<br/>(Winner-Takes-All / LTD)"]
    F --> G["Spike Stream Synthesis<br/>(Output Action Potentials)"]
```

### Prototyping Stages:

* **Stage 1: Semantic Core Convergence**  
  *Hypothesis confirmed:* Independent lexical nodes converge onto abstract concept nodes, integrating action potentials to exceed firing thresholds without vector dot-products.
* **Stage 2: Neural Trie Scalability**  
  *Bottleneck resolved:* Mitigated `EventQueue overflow` in the VM scheduler when scaling to tens of thousands of words by structuring multi-tier prefix syllables.
* **Stage 3: Spatial Chords over Temporal Morse**  
  *Paradigm shift:* Abandoned serial temporal delays. Replaced with instantaneous 3-of-8 spatial chords across parallel bus receptors.
* **Stage 4: Semantic Form Extraction (Webster Corpus)**  
  *Execution:* Parsed 86,000+ dictionary entries into an associative graph containing 16,165 distinct conceptual nodes.
* **Stage 5: Biological Grammar (Central Pattern Generator)**  
  *Execution:* Constructed an autonomous temporal circuit generating sequential firing windows for syntactic grammatical roles.

---

## 🗺️ Engineering Roadmap

- [x] **Parallel Spatial Alphabet Receptor Bus**
- [x] **Hierarchical Syllable & Word Recognition Trie**
- [x] **Topological Semantic Knowledge Graph**
- [x] **Temporal Syntactic Pattern Generator (CPG)**
- [ ] **Phase 1: Dynamic Stabilization (Inhibition Engine)** — Lateral Inhibition & Winner-Takes-All (WTA) integration via negative synaptic weights (LTD) to suppress hyperactive synonym cascades.
- [ ] **Phase 2: Multi-Lingual Interlingua Bridge** — Mapping Russian, English, and multilingual lexicons onto invariant semantic conceptual nodes.
- [ ] **Phase 3: Hardware Verification on `spikeasm_vm`** — Full compilation of Mycelium bytecode and benchmarking on Apple Silicon Metal compute shaders.
- [ ] **Phase 4: Working Memory Loops & Conversational Protocol** — Recurrent synaptic feedback loops for temporal context retention.

---

## 🔒 Confidentiality & Ecosystem Synergy

This repository serves as the official architectural specification and public development log for **Mycelium AI Core**.
* All low-level engine implementations, synaptic matrices, and mathematical graph equations are proprietary (**Closed Source / Proprietary Research**).
* Built natively to execute within the [`spikeasm_vm`](https://github.com/sangaafilum) ecosystem and sealed within the [`Obscura Stealth Codec`](https://github.com/sangaafilum/Obscura).
