THEORY_MODULE = {

    # ── Alapfogalmak ────────────────────────────────────────────────────────

    "quantum_state": {
        "title": "Kvantumállapot",
        "latex": r"""
\mathcal{H} = \mathbb{C}^d

|\psi\rangle =
\begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_d \end{bmatrix}

\sum_{\lambda=1}^{d} |c_\lambda|^2 = 1
""",
        "short_explanation": (
            "A kvantumrendszer állapottere Hilbert-tér. Tiszta állapot esetén az állapotot "
            "egy normált komplex állapotvektor írja le."
        ),
        "beginner_explanation": (
            "A c_λ komponensek valószínűségi amplitúdók. Méréskor nem maga az amplitúdó, "
            "hanem annak abszolútérték-négyzete ad valószínűséget."
        ),
        "program_usage": (
            "Állapotvektor módban a program komplex együtthatókat kér, "
            "majd ellenőrzi vagy elvégzi a normalizálást."
        ),
    },

    "state_vector_two_qubits": {
        "title": "Kétqubites állapotvektor",
        "latex": r"""
|\psi\rangle =
c_{00}|00\rangle + c_{01}|01\rangle + c_{10}|10\rangle + c_{11}|11\rangle

|c_{00}|^2 + |c_{01}|^2 + |c_{10}|^2 + |c_{11}|^2 = 1
""",
        "short_explanation": (
            "Két qubit állapottere a két egyqubites állapottér tenzorszorzata, "
            "ezért a számítási bázis négy elemből áll: |00⟩, |01⟩, |10⟩, |11⟩."
        ),
        "beginner_explanation": (
            "Egy qubithez két bázisállapot tartozik, két qubithez már négy. "
            "Ezért kell a programban négy komplex együttható."
        ),
        "program_usage": (
            "A bemeneti vektor hossza két qubit esetén pontosan 4."
        ),
    },

    "density_matrix": {
        "title": "Sűrűségmátrix",
        "latex": r"""
\hat{\rho} \geq 0 \qquad \mathrm{tr}(\hat{\rho}) = 1

\hat{\rho}_{\mathrm{tiszta}} = |\psi\rangle\langle\psi|
""",
        "short_explanation": (
            "Az általános kvantumállapotot egységnyi nyomú, pozitív szemidefinit sűrűségmátrix "
            "írja le. Tiszta állapotnál ez az állapotvektorhoz tartozó egydimenziós projektor."
        ),
        "beginner_explanation": (
            "A sűrűségmátrix azért hasznos, mert tiszta és kevert állapotokat is egységesen "
            "tud kezelni."
        ),
        "validity_conditions": [
            r"\hat{\rho} = \hat{\rho}^{\dagger}",
            r"\hat{\rho} \geq 0",
            r"\mathrm{tr}(\hat{\rho}) = 1",
        ],
        "program_usage": (
            "A program hermitikusságot, pozitív szemidefinitséget és egységnyi nyomot ellenőriz."
        ),
    },

    "pure_state": {
        "title": "Tiszta állapot",
        "latex": r"""
\hat{\rho}_{\mathrm{tiszta}} = |\psi\rangle\langle\psi|

\mathrm{tr}(\hat{\rho}^2) = 1
""",
        "short_explanation": (
            "A tiszta állapot egyetlen állapotvektorral megadható kvantumállapot."
        ),
        "beginner_explanation": (
            "Tiszta állapotnál nincs klasszikus keverési bizonytalanság. "
            "A sűrűségmátrix projektor alakú."
        ),
        "program_usage": (
            "A program a Tr(ρ²) értékkel vizsgálja a tisztaságot."
        ),
    },

    "mixed_state": {
        "title": "Kevert állapot",
        "latex": r"""
\hat{\rho} = \sum_i w_i \hat{\rho}_i
\qquad w_i \geq 0, \quad \sum_i w_i = 1

\mathrm{tr}(\hat{\rho}^2) < 1
""",
        "short_explanation": (
            "Kevert állapot különböző kvantumállapotok véletlenszerű keveréseként állítható elő."
        ),
        "beginner_explanation": (
            "A kevert állapot nem ugyanaz, mint a szuperpozíció. A keverés klasszikus "
            "valószínűségi bizonytalanság, a szuperpozíció pedig kvantumos lineáris kombináció."
        ),
        "program_usage": (
            "Ha Tr(ρ²) < 1, a program kevert állapotként jelöli."
        ),
    },

    # ── Qubit, bázis, Bloch-gömb ────────────────────────────────────────────

    "qubit_computational_basis": {
        "title": "Qubit számítási bázis",
        "latex": r"""
|\psi\rangle = c_0|0\rangle + c_1|1\rangle

|c_0|^2 + |c_1|^2 = 1
""",
        "short_explanation": (
            "A qubit a kvantuminformáció alapegysége. A számítási bázis két vektora |0⟩ és |1⟩."
        ),
        "beginner_explanation": (
            "A qubit képes a |0⟩ és |1⟩ állapotok szuperpozíciójára, ezért gazdagabb "
            "szerkezetű, mint a klasszikus bit."
        ),
        "program_usage": (
            "A kétqubites program számítási bázisa: |00⟩, |01⟩, |10⟩, |11⟩."
        ),
    },

    "bloch_sphere": {
        "title": "Bloch-gömb",
        "latex": r"""
\hat{\rho} = \frac{\hat{I} + \mathbf{s} \cdot \hat{\boldsymbol{\sigma}}}{2}

|\mathbf{s}| \leq 1

|\mathbf{s}| = 1 \Rightarrow \text{tiszta állapot}

|\mathbf{s}| < 1 \Rightarrow \text{kevert állapot}
""",
        "short_explanation": (
            "A qubit állapotai geometriailag a Bloch-gömb pontjaival szemléltethetők."
        ),
        "beginner_explanation": (
            "A gömb felszíne a tiszta állapotokat, a belseje a kevert állapotokat jelenti. "
            "Minél közelebb van a pont a középponthoz, annál kevertebb az állapot."
        ),
        "program_usage": (
            "Redukált egyqubites állapotok vizualizálására nagyon hasznos."
        ),
    },

    "pauli_matrices": {
        "title": "Pauli-mátrixok",
        "latex": r"""
\hat{\sigma}_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
\quad
\hat{\sigma}_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}
\quad
\hat{\sigma}_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}

[\hat{\sigma}_a, \hat{\sigma}_b] = 2i\epsilon_{abc}\hat{\sigma}_c
""",
        "short_explanation": (
            "A Pauli-mátrixok a kétállapotú kvantumrendszer alapvető mátrixai."
        ),
        "beginner_explanation": (
            "Segítségükkel leírható a qubit polarizációja, mérése és sok egyqubites művelet."
        ),
        "program_usage": (
            "Bloch-vektor, kapuk, mérések és forgatások implementációjához alap."
        ),
    },

    # ── Kvantumkapuk ─────────────────────────────────────────────────────────

    "identity_gate": {
        "title": "Identitáskapu",
        "latex": r"""
\hat{I} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
""",
        "short_explanation": (
            "Az identitáskapu változatlanul hagyja a qubit állapotát."
        ),
        "beginner_explanation": (
            "Akkor hasznos, amikor egy többqubites rendszerben csak az egyik qubiten akarunk "
            "műveletet végezni: pl. H⊗I esetén az első qubitre H hat, a másodikra I."
        ),
        "program_usage": (
            "Kétqubites kapuépítéshez szükséges: tenzorszorzatban használjuk."
        ),
    },

    "one_qubit_gate_x": {
        "title": "X-kapu (NOT)",
        "latex": r"""
\hat{X} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}

\hat{X}|0\rangle = |1\rangle \qquad \hat{X}|1\rangle = |0\rangle
""",
        "short_explanation": (
            "Az X-kapu a klasszikus NOT kapu kvantumos megfelelője."
        ),
        "beginner_explanation": (
            "A |0⟩ állapotot |1⟩-be, a |1⟩ állapotot |0⟩-ba viszi. "
            "Szuperpozíció esetén mindkét komponensre lineárisan hat."
        ),
        "program_usage": (
            "Egyqubites kapuszimulációban alapművelet."
        ),
    },

    "one_qubit_gate_y": {
        "title": "Y-kapu",
        "latex": r"""
\hat{Y} = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}

\hat{Y}|0\rangle = i|1\rangle \qquad \hat{Y}|1\rangle = -i|0\rangle
""",
        "short_explanation": (
            "Az Y-kapu a Pauli-mátrixok egyike. A bitfordítást fázisváltozással kombinálja."
        ),
        "beginner_explanation": (
            "Az X-kapu felcseréli a |0⟩ és |1⟩ állapotokat. Az Y-kapu szintén felcserél, "
            "de közben komplex fázist is ad a komponensekhez."
        ),
        "program_usage": (
            "Kapuszimulátorban az X és Z mellett alap Pauli-kapuként szerepel."
        ),
    },

    "one_qubit_gate_z": {
        "title": "Z-kapu",
        "latex": r"""
\hat{Z} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}

\hat{Z}|0\rangle = |0\rangle \qquad \hat{Z}|1\rangle = -|1\rangle
""",
        "short_explanation": (
            "A Z-kapu a |0⟩ és |1⟩ komponensek relatív fázisát változtatja meg."
        ),
        "beginner_explanation": (
            "A bázisállapotok mérési valószínűsége önmagában nem feltétlenül változik, "
            "de a relatív fázis interferenciahelyzetekben döntő."
        ),
        "program_usage": (
            "Fázishatás és interferencia oktatásához hasznos."
        ),
    },

    "hadamard_gate": {
        "title": "Hadamard-kapu",
        "latex": r"""
\hat{H} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}

\hat{H}|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}

\hat{H}|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
""",
        "short_explanation": (
            "A Hadamard-kapu a számítási bázisállapotokat egyenlő súlyú szuperpozíciókba viszi."
        ),
        "beginner_explanation": (
            "Ez az egyik legfontosabb kvantumkapu: a biztos |0⟩ vagy |1⟩ állapotból "
            "szuperpozíciós állapotot készít."
        ),
        "program_usage": (
            "Bell-állapot készítéséhez és kvantumkörök oktatásához alapkapu."
        ),
    },

    "phase_gate": {
        "title": "Fáziskapu",
        "latex": r"""
\hat{T}(\varphi) = \begin{bmatrix}
e^{-i\varphi/2} & 0 \\ 0 & e^{i\varphi/2}
\end{bmatrix}
""",
        "short_explanation": (
            "A fáziskapu a Z-kapu általánosítása: tetszőleges φ szögű fázisváltozást hoz létre."
        ),
        "beginner_explanation": (
            "A fázis a kvantumállapot olyan része, amely közvetlenül nem mindig látszik "
            "a mérési valószínűségekben, de más állapotokkal interferálva megjelenik."
        ),
        "program_usage": (
            "Egyqubites unitér műveletek és Bloch-gömb forgatások tanításához használható."
        ),
    },

    "cnot_gate": {
        "title": "cNOT kapu (vezérelt NOT)",
        "latex": r"""
\mathrm{cNOT} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}

|10\rangle \mapsto |11\rangle \qquad |11\rangle \mapsto |10\rangle
""",
        "short_explanation": (
            "A cNOT kétqubites vezérelt NOT: ha a vezérlő qubit |1⟩, megfordítja a célqubitet."
        ),
        "beginner_explanation": (
            "A cNOT a legtöbbet használt kétqubites kvantumkapu. "
            "Hadamard-kapuval kombinálva Bell-állapotot hoz létre: "
            "H⊗I alapon → cNOT → |Φ+⟩."
        ),
        "program_usage": (
            "A program CNOT mátrixot alkalmaz a teljes kétqubites állapotvektorra."
        ),
    },

    "controlled_gate_general": {
        "title": "Vezérelt kvantumkapu",
        "latex": r"""
\hat{C}_U = |0\rangle\langle 0| \otimes \hat{I}
           + |1\rangle\langle 1| \otimes \hat{U}
""",
        "short_explanation": (
            "A vezérelt kapu kétqubites művelet: az egyik qubit vezérli, "
            "hogy a másikon történjen-e művelet."
        ),
        "beginner_explanation": (
            "Szuperpozíciós vezérlő esetén a folyamat kvantumos korrelációt, "
            "akár összefonódást is létrehozhat."
        ),
        "program_usage": (
            "A cNOT ennek speciális esete, ahol U = X."
        ),
    },

    # ── Összetett rendszerek, összefonódás ───────────────────────────────────

    "composite_system": {
        "title": "Összetett kvantumrendszer",
        "latex": r"""
\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B

|\psi_{AB}\rangle = \sum_{\lambda, l} c_{\lambda l} |\lambda;A\rangle \otimes |l;B\rangle
""",
        "short_explanation": (
            "Összetett kvantumrendszer állapottere a részrendszerek állapottereinek "
            "tenzorszorzata."
        ),
        "beginner_explanation": (
            "Két qubit közös állapota nem mindig írható le úgy, hogy külön megadjuk "
            "az első és a második qubitet. Ez vezet az összefonódáshoz."
        ),
        "program_usage": (
            "A program kétqubites állapottere 2×2 = 4 dimenziós."
        ),
    },

    "tensor_product": {
        "title": "Tenzorszorzat",
        "latex": r"""
\begin{bmatrix} a_0 \\ a_1 \end{bmatrix}
\otimes
\begin{bmatrix} b_0 \\ b_1 \end{bmatrix}
=
\begin{bmatrix} a_0 b_0 \\ a_0 b_1 \\ a_1 b_0 \\ a_1 b_1 \end{bmatrix}
""",
        "short_explanation": (
            "Összetett rendszerek állapotait tenzorszorzattal építjük fel."
        ),
        "beginner_explanation": (
            "Két egyqubites állapotból így lesz egy négykomponensű kétqubites állapot."
        ),
        "program_usage": (
            "Kapuk és többqubites állapotok felépítéséhez szükséges."
        ),
    },

    "product_state": {
        "title": "Szorzatállapot",
        "latex": r"""
|\psi_{AB}\rangle = |\psi_A\rangle \otimes |\psi_B\rangle
""",
        "short_explanation": (
            "Szorzatállapot esetén az összetett rendszer állapota két részrendszer "
            "állapotának tenzorszorzata."
        ),
        "beginner_explanation": (
            "Ilyenkor a két részrendszer között nincs kvantumos összefonódás."
        ),
        "program_usage": (
            "Tiszta állapotnál a szorzat alak szeparábilitást jelent."
        ),
    },

    "entanglement": {
        "title": "Összefonódás",
        "latex": r"""
\hat{\rho}_{AB} \neq \sum_\lambda w_\lambda
\hat{\rho}_{A\lambda} \otimes \hat{\rho}_{B\lambda}
""",
        "short_explanation": (
            "Összefonódás akkor van, ha az állapot nem írható fel szeparábilis alakban."
        ),
        "beginner_explanation": (
            "Ilyenkor a két részrendszer közös kvantumállapota nem bontható szét "
            "két független részre."
        ),
        "program_usage": (
            "A program tiszta állapotnál redukált tisztaságot, "
            "kevert állapotnál részleges transzponálást használ."
        ),
    },

    "separability": {
        "title": "Szeparábilitás",
        "latex": r"""
\hat{\rho}_{AB} = \sum_\lambda w_\lambda
\hat{\rho}_{A\lambda} \otimes \hat{\rho}_{B\lambda}

w_\lambda \geq 0 \quad \sum_\lambda w_\lambda = 1
""",
        "short_explanation": (
            "Egy összetett állapot szeparábilis, ha korrelálatlan tenzorszorzat-állapotok "
            "keverékeként előállítható."
        ),
        "beginner_explanation": (
            "Szeparábilis állapotban lehet klasszikus korreláció, de nincs kvantumos "
            "összefonódás."
        ),
        "program_usage": (
            "Kevert állapotoknál a szeparábilitás vizsgálata bonyolultabb; "
            "két qubit esetén használható a PPT-teszt."
        ),
    },

    # ── Parciális nyom, redukált állapot ─────────────────────────────────────

    "partial_trace": {
        "title": "Parciális nyom",
        "latex": r"""
\hat{\rho}_A = \mathrm{tr}_B(\hat{\rho}_{AB})
= \sum_l \langle l;B | \hat{\rho}_{AB} | l;B \rangle
""",
        "short_explanation": (
            "Parciális nyommal az összetett rendszerből megkapjuk "
            "az egyik részrendszer redukált állapotát."
        ),
        "beginner_explanation": (
            "Ez olyan, mintha csak az egyik qubitet tartanánk meg, "
            "a másik qubit információját pedig kiátlagolnánk."
        ),
        "program_usage": (
            "A program tiszta állapotoknál a redukált állapot tisztaságából "
            "következtet az összefonódásra."
        ),
    },

    "schmidt_decomposition": {
        "title": "Schmidt-felbontás",
        "latex": r"""
|\psi_{AB}\rangle = \sum_\lambda \sqrt{w_\lambda}
|\lambda;A\rangle \otimes |\lambda;B\rangle

w_\lambda \geq 0 \quad \sum_\lambda w_\lambda = 1
""",
        "short_explanation": (
            "Tiszta kétrészes állapot mindig felírható ortogonális tenzorszorzat-állapotok "
            "Schmidt-felbontásaként."
        ),
        "beginner_explanation": (
            "Ha csak egy nemnulla Schmidt-együttható van, az állapot szorzatállapot. "
            "Ha több van, az állapot összefonódott."
        ),
        "program_usage": (
            "SVD-vel megvalósítható, és magyarázó panelben jól mutatja "
            "az összefonódás szerkezetét."
        ),
    },

    "pure_state_entanglement_test": {
        "title": "Tiszta állapot összefonódásának tesztje",
        "latex": r"""
|\psi_{AB}\rangle \ \text{összefonódott}
\iff \hat{\rho}_A \ \text{kevert}

\mathrm{tr}(\hat{\rho}_A^2) < 1
\Rightarrow \text{összefonódott}
""",
        "short_explanation": (
            "Tiszta kétrészes állapotnál az egyik részrendszer redukált állapotának "
            "kevertsége jelzi az összefonódást."
        ),
        "beginner_explanation": (
            "Ha az egész állapot tiszta, de az egyik qubit önmagában kevertnek látszik, "
            "akkor az információ a két qubit közös összefonódott állapotában van."
        ),
        "program_usage": (
            "A jelenlegi kód ezt használja tiszta állapotok esetén."
        ),
    },

    # ── Bell-állapotok ───────────────────────────────────────────────────────

    "bell_states": {
        "title": "Bell-állapotok",
        "latex": r"""
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}

|\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}

|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}

|\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}
""",
        "short_explanation": (
            "A Bell-állapotok két qubit maximálisan összefonódott ortogonális állapotai."
        ),
        "beginner_explanation": (
            "Ezek az összefonódás legegyszerűbb és legfontosabb példái. "
            "Egyik Bell-állapot sem bontható két külön qubit állapotára."
        ),
        "program_usage": (
            "Előre betölthető példák: a felhasználó kiválaszthatja, a program pedig "
            "megmutatja a sűrűségmátrixot, a redukált állapotokat és az összefonódást."
        ),
    },

    "singlet_state": {
        "title": "Szinglet állapot",
        "latex": r"""
|\Psi^-\rangle = \frac{|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle}{\sqrt{2}}
""",
        "short_explanation": (
            "A szinglet a Bell-bázis egyik állapota, forgásszimmetrikus alakban is felírható."
        ),
        "beginner_explanation": (
            "A két spin tökéletesen antikorrelált: ha az egyik adott irányban felfelé mutat, "
            "a másik lefelé."
        ),
        "program_usage": (
            "Bell-nemlokalitás, EPR-példa és korrelációk szemléltetésére használható."
        ),
    },

    # ── PPT, von Neumann-entrópia ─────────────────────────────────────────────

    "partial_transpose_ppt": {
        "title": "Részleges transzponálás / PPT-teszt",
        "latex": r"""
\hat{\rho}^{T_B}

\exists\, \lambda_i < 0
\Rightarrow \text{összefonódott}
""",
        "short_explanation": (
            "Kétqubites kevert állapotoknál a részleges transzponálás sajátértékei alapján "
            "felismerhető az összefonódás."
        ),
        "beginner_explanation": (
            "Ha a részlegesen transzponált mátrixnak negatív sajátértéke van, "
            "akkor az eredeti állapot nem lehet szeparábilis."
        ),
        "program_usage": (
            "A jelenlegi kód kevert állapotoknál ezt a módszert alkalmazza."
        ),
    },

    "von_neumann_entropy": {
        "title": "Von Neumann-entrópia",
        "latex": r"""
S(\hat{\rho}) = -\mathrm{tr}(\hat{\rho} \log \hat{\rho})
= -\sum_\lambda \rho_\lambda \log \rho_\lambda
""",
        "short_explanation": (
            "A von Neumann-entrópia a kvantumállapot kevertségének és "
            "információtartalmának alapmennyisége."
        ),
        "beginner_explanation": (
            "Tiszta állapotnál nulla, kevert állapotnál pozitív. Sajátértékekből számítható."
        ),
        "program_usage": (
            "A program sajátértékekből számolhatja, például összefonódási entrópiához."
        ),
    },

    "entanglement_entropy": {
        "title": "Összefonódási entrópia",
        "latex": r"""
E(|\psi_{AB}\rangle) = S(\hat{\rho}_A) = S(\hat{\rho}_B)

= -\sum_\lambda w_\lambda \log_2 w_\lambda
""",
        "short_explanation": (
            "Tiszta kétrészes állapot összefonódása a redukált állapot "
            "von Neumann-entrópiájával mérhető."
        ),
        "beginner_explanation": (
            "Minél kevertebb az egyik részrendszer önmagában, "
            "annál nagyobb az összefonódás a másik részrendszerrel."
        ),
        "program_usage": (
            "Érdemes beépíteni: ne csak igen/nem választ adjon az összefonódásra, "
            "hanem mértéket is."
        ),
    },

    # ── Mérések ──────────────────────────────────────────────────────────────

    "born_rule": {
        "title": "Born-szabály",
        "latex": r"""
p_\lambda = |\langle e_\lambda | \psi \rangle|^2

p_\lambda = \mathrm{tr}(\hat{P}_\lambda \hat{\rho})
""",
        "short_explanation": (
            "A Born-szabály adja meg, hogy egy adott mérési eredmény "
            "milyen valószínűséggel jelenik meg."
        ),
        "beginner_explanation": (
            "Az amplitúdó önmagában nem valószínűség. "
            "A valószínűséget az abszolútérték-négyzet adja."
        ),
        "program_usage": (
            "Mérési szimulációhoz és bázisállapotok valószínűségeinek kijelzéséhez "
            "használható."
        ),
    },

    "projective_measurement": {
        "title": "Projektív mérés",
        "latex": r"""
p_\lambda = \mathrm{tr}(\hat{P}_\lambda \hat{\rho})

\hat{\rho} \rightarrow \hat{\rho}_\lambda
= \frac{\hat{P}_\lambda \hat{\rho} \hat{P}_\lambda}{p_\lambda}
""",
        "short_explanation": (
            "Projektív mérésnél az eredményekhez ortogonális projektorok tartoznak. "
            "A mérés eredménye véletlenszerű, és az állapot a kapott eredménynek megfelelően "
            "módosul."
        ),
        "beginner_explanation": (
            "A kvantummérés nem egyszerű leolvasás: a mérés után az állapot általában "
            "megváltozik."
        ),
        "program_usage": (
            "Mérési szimulációhoz és bázisállapotok valószínűségeinek kijelzéséhez."
        ),
    },

    # ── Egyéb fontos fogalmak ─────────────────────────────────────────────────

    "unitary_operation": {
        "title": "Unitér művelet",
        "latex": r"""
\hat{U}^\dagger \hat{U} = \hat{I}

\hat{\rho} \rightarrow \hat{U} \hat{\rho} \hat{U}^\dagger
""",
        "short_explanation": (
            "Izolált kvantumrendszer állapotváltozását unitér művelet írja le."
        ),
        "beginner_explanation": (
            "Az unitér művelet megőrzi a normát, ezért a mérési valószínűségek összege "
            "továbbra is 1 marad."
        ),
        "program_usage": (
            "A kvantumkapuk unitér mátrixokként implementálhatók."
        ),
    },

    "fidelity": {
        "title": "Hűség",
        "latex": r"""
F = |\langle\psi|\psi'\rangle|^2

F(\hat{\rho}, \hat{\rho}') =
\left(\mathrm{tr}\sqrt{\sqrt{\hat{\rho}}\,\hat{\rho}'\sqrt{\hat{\rho}}}\right)^2
""",
        "short_explanation": (
            "A hűség két kvantumállapot hasonlóságának mértéke."
        ),
        "beginner_explanation": (
            "F = 1 esetén az állapotok azonosak, F = 0 esetén ortogonálisak."
        ),
        "program_usage": (
            "Két bemeneti állapot összehasonlítására vagy állapotbecslés oktatására "
            "használható."
        ),
    },

    "no_cloning": {
        "title": "Klónozhatatlanság",
        "latex": r"""
|\psi\rangle \otimes |\psi_0\rangle
\not\longrightarrow
|\psi\rangle \otimes |\psi\rangle
\quad \text{ismeretlen } |\psi\rangle \text{ esetén}
""",
        "short_explanation": (
            "Ismeretlen kvantumállapot nem másolható tökéletesen."
        ),
        "beginner_explanation": (
            "Ez nem technikai korlát, hanem a kvantumelmélet szerkezetéből következik."
        ),
        "program_usage": (
            "Oktató modulban magyarázható, miért különbözik a qubit a klasszikus bittől."
        ),
    },

    "locc": {
        "title": "LOCC",
        "latex": r"""
\mathrm{LOCC} = \text{Local Operations and Classical Communication}
""",
        "short_explanation": (
            "LOCC alatt lokális műveleteket és klasszikus kommunikációt értünk."
        ),
        "beginner_explanation": (
            "Alice és Bob a saját rendszerükön műveleteket végezhetnek, egymásnak klasszikus "
            "üzeneteket küldhetnek, de kvantumcsatorna nélkül nem tudnak új összefonódást "
            "létrehozni."
        ),
        "important_fact": (
            "Lokális műveletek és klasszikus kommunikáció nem növelik az összefonódást."
        ),
        "program_usage": (
            "Szakdolgozati részben jól használható az összefonódás erőforrásként való "
            "értelmezéséhez."
        ),
    },

    "entanglement_as_resource": {
        "title": "Összefonódás mint erőforrás",
        "latex": r"""
|\Phi^+_{AB}\rangle = \frac{|0;A\rangle|0;B\rangle + |1;A\rangle|1;B\rangle}{\sqrt{2}}

E(|\Phi^+\rangle) = 1 \text{ ebit}
""",
        "short_explanation": (
            "Egy megosztott Bell-állapot egységnyi összefonódásnak tekinthető."
        ),
        "beginner_explanation": (
            "A megosztott összefonódás kvantumkommunikációs erőforrás: "
            "például teleportációhoz használható."
        ),
        "program_usage": (
            "Bell-példák mellé kiírható: maximálisan összefonódott, E = 1 ebit."
        ),
    },
}
