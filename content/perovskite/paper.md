

![0_image_0.png](0_image_0.png)

# Chalcogenide Perovskites: Tantalizing Prospects, Challenging Materials

Kostiantyn V. Sopiha, Corrado Comparotto, José A. Márquez, and Jonathan J. S. Scragg* Chalcogenide perovskites have recently emerged into the spotlight as highly robust, earth abundant, and nontoxic candidates for various energy conversion applications, not least photovoltaics (PV). Now, a serious effort is required to determine if they can emulate the PV performance of the betterknown, part-organic halide perovskites, in applications such as tandem solar cells. This review summarizes the surprisingly large body of literature pertaining to chalcogenide perovskites, which have been investigated for many years despite only recently being considered for applications. The confusing variety of claims coming from computational materials discovery is clarified, and it is specified which chalcogenide perovskites actually exist and should form the focus of experimental work. The highly interesting optoelectronic and transport properties of the known materials at their current stage of development are summarized, which makes a clear case for investigating them further. The existing synthesis literature is collated, which provides some important and possibly unnoticed clues to experimentalists grappling with these somewhat challenging materials. The authors hope that the highlighting of this information will facilitate further exciting studies, better approaches, and new progress for chalcogenide perovskites.

## 1. Introduction

In the past decade, the field of photovoltaics (PV) has been turned on its head by the arrival of "perovskite" materials. In this context, "perovskite" means hybrid organic–inorganic halides crystallizing in perovskite structures, and such materials have shown better intrinsic properties for PV applications than K. V. Sopiha, C. Comparotto, J. J. S. Scragg Solar Cell Technology Division Dept. Materials Science and Engineering Uppsala University Uppsala 75237, Sweden E-mail: jonathan.scragg@angstrom.uu.se J. A. Márquez Department of Structure and Dynamics of Energy Materials Helmholtz-Zentrum Berlin für Materialien und Energie (HZB) 14109 Berlin, Germany The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adom.202101704.

© 2021 The Authors. Advanced Optical Materials published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.

## Doi: 10.1002/Adom.202101704

almost anything that has come before. 

High absorption coefficients allow efficient solar cells to be made from films in the range of 300–500 nm thick, while high mobilities for electrons and holes, and a lack of deep defects, allow long charge carrier diffusion lengths and lead to efficient collection of photoexcited electrons.[1,2]
These properties have underpinned the rapid rise of certain halide perovskites to high efficiency in PV cells.

While very impressive single-junction solar cell efficiencies have been reached,[3]
the "killer" application of PV perovskites in the near term is thought to be the augmentation of commercial crystalline silicon solar cells with wide-bandgap perovskite top cells, to create a tandem device. 

Si-perovskite tandem device efficiencies have reached 29%, which already exceeds the record for silicon technology alone, clearly demonstrating the promise of this concept.[4] Such tandem devices could be manufactured with high throughput, with some studies predicting lower per-Watt costs than existing technology.[5] Unsurprisingly, attempts to commercialize this technology are already underway.[6]
Apart from their optoelectronic properties, a useful engineering factor for halide perovskites is the ability to deposit films at low temperatures, in the range of 80–150 °C.[7] The ability to form highly crystalline, large-grained halide perovskite layers at low temperature, using simple solution-based approaches, has been an integral part of the rapid improvement in device performance compared with other (inorganic) PV 
technologies.[7] Besides, a low deposition temperature allows for straightforward integration of halide perovskite top cells onto completed Si subcells without risk of damage to the latter.

Despite their advantages, halide perovskite solar cells face challenges in terms of their long-term stability, due to degradation of the perovskite bulk and interfaces under various combinations of internal and external stressors such as heat, light, humidity, and electric fields.[8–11] For any new PV technology aiming at mainstream applications, long term stability must meet or exceed the high bar set by existing (Si) technologies. Performance warranties from some Si module manufacturers are at 25 years with as little as 10% degradation, and this is expected to improve to 30 years within a decade.[12] Even a small compromise in the operational lifetime of a perovskite– silicon tandem PV module could offset efficiency gains, erode cost reductions, and make the technology less attractive for 

![1_image_0.png](1_image_0.png)

 
investors.[5] The stability of halide perovskites might be enhanced by external means, such as encapsulation, but the ultimate solution lies in modifying the intrinsic properties of the perovskite materials themselves. To what extent this can be achieved with halide perovskites while retaining their good qualities is a question that is under intense research today.

Another family of PV materials, the chalcogenides, have already provided high-performance examples that have reached commercial applications in single-junction solar cells 
(principally Cu(In,Ga)(S,Se)2 and CdTe), and this family could thus be an alternative source of tandem top cell materials. Unlike the halide perovskites, good environmental stability is a common feature of chalcogenide compounds, which is an important advantage and underpins their commercialization by companies such as First Solar, Inc and Avancis GmbH. The challenges here are different from the halide perovskite case. One issue is that the better stability tends to go hand-inhand with higher temperature synthesis (>400 °C). While this can present problems for monolithic integration with Si cells, recent results have shown that this can be dealt with.[13,14] A 
more serious issue is that none of the emerging chalcogenide candidates has shown sufficiently high efficiency. To achieve a Si-based tandem device with over 30% efficiency, the top cell must have efficiency in the range of 17–19% for bandgaps in the range of 1.7–1.8 eV.[15] To date, the best example from the chalcogenides is Cu(In,Ga)S2, with a 15.5% efficiency at an 
≈1.65  eV bandgap.[16] **Figure** 1 compiles open-circuit voltage data from solar cells based on different material categories, compared to the band-gap dependent Shockley–Queisser (SQ) limit. Data are shown for chalcogenides in the chalcopyrite group (i.e., Cu(In,Ga)Se2 and derivatives), "emerging" chalcogenides including Cu2ZnSnS4 and other newer examples, halide perovskites containing organic cations as well as pure inorganic halide perovskites. The data are assembled from several sources;[17–19] the reader is referred to these and the references therein for more detailed information. The figure shows that the halide perovskites stand out in terms of low voltage losses in the relevant bandgap range. The chalcogenides 

![1_image_1.png](1_image_1.png)

nearest the appropriate bandgap range (of which there are few) have considerably larger voltage losses with respect to the SQ limit. Part of these voltage losses could simply be due to nonoptimal contacts and interfaces in the solar cell structures used.[20] However, unlike the halide perovskites, none of the chalcogenide candidates has shown any other primary indication of high photovoltaic potential, such as a high luminescence quantum yield that would suggest open-circuit voltage potential near the SQ limit. This points to a widespread problem of low defect tolerance in the wide gap chalcogenide absorber materials that have been examined thus far.

In summary, while halide perovskite PV researchers have become increasingly invested in the search for alternative perovskites that can fully eliminate instability issues (and, ideally, avoid the use of Pb), chalcogenide PV researchers are searching for new wide bandgap materials with higher defect tolerance and device performance. These parallel pursuits may now converge in a relatively new family of materials, which are chalcogenides that adopt perovskite-type structures. Even at the very early stages, chalcogenide perovskites appear to fulfill many of the key optoelectronic and chemical prerequisites for high efficiency PV, including exceptional stability and intense luminescence. At the same time, their synthesis chemistry has stark differences to that of halide perovskites, and thin film growth apparently presents challenges. A short perspective on this topic was published in 2019,[21] but recent progress and growing interest has prompted us to put forward a more extensive review.

This review is intended to help kick-start a serious investigation of the chalcogenide perovskites, which is needed to determine their usefulness for PV applications. We hope that it can clear up some of the early misunderstandings that are natural in a new field, and provide guidance for researchers aiming to enter this area. Section  2 provides an assessment of which chalcogenide perovskites actually exist. It becomes clear that the family is rather smaller than imagined by many, but that it still contains candidates for tandem PV as well as other applications. Section  3 deals with the chemical properties, emphasizing the abundance, stability, and low toxicity of chalcogenide perovskites compared to other PV materials. Section 4 concerns optoelectronic properties, highlighting the critical unresolved questions surrounding chalcogenide perovskites' potential in PV. Section  5 covers the current understanding of synthesis and formation of chalcogenide perovskites, points out some inherent problems with the currently used methods from thin film growth and derives useful lessons from the solid-state synthesis literature. Section 6 summarizes the key take-home messages from the previous sections.

## 2. The Discovered Chalcogenide Perovskites

This section summarizes which chalcogenide perovskites exist, or which might exist based on published data. We focus only on ABX3 compounds where X is S or Se. Oxide perovskites tend to possess bandgaps much too wide for PV, besides being a class of compounds in themselves, while telluride perovskites have been neither reported experimentally nor predicted to be stable computationally.

 

![2_image_0.png](2_image_0.png)

## 2.1. Perovskite Structures

ABX3 chalcogenides exhibit many different structural motifs with different connectivity of BX6 octahedra.[22] Only some of these—specifically those with corner-sharing BX6 octahedraare classified as perovskite structures, and various distorted versions of these occur. The main prototype structures discussed here are depicted in **Figure** 2, of which the perovskite structures are the GdFeO3-type (space group *Pnma*) and YScS3-type (space group *Pna21*). In the latter, there is a slight displacement of the B-site cations away from the center of their BX6 octahedra. 

Nonperovskite configurations include networks of edge- or face-sharing BX6 octahedra, including the hexagonal BaNiO3type (space group *P63/mmc*), the "needle-like" (NH4CdCl3-type, space group *Pnma*) and the UFeS3-type (space group *Cmcm*) structures. All reported ABX3 perovskites (except for several model compounds in simulations) show either II-IV-VI3 or IIIIII-VI3 chemical formulae, but not all such formulae lead to perovskite structures. In fact, many compounds in literature are loosely referred to as a "perovskite" based on an ABX3 chemical formula, despite having nonperovskite crystal structures.

Both perovskite structures illustrated in Figure 2 are distortions of the idealized cubic perovskite. **Figure** 3 illustrates the decrease in structural symmetry from cubic perovskite, via pseudo-cubic (distorted) perovskites and to nonperovskites. 

The most relevant form for our purposes is the GdFeO3-type structure, known as β-phase in the chalcogenide perovskite literature due to being observed at higher temperature. Another relevant phase is the nonperovskite NH4CdCl3-type, which has become known as α-phase and appears at lower temperature in some ABX3 systems. We note that this α/β nomenclature differs from that used for halide perovskites. To avoid confusion, we will primarily refer to the structures by the prototype names.

## 2.2. Experimental Structures Of Abx3 Compounds (X = **S, Se)**

Table 1 compiles the structures of ABX3 compounds experimentally reported to-date for X = S or Se. The set of compounds adopting the corner sharing perovskite structures consists of IIIV-VI3 compounds (II = Ba, Sr, Ca, Eu; IV = Zr, Hf; VI = S, Se) 
and III1-III2-VI3 compounds (III1 and III2 = Lanthanides, Y, Sc; VI = S, Se). If we exclude the compounds containing radioactive elements, there are eight II-IV-VI3 and thirteen III1-III2-VI3 experimentally reported chalcogenide perovskites. Below, we bring out the important findings for the sulfides and selenides.

Sulfides: The most commonly synthesized sulfide perovskite is BaZrS3, which is reported to crystallize in the GdFeO3-type structure irrespective of the deposition method and temperature.[23,24,32,41,42,68–73] Similarly, BaHfS3 has only been found in the GdFeO3-type phase by several authors.[23–25]
By contrast, SrZrS3 occurs in two distinct modifications depending on the growth process[70,92]—low-temperature NH4CdCl3-type (α-phase) and high temperature GdFeO3type (β-phase)—with the phase transition at about 980 °C.[92]
Most studies report the GdFeO3-type modification for SrZrS3, due to using synthesis temperatures above the transition.[23,24,32,70,92] EuZrS3 seems to have similar behavior Figure 3. Structural relationship between different ABX3 phases, taken from halide perovskite literature. The figure indicates two relevant phases for 

![2_image_1.png](2_image_1.png)

![2_image_2.png](2_image_2.png)

the purposes of chalcogenide perovskites, related by a phase transition triggered by changing temperature. Adapted with permission from J. A. Steele et al., *Acc. Mater. Res*. 2020, 1, 3. Copyright 2020, American Chemical Society.

 

![3_image_1.png](3_image_1.png)

| Table 1. Crystal structures of experimentally grown ABX3 chalcogenide compounds reported in literature. Entries in bold have had perovskite structures reported. Compound Phases reported Compound Phases reported BaHfS3 GdFeO3-type[23–25] LaYbS3 Below 1270 K, UFeS3-type[26,27] High-temperature YScS3-type[26,28] CeErS3-type[29] BaNbSe3 Off-stoichiometric hexagonal[30,31] BaSnS3 NH4CdCl3-type  LaYbSe3 UFeS3-type[27] (high-pressure synthesis)[32,33] LaYS3 CeTmS3-type[28,34,35] BaTaS3 BaNiO3-type hexagonal[36] NdScS3 YScS3-type[37] BaTaSe3 Off-stoichiometric hexagonal[38] NdLuS3 UFeS3-type[28] BaNiO3-type[39] NdLuSe3 UFeS3-type[40] BaTiS3 Hexagonal[32,41–45] NdYbS3 UFeS3-type[28,47] U Misfit off-stoichiometric[46] NdYbSe3 FeS3-type[27] BaTiSe3 BaNiO3-type[39] PbHfS3 NH4CdCl3-type[48–50] BaUS3 GdFeO3-type[23] PbSnS3 NH4CdCl3-type (high-pressure synthesis)[33] NH4CdCl3-type[51,52] BaVS3 Hexagonal above 240 K[53–56] Cmc21 or Cmcm below 240 K[53–57] BaNiO3-type hexagonal[58] PbTiS3 Tetragonal but authors say that inaccurate[43,49,59] Misfit off-stoichiometric[60–64] BaVSe3 Hexagonal, isostructural with BaVS3 [65] PbVS3 Misfit off-stoichiometric[66] PbZrS3 NH4CdCl3-type[48,49,67] BaZrS3 GdFeO3-type[23,24,32,41,42,68–73] PrLuS3 UFeS3-type[28] BaZrSe3 Hexagonal off-stoichiometric misfit  (distorted BaNiO3-type)[74,75] BaNiO3-type[39] PrLuSe3 UFeS3-type[40] PrScS3 YScS3-type[37] PrYbS3 UFeS3-type[28] CaHfS3 GdFeO3-type[23] PrYbSe3 UFeS3-type[27] CaSnS3 GdFeO3-type[76]a) SmScS3 YScS3-type[37] CaZrS3 GdFeO3-type[23,42] SmYbSe3 UFeS3-type[27] CeLuS3 UFeS3-type[28] SnHfS3 NH4CdCl3-type[50] CeErS3 CeErS3-type[29] SnNbS3 Misfit off-stoichiometric[64] CeHoS3 CeTmS3-type[29] SnSnS3 NH4CdCl3-type[77] CeScS3 YScS3-type[37] SnZrS3 NH4CdCl3-type[80] GdFeO3-type[78,79] SrHfS3 GdFeO3-type[23–25] CeTmS3 CeTmS3-type[81] SrHfSe3 NH4CdCl3-type[82] CeErS3-type[29] SrSnS3 NH4CdCl3-type (high-pressure synthesis)[32,33] CeYbS3 UFeS3-type[28] SrTiS3 Hexagonal[32,41] CeErS3-type[29] Hexagonal off-stoichiometric misfit  (distorted BaNiO3-type)[75,83–87] CeYbSe3 UFeS3-type[27] CuTaS3 CuTaS3-type[88–91] SrTiSe3 Hexagonal off-stoichiometric misfit  (distorted BaNiO3-type)[75] DyScS3 YScS3-type[37] ErScS3 YScS3-type[37] SrZrS3 α-phase (NH4CdCl3-type) < 980 °C and β-phase (GdFeO3-type) > 980 °C[92] α-phase@850 °C and β-phase@1100 °C[70] NH4CdCl3-type[68] GdFeO3-type[23,24,32] EuHfS3 GdFeO3-type[23] SrZrSe3 NH4CdCl3-type[74] EuZrS3 NH4CdCl3-type[93] TbScS3 YScS3-type[37] EuZrSe3 NH4CdCl3-type[94] UCrS3 GdFeO3-type[96] Adv. Optical Mater. 2022, 10, 2101704 2101704 (4 of 27) © 2021 The Authors. Advanced Optical Materials published by Wiley-VCH GmbH   |
|---|

![3_image_0.png](3_image_0.png)

## ![4_Image_1.Png](4_Image_1.Png)

Table 1. Continued. 

| Compound                                                                              | Phases reported   | Compound   | Phases reported   |
|---------------------------------------------------------------------------------------|-------------------|------------|-------------------|
| GdScS3                                                                                | YScS3-type[37]    | UNiS3      | GdFeO3-type[97]   |
| GdFeO3-type[95]                                                                       |                   |            |                   |
| HoScS3                                                                                | YScS3-type[37]    | URhS3      | GdFeO3-type[98]   |
| LaErS3                                                                                | CeErS3-type[29]   | UVS3       | GdFeO3-type[96]   |
| LaLuS3                                                                                | YScS3-type[28]    | YScS3      | YScS3-type[37,99] |
| LaScS3                                                                                | YScS3-type[37]    |            |                   |
| LaTmS3                                                                                | CeErS3-type[29]   |            |                   |
| a)Structural characterization matched SnS2 phase, existence of perovskite not proven. |                   |            |                   |

considering that the low-temperature NH4CdCl3-type[93] and the higher-temperature GdFeO3-type[23] phases were reported in different works. The related compounds, SrHfS3
[23–25] and EuHfS3,
[23] have only been grown in the GdFeO3-type structure (owing to higher temperature synthesis), but considering the chemical similarity of Zr and Hf, they may have low-temperature NH4CdCl3-type modifications as well. CaZrS3 and CaHfS3 were claimed to have been made in the GdFeO3-type structure,[23,42,68] although several authors noted that these compounds required higher growth temperatures than, e.g., 
BaZrS3,
[25,41,42] implying that they might be unstable at lower temperatures.

Most studies agree that BaTiS3 and SrTiS3 both have hexagonal symmetry.[32,41–45] Clearfield noted that hexagonal BaTiS3 becomes disordered and S-deficient with increasing preparation temperature,[42] which could be related to formation of the off-stoichiometric misfit BaTiS3 compounds with a distorted hexagonal lattice,[46] commonly observed for SrxTiSy.

[75,83–87]
Hexagonal symmetry was also reported for BaTaS3
[36] and BaVS3.

[53–56,58]
Recently, Shaili et al. reported the synthesis of CaSnS3 at a relatively low temperature of 500 °C.[76] However, the reported X-ray diffraction (XRD) patterns, refined assuming the GdFeO3type structure, correspond well to SnS2. Since their derived lattice constant c was also about 15% larger than calculated for CaSnS3,
[100] we suppose that the structural assignment is erroneous.

There are several ABS3 compounds with A = Pb2+ or Sn2+, including PbZrS3,
[48,49,67] PbHfS3,
[48–50] PbSnS3,
[33,51,52]
SnZrS3,
[80] SnHfS3,
[50] and SnSnS3 (Sn2S3 with mixed +2/+4 valence of Sn).[77] All these systems crystallize in the NH4CdCl3type structure. When A = Sn, Pb, Bi and B = Ti, Ta, Nb, V or Cr, the off-stochiometric misfit layer compounds are formed instead.[60–64,66,101]
Several III-III-S3 systems have also been identified. The typically adopted structures are the distorted perovskite YScS3-type, derived from the GdFeO3 prototype by a slight displacement of the B cation, and the nonperovskite UFeS3 (or NdYbS3)- type structure. A series of lanthanide (Ln) compounds LnScS3 were made by Rodier et al. and found to have the YScS3 structure,[37,99] although later CeScS3 and GdScS3 were reassigned to the GdFeO3-type.[78,79,95] The original misidentification was likely due to the similarity of YScS3-type and GdFeO3-type structures, implying that the assignments for the other Ln compounds might need to be revisited.

![4_image_0.png](4_image_0.png)

Tien et al. attempted to grow LnLn′S3 compounds with Ln =
La, Ce, Pr, Nd and Ln′ = Lanthanides or Y.[28] They found stable compounds only when the ionic radii of Ln and Ln′ were substantially different. Two compounds of YScS3-type were identified: LaYbS3 and LaLuS3. Later, Rodier et al. discovered that LaYbS3 undergoes a structural transformation to a low-temperature UFeS3-type phase between 1270 and 1520 K,[26] indicating that perovskite is a high-temperature phase in III-III-S3 ABS3 as well. This conclusion is consistent with the newer findings of Mitchell et al., who produced UFeS3-type LaYbS3 at 1223 K.[27]
Kuhar et al.[35] and Crovetto et al.[34] reported formation of nonperovskite LaYS3 (monoclinic; CeTmS3-type), in accordance with the earlier work by Tien et al. Several studies reported synthesis of the related ABS3 compounds from the series of LnMS3
(Ln = Lanthanides or Y; M = Ti, V, Cr, Mn, Fe, Co or Ni),[102–105]
but none of them was found to form a perovskite structure.

Several other ABS3 compounds with various symmetries have also been reported in the literature. One of them is CuTaS3, which has been shown to appear in a "needle-like" phase with a structure different from the NH4CdCl3-type discussed above.[88–91]
Finally, we note a series of GdFeO3-type compounds containing uranium,[106] including URuS3,
[98] URhS3,
[98] UNiS3,
[97] UVS3,
[96]
UCrS3,
[96] and BaUS3.

[23] Obviously, these compounds have little practical relevance for PV, and hence are disregarded.

Selenides: Only a few ABSe3 combinations have with certainty been synthesized in the perovskite phase with GdFeO3type symmetry, and all of them contain uranium[107–109] or thorium.[110] Obviously, application of such compounds in solar cells would not be practical. Other findings for the selenides are briefly summarized below.

Growth of BaZrSe3 was first reported by Aslanov, who concluded that it crystallizes in a hexagonal structure, and that BaTiSe3 and BaTaSe3 were isostructural with BaZrSe3.

[39] Later, Tranchitella et al. found that BaZrSe3 instead forms an off-stoichiometric misfit phase,[74,75] which was also seen for SrTiSe3.

[75]
Given these findings, a GdFeO3-type perovskite structure for BaHfSe3, as reported in the Ph.D. thesis of Moroz,[111] seems unlikely. A misidentification, possibly related to substantial oxygen contamination, is possible.

ABSe3 compounds with slightly smaller A cations, namely, SrZrSe3,
[74] SrHfSe3,
[82] and EuZrSe3,
[94] were all grown in the NH4CdCl3-type phase. To the best of our knowledge, no phase transitions or alternative crystal structures have been reported for these compounds, in contrast to their sulfide relatives. For Ca at the A site, no ternary compounds have been reported. 

## 

Tranchitella et al. mentioned that their attempts to prepare CaZrSe3 yielded a mixture of CaSe and ZrSe2.

[74] Moroz et al. 

also reported that CaHfSe3 could not be obtained.[82,111]
A series of III-III-Se3 combinations has also been studied by Mitchell et al.[27] and Jin et al.,[40] who found that LnYbSe3
(Ln = La, Ce, Pr, Nd or Sm) and LnLuSe3 (Ln = Pr or Nd) 
crystallize in the UFeS3-type structure. Later, Jin et al. also reported that slightly off-stoichiometric GdScSe3 (i.e., 
Gd1.05Sc0.95Se3) also forms in the UFeS3-type structure.[95]

## 2.3. Structural Factors And The Rarity Of True Perovskite Chalcogenides

The previous section revealed that true perovskite chalcogenides are actually rather rare, occurring primarily among sulfides, with many examples only emerging as high-temperature phases rather than ground states. The relative rarity of true chalcogenide perovskites seems related to the Goldschmidt tolerance factor t r r r r A X
2( B X ) = ++
[112] and octahedral factor rr B
X
µ = .

[113,114]
These quantities are empirical parameters for predicting stability and type of ABX3 structures using tabulated radii, rA, 
rB, and rX. True perovskites are generally expected for 0.7 <
t <  1.1, with the undistorted cubic symmetry usually forming for t = 0.9–1. At the same time, only those ABX3 combinations which have ( 2 − < 1) µ < − ( 3 1) form stable perovskites.[115]
Various definitions of ionic radii exist but must be used consistently to provide meaningful results.[116] Consequently, we limit ourselves to the values deduced by Shannon.[117] While various modifications of the structural factors have been proposed, to incorporate electronegativity,[22] to account for alloying[115] or to combine them into single expression,[114] we use the conventional definitions for simplicity. We note that this approach is only empirical, and exceptions can occur.

Since O is a small anion (rO = 1.40 Å), a huge number of cationic combinations yield both t and μ in the desired ranges, explaining why over 90% of metal ions are found in ABO3 perovskites.[115] In the case of sulfides (rS = 1.84 Å) and selenides (rSe = 1.98 Å), the reduction in structural factors due to the larger anions must be balanced by switching to correspondingly larger cations. Placing a heavier alkali-earth or rare-earth cation at the A site easily satisfies the criteria for t,
[32] but there are very few options for the B-site with large enough radius to keep μ above its critical value. For the case of sulfides with the A cation from the heavier alkali-earths (i.e., Ba2+, Sr2+, Ca2+), a B cation with stable oxidation state of 4+ is needed to form a IIIV-VI3-type compound. Excluding toxic Pb, possible candidates are Ti, Zr, Hf, and Sn. Unfortunately, all these elements give μ values below the threshold of 0.41, see **Figure** 4. The highest μ value, 0.39, is achieved for (A)ZrS3 (rZr = 0.72 Å, rS = 1.84 Å), 
explaining why most experimental studies to-date concern such compounds. As the octahedral factor gets even lower for smaller B cations, the probability of forming perovskites (and hence, the frequency of experimental reports) decreases rapidly. This problem is even worse for Se anions. While μ is the hardest to satisfy, t is still relevant, because a lower μ can be tolerated when t is closer to unity.[113] This explains why BaZrS3 is the most reported chalcogenide perovskite.

![5_image_1.png](5_image_1.png)

## 2.4. Structures From Density Functional Theory (Dft)

Although many compounds have been experimentally investigated, calculations can identify unexplored possibilities, or at least help rationalize observed trends. Considerable effort has been devoted to identifying stable ABX3 structures and analyzing their properties with DFT. Many of these works employed high-throughput material screening, which has the disadvantage of sacrificing accuracy and thoroughness to the benefit of rapid discovery. For instance, Körbel et al. analyzed the stability of over 32 000 ABX3 combinations (not limited to chalcogenides), but did so for a high-symmetry cubic phase containing 5 atoms only, with an additional analysis of just one distortion type for a selected subset of compounds.[118] As a result, the ground state energies of chalcogenide ABX3 reported by Körbel are consistently higher than those found elsewhere. 

In the study performed by Kuhar et al., 705 different ABS3 combinations in eight symmetries were analyzed,[35] but the results show overall poor agreement with all other works, which might be due to the use of different functional but may also indicate a systematic error. The key parameters and limitations of the high-throughput computational works on this topic are summarized in **Table** 2.

A recurring problem with the high-throughput works is that they tend to focus only on one aspect of thermodynamic stability: 
either on the energy of the perovskite ABX3 structure versus the competing ABX3 structures,[22,119] or on the energy of formation of ABX3 with respect to competing phases.[118,121] Strictly, stability can only be established by evaluating both parameters. Construction of exhaustive convex hulls or more complete sets of decomposition reactions would be needed to firmly establish thermodynamic stability of the ABX3 compounds.[122] In the meantime, we attempt to make sense of the available literature data. For consistency, we summarize the results from various sources by adjusting all reported energies according to the following definitions for Hf, the formation energy with respect to binaries, and for Hg, the energy with respect to the ground state, where all terms are energies (Ex) in the relevant structure

$$H_{\mathrm{f}}=E_{\mathrm{ABX}_{\mathrm{i}}}^{\mathrm{preexkise}}-E_{\mathrm{BX}_{\mathrm{i}}}-E_{\mathrm{AX}}$$
$$\left(1\right)$$
perovskit = − 3 BX2 − AX (1)
$$H_{\mathrm{g}}=E_{\mathrm{ABX}_{\mathrm{i}}}^{\mathrm{preonsize}}-E_{\mathrm{ABX}_{\mathrm{i}}}^{\mathrm{ground\,state}}$$
$$\mathrm{(2)}$$
ground state = − 3 3 (2)

![5_image_0.png](5_image_0.png)

 

![6_image_1.png](6_image_1.png)

Table 2. Summary of the most important computational studies about stability of ABX3 chalcogenide perovskites.

| Reference                                                                                              | Functional                                                   | Systems considered                                                             | Stability criteria                                                                 | Remarks                                                                         | # phases   |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------|
| Sun et al.[119]                                                                                        | PBEsol                                                       | A = Ca, Sr, Ba, B = Ti, Zr, Hf                                                 | Formation energy difference for ABX3                                               | 4                                                                               |            |
| X = S, Se                                                                                              | phases                                                       |                                                                                |                                                                                    |                                                                                 |            |
| Huo et al.[120]                                                                                        | PBE                                                          | A = Mg, Zn, Cd, Ca, Sr, Ba, Sn, Pb B = Ti, Zr, Hf, Si, Ge, Sn, Pb X = O, S, Se | Formation energy difference  for ABX3 phases.                                      |                                                                                 |            |
| Energy with respect to binary phases. Phonon spectra                                                   | 4                                                            |                                                                                |                                                                                    |                                                                                 |            |
| Brehm et al.[22]                                                                                       | LDA                                                          | X = S (all)                                                                    |                                                                                    |                                                                                 |            |
| 1) A = Ca, Sr, Ba, Pb, Sn with B = Zr, Ti 2) A = K, Rb, Cs, Tl with B = V, Nb 3) A = Bi with B = Sc, Y | Formation energy difference                                  | Included entropy contribution.                                                 | 22                                                                                 |                                                                                 |            |
| for ABX3 phases                                                                                        | Less accurate functional                                     |                                                                                |                                                                                    |                                                                                 |            |
| Kuhar et al.[35]                                                                                       | mBEEF                                                        | 705 different ABS3 combinations                                                | Formation energy difference  for ABX3 phases. Convex hulls based  on OQMD database | Symmetry defined before  ionic relaxation. Poor consistency with  other studies | 8          |
| Körbel et al.[118]                                                                                     | PBE                                                          | A and B = all elements up to Bi,                                               |                                                                                    |                                                                                 |            |
| excluding rare gases and lanthanides X = N, halogens, chalcogens. Over 32 000 systems in total         | Convex hulls based on MP                                     | Quantification of instabilities                                                |                                                                                    |                                                                                 |            |
| and OQMD                                                                                               | is impossible based on  one phase results only               | Only cubic                                                                     |                                                                                    |                                                                                 |            |
| Filippone et al.[121]                                                                                  | PBEsol, SCAN,                                                |                                                                                |                                                                                    |                                                                                 |            |
| SCAN + rVV10                                                                                           | A = Ca, Sr, Ba B = Ti, Zr, Hf X = S, Se                      | Energy with respect                                                            | Only                                                                               |                                                                                 |            |
| to binary phases                                                                                       | GdFeO3-type                                                  |                                                                                |                                                                                    |                                                                                 |            |
| If either of these quantities is positive, the ABX3 structure                                          | energy than the perovskite ground state and might form under |                                                                                |                                                                                    |                                                                                 |            |

If either of these quantities is positive, the ABX3 structure in question is unstable, which will hinder synthesis or render it impossible. In practice, slightly unstable phases can be realized if both energies do not exceed certain thresholds—set at 200 meV f.u.−1 for Hf and 50 meV f.u.−1 for Hg as discussed below. The difference between these energies, Hf - Hg, determines the stability of the ABX3 ground state against decomposition irrespective of its crystal structure. It should be stressed that any compound hitherto predicted to be stable can later be proven unstable if a more favorable decomposition route or more stable ground state is identified, but the unstable phases cannot be stabilized through such future revisions.

Table 3 compiles the literature data for Hf and Hg for ABX3 with A = Ba, Sr, Ca, B = Zr, Hf, Ti, Sn, and X = S, Se. Energies presented by Körbel et al.[118] and Kuhar et al.[35] are excluded due to the aforementioned limitations. To minimize the variations, only one set of energies from Filippone et  al.[121]—
those computed with PBEsol functional—is presented. Energy values are estimated from figures if not given explicitly, as in the work of Huo et al.[120] We supplement the literature values with data available from the Materials Project (MP)[100] and Open Quantum Materials Database (OQMD).[123] We note that the family of III-III-X3 perovskites has only been analyzed in a high-throughput manner by Kuhar et al.[35] and only one representative, YScS3, has been studied in detail by Zhang et al.[124]
Owing to the lack of data, these compounds and II-IV-X3 perovskites containing uranium are excluded from the discussion below.

Based on the available calculations, BaZrS3 and BaHfS3 are the only ABX3 chalcogenides that can be confidently claimed stable and be ascribed the GdFeO3-type ground state. For BaZrS3, this conclusion was reached in nearly every theoretical study,[100,119–121,123,125] with the exception of Brehm et al.[22] For BaHfS3, the NH4CdCl3-type structure has only slightly higher energy than the perovskite ground state and might form under certain growth conditions.[100,119]
SrZrS3 and SrHfS3 are somewhat less stable in the perovskite phase than their Ba-containing counterparts due to the slightly smaller tolerance factors. Most studies agree that the NH4CdCl3-type is the ground state, with the GdFeO3-type structure being within 75 meV f.u.−1 higher in energy.[22,100,119,120,128]
The only exception is OQMD, which indicates that the NH4CdCl3-type and GdFeO3-type phases have nearly identical energies.[123] Likewise, the NH4CdCl3-type phase of SrHfS3 is between zero[120] and 35 meV f.u.−1[119] more stable than the GdFeO3-type phase. Our assessment is that the NH4CdCl3-type phase is the ground state for both compounds, with the perovskite phase being close in energy. All reported Hf values are negative for SrZrS3 and SrHfS3,
[100,121,123] indicating that they are stable with respect to the binaries.

The predicted GdFeO3-type ground states for BaZrS3 and BaHfS3, as well as the NH4CdCl3-type ground state for SrZrS3, have all been observed experimentally (see Table 1). Importantly, the GdFeO3-type perovskite structure for SrZrS3 appeared at temperatures above 980 °C.[70,92] The stabilization of GdFeO3type SrZrS3 at higher temperature signifies that it has higher entropy than the NH4CdCl3-type ground state. Indeed, Brehm et al. demonstrated that GdFeO3-type phases have higher vibrational entropy than their NH4CdCl3-type counterparts,[22]
although unfortunately this is the only report explicitly dealing with the entropy contribution to the free energy of chalcogenide perovskites. For this reason, we call for a more extensive analysis of this material aspect. In the meantime, based on the case of SrZrS3, phase transitions into the GdFeO3-type phase can be anticipated in all systems where Hg is below 50 meV 
f.u.−1 This value is estimated based on the Hg values for SrZrS3 listed in Table 3 and used henceforth to analyze the possibility of growing GdFeO3-type phases for other ABX3 compounds. 

![6_image_0.png](6_image_0.png)

![7_image_0.png](7_image_0.png)

Table 3. Energies of selected GdFeO3-type ABX3 perovskites with respect to binaries (Hf) and with respect to the corresponding ABX3 ground states (Hg) reported in different works. The majority of Hg values were obtained by comparing GdFeO3-type with NH4CdCl3-type and BaNiO3type structures, except for those in parenthesis. Asterisks (*) indicate values computed by combining Hg from Huo et al.[120] and Hg from the other sources cited. Values without zero-point energies are taken from Brehm et al.[22] Energies computed with PBEsol functional are taken from Filippone et al.[121] Most values from Huo et al.[120] were extracted from the presented figures. The **bold** font highlights the values used for the construction of Figure 5.

| Compound                                | Hf  [meV f.u.−1 ]                   | Hg [meV f.u.−1 ] [119]  0,[120]  0[100]                 |
|-----------------------------------------|-------------------------------------|---------------------------------------------------------|
| BaHfS3                                  | −435, [121] −290[100]               | 0,                                                      |
| BaHfSe3                                 | −103, [121]  42[120]                | 91, [119]  110[120]                                     |
| BaSnS3                                  | 160*,[123]  169*[100]               | 355[120]                                                |
| BaSnSe3                                 | -                                   | 331[120]                                                |
| BaTiS3                                  | −184, [121] −249[125]               | 161, [119]  194,[120]  108,[22] (163),[22]  237[125]    |
| BaTiSe3                                 | 181, [121]  354[120]                | 288, [119]  393[120]                                    |
| BaZrS3                                  | −456, [121] −339,[120] −350,[123]   | 0, [119]  0,[120]  13[22]                               |
| −317,[100] −221[125]                    |                                     |                                                         |
| BaZrSe3                                 | −133, [121] −56,[120] −40[123]      | 95, [119]  60,[120]  50[126]                            |
| CaHfS3                                  | 105, [121]  186[100]                | 0, [119]  0[120]                                        |
| CaHfSe3                                 | 293[121]                            | 0, [119]  0[120]                                        |
| CaSnS3                                  | 541, [123]  547[100]                | 226, [120]  (225),[100]  (185)[123]                     |
| CaSnSe3                                 | -                                   | 241[120]                                                |
| CaTiS3                                  | 270, [121]  306[120]                | 40, [119]  10,[120]  (40)[22]                           |
| CaTiSe3                                 | 453[121]                            | 39, [119]  30[120]                                      |
| [121]  185,[120]  175,[123]  183[100]   | 0, [119]  0,[120]  0,[22]  (58)[22] |                                                         |
| CaZrS3                                  | 108,                                |                                                         |
| CaZrSe3                                 | 290[121]                            | 0, [119]  0[120]                                        |
| SrHfS3                                  | −125, [121] −24[100]                | 35, [119]  0[120]                                       |
| [121]  248[120]                         | 83, [119]  90[120]                  |                                                         |
| SrHfSe3                                 | 129,                                |                                                         |
| SrSnS3                                  | 360*,[123]  380*[100]               | 355, [120]  470[127]                                    |
| SrSnSe3                                 | -                                   | 392, [120]  430[127]                                    |
| SrTiS3                                  | 116, [121]  173[120]                | 95, [119]  73,[120]  (>128)[22]                         |
| SrTiSe3                                 | 368[121]                            | 143, [119]  121[120]                                    |
| SrZrS3                                  | −135, [121] −70,[123] −42[100]      | 45, [119]  57,[120]  10,[100] 0,[123]  73,[22]  12[128] |
| [121]  175,[120]  158*,[123]  166*[100] | 83, [119]  30[120]                  |                                                         |
| SrZrSe3                                 | 114,                                |                                                         |

As an example, a phase transition between GdFeO3-type and NH4CdCl3-type phases is likely to occur in SrHfS3, which has so far only been grown in the former but might transform into the latter at lower temperatures (since Hg values for SrHfS3 and SrZrS3 are similar).

For BaZrSe3, BaHfSe3, SrZrSe3, and SrHfSe3, the reported Hg energies indicate that all four have NH4CdCl3-type ground state, with the GdFeO3-type perovskite being between 50 and 100  meV f.u.−1 higher in energy. In other words, the selenide perovskites are substantially less stable than their sulfide relatives, as expected from the decrease in the octahedral and tolerance factors (see Figure  4). This is consistent with experiment, which hitherto did not produce any perovskite phases for these compounds. When it comes to the stability with respect to binaries, BaZrSe3 is the only selenide ABX3 that 

 

![7_image_1.png](7_image_1.png)

was found to have negative Hf by most authors.[119,120,126] The Hf values for BaHfSe3 are less consistent, but there is at least agreement that the ground state NH4CdCl3-type phase is stable against decomposition into binaries. On the other hand, the calculations predict that the NH4CdCl3-type ground states of SrZrSe3 and SrHfSe3 are prone to decompose into the binary selenides—all Hf energies are positive,[100,120,121,123] as well as the corresponding Hf–Hg values. In theory, this should hinder formation of SrZrSe3 and SrHfSe3 ternary phases even in the predicted NH4CdCl3-type ground state, but this does not agree with the experimental findings where the NH4CdCl3-type was indeed observed. The possible explanations for this discrepancy include, from the computational side, the choice of exchangecorrelation functional or the omission of van der Waals interactions. (Filippone et al. demonstrated that inclusion of van der Waals interactions stabilizes the ABX3 perovskites by up to 60 meV f.u.−1.

[121]) From the experimental side, the synthesis was carried out at temperatures of 800 °C or higher,[74,82] and hence the difference in the entropy contribution to free energy must have been significant. This factor is ignored in standard energy calculations dealing with ground states (T = 0 K). It has already been estimated for halide perovskites using phonon calculations that entropy can indeed contribute more to the product than to the reactants.[129] Computational analysis of the effect would be extremely valuable for chalcogenide ABX3. In the absence of such, we define a separate energy threshold of 200 meV f.u.−1 for Hf, above which the predicted ABX3 is likely to decompose into binaries. This threshold value is selected to match the available observations and predictions for ABX3, but this may need to be revised when more date becomes available.

More contradictory results were reported for CaZrS3, CaHfS3, CaZrSe3, and CaHfSe3. Sun et al.[119] and Huo et al.[120]
both found that the GdFeO3-type is more stable than the other three phases considered (NH4CdCl3-type, hexagonal BaNiO3type, and cubic perovskite). This prediction agrees with the GdFeO3-type structures of CaZrS3 and CaHfS3 observed experimentally. However, analysis of just three phases is insufficient to make a conclusion about the ground state in this case. For instance, by analyzing 22 crystal structures, Brehm et al.[22]
found that CaZrS3 stabilizes in a completely different prototype with a mixed edge- and corner-sharing connectivity of BX6 octahedra. The computed energy for this structure is 58 meV f.u.−1 lower than of the GdFeO3-type CaZrS3, which exemplifies the need to include more crystal symmetries for ABX3 (especially with A = Ca) in future studies. Along with the uncertainty around ground states, CaZrS3, CaHfS3, CaZrSe3, and CaHfSe3 appear prone to decomposition into binaries, since all reported Hf values are positive. For CaZrS3 and CaHfS3, the values vary between 100 and 200 meV f.u.−1. This could be the reason why growth of CaZrS3 and CaHfS3 required further increase in temperature.[25,41,42] The instability of CaZrSe3 and CaHfSe3 is even more severe, as the computed Hf values exceed 200 meV f.u.−1, as discussed in the work of Filippone et al.[121] This seems to explain why the reported synthesis attempts were not successful.

The Ti containing sulfides and selenides, BaTiS3, BaTiSe3, SrTiS3, SrTiSe3, CaTiS3, and CaTiSe3, have octahedral factors μ of 0.33 and 0.31 (see Figure  4), much lower than the minimum value for stable perovskite structures (0.41). As such, it 

 

![8_image_1.png](8_image_1.png)

is not surprising that none of these compounds has GdFeO3type ground state (all Hg are positive). In most computational studies, the BaNiO3-type hexagonal phase was found to be the ground state for BaTiS3 and BaTiSe3, with the perovskite GdFeO3-type phase being 100–250 and 250–400 meV f.u.−1 higher in energy, respectively.[22,119,120,125] All computed Hf values for BaTiS3 are negative, indicating stability with respect to binaries, agreeing with the experimental findings. As for BaTiSe3, the computed Hf are all positive, and the sign of Hf–Hg depends on the combination of energies taken from Table 3. Further analysis is needed to clarify this point. Sun et al.[119] and Huo et  al.[120] predicted the NH4CdCl3-type ground state for SrTiS3 and SrTiSe3, with the Hg energies exceeding the 50 meV f.u.−1 threshold (70–100 meV f.u.−1 for SrTiS3 and 120–150 meV f.u.−1 for SrTiSe3). The Hg and even Hf–Hg values are positive, indicating possible decomposition into the binaries, although this does not match experimental findings. Again, the consideration of more structures might have resolved this discrepancy. In the meantime, the available information does let us conclude that formation of GdFeO3-type phases for SrTiS3 and SrTiSe3 is highly unlikely. While both CaTiS3 and CaTiSe3 also have the lowest energy in the NH4CdCl3-type ground state, the GdFeO3type phases are only between 10 and 40  eV f.u. −1 higher in energy, i.e., within the threshold of 50 meV f.u. −1 On the other hand, the computed Hf values, 300 meV f.u. −1 for CaTiS3 and 450  meV f.u.−1 for CaTiSe3, lie well above the corresponding threshold of 200 meV f.u.−1, and thus these ternary compounds are unlikely to form at all. These considerations might explain why synthesis of CaTiS3 or CaTiSe3 has not been reported.

For the Sn-containing compounds, BaSnS3, SrSnS3, CaSnS3, BaSnSe3, SrSnSe3, and CaSnSe3, the results again point to nonperovskite structures as the ground state; the corresponding Hg values exceed the threshold of 50 meV f.u.−1 several times over. The data in Table  3 show that all (A)SnS3 have positive Hf, exceeding the threshold of 200 meV f.u. −1 in most cases, ensuring that none of the six compounds can be stabilized as a perovskite. This is another indication that the experimental structure reported by Shaili et al.[76] has been misidentified.

Surprisingly, little attention has been paid to III-III-X3-type perovskites. Zhang et al. analyzed YScS3 and found that it has nonperovskite UFeS3-type ground state, but with the perovskite phase lying only 17 meV f.u.−1 higher in energy.[124] The authors also found that YScS3 transforms from the prototypical YScS3type into the less distorted GdFeO3-type structure upon ionic relaxation. This finding means that the prototype structure is incorrect. In any case, both YScS3-type and GdFeO3-type phases are perovskites, differing merely by a slight displacement of the Sc atom.[124]
Figure 5 summarizes the computed values of Hg and Hf, weighted against the energy thresholds, for the most studied ABX3 chalcogenides—those with A = Ba, Sr, Ca, B = Ti, Zr, Hf, and X = S, Se. As one can see, only a handful of them—three 
(A)ZrS3 and three (A)HfS3—could be expected to form perovskite structures. This conclusion somewhat limits the selection pool for future material engineering and suggests focusing the research on these few stable chalcogenide perovskites. There might also be some interesting material candidates among stable III-III-X3 perovskites, but these are still barely explored such that we find it currently impossible to assess their PV potential.

## 2.5. Alloying Of Bazrs3

This section focuses on alloying of BaZrS3, which is the most popular chalcogenide perovskite synthesized by several independent research teams. Alloying can usually be realized between elements of the same valency and similar ionic radii. To obtain a wide range of alloy compositions, it is desirable that the terminal compounds have the same crystal structures. 

Based on the preceding sections, this suggests that alloying will be restricted to incomplete substitution of one or more of the constituing elements, Ba, Zr or S.

Several authors have investigated alloying BaZrS3 on the anion site by partial replacement of S with O or Se. Perera et al. claimed to have synthesized BaZr(O,S)3 alloys with different O/S ratios, based on their observation of a gradual shift in absorption edge but without direct characterization of the crystal structure.[68] By contrast, an earlier study found that BaZrS3 crystals segregated alongside BaZrO3 crystals in mixed O–S systems, with no solid solution forming.[42] Marquez et al. confirmed that there is indeed no crystalline solid solution, but they also saw the gradual shift in optical absorption edge for partly sulfurized BaZrO3, see **Figure** 6a,b.[130] They reconciled these seemingly contradicting results by postulating the existence of an amorphous BaZr(O,S)3 phase. Computationally, Vonrüti et  al. analyzed several BaZr(O,S)3 structures in a limited 40-atom supercell.[131] In our appraisal, their 

![8_image_0.png](8_image_0.png)

![9_image_0.png](9_image_0.png)

 

![9_image_1.png](9_image_1.png)

results favor decomposition into the pristine end members. Pilania et al. considered a larger set of anionic arrangements focusing on the O/S = 0.5 composition in a 20 atom supercell.[115] Although all investigated configurations were found unstable for CaHf(O0.5,S0.5)3, BaZr(O0.5,S0.5)3, BaHf(O0.5,S0.5)3, and SrHf(O0.5,S0.5)3, several configurations did attain negative mixing enthalpies when replicated in CaZr(O0.5,S0.5)3 and SrZr(O0.5,S0.5)3. On the other hand, stability with respect to the competing phases was not considered, and in the light of the previous sections, this casts doubt on the existence of such compounds.

Adding Se at the S site in BaZrS3 offers better miscibility due to the smaller difference in ionic radii. However, the nonperovskite ground state of BaZrSe3 and the existence of a competing Ba1.07ZrSe3 phase discovered by Tranchitella et al.[74,75]
naturally confine the range of alloying toward the more S-rich side. Nishigaki et al. reported synthesis of BaZr(S,Se)3 with the distorted perovskite symmetry at Se/(S + Se) = 0.4,[24] with both the bandgap and structural changes indicating successful alloying, see Figure 6c.

Alloying on the A site (Ba) presents few options due to the lack of larger divalent candidates for substitution. Sr is the main candidate, but perovskite is only the high-temperature phase of SrZrS3, and thus the maximum extent of alloying should be temperature-dependent. To the best of our knowledge, allowing with Sr (or Ca) has not been investigated in literature.

Partial replacement of the B cation, Zr, can provide more possibilities. A natural choice is Ti, but again the range of alloying is limited due to the nonperovskite ground state of BaTiS3. Correspondingly, Meng et  al. observed segregation of hexagonal BaTiS3 already at Ti/(Zr + Ti) = 0.1.[125] Ba(Zr,Ti)S3 without noticeable presence of secondary phases was realized at Ti/(Zr+Ti) = 0.05 by Nishigaki et al.[24] and at Ti/(Zr + Ti) = 0.04 by Wei et al.,[72] see Figure 6c–e. Another candidate for alloying on the B site is Hf. It is expected to produce a fully miscible Ba(Zr,Hf)S3 alloy because of the very similar ionic radii of Zr and Hf. We are not aware of any experimental study of Ba(Zr,Hf)S3 alloying to-date. Further possibilities, including substitution of Zr by Sn, remain to be investigated.

## 2.6. Summary Of Stable Perovskite Phases And Their Bandgap Range

Our appraisal of the literature to date reveals that there are rather fewer chalcogenide perovskite compounds than might previously have been perceived. For one thing, there is no good evidence of any selenide (or telluride) perovskites, apart from those based on uranium. Thus, a better label for this family may simply be "sulfide perovskites." In terms of sulfides exhibiting a perovskite structure as their ground state, BaZrS3 and BaHfS3 are the only clear-cut examples. While there are other experimentally determined perovskites among the sulfides, like Sr(Zr,Hf)S3, or EuZrS3, these appear to form only at higher temperatures (e.g., above 900 °C), which may restrict their applications. Others, such as CaSnS3, may have been wrongly assigned 
(although this must be reinvestigated). Additional examples of genuine sulfide perovskites include lanthanide LnScS3 and LnLn′S3, many of which are proven stable but the data to assess their PV potential is currently missing. The only piece of information available is from the computation study of YScS3 concluding that the material has an optical absorption onset of over 3  eV, which is more relevant for transparent conductive films than for solar absorbers.[124]
Table 4. Summary of bandgaps for the known chalcogenides adopting perovskite structures. Bandgaps are experimental values when available, otherwise from calculations (marked *).

| Compound/alloy                               | Bandgap [eV]                               |
|----------------------------------------------|--------------------------------------------|
| BaZrS3                                       | 1.75,[73]  1.82,[71]  1.89,[136]  1.94[24] |
| BaHfS3                                       | 2.17,[24]  2.06[25]                        |
| SrZrS3 (β phase)                             | 2.05,[70]  2.14[24]                        |
| SrHfS3 (β phase)                             | 2.32,[25]  2.41[24]                        |
| BaZr(S1-xSex)3                               | 1.76 (x = 0.4)[24]                         |
| Ba(Zr1-xTix)S3                               | 1.63 (x = 0.05),[24]  1.51 (x = 0.04)[72]  |
| YScS3                                        | ≈3*[124]                                   |
| Additional compounds Ba2ZrS4 (RP with n = 1) | 1.33[137]                                  |
| Ba3Zr2S7 (RP with n = 2)                     | 1.28[137]                                  |

Based on the preceding sections, we can summarize the known scope of bandgaps within the stable chalcogenide perovskites and their alloys—shown in **Table** 4—to see whether and where they may find applications in PV or other contexts. We note that the literature is incomplete, so this summary is subject to future extensions.

The bandgap of BaZrS3 is reported in the range of 1.75–1.95  eV. The reason for the ≈0.2  eV spread is unclear at the present time. Part of the explanation could be different amounts of Hf impurities, which are common at the level of several at% in Zr source materials,[132] and part due to different material quality and characterization methods. Further possible reasons for the spread are discussed in Section  4. The lowest reported bandgaps are for alloys of BaZrS3, with 4–5% of Ti at the B site causing the bandgap to drop by ≈0.3 eV. Se alloying was also capable of producing bandgaps down to 1.76 eV (from a reference point of 1.94 eV for BaZrS3 in the same study). We note that the exact values of the alloy bandgaps may be subject to similar variations as those of the parent compound; this matter needs further investigation. In any case, BaZrS3 and its alloys are in principle suitable for applications in tandem PV with silicon bottom cells, for which the ideal top cell bandgap is in the interval 1.7–1.8 eV.[133] While it is possible that Ba(Ti,Zr)
S3 can be applied in single junction solar cells, at present there 

 

![10_image_1.png](10_image_1.png)

![10_image_0.png](10_image_0.png)

is no evidence of low enough bandgaps for chalcogenide perovskites to be used as tandem bottom cells.

The other known chalcogenide perovskites have wider bandgaps than BaZrS3. The values for BaHfS3 and SrZrS3 are around 2.1 eV, for SrHfS3 they are in the range from 2.3 to 2.4 eV. These numbers could also be tuned by alloying, but since the parent compounds are less stable in the perovskite phase than BaZrS3
(see Table 3), they presumably can tolerate even lower concentrations of alloy elements. Nevertheless, these materials could find applications in future in multijunction PV, in semitransparent PV (such as for building-integrated PV, agrivoltaics, etc.) or in direct solar water splitting and photocatalytic processes, where their apparent stability, strong light absorption, and earth abundance are still highly advantageous. We also note that SrHfS3 is under investigation for green light emitting diodes (LEDs).[25]
Finally, we note that layered, or "2D" phases of the Ruddlesden–
Popper (RP) type have been reported, in which ABX3 layers in the perovskite structure are interspersed by planes of alkali metal cations at every nth ABX3 layer. This results in chemical formulae of the general type An+1BnX(3n+1). Experimental examples include Ba3Zr2S7 (n = 2) and Ba2ZrS4 (n = 1); n = ∞ corresponds to the parent perovskite structure.[134] These particular compounds demonstrate narrower bandgaps, ≈1.3 eV, making them potentially suitable for single junction solar cells.[134,135] However, since they fall outside the strict scope of this review, we remark upon these compounds for the interested reader, without discussing them further.

## 3. Chemical Properties 3.1. Abundance And Toxicity

Two increasingly important considerations for PV are a) sufficient availability of the constituent elements, to sustain large scale production at low cost, and b) low toxicity, to reduce lifecycle impacts and risks of the technology. Both aspects are complex, and a full discussion is beyond the scope of this review. Here, we simply perform a basic comparison to existing and emerging PV technologies based on Si, GaAs, CdTe, Cu(In,Ga)Se2 (CIGS), halide perovskites, and Cu2ZnSnS4 (CZTS).

The abundances of some PV-relevant elements in the Earth's crust are given in **Figure** 7, with the elements found in the 

![10_image_2.png](10_image_2.png)

chalcogenide perovskites highlighted in yellow. All the mentioned elements except for Hf and Se lie in the top 20 most abundant, having higher abundance than, for example, Zn, Cu, and Pb. Data are taken from the work of Lide.[138] These figures do not translate to prices, because of the different accessibility and peculiarities of the mining and purification processes. Still, the relative abundances do indicate that a PV technology based on chalcogenide perovskites would be unlikely to face limitations in the availability of the core elements, creating the potential for low-cost production. This is in contrast to the challenges faced by Cu(In,Ga)Se2 and CdTe due to the scarcity of In and, particularly, Te. Other emerging chalcogenides also have an unfortunate tendency to incorporate rare elements, such as Agalloyed CIGS, Ge-alloyed Cu2ZnSn(S,Se)4 and Sb2(S,Se)3, where Ag, Ge, and Sb have abundances comparable to In.

In terms of toxicity, the absence of any heavy metals such as As, Cd or Pb is also advantageous. In fact, the elements found in the chalcogenide perovskites are more benign than in CIGS or CZTS, with Cu and Zn being eco-toxic in their (many) soluble forms. By contrast, the alkali earth metals including Sr have various roles in living organisms and therefore are not considered toxic apart from at extreme exposure levels.[139] Ba is toxic in its few water-soluble forms (e.g., BaCl2) but since most of its stable compounds are highly insoluble, its toxicity is minimal in practice (e.g., BaSO4 is used as a radiocontrast agent in medical X-ray imaging[138]). Zr and Ti are ubiquitous in living organisms despite not having natural biological roles,[140] while S is nontoxic apart from in certain biologically active compounds (e.g., H2S). Therefore, from a toxicity perspective, chalcogenide perovskites offer considerable benefits over both traditional PV including CdTe and GaAs as well as the emerging Pb-containing halide perovskites.

## 3.2. Stability

While poor chemical and environmental stability is a major 

![11_image_0.png](11_image_0.png) concern for halide perovskites, the chalcogenide perovskites appear to be devoid of such problems. This has been most strikingly demonstrated by Niu et  al.,[141] who performed thermogravimetric analysis—in air—on SrZrS3, BaZrS3 and several related chalcogenides, as shown in **Figure** 8a. They observed that chemical degradation (i.e., oxidation) of the materials in these conditions commenced only from 500 to 600 °C, as confirmed by the mass change and postanalysis by XRD. It was also reported that long-term ambient air storage as well as repeated water rinsing had no effect on the XRD pattern or the characteristics observed by UV–vis spectrophotometry for BaZrS3.

[68]
Wang et al. also reported the effects of water dipping on BaZrS3 bulk powders; they found that certain degradation was observable for less crystalline material, but that well-crystallized samples did not undergo degradation.[142] Gupta et al.[73] performed direct stability comparisons between BaZrS3 and methylammonium lead iodide (MAPbI3). They recorded photoluminescence 
(PL) intensity during ambient storage and steam exposure, as shown in Figure  8b. For ambient storage, the PL intensity of MAPbI3 halved after 3–4 days, whereas this took around 5 weeks for the BaZrS3 sample. For steam exposure, the PL of MAPbI3 was extinguished within 60 s, while the BaZrS3 sample retained more than 80% of its PL intensity after 10 min of treatment (further durations were not reported). The shape of the PL and the XRD pattern of the BaZrS3 sample were unchanged by the treatments. In the same work, the enhanced stability of the chalcogenide perovskite was attributed to two effects: 1) a substantially lower degradation of the crystal surface via interaction with water, as determined by ab initio molecular dynamics simulations, and 2) a much larger activation barrier for anion vacancy diffusion in the bulk. In the latter case, the lowest activation energy determined among various migration pathways was 0.43 eV higher in BaZrS3 compared to MAPbI3, as shown in Figure 8c,d. The difference was calculated to result in a seven-order of magnitude reduction in room temperature vacancy migration rate in the chalcogenide. This in turn was proposed to reduce photo-induced degradation—occurring as a result of anion vacancy creation and migration—which is one aspect of the stability problem in halide perovskites.[143] However, slow diffusion of S vacancies or other species can also be related to the general environmental stability of the chalcogenide compounds, because any chemical changes initiated at surfaces—such as oxidation—must be mediated by diffusion processes if they are to affect the bulk of the material.

The above findings provide striking indications of stability in certain chalcogenide perovskites, but more comprehensive studies need to be carried out to understand the origins and extent of this phenomenon. For instance, it would be relevant to understand to what extent the stability depends on the type of anions, and to what extent it depends on the different cationic components. Furthermore, a closer examination of the chemical and structural characteristics of the material surfaces before and after air, heat and humidity treatments, e.g., by X-ray photoelectron spectroscopy (XPS) or Raman characterization, would shed more light on any critical changes that are occurring.

## 4. Optoelectronic Properties And Defect Chemistry

The attention gained by chalcogenide perovskites is largely attributable to the first-principles calculations demonstrating impressive optoelectronic properties—comparable to their halide cousins—which have now begun to be verified in experiment. In this section, we first review optical absorption and emission phenomena, before discussing the reported results concerning the nature of the bandgaps, band edges and tails, charge transport, and defect chemistry. While the early results are indeed very promising, there is still uncertainty around some basic properties that we highlight here as a basis for future work.

## 4.1. Light Absorption And Luminescence

For PV devices, the strength of light absorption is an important parameter, because it determines the minimum thickness 

 

![12_image_1.png](12_image_1.png)

of the absorber layer necessary, and by extension, the material consumption per unit area. A thinner absorber offers lower series resistance and means that photogenerated charge carriers must cover a shorter path before being collected. This relaxes requirements on carrier mobility and/or lifetime. Thus, a better absorber can—all other things being equivalent—deliver high efficiency for poorer bulk properties, and with lower resource consumption.

In terms of light absorption, the chalcogenide perovskites are indeed truly exceptional. Their band edges, according to several authors, are composed mainly of sulfur 3p valence states and transition metal d conduction states, and these states have a very high joint density.[24] The result is a calculated absorption coefficient (α) that climbs rapidly above 105 cm−1 within 0.3–0.5  eV above the onset of absorption.[24,119,125] Meng et  al. 

made comparable calculations for BaZr(S,Se)3, Ba(Ti,Zr)S3, and halide perovskite MAPbI3, which showed very similar behavior 
(**Figure** 9a).[125] The comparison made by Nishigaki et  al. for BaZrS3, SrZrS3, BaHfS3, and SrHfS3 with MAPbI3, GaAs, and CuInSe2 determined that the absorption coefficient of the chalcogenide perovskites exceeded that of the established PV materials by up to one order of magnitude (Figure 9b).[24]
These large absorption coefficients have been confirmed by experimental studies, which all agree that α exceeds 2 × 105 cm−1 at photon energies of 0.5 eV above the bandgap.[24,71,130,144] Possibly the most convincing data come from Nishigaki et al., who supplemented DFT calculations with ellipsometry measurements on pelletized powders of several chalcogenide perovskites, and were able to show extremely good agreement.[24] As a result of the excellent light absorption, an absorber thickness of around 500 nm would be sufficient for high efficiency solar cells,[24] less than half the material thickness used in commercial chalcogenide thin film solar cells.

As the reverse of light absorption, efficient light emission at open circuit is a critical early indicator of high PV potential, that can be assessed before the technical challenges of device integration are approached. A high external luminescence efficiency (ηext) indicates small quasi-Fermi level splitting losses associated with nonradiative recombination, which in turn implies a potential for high open-circuit voltage.[145] Thus, the magnitude of ηext is an important means to assess the defect tolerance and estimate open-circuit voltage that the material could yield in a solar cell in the best case. A few studies have already reported promising external luminescence efficiencies for chalcogenide perovskites. For SrZrS3 (Eg = 2.13  eV), a ηext of ≈0.05% was determined (see Figure 9c) for one-sun equivalent illumination (extrapolated to a power density of 300 Wm−2, which corresponds to one-sun illumination for 532  nm radiation and the given bandgap[70]). This is still much lower than the 1−5% achieved in >20%  efficient halide perovskite and CIGS 
solar cells,[146,147] but considering the early stage of development and that the measurements were made on nonoptimized powders, the values are encouraging. Perhaps a fairer comparison is with other emerging inorganic PV materials. Indeed, the ηext values reported for SrZrS3 powders already exceed those of top-efficient Cu2ZnSn(S,Se)4 solar cells and evaporated CsPbI3 absorber layers.[148,149] In terms of open-circuit voltage, ηext of 0.05% at a bandgap of 2.13  eV corresponds to an implied Voc of 1.6  eV, an impressive 90% of the SQ limit.[150] This sets a 

![12_image_0.png](12_image_0.png)

 

![13_image_1.png](13_image_1.png)

precedent for wide gap chalcogenides and provides a clear indication that the optoelectronic quality of chalcogenide perovskites can meet or exceed that of traditional PV materials, even in the early stages of their development. In the same study, the PL intensity of BaZrS3 was about 1/20th that of SrZrS3, although again we point out that the samples were in no way optimized for optoelectronic performance. Incidentally, the related Ruddlesden–Popper phase Ba3Zr2S7 has also displayed excellent PL efficiency, 0.1% for one sun-equivalent illumination, corresponding to an implied Voc of 0.83  V at a bandgap of 1.28 eV, i.e., 80% of the SQ limit. Finally, it has been noted that the PL emission of undoped SrHfS3 is visible to the naked eye,[25] which is a qualitative indicator of high luminescence efficiency.

Excitonic effects are also important for certain materials, although exciton binding energies in 3D semiconductors (unlike in 2D and layered 3D) are typically lower than thermal energy at room temperature (e.g., ≈10 meV in MAPbI3
[151]). In the case of chalcogenide perovskites, the absorption and photoluminescence measurements in the literature are performed at room temperature, showing no signs of excitonic features. Further information might be obtained in future through measurements at low-temperature, or via investigation of quantum dot chalcogenide perovskite samples.

The reported light absorption and emission measurements reveal important similarities between chalcogenide and halide perovskites, particularly in terms of defect tolerance. These results alone provide strong motivation to pursue chalcogenide perovskites for PV applications and beyond. At the same time, 

## 4.2. Absorption Onset And Band Tailing

For BaZrS3, the current literature gives conflicting results concerning the size and nature of the optical bandgap, while the absorption onset region has stark differences to those of traditional PV materials.

In all cases, the band structure determined by DFT calculations has indicated a direct bandgap for BaZrS3,
[24,68,70,119,125,152,153]
which is intuitive given the excellent near-gap light absorption. However, few authors have commented on the selection rules governing the fundamental transition. Hanzawa et  al. concluded that the transition is allowed,[25] but Peng et  al. determined that the lowest energy transition in BaZrS3 is in fact forbidden, with the first allowed transition having an energy around 0.1  eV higher than the fundamental bandgap.[154] A 
similar result was found by Nishigaki et al. who reported that the lowest energy transition (V1→C1) is nonallowed, while the next-lowest energy transition (V2→C1) dominates α(E) from about 0.1  eV above the onset (see Figure  9d).[24] The possible unusual nature of the lowest energy transitions means that extracting bandgap values from experimental data using, e.g., 
Tauc plots—already an area subject to various errors of interpretation—must be done with extra care. This might underlie the large spread of experimental bandgap values reported for BaZrS3 (see Table 4).

![13_image_0.png](13_image_0.png)

 

![14_image_1.png](14_image_1.png)

On the other hand, the room-temperature PL peak position is very consistent. The reported positions from the six available studies yield an average of 1.82 ± 0.04 eV.[69–71,73,137,144] Notably, estimation of PL peak position is far less subject to measurement error than bandgap estimation from, e.g., Tauc plots. 

From this we conclude that ≈1.8 eV is a more reliable estimation of the bandgap of BaZrS3, assuming that the peak arises from the band-to-band transition. However, PL measurements do not explain the spread of optical absorption data nor shed light on the bandgap type. The PL peak position, however consistent, can also lie lower than the true gap because of band tailing and sub-bandgap absorption or when defect levels are involved in the luminescence process. We return to the possible origins of the above discrepancies later. For now, we are forced to conclude that the bandgap of BaZrS3, by far the best studied chalcogenide perovskite, is not yet well-enough characterized to convincingly determine its size or type. Until the issue is resolved, the DFT and experimental bandgaps for all the chalcogenide perovskites should be treated with some open-mindedness. We point out that these inconsistencies do not affect the promising high magnitude of the absorption coefficient, which is found both theoretically and experimentally.

Besides the bandgap itself, it is also important to make early analysis of band tails, which are caused by the existence of sub-bandgap states in a material. Quantifying band tails is important for assessing the open-circuit voltage potential of a material. A straightforward means to characterize band tails is via the Urbach energy EU, measured by the inverse gradient of ln(α) versus α at the onset region. In highly crystalline materials with direct gaps and minimal subgap states, e.g., GaAs, EU values can be in the range of 7–10 meV.[155] Nishigaki et al. 

determined an EU value of 28.1 meV from their ellipsometry data for BaZrS3.

[24] For other literature examples, we determined Urbach energies of about 75 meV.[71,144] It should be borne in mind that, without having good understanding of the bandgap type (whether it is indirect/direct, forbidden/allowed), it is not possible to surely attribute these measurements to subgap states. To characterize properly subgap states, sensitive measurements are required to probe the absorption when the density of states becomes very low. This is currently not available in the chalcogenide perovskite literature where in the best case the absorption coefficient measurements are resolved only down to 2–3 orders of magnitude.

Another window onto subgap states can be via PL measurements. In the presence of band tails, the PL peak can extend far below the bandgap. Indeed, all PL measurements for chalcogenide perovskites show a relatively large degree of broadening, especially toward lower energies; see **Figure** 10a. Whereas the PL for the MAPbI3 sample synthesized by Gupta et  al. had a full width at half-maximum (FWHM) of barely 90 meV and is essentially symmetrical, the best FWHM values for the chalcogenide perovskites range from 120 meV for SrZrS3 to 250 meV 
for BaZrS3.

[73] Because the high-energy wing of the PL spectra depends exclusively on the temperature, a broader PL peak must have a larger red-shift with respect to the bandgap energy, and this yields a larger penalty on the open-circuit voltage potential.[156,157] For comparison, assuming a band-to-band transition in BaZrS3, we calculated a theoretical PL spectrum from the absorption coefficient data reported by Nishigaki et  al.[24]
The result is a PL peak centered at 1.92 eV with an FWHM of 
≈95 meV (see Figure 10b), i.e., significantly narrower than what is found in the literature, and at 100 meV higher energy. This comparison demonstrates that current experimental samples are not ideal. Still, at the present time materials synthesis of chalcogenide perovskites is in its infancy, and optimization is expected to lead to further improvements.

While more data is needed, we point to some general phenomena that can help understand the large sample-to-sample variation, the general broadening of the PL response, and the disagreement between calculated and experimental data. To begin with, the fact that different bandgaps and PL peak widths are measured for different samples of BaZrS3 strongly suggests that "extrinsic" factors are distorting the intrinsic properties of the material. The most obvious source of these could be secondary phases with narrower bandgaps, which could occur for nonoptimized synthesis and especially in the event of nonstoichiometry. On the Ba-rich side, we note that all the phases belonging to the An+1BnS3n+1 series have narrower bandgaps than the perovskite phase.[137,158] The presence of smaller bandgaps could strongly affect absorption and emission measurements, giving the appearance of long tails or shifting the absorption onset. On the Zr-rich side, ZrS2 or ZrS3 could be 

![14_image_0.png](14_image_0.png)

 

![15_image_1.png](15_image_1.png)

expected, which have reported bandgaps in a range from 1.7 to 2.8  eV.[159,160] Another possibility is that stoichiometry or temperature differences could induce phase transitions or structural distortions in synthetic material. Calculations have indicated that the bandgap of BaZrS3 is sensitive to the precise degree of rotation of the ZrS6 octahedra:[33,35] the bandgap difference between a hypothetical cubic perovskite phase of BaZrS3 and the true orthorhombic phase, in which the octahedra are rotated by ≈9°, is nearly 0.7 eV.[35] Whether the degree of octahedral rotation might depend on growth conditions 
(such as temperature), strain and so on, remains to be established. Finally, as noted above, common impurities, such as Hf in Zr, could also modify bandgaps and PL signals.

## 4.3. Charge Carrier Transport And Recombination

There is little information on charge transport in chalcogenide perovskites, largely because few studies have dealt with thin film samples for which such measurements are most readily made. Computational studies have determined low effective masses for holes and electrons, due to the dispersive nature of the band edges.[125] The band direction-averaged effective masses of electrons and holes in BaZrS3 are 0.3m0 and 0.5m0, respectively, which are only slightly larger than those calculated for halide perovskites such as MAPbI3 (0.2m0 for electrons and 0.3m0 holes[161]). The effective masses of SrZrS3 and CaZrS3 are somewhat larger than for BaZrS3.

[24]
Wei et al. made Hall measurements on BaZrS3 films made by sulfurization of oxide precursors, and found electron mobility values up to 13.7 cm2 V−1 s−1 with an equilibrium carrier density of 3 × 1020 cm−3.

[71] In that case the material was n-type. Zeng et  al., for similarly prepared films, found 9.4 cm2 V−1 s−1 hole mobility and a p-type carrier density of 8 × 1017 cm−3.

[144] The type change is evidence that the processing and composition variations could shift the Fermi level to either side of midgap, as discussed further in the next section. Yu et  al. made films by sulfurization of Ba–Zr–S precursors and reported electron mobility of 16.8 cm2 V−1 s−1 and hole mobility of 2.6 cm2 V−1 s−1.

[162] The mobility values reported for chalcogenide perovskites are comparable to other direct bandgap inorganic compound semiconductors. 

For instance, the sum mobilities (hole plus electron mobilities) around 30–40 cm2 V−1 s−1 are measured for CsPbI3 and CZTS.[149,163] However, due to various influences of sample type, quality, measurement method and the associated uncertainties, more measurements are required to build up a consistent picture.[164]
In terms of charge carrier lifetimes, little is reported todate. From a fundamental point of view, we note that BaZrS3 belongs to a rarefied group of "highly polarisable" semiconductors, i.e., materials with relatively narrow bandgaps as well as low-frequency dielectric constants above ≈50; these are characteristics that rarely go together.[165,166] For photovoltaics, a high dielectric constant is argued to be beneficial via its contribution to charge carrier screening, thereby reducing recombination rates and extending carrier lifetimes. This phenomenon may be part of the reason that halide perovskite solar cells have reached such high efficiencies.[165] BaZrS3 was found to have an exceptionally large average dielectric constant of 80 ±
14,  exceeding the highest reported values for other semiconductors with bandgaps in the visible light range, including halide perovskites.[166] This inspires optimism that long charge carrier lifetimes may also be obtained in high quality samples of BaZrS3 and possibly other chalcogenide perovskites. Experimentally, charge carrier lifetimes have not been determined directly, but a PL emission lifetime of <7  ns  was determined at 300 K in BaZrS3 sample.[71] However, the time-resolved PL 
decay was not modeled and not many details about the measurement conditions were provided, while the samples themselves did not demonstrate high crystalline quality or chemical purity.

Radiative recombination rates are also not discussed in the literature yet, since the values for the radiative constant krad of the chalcogenide perovskites have not been calculated. Using the DFT calculated data presented in the literature we can make a rough estimate for krad. With band direction-averaged effective masses of electrons and holes of 0.3m0 and 0.5m0, respectively,[125] a combined density of states product NCNV of 6.7 × 1037 cm−6 is estimated using the standard semiconductor equations. This yields a range of intrinsic charge carrier concentration ni 2 of 1.4 × 106–1.4 × 104 cm−6 for bandgap values between 1.88 and 2 eV. With these ni 2 values and using the van Roosbroeck–Shockley equation[167] with the absorption coefficient and the refractive index nr reported by Nishigaki et al.,[24]
we obtain a range of krad values of 10−11 to 10−9 cm3 s−1. These values are in reasonable agreement with the ones reported for other direct semiconductors like halide perovskites[168] or CIGS,[169] and significantly larger than the ones reported for Si at 300 K.[170] The relatively large radiative constant suggests that, as for halide perovskites, the detailed balance efficiency limit at one sun equivalent conditions for chalcogenide perovskites will not be limited by Auger recombination, in contrast to what occurs in Si solar cells. We stress that dedicated experiments considering both transient and steady-state photoluminescence measurements are needed to quantify these values with more precision.

In addition to the experimental studies, charge carrier dynamics in chalcogenide perovskites have been investigated computationally using nonadiabatic molecular dynamics simulations. Nijamudheen and Akimov[171] calculated specific times for nonradiative electron–hole recombination in pristine BaZrS3 as well as alloys with Ti or Hf (at the Zr site) and O or Se (at the S site). They found that symmetry breaking, induced by alloying, promotes nonradiative carrier recombination. This effect was most severe in the case of alloying with Ti and O. The extent to which these results permit estimation of true carrier lifetimes is a topic of ongoing debate.[172,173] At the same time, consideration of intrinsic defects would be necessary to evaluate the typically dominant recombination path via deep defects (i.e., Shockley–Read–
Hall recombination).[174] Guo and Wang analyzed hot carrier dynamics in SrSnX3 (X = S,Se) and concluded that the decay times are longer than in organic–inorganic perovskites.[175]
Unfortunately, as concluded in Section  2, these compounds are unlikely to form. Whether more stable chalcogenide perovskites exhibit similarly favorable hot carrier dynamics remains to be determined.

![15_image_0.png](15_image_0.png)

 

![16_image_1.png](16_image_1.png)

## 4.4. Defect Chemistry And Doping

If any single issue is decisive when determining which materials are suited for optoelectronic applications such as solar cells, it is defect chemistry. Fortunately for the chalcogenide perovskites, the early results on defect properties are very promising. First, we consider the potential for formation of deep defects—which we define as those with transition energy levels near midgap. Two reports present defect calculations for BaZrS3.

[125,144] The most significant difference between these works stems from the adoption of different Hubbard U values for the Zr 4d electrons: 4.5 and 1.65 eV, respectively. Meng et al. calculated transition energy levels and formation energies of all 12 possible native point defects BaZrS3.

[125] They suggested five 
"deep" defect levels, created by Si, SZr, SBa, Zri, and ZrS. The first two, Si and SBa, can be discounted immediately, because they are acceptors sitting close to the conduction band edge (see Figure 11a). This means that they would have negligible contribution to Shockley–Read–Hall (defect-assisted) recombination, although they could have some effect on carrier mobility due to trapping/de-trapping. The next two "deep" defects, ZrS and SZr, had relatively high formation energies, >2 eV for all growth conditions considered, which will lead to negligible defect concentrations. Zri is the deep defect having lowest formation energy, but even for Zr-rich growth conditions, this reaches just below 2  eV. By way of comparison, the suspected deep defects VS and SnZn in the well-known emerging PV material Cu2ZnSnS4 have formation energy below 1  eV, and as low as 0.6  eV in certain conditions.[176] This difference will lead to a substantially higher deep defect concentration in Cu2ZnSnS4 compared to BaZrS3, other things being equal. Thus, from a defect point of view, given the limited information, BaZrS3 is already more promising than existing candidates for inorganic, earth abundant PV absorbers.

While the results of Meng et al. gave a positive picture, Wu et al. went further and claimed that, with a more accurate Hubbard U value for Zr 4d orbitals (1.65 eV), none of the intrinsic defects generate deep levels at all.[177] Specifically, the authors found that VBa and BaZr are shallow acceptors, VS, Bai, Zri, ZrBa, BaS, and ZrS are shallow donors, and VZr, Si, SBa, and SZr behave as self-passivated defects without midgap states in the neutral charge state. The self-passivation behavior was enabled by the spontaneous rearrangement of S atoms into small sulfur clusters with SS bonds. If true, such defect chemistry would, in principle, allow BaZrS3 to be made free of deep defects, which would place it firmly in the category of "defect tolerant" semiconductors. This is consistent with the promising luminescence efficiencies mentioned above. On the other hand, Wu et al. also found that hybrid functional yields deeper in-gap donor states for VZr, Si, SBa, and SZr due to less thorough selfpassivation. Still, all deep defects were found to have high formation energies, which limit their equilibrium concentrations, especially at S-poor conditions. Therefore, purely from the defect chemistry perspective, S-poor synthesis of BaZrS3 seems favorable.

Going forward, it is important that the mentioned calculations are clarified, and performed for other materials apart from BaZrS3. In addition, more defect types can be considered, in particular defect complexes, which in some materials have exceptionally low formation energies (e.g., {CuZn + ZnCu} in Cu2ZnSn(S,Se)4
[176]). Defect complexes can lead to phenomena such as preferred off-stoichiometric compositions, ordered defect compounds or disorder in the crystal structure. Indeed, it has been reported several times that BaZrS3 was formed with S-poor composition, which persisted despite annealing with excess S vapor.[178] This could imply formation of S-poor neutral defect complexes such as {VS + BaZr}. It will be important to explore this and related issues in BaZrS3 and the other chalcogenide perovskites.

The other important aspect of defect chemistry is doping. 

The type and density of doping and the degree to which it can be controlled are important for solar cell design and performance. The defect calculations of Meng et  al. predict several shallow intrinsic defects, including the donors (Bai, ZrBa, VS, 
and BaS) and the acceptors (BaZr and VZr). They concluded that S-poor growth conditions are likely to lead to degenerate n-type doping by VS, while S-rich conditions could create weak p-type material due to the balance of VS and Si.

[179] On the contrary, Wu et al. predicted that all defects with relatively low formation energies (below 1  eV in the neutral charge state) are shallow donors (VS, Zri, ZrBa, and ZrS), which led the authors to conclude that BaZrS3 cannot be intrinsically p-type irrespective of the growth conditions. Still, the Fermi level can be somewhat shifted depending on the growth conditions—higher majority carrier (electron) concentration, primarily due to VS, is expected in S-deficient BaZrS3.

Experimental reports do seem to support the possibility of ambipolar intrinsic doping in BaZrS3. In two cases, p-type doping was found.[144,178] In these cases, the carrier concentrations were 8 × 1017 cm−3 and 3 × 1017 cm−3 (the latter estimated from conductivity data taken from the work of Yan et  al.[178] using the mobility value of Zeng et al.,[144] 9.4 cm2 V−1 s−1). In 

![16_image_0.png](16_image_0.png)

 

![17_image_1.png](17_image_1.png)

another instance, intrinsic behavior was found,[136] and in yet another, n-type conduction was reported with a carrier concentration of 5  × 1020 cm−3.

[71] These findings do not show a clear correlation between doping type/density and the growth parameters or composition of the materials (although limited information is provided), so further investigations are needed. 

An important experiment would be to characterize charge carrier type and density for high-quality samples of chalcogenide perovskites (e.g., single crystals) annealed in different S vapor atmospheres; this may influence the proportions of the important donors and acceptors in a more controllable manner.

Hanzawa et al. showed experimentally that SrHfS3 could be extrinsically doped both n-type and p-type using phosphorous (P) at the S site or lanthanum (La) at the Hf site; see Figure 11b,c. Without doping, the conductivity was very low.[25]
The authors suggested that ambipolar doping can in general be expected in the chalcogenide perovskites due to the fact that their band edges lie within an appropriate range with respect to the vacuum level.[25] Multiple additional possibilities for extrinsic dopants can be suggested—and should be exploredincluding alkali metals (Li, Na, K, etc.) as p-type dopants.

For solar cell design, the ability to control doping type and concentration from intrinsic to degenerate levels could be extremely useful. To fabricate efficient solar cells based on p–n heterojunctions, carrier concentrations below 1017 cm−3 are desirable, and much lower if p–i–n structures are to be used. Doping control is also valuable for formation of low-resistance, carrier-selective contacts.

## 4.5. Devices Using Chalcogenide Perovskites

Initial studies have encountered challenges in growing highquality chalcogenide perovskite thin films, as a prerequisite for making devices. As we discuss in the next section, this is likely due to inappropriate growth conditions, necessitating exceptionally high growth temperatures. As a result, it has not been possible to grow chalcogenide perovskite thin films on conductive substrates, and therefore the fabrication of solar cells has been elusive. In two cases, device test structures have been formed by depositing contacts onto the surface of BaZrS3 thin films grown on insulating substrates.[71,73] In both cases, the current flow between these surface contacts was enhanced under illumination, indicating generation and transport of charge carriers. This area is naturally of great importance, but inability to grow high-quality thin films is a major bottleneck at present. In the final chapter, we summarize the materials chemistry underlying formation of chalcogenide perovskites, which reveals important clues to making progress on this front.

## 5. Synthesis And Synthetic Challenges

While the crystal structure and optoelectronic properties of chalcogenide perovskites seem similar to those of halide perovskites, the synthesis approaches adopted are completely different. This appears to be connected to the very different chemical properties of the chalcogenide compounds, as already hinted at in Section 3. Here, we review the synthesis methods employed for chalcogenide perovskites in various forms. Our focus is on the prospects for high-quality thin film growth. We find that the existing studies have used inappropriate methods, which may explain the challenges encountered for making good quality thin films. A targeted effort from this point could unlock major progress in the field.

## 5.1. Lessons From Solid-State Synthesis

A good deal of the literature of chalcogenide perovskites concerns materials prepared by bulk solid-state synthesis.[23–25,42,68,70,72,74,92,93,127,137,141,142,152,178,180–184] The typical growth conditions, including temperatures in excess of 1000 °C 
and reaction periods of many hours to days, are designed to facilitate complete interdiffusion of reactant materials over large length scales (µm to mm), to yield homogeneous and crystalline bulk material. These conditions are totally different to those that will be used for PV devices, and this can lead to some potentially misleading conclusions. One such example is the observation of perovskite structures for SrZrS3
[24,92] and EuZrS3.

[93] In fact, while these materials do happen to crystallize in this structure at the temperature of solid-state synthesis, at the temperatures commonly used for thin film synthesis 
(<700 °C), they would preferably adopt the NH4CdCl3-type structure (see Section  2), unless stabilized by some external factors. In the same vein, some materials may change their physicochemical properties and exhibit incipient structural degradation, due to, e.g., anion deficiency, when grown at high temperatures.[42,59] Indeed, several authors have reported sulfur deficiency, in the range 1–6 at% in BaZrS3 samples synthesized by reacting BaZrO3 with flowing CS2 at 900–1200 °C.[42,68,152,178]
In other methods, especially where the reaction was carried out in a sealed vessel, stoichiometric or even S-rich material has been grown (e.g., for BaZrS3
[183,184] and for SrZrS3
[92]). Sulfur deficiency can be connected to the low formation energy of S vacancies discussed earlier, and is likely to result in n-type material which may even become degenerate in the worst case.[125] Thus, it should be remembered that the material prepared from solid-state synthesis does not necessarily represent the best achievable absorber.

Nonetheless, some key insights have been gained in the solid-state synthesis literature. First, several authors reported difficulties in forming BaZrS3 using "standard" reaction conditions, i.e., mixing stoichiometric quantities of the elements or binary sulfides. For example, Hahn and Mutschke found that BaS and ZrS2 did not react together until a temperature of 900 °C was reached,[41] despite the fact that the ternary phase is known to be more thermodynamically stable than the binaries. This result indicates a large kinetic barrier to phase formation. A hypothesis is that the initial formation of a BaZrS3 layer—at the interface of BaS and ZrS2 particles—restricts further diffusion of one or more of the reacting elements. Thus, growth of the ternary phase becomes diffusion limited and considerable thermal energy is needed to drive it to completion by Reaction (1)
BaS Z+ → rS2 3 BaZrS (slow) (Reaction 1)

![17_image_0.png](17_image_0.png)

## 

The more widely used solid-state route for preparing chalcogenide perovskites is the reaction of an oxide precursor with flowing CS2, see Reaction (2). Clearfield showed that this process can yield phase-pure BaZrS3, and concluded that the required time and temperature to displace all oxygen was 4 h at 1050 °C.[42]

## 2Bazro3 2 + → 3Cs 2Bazrs 3 3 2 + Co (Reaction 2)

As noted above, it can be desirable to perform solid-state synthesis under milder conditions. For chalcogenides, this can often be achieved by providing a molten sulfur (S) phase.[59]
Wang and co-workers synthesized BaZrS3 by a solid state route using excess S, ostensibly to create this molten phase.[142,182,183]
In this way, a growth temperature as low as 500–600 °C could be used, with a high BaZrS3 yield. The quantity of S excess, expressed as α in Reaction (3), was important. If too little excess S was added, the BaZrS3 product was nonexistent (α =
0) or poorly crystallized (α <  0.5), with the main products being BaS, BaS2, and ZrS2. On the other hand, if a too large S excess was added (α > 1.5), the S-rich binary compounds BaS3 and ZrS3 were the major products. The largest yield of BaZrS3 occurred for intermediate α values. In this intermediate range, secondary phases, when observed, were only BaS3 and ZrO2.

[142]
Reaction (3) also includes the presence of 0.1 moles BaCl2. This was found to assist the reaction: if BaCl2 was omitted, higher temperatures were required to drive BaZrS3 formation, and the yield was somewhat lower[142]

0.9BaS 0.1BaCl ZrS S BaZrS S ,Cl fast
* BaZrS${}_{1}$ (+S${}_{2}$,Cl${}_{2}$)(fast) (0.5 $<a<1.5$) (Reaction 3)

![18_image_1.png](18_image_1.png)

2 2 α 3 2 2

+ + + → +
While these results are clear proof that BaZrS3 can be grown at temperatures suitable for solar cell integration, the dramatic effect of excess S was not adequately explained. Although Wang et al. implied that the excess S generated a molten phase, the reported reaction conditions do not appear to support this claim: the small amounts of S would have been able to vaporize entirely as S8 in most of the experiments. Neither does BaCl2 create a molten phase at the relevant temperatures; its melting point is ≈960 °C. Another conjecture was that vaporization of BaS3(g) and ZrS3(g) played a role in the formation of the ternary phase. However, we have been unable to find evidence that these phases have significant vapor pressures. Instead, we provide another explanation based on the changing S pressure in the reaction vessel, which should have been the main result of changing the value of α in Reaction (3).

For increasing α (i.e., increasing S pressure, ps), Wang et al. 

observed a sequence of phase formation as follows: BaS +
ZrS2 → BaS2 + ZrS2 → BaZrS3 (+ BaS3) → BaS3 + ZrS3. The appearance of BaS3 at α ≈ 0.5 was followed by the sudden formation of BaZrS3 at high yield. This apparent accelerating effect could be related to the melting point of BaS3 being relatively low, 554 °C,[185] because molten or near-molten BaS3 could admit much faster in-diffusion of Zr compared to BaS2 or BaS, which have melting points of 700 and 925 °C, respectively. Thus, under conditions of ps and temperature (T) where BaS3 becomes the stable binary phase, the formation of BaZrS3 could be accelerated compared to Reaction (1), as below

![18_image_0.png](18_image_0.png)

## Bas S( ) + → S G 2 3 ( ) Bas L( ) (Reaction 4A) Bas L 3 2 ( ) + → Zrs Bazrs3 2 +S G( ) (Reaction 4B)

$$({\mathrm{Reaction~2}})$$

At the higher limit of ps, α >  1.5, the appearance of ZrS3 was associated with the decrease and disappearance of BaZrS3. 

The formation of ZrS3, following Reaction (5), may somehow block the ternary phase from forming. Another possibility is that a too-high ps causes BaZrS3 itself to become unstable, Reaction (6)

## Zrs 1 2 2 + → /2S Zrs3 (Reaction 5)

(Reaction $6$) . 
$\mathrm{a}+\mathrm{Z}\mathrm{r}\mathrm{S}_{3}$ . 

## Bazrs3 2 + → 1.5S G( ) Bas Z 3 3 + Rs (Reaction 6)

Regardless of the mechanistic details, the appearance of the secondary phases (BaS3 and ZrS3) seems to define a window of ps between which BaZrS3 forms quickly at a given temperature. Within this "fast-formation" window, ps is high enough to form BaS3 (Reaction (4a)), but low enough to avoid ZrS3 formation (Reaction (5)). The fast-formation window could be defined in terms of ps(T) curves for the formation of BaS3 and ZrS3 and for Reaction (6),[186] but unfortunately complete thermodynamic data is lacking. The ps(T) curve for Reaction (5) is known,[187] and is shown in **Figure** 12. Apart from that, we have to rely on guesswork. If the decomposition of BaZrS3 by Reaction (6) is the true upper limit, then the fast-formation window will extend to somewhat higher ps values than the curve in Figure 12, due to the extra stability of the ternary phase over a mixture of binaries.[186] Meanwhile, we know from Wang et al. 

that BaS3 forms at a relatively lower ps than ZrS3. Thus, the 
 

![19_image_1.png](19_image_1.png)

fast-formation window extends to lower ps than the curve in Figure 12. The overall picture is that the fast-formation window for BaZrS3, while so far poorly defined, is distributed approximately around the ps(T) curve for ZrS3 formation, as illustrated by the yellow region in Figure 12. Within the picture described above, the role of the BaCl2 additive is not yet clear. One possibility is that it helped regulate ps by absorbing S vapor, keeping it low enough to avoid decomposition of BaZrS3.

[43] Another possibility is that it acts as a precursor for forming BaS3.

Although the picture is still incomplete, there are some important lessons for thin film growth of chalcogenide perovskites, or at least for BaZrS3. The first is that severe kinetic limitations may operate in simple formation processes. This could result in poor crystallization at lower growth temperatures, for example. However, under the right conditions, it has been shown that BaZrS3 can be formed at reasonable thin film growth temperatures (≈500–600 °C). A point of particular importance seems to be providing an appropriate partial pressure of S, in order to take advantage of a faster phase formation route via the low-melting point secondary phase BaS3.

## 5.2. Thin Film Growth

Before applying the above discussion to the case of thin film growth of chalcogenide perovskites, we briefly cover the general methodologies used for halide perovskite film growth, and why different methods must be used for chalcogenides. Halide perovskites are typically deposited by coating from a solution of metal halides (e.g., PbI2), organic cations (e.g., MA+), and various additives, followed by mild heating (<250 °C) during which the solvent evaporates while the perovskite film crystallizes. The solvent is chosen for good solubility of the precursor materials and a relatively low boiling point; dimethyl formamide and dimethyl sulfoxide are common examples.[7] Mild heating or addition of an antisolvent causes saturation and precipitation of the perovskite.[188] Both the cationic and anionic components of the halide perovskite can be provided in a single solution without the need for additional counterions. Solution growth of halide perovskites is normally made within a glove box, to avoid degradation of the perovskite product by contact with air or moisture.

To date, direct solution-based deposition has not been applied to chalcogenide perovskites. In principle it could be achieved using salts of the alkaline earth metals and group IV transition metals along with, e.g., thiourea, which would be coated and heat-treated. Since the metal salt precursors are in most cases air sensitive, it would again be necessary to use a glove box to achieve air- and moisture-free conditions (on the other hand, the final product is air stable). An alternative method, which circumvents the instability of the precursor material, is to deliberately deposit an oxide film that is later converted to a chalcogenide by thermal processing with a source of S(e).

For chalcogenides in general, it is much more common to grow thin films by physical vapor deposition (PVD) approaches, including thermal and e-beam evaporation, as well as sputtering. These methods can deposit highly pure and additive-free films. A spectrum of deposition procedures exists in which the elements are deposited simultaneously or sequentially, and the 

![19_image_0.png](19_image_0.png)

thermal energy needed to react them may be provided either during deposition, or subsequently in a separate heating step. The chalcogen element may be included in the deposition step, or may be added entirely during the heating process, or some combination of the two. Regardless of the growth sequence, the temperatures required for formation of highly crystalline materials are nearly always in the range of 450–600 °C.

For PVD processes, the material sources are normally the pure metal elements or their binary sulfides/selenides. Nearly always, these source materials must be handled in air, unless the PVD system is especially equipped for inert handling. This creates a problem for chalcogenide perovskites, because the pure elements Sr and Ba, as well as several of their sulfides/ selenides, are air sensitive. Moreover, some of the binary sulfides/selenides formed en route to making chalcogenide perovskites might be unstable in air. Therefore, measures must be taken to minimize air exposure of source materials and intermediates, as well as to allow safe handling, chamber cleaning, and so on. Nevertheless, assuming that appropriate measures can be taken for handling precursor materials, there are numerous methods by which chalcogenide perovskites could be grown by PVD, and once the ternary phase is formed, it is completely air stable.

The first reports of thin film synthesis of chalcogenide perovskites emerged in 2019 and 2020,[34,69,71,73,136] and the nonperovskite but chemically related LaYS3 compound in 2017.[34,35]
We highlight (but do not discuss) one report on preparation of thin films by solution deposition of colloidal BaZrS3 nanoparticles,[189] and two reports coming to press at the time of writing, concerning epitaxial growth of BaZrS3.

[190,191] Concerning the 
"traditional" thin films growth, in most cases high temperatures 
(>900 °C) were used to form the desired compounds. This is too high to be compatible with metal or transparent conductive oxides, which would form the back contact in a device. In some instances, the high temperatures were a necessary part of the synthesis process: following the majority of the solid state literature, and to circumvent the difficulty of handling alkali earth metals, several groups have deposited BaZrO3 films and then converted them to sulfides in a thermal process (i.e., Reaction (3)), using either CS2 or H2S. Wei et al. converted pulsedlaser deposited (PLD) BaZrO3 films on sapphire substrates by annealing in CS2 flux at 900–1050 °C for 2–4 h,[71] and Gupta et al. performed essentially the same process on solution-deposited BaZrO3 films on quartz.[73] Márquez et al. converted PLDgrown BaZrO3 into increasingly sulfur-rich films by heating in H2S from 700 to 1100 °C.[130] The use of oxide precursors carries the inherent problem noted by Clearfield, that complete conversion of an oxide precursor to a sulfide compound requires a combination of high temperatures and long times, e.g., >900 °C 
for several hours, due to the high stability of the oxides. Thus, routes in which oxide precursors are used, or in which any appreciable oxygen contamination is obtained, will invariably require high temperatures to generate the target compound. As noted by Crovetto et  al., this makes the process incompatible with normal conductive back contacts, whether metal or oxidebased.[34] Furthermore, it seems difficult to remove all oxygen: for Márquez et al., the S/(O+S) ratio saturated at 0.85 for a 30 min treatment in H2S at 1100 °C.[130] For Wei et al., a strong oxygen peak was recorded by energy dispersive X-ray spectroscopy 

 

![20_image_1.png](20_image_1.png)

(EDS), though not quantified, after a CS2 sulfurization at 1050 °C for 4 h, see **Figure** 13a.[71]
In terms of morphology, the grains of BaZrS3 achieved micrometer-scale diameters only above ≈1000 °C growth temperature, see Figure 13a,b. By contrast, other PV chalcogenides achieve grain sizes in this range for growth temperatures of 450–550 °C, and halide perovskites below 200 °C. This seems to reinforce the idea of slow diffusion within the ternary phase, since grain growth is a diffusion-limited process.

There are fewer examples in which nonoxide precursors were used, but two recent cases are instructive. Comparotto et al. produced slightly S-rich, amorphous BaZrS3 films by reactive sputtering, which were crystallized by rapid thermal processing in an inert atmosphere (i.e., without excess S) at temperatures from 650 to 1000 °C.[69] Yu et al. followed a similar procedure but used PLD to grow slightly S-deficient Ba–Zr–S 
precursor films, which were annealed in an atmosphere containing CS2, at 500–900 °C.[162] In both reports, the grain size of the films was limited to about 100  nm even for the higher annealing temperatures (see Figure 13c). Both studies also used FWHM of the (121) XRD reflection to judge crystallization, Figure 13c,d. The results were comparable, showing that crystallization improved continuously in the range of ≈600–900 °C. 

Again, these results imply slow diffusion kinetics.

In summary, the slow progress and disappointing optoelectronic results for thin film chalcogenide perovskites, compared to the exciting findings derived from powder materials, appear to be related to the wrong choice of growth conditions. The apparent need for high growth temperatures, the sluggish crystallization and incompatibility with conductive substrates stem from the same issue. Using oxide precursors carries the inherent difficulty of removing oxygen, while the attempts at direct crystallization from amorphous precursor films failed due to (presumably) slow diffusion kinetics. Based on Section  5.1, a more effective thin film synthesis method for BaZrS3 would be to go via a diffusion-enhancing intermediate phase of BaS3. 

The generation of this phase would not have occurred in any of the thin film cases mentioned above, due either to the absence of a sulfur-excess, and/or because Ba in the precursors was already bound into a matrix containing both S/O and Zr. To encourage BaS3 formation during the reaction process, precursors should be incompletely reacted, containing, e.g., metallic Ba, or stacked or incompletely sulfurized layers, e.g., BaS/Zr. A Ba-rich composition may also help provide the binary phase in excess. Apart from the BaS3-route, another widely used approach for assisting diffusion is to use additives that generate low-melting phases or otherwise influence grain growth. This is common practice for other chalcogenides including CIGS, CZTS, and CdTe, where sodium from the glass substrates, or added metal chlorides or fluorides, are nearly always important to enhance crystallization.[192,193] Again, this has not been tried for chalcogenide perovskites. If suitable growth conditions are 

![20_image_0.png](20_image_0.png)

 

![21_image_1.png](21_image_1.png)

employed, we have every expectation that the promising optoelectronic performance already demonstrated in powder-based chalcogenide perovskite materials can be recreated and even enhanced in thin film materials, finally unlocking the possibility to integrate the chalcogenide perovskites into devices.

## 6. Summary And Outlook

Chalcogenide perovskites are an emerging material group hoped to combine the most favorable application-relevant properties of both halide perovskites and chalcogenides. A particularly interesting application area is in tandem solar cells based on the Si platform. For this, halide perovskites show high performance, but poorer-long term stability (besides containing toxic elements). On the other hand, well-known chalcogenide alternatives, such as CdSe, CdTe, Cu(In,Ga)(S,Se)2, and Cu2ZnSn(S,Se)4—while generally very stable—exhibit large voltage losses with respect to the SQ limit, once their band gaps have been tuned into the necessary range for a tandem cell (ca 1.6–1.8  eV). Other emerging wide gap chalcogenides also lack indications of high photovoltaic potential, such as a strong luminescence quantum yield.

Chalcogenide perovskites appear to dispense with the disadvantages of both the above material groups. They contain primarily earth abundant and nontoxic elements, and they have been demonstrated to have exceptional environmental stability. 

They exhibit higher absorption coefficients than any mainstream chalcogenide or halide perovskite, and some of them have shown external luminescence efficiencies that would, in theory, allow a Voc corresponding to 90% of the SQ limit. These properties are encouraging in view of implementing chalcogenide perovskites as top cell in a tandem solar cell, but also for other energy conversation applications such as solid-state lighting.

The purpose of this review is to support a renewed push for development of chalcogenide perovskites. Our aim was to create clarity in the face of some early misconceptions and disappointing experimental outcomes that sit alongside various impressive claims, and to identify the critical hurdles that would need to be overcome for chalcogenide perovskites to emerge fully onto the PV stage. In this final section, we summarize some of the key results and needs, as related to each of the foregoing sections.

In terms of the discovered (or predicted) chalcogenide perovskites, we can confidently state that there are fewer in this family than has been imagined by many authors. Despite some contradicting claims, the assessed picture is that all the practically applicable II-IV-VI3-type ABX3 compounds are sulfides, and only BaZrS3 and BaHfS3 surely possess a ground state perovskite structure. Others, such as the Sr-equivalents, can be formed as high-temperature phases. Several III-III-VI3-type ABX3 perovskites have also been demonstrated, but these have not been explored beyond determining basic structural parameters yet. The relative lack of chalcogenide perovskites is a consequence of nonideal structural factors, especially the scarcity of sufficiently large B-site cations to fulfill the minimum requirement for the octahedral factor. Still, there is quite broad scope for bandgap and other properties to be tuned, via alloying on any of the lattice sites of BaZrS3, while the high temperature phases may still find their way into applications such as solidstate lighting. The above observations rationalize the relative lack of publications concerning chalcogenide perovskites other than BaZrS3, but also allow us now to focus our efforts on this more limited family of materials for which more information is already available. There are a few gaps and question marks in the existing literature regarding structural stability and/or characterization, which we identified here.

The existing literature—primarily from powder samplesproves good optoelectronic properties of chalcogenide perovskites. Powder materials have verified the exceptionally strong optical absorption, although there remains some surprising lack of agreement over the size and nature of the bandgap, at least in BaZrS3. Regarding PL emission, better results have been demonstrated for the high-T SrZrS3 and SrHfS3 phases than for BaZrS3 itself; still, there are few data points and it is not clear if this reflects an intrinsic difference, and the possible role of impurities and secondary phases is not yet elucidated. 

Certainly, the PL broadening of BaZrS3 is concerning, but needs to be evaluated in better-characterized materials grown in a more controllable matter; meanwhile sensitive measurements of the absorptivity will help to understand the possibly unusual band structure and the nature of any subgap states. At the same time, the reported high dielectric constant of BaZrS3 is technologically very promising (for high charge carrier lifetimes).

In terms of defect tolerance (a cornerstone of the success of halide perovskites), information is still limited for chalcogenide perovskites. Therefore, a well-balanced comparison of halide and chalcogenide perovskites in this respect is currently impossible. The two theoretical works (again, only for BaZrS3) do seem to suggest that BaZrS3 is defect-tolerant: it does not have low-energy defects with deep energy levels that would contribute to Shockley–Read–Hall recombination. This conclusion is supported by the available PL measurements. However, the information, while encouraging, is still fragmented. More work is still needed to make a direct and detailed comparison of the defect chemistries at this stage, including on the roles of other defect types, including ever-present impurities such as O and Hf. Clearly, there is scope for material processing to impact defect concentrations, and several chalcogenide perovskites have demonstrated the technologically useful feature of variable doping level and type. Reasonable charge carrier mobilities for emerging materials have been reported, especially promising considering that most optoelectronic and transport measurements have been made on relatively poor-quality materials from high temperature synthesis, which is expected to lead to degenerate doping and large off-stoichiometry. This suggests there is room for improvements in all characteristics thus far determined.

Thin film synthesis has been the major sticking point for chalcogenide perovskites so far. The suitable synthesis methods seem more akin to those for other chalcogenides than those for halide perovskites. In particular, solution processing—often viewed as a competitive advantage of halide perovskites—is likely not an option for chalcogenide perovskites. This is presumably due to the need for thermal activation of chemical rearrangements, which is in turn dictated by the higher strength of chemical bonds. Conversely, it is precisely these 

![21_image_0.png](21_image_0.png)

features which underlie the stability of the materials themselves. Certainly, solution processable materials are advantageous for fast progress in research and development, but the need for high-temperature processing may pay off by yielding better stability. As examples, CdTe and CIGS also require hightemperature processing, but are in turn devoid of the major stability issues inherent to halide perovskites. Meanwhile, the main bottlenecks for CdTe and CIGS technology are not related to their high-temperature processing, and their embodied energy is still substantially lower than for Si-based technology, due to their thin film nature.

Synthesis work for chalcogenide perovskite thin films (only BaZrS3 to date) has therefore focused on physical vapor deposition methods. A conception has emerged that chalcogenide perovskites require unusually high growth temperatures and are incompatible with conductive substrates; this would spell serious problems for PV integration. Our analysis of the literature suggests that this characterization is premature. Two bottlenecks become immediately obvious. The first is an apparent problem of low diffusivity that slows phase formation and grain growth of BaZrS3. The second relates to the difficulty of exchanging oxygen for sulfur when using oxide precursors, which has so far been the most common method employed. The solid-state synthesis literature provides valuable lessons for thin film growers. One is that oxide precursors should be avoided completely. Another is that a phase formation route going via BaS3 seems to have much faster kinetics, allowing lower temperature growth comparable to other chalcogenides. This approach should be easy to emulate in thin film growth, but so far has not been reported. These lessons, combined with the application of additives for enhancing crystallization, which is already normal for other chalcogenides, show that there is potential for considerable improvements in materials quality from thin film methods, over and above that already demonstrated by bulk samples. Such improvements are expected to automatically lead to progress in understanding the optoelectronic properties of the emerging chalcogenide perovskites, and facilitate progress toward device integration.

## Acknowledgements

The authors gratefully acknowledge the Göran Gustafsson Foundation (Grant No. 1927), the Swedish Research Council (2017-04336), the Swedish Foundation for Strategic Research (SSF, contract RMA15-0030), and the strategic research area STandUP for Energy for funding this research.

## Conflict Of Interest

The authors declare no conflict of interest.

## Keywords

chalcogenide perovskites, earth-abundant materials, energy materials, optoelectronics, photovoltaics Received: August 16, 2021 Revised: October 11, 2021 Published online: December 13, 2021

 

![22_image_1.png](22_image_1.png)

[1] R. Brenes, D. Guo, A. Osherov, N. K. Noel, C. Eames, E. M. Hutter, S. K.  Pathak, F.  Niroui, R. H.  Friend, M. S.  Islam, H. J.  Snaith, V. Bulović, T. J. Savenije, S. D. Stranks, *Joule* **2017**, 1, 155.

[2] J. J.  Yoo, G.  Seo, M. R.  Chua, T. G.  Park, Y.  Lu, F.  Rotermund, Y.-K.  Kim, C. S.  Moon, N. J.  Jeon, J.-P.  Correa-Baena, V.  Bulović, S. S. Shin, M. G. Bawendi, J. Seo, *Nature* **2021**, 590, 587.

[3] E. H. Jung, N. J. Jeon, E. Y. Park, C. S. Moon, T. J. Shin, T.-Y. Yang, J. H. Noh, J. Seo, *Nature* **2019**, 567, 511.

[4] M. A.  Green, E. D.  Dunlop, J.  Hohl-Ebinger, M.  Yoshita, N. Kopidakis, X. Hao, *Prog. Photovoltaics* **2020**, 28, 629.

[5] L. A. Zafoschnig, S. Nold, J. C. Goldschmidt, *IEEE J. Photovoltaics* 2020, 10, 1632.

[6] Oxford PV hopes to deliver perovskite-silicon tandem solar cells within a year | Perovskite-Info, https://www.perovskite-info.com/
oxford-pv-hopes-deliver-perovskite-silicon-tandem-solar-cellswithin-year (accessed: November 2020).

[7] A.  Dubey, N.  Adhikari, S.  Mabrouk, F.  Wu, K.  Chen, S.  Yang, Q. Qiao, *J. Mater. Chem. A* **2018**, 6, 2406.

[8] H. Xie, M. Lira-Cantu, *J. Phys. Energy* **2020**, 2, 024008. [9] Q.  Wang, N.  Phung, D. D.  Girolamo, P.  Vivo, A.  Abate, Energy Environ. Sci. **2019**, 12, 865.

[10] B.  Chen, J.  Song, X.  Dai, Y.  Liu, P. N.  Rudd, X.  Hong, J.  Huang, Adv. Mater. **2019**, 31, 1902413.

[11] N. Phung, A. Abate, *Small* **2018**, 14, 1802573.

[12] M.  Fischer, M.  Woodhouse, S.  Herritsch, J.  Trube, International Technology Roadmap for Photovoltaic (ITRPV), VDMA E. V. Photovoltaic Equipment, Frankfurt, Germany **2020**.

[13] A. R.  Jeong, S. B.  Choi, W. M.  Kim, J.-K.  Park, J.  Choi, I.  Kim, J. Jeong, *Sci. Rep.* **2017**, 7, 15723.

[14] A. Hajijafarassar, F. Martinho, F. Stulen, S. Grini, S. López-Mariño, M.  Espíndola-Rodríguez, M.  Döbeli, S.  Canulescu, E.  Stamate, M.  Gansukh, S.  Engberg, A.  Crovetto, L.  Vines, J.  Schou, O. Hansen, *Sol. Energy Mater. Sol. Cells* **2020**, 207, 110334.

[15] T. P. White, N. N. Lal, K. R. Catchpole, *IEEE J. Photovoltaics* **2014**, 
4, 208.

[16] H.  Hiroi, Y.  Iwata, S.  Adachi, H.  Sugimoto, A.  Yamada, *IEEE J.* 
Photovoltaics **2016**, 6, 760.

[17] L. H.  Wong, A.  Zakutayev, J. D.  Major, X.  Hao, A.  Walsh, T. K. Todorov, E. Saucedo, *J. Phys. Energy* **2019**, 1, 032001.

[18] S.  Gharibzadeh, B. A.  Nejand, M.  Jakoby, T.  Abzieher, D.  Hauschild, S.  Moghadamzadeh, J. A.  Schwenzer, P.  Brenner, R.  Schmager, A. A.  Haghighirad, L.  Weinhardt, U.  Lemmer, B. S.  Richards, I. A.  Howard, U. W.  Paetzold, *Adv. Energy Mater.* 2019, 9, 1803699.

[19] J. Keller, K. V. Sopiha, O. Stolt, L. Stolt, C. Persson, J. J. S. Scragg, T. Törndahl, M. Edoff, *Prog. Photovoltaics* **2020**, 28, 237.

[20] M.  Stolterfoht, P.  Caprioglio, C. M.  Wolff, J. A.  Márquez, J.  Nordmann, S.  Zhang, D.  Rothhardt, U.  Hörmann, Y.  Amir, A.  Redinger, L.  Kegelmann, F.  Zu, S.  Albrecht, N.  Koch, T.  Kirchartz, M.  Saliba, T.  Unold, D.  Neher, *Energy Environ. Sci.* 2019, 12, 2778.

[21] A.  Swarnkar, W. J.  Mir, R.  Chakraborty, M.  Jagadeeswararao, T. Sheikh, A. Nag, *Chem. Mater.* **2019**, 31, 565.

[22] J. A.  Brehm, J. W.  Bennett, M. R.  Schoenberg, I.  Grinberg, A. M. Rappe, *J. Chem. Phys.* **2014**, 140, 224703.

[23] R. Lelieveld, D. J. W. IJdo, *Acta Crystallogr., B* **1980**, 36, 2223.

[24] Y.  Nishigaki, T.  Nagai, M.  Nishiwaki, T.  Aizawa, M.  Kozawa, K.  Hanzawa, Y.  Kato, H.  Sai, H.  Hiramatsu, H.  Hosono, H. Fujiwara, *Sol. RRL* **2020**, 4, 1900555.

[25] K. Hanzawa, S. Innura, H. Hiramatsu, H. Hosono, *J. Am. Chem.* 
Soc. **2019**, 141, 5343.

[26] N. Rodier, R. Julien, V. Tien, *Acta Crystallogr., Sect. C: Struct. Chem.*
1983, 39, 670.

[27] K.  Mitchell, R. C.  Somers, F. Q.  Huang, J. A.  Ibers, *J. Solid State* Chem. **2004**, 177, 709.

![22_image_0.png](22_image_0.png)

## ![23_Image_1.Png](23_Image_1.Png)

[28] V. Tien, D. Carre, P. Khodadad, *C. R. Seances Acad. Sci., Ser. C* **1970**, 
271, 1571.

[29] G. B.  Jin, E. S.  Choi, R. P.  Guertin, J. S.  Brooks, T. H.  Bray, C. H. Booth, T. E. Albrecht-Schmitt, *Chem. Mater.* **2007**, 19, 567.

[30] T. Ohtani, S. Honji, M. Takano, *J. Solid State Chem.* **1997**, 132, 188.

[31] B.-H.  Chen, G.  Sàghi-Szabó, B.  Eichhorn, J.-L.  Peng, R.  Greene, Mater. Res. Bull. **1992**, 27, 1249.

[32] B.  Okai, K.  Takahashi, M.  Saeki, J.  Yoshimoto, *Mater. Res. Bull.*
1988, 23, 1575.

[33] S. Yamaoka, B. Okai, *Mater. Res. Bull.* **1970**, 5, 789.

[34] A.  Crovetto, R.  Nielsen, M.  Pandey, L.  Watts, J. G.  Labram, M.  Geisler, N.  Stenger, K. W.  Jacobsen, O.  Hansen, B.  Seger, I. Chorkendorff, P. C. K. Vesborg, *Chem. Mater.* **2019**, 31, 3359.

[35] K.  Kuhar, A.  Crovetto, M.  Pandey, K. S.  Thygesen, B.  Seger, P. C. K.  Vesborg, O.  Hansen, I.  Chorkendorff, K. W.  Jacobsen, Energy Environ. Sci. **2017**, 10, 2579.

[36] R. A. Gardner, M. Vlasse, A. Wold, *Inorg. Chem.* **1969**, 8, 2784.

[37] N. Rodier, P. Laruelle, J. Flahaut, *C. R. Seances Acad. Sci.* **1969**, 269, 1391.

[38] P. C. Donohue, J. F. Weiher, *J. Solid State Chem.* **1974**, 10, 142. [39] L. A. Aslanov, *Zh. Neorg. Khim.* **1964**, 9, 2022.

[40] G. B.  Jin, E. S.  Choi, R. P.  Guertin, J. S.  Brooks, C. H.  Booth, T. E. Albrecht-Schmitt, *Inorg. Chem.* **2007**, 46, 9213.

[41] H. Hahn, U. Mutschke, *Z. Anorg. Allg. Chem.* **1957**, 288, 269.

[42] A. Clearfield, *Acta Crystallogr.* **1963**, 16, 135.

[43] Y. Wang, N. Sato, K. Yamada, T. Fujino, *Shigen to Sozai* **2000**, 116, 703.

[44] S. Niu, G.  Joe, H. Zhao, Y. Zhou, T.  Orvis, H. Huyan, J. Salman, K. Mahalingam, B. Urwin, J. Wu, Y. Liu, T. E. Tiwald, S. B. Cronin, B. M.  Howe, M.  Mecklenburg, R.  Haiges, D. J.  Singh, H.  Wang, M. A. Kats, J. Ravichandran, *Nat. Photonics* **2018**, 12, 392.

[45] J. Huster, *Z. Naturforsch., B* **1980**, 35, 775. [46] M. Saeki, M. Onoda, *J. Solid State Chem.* **1994**, 112, 65.

[47] D. Carre, P. Laruelle, *Acta Crystallogr., B* **1974**, 30, 952.

[48] R. Lelieveld, D. J. W. Ijdo, *Acta Crystallogr., B* **1978**, 34, 3348. [49] W. Sterzel, J. Horn, *Z. Anorg. Allg. Chem* **1970**, 376, 254.

[50] G. A. Wiegers, A. Meetsma, R. J. Haange, J. L. de Boer, *Acta Crystallogr., C* **1989**, 45, 847.

[51] J. C. Jumas, M. Ribes, É. Philippot, M. Maurin, *C. R. Seances Acad.* 
Sci. **1972**, 275, 269.

[52] W. H. Paar, R. Miletich, D. Topa, A. J. Criddle, M. K. D. Brodtkorb, G. Amthauer, G. Tippelt, *Am. Mineral.* **2000**, 85, 1066.

[53] M.  Ghedira, J.  Chenavas, F.  Sayetat, M.  Marezio, O.  Massenet, J. Mercier, *Acta Crystallogr., B* **1981**, 37, 1491.

[54] S.  Fagot, P.  Foury-Leylekian, S.  Ravy, J. P.  Pouget, M.  Anne, G. Popov, M. V. Lobanov, M. Greenblatt, *Solid State Sci.* **2005**, 7, 718.

[55] T.  Inami, K.  Ohwada, H.  Kimura, M.  Watanabe, Y.  Noda, H. Nakamura, T. Yamasaki, M. Shiga, N. Ikeda, Y. Murakami, Phys. Rev. B **2002**, 66, 073108.

[56] M. Ghedira, M. Anne, J. Chenavas, M. Marezio, F. Sayetat, J. Phys. 

C: Solid State Phys. **1986**, 19, 6489.

[57] F. Sayetat, M. Ghedira, J. Chenavas, M. Marezio, J. Phys. C: Solid State Phys. **1982**, 15, 1627.

[58] R. A. Gardner, M. Vlasse, A. Wold, *Acta Crystallogr., B* **1969**, 25, 781. [59] Y. Wang, N. Sato, K. Yamada, T. Fujino, *Shigen to Sozai* **2000**, 116, 211.

[60] X.  Shen, D.  Cheng, H.-F.  Zhao, Y.  Yao, X.-Y.  Liu, R.-C.  Yu, Chin. 

Phys. B **2013**, 22, 116102.

[61] Y. Ohno, *Phys. Rev. B* **1991**, 44, 1281.

[62] Y. Ohno, *Solid State Commun.* **1991**, 79, 1081.

[63] S.  van  Smaalen, A.  Meetsma, G. A.  Wiegers, J. L.  de  Boer, *Acta* Crystallogr., B **1991**, 47, 314.

[64] C. Sourisseau, R. Cavagnat, J. L. Tirado, *J. Raman Spectrosc.* **1992**, 
23, 647.

![23_image_0.png](23_image_0.png)

[65] J.  Kelber, A. H.  Reis, A. T.  Aldred, M. H.  Mueller, O.  Massenet, G. DePasquali, G. Stucky, *J. Solid State Chem.* **1979**, 30, 357.

[66] M. Onoda, K. Kato, Y. Gotoh, Y. Oosawa, *Acta Crystallogr., B* **1990**, 
46, 487.

[67] S. Yamaoka, *J. Am. Ceram. Soc.* **1972**, 55, 111.

[68] S.  Perera, H.  Hui, C.  Zhao, H.  Xue, F.  Sun, C.  Deng, N.  Gross, C. Milleville, X. Xu, D. F. Watson, B. Weinstein, Y.-Y. Sun, S. Zhang, H. Zeng, *Nano Energy* **2016**, 22, 129.

[69] C.  Comparotto, A.  Davydova, T.  Ericson, L.  Riekehr, M. V.  Moro, T. Kubart, J. Scragg, *ACS Appl. Energy Mater.* **2020**, 3, 2762.

[70] S. Niu, H. Huyan, Y. Liu, M. Yeung, K. Ye, L. Blankemeier, T. Orvis, D.  Sarkar, D. J.  Singh, R.  Kapadia, J.  Ravichandran, *Adv. Mater.* 2017, 29, 1604733.

[71] X. Wei, H. Hui, C. Zhao, C. Deng, M. Han, Z. Yu, A. Sheng, P. Roy, A. Chen, J. Lin, D. F. Watson, Y.-Y. Sun, T. Thomay, S. Yang, Q. Jia, S. Zhang, H. Zeng, *Nano Energy* **2020**, 68, 104317.

[72] X. Wei, H. Hui, S. Perera, A. Sheng, D. F. Watson, Y.-Y. Sun, Q. Jia, S. Zhang, H. Zeng, *ACS Omega* **2020**, 5, 19.

[73] T.  Gupta, D.  Ghoshal, A.  Yoshimura, S.  Basu, P. K.  Chow, A. S. Lakhnot, J. Pandey, J. M. Warrender, H. Efstathiadis, A. Soni, E.  Osei-Agyemang, G.  Balasubramanian, S.  Zhang, S.-F.  Shi, T.-M.  Lu, V.  Meunier, N.  Koratkar, *Adv. Funct. Mater.* **2020**, 30, 2001387.

[74] L. J. Tranchitella, B. H. Chen, J. C. Fettinger, B. W. Eichhorn, J. Solid State Chem. **1997**, 130, 20.

[75] L. J.  Tranchitella, J. C.  Fettinger, P. K.  Dorhout, P. M.  Van Calcar, B. W. Eichhorn, *J. Am. Chem. Soc.* **1998**, 120, 7639.

[76] H.  Shaili, M.  Beraich, A.  El hat, M.  Ouafi, E.  mehdi Salmani, R.  Essajai, W.  Battal, M.  Rouchdi, M.  Taibi, N.  Hassanain, A. Mzerd, *J. Alloys Compd.* **2021**, 851, 156790.

[77] D. Mootz, H. Puhl, *Acta Crystallogr.* **1967**, 23, 471.

[78] D. J. W. IJdo, *Acta Crystallogr., B* **1980**, 36, 2403. [79] K.-J. Range, A. Gietl, U. Klement, *Z. Kristallogr. - Cryst. Mater.* **1993**, 
207, 147.

[80] A. Meetsma, G. A. Wiegers, J. L. de Boer, *Acta Crystallogr., C* **1993**, 
49, 2060.

[81] N. Rodier, *Bull. Mineral.* **1973**, 96, 350.

[82] N. A.  Moroz, C.  Bauer, L.  Williams, A.  Olvera, J.  Casamento, A. A.  Page, T. P.  Bailey, A.  Weiland, S. S.  Stoyko, E.  Kioupakis, C. Uher, J. A. Aitken, P. F. P. Poudeu, *Inorg. Chem.* **2018**, 57, 7402.

[83] O.  Gourdon, V.  Petricek, M.  Evain, *Acta Crystallogr., B* **2000**, 56, 409.

[84] O.  Gourdon, E.  Jeanneau, M.  Evain, S.  Jobic, R.  Brec, H.-J.  Koo, M.-H. Whangbo, *J. Solid State Chem.* **2001**, 162, 103.

[85] M. Saeki, M. Onoda, *J. Solid State Chem.* **1993**, 102, 100.

[86] M.  Onoda, M.  Saeki, A.  Yamamoto, K.  Kato, *Acta Crystallogr., B*
1993, 49, 929.

[87] J. Cuya, N. Sato, K. Yamamoto, H. Takahashi, A. Muramatsu, *Thermochim. Acta* **2004**, 419, 215.

[88] Z.  Wang, Y.  Han, P.  Liu, Y.  Li, S.  Xu, J.  Xiang, R. N.  Ali, F.  Su, H. Zeng, J. Jiang, B. Xiang, *Appl. Surf. Sci.* **2020**, 499, 143932.

[89] J.  Heo, L.  Yu, E.  Altschul, B. E.  Waters, J. F.  Wager, A.  Zunger, D. A. Keszler, *Chem. Mater.* **2017**, 29, 2594.

[90] D.  Cheng, H.  Jin, B.  Li, X.  Wang, Q.  Chu, Y.  Lu, X.  Liu, X.  Zhao, Chem. Res. Chin. Univ. **2012**, 28, 171.

[91] S. A. Sunshine, J. A. Ibers, *Acta Crystallogr., C* **1987**, 43, 1019.

[92] C. S. Lee, K. M. Kleinke, H. Kleinke, *Solid State Sci.* **2005**, 7, 1049.

[93] S.-P.  Guo, Y.  Chi, J.-P.  Zou, H.-G.  Xue, *New J. Chem.* **2016**, 40, 10219.

[94] A. Mar, J. A. Ibers, *Acta Crystallogr., C* **1992**, 48, 771.

[95] G. B.  Jin, E. S.  Choi, T. E.  Albrecht-Schmitt, *J. Solid State Chem.*
2009, 182, 1075.

[96] H. Noel, *C. R. Seances Acad. Sci.* **1973**, 277, 463.

[97] M. D. Ward, J. A. Ibers, *Acta Crystallogr., E* **2014**, 70, i4.

[98] A. Daoudi, H. Noel, *Inorg. Chim. Acta* **1987**, 140, 93.

## ![24_Image_1.Png](24_Image_1.Png)

[99] N. Rodier, P. Laruelle, *C. R. Seances Acad. Sci.* **1970**, 270, 2127.

[100] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S.  Cholia, D.  Gunter, D.  Skinner, G.  Ceder, K. A.  Persson, APL Mater. **2013**, 1, 011002.

[101] G. A. Wiegers, A. Meerschaut, *J. Alloys Compd.* **1992**, 178, 351.

[102] S.  Kikkawa, Y.  Fujii, Y.  Miyamoto, A.  Meerschaut, A.  Lafond, J. Rouxel, *Mater. Res. Bull.* **1999**, 34, 279.

[103] T. Murugesan, S. Ramesh, J. Gopalakrishnan, C. N. R. Rao, *J. Solid* State Chem. **1981**, 38, 165.

[104] N.  Cho, S.  Kikkawa, F.  Kanamaru, Y.  Takeda, O.  Yamamoto, H. Kido, T. Hoshikawa, *Solid State Ionics* **1993**, *63–65*, 696.

[105] T. Takahashi, S. Osaka, O. Yamada, *J. Phys. Chem. Solids* **1973**, 34, 1131.

[106] A. A. Narducci, J. A. Ibers, *Chem. Mater.* **1998**, 10, 2811.

[107] H. Noel, *C. R. Seances Acad. Sci.* **1974**, 279, 513.

[108] J.  Prakash, M. S.  Tarasenko, A.  Mesbah, S.  Lebègue, C. D. Malliakas, J. A. Ibers, *Inorg. Chem.* **2016**, 55, 7734.

[109] A. Daoudi, H. Noel, *J. Less-Common Met.* **1989**, 153, 293.

[110] H. Noel, *Rev. Chim. Miner.* **1977**, 14, 295.

[111] N. A. Moroz, *Ph.D. Thesis*, University of Michigan, **2017**.

[112] V. M. Goldschmidt, *Naturwissenschaften* **1926**, 14, 477.

[113] M. R. Filip, F. Giustino, *Proc. Natl. Acad. Sci. USA* **2018**, 115, 5397.

[114] C. J. Bartel, C. Sutton, B. R. Goldsmith, R. Ouyang, C. B. Musgrave, L. M. Ghiringhelli, M. Scheffler, *Sci. Adv.* **2019**, 5, 0693.

[115] G.  Pilania, A.  Ghosh, S. T.  Hartman, R.  Mishra, C. R.  Stanek, B. P. Uberuaga, *npj Comput. Mater.* **2020**, 6, 71.

[116] A. S. Bhalla, R. Guo, R. Roy, *Mater. Res. Innovations* **2000**, 4, 3.

[117] R. D. Shannon, Acta Crystallogr., Sect. A: Cryst. Phys., Diffr., Theor. 

Gen. Crystallogr. **1976**, 32, 751.

[118] S.  Körbel, M. A. L.  Marques, S.  Botti, *J. Mater. Chem. C* **2016**, 4, 3157.

[119] Y.-Y. Sun, M. L. Agiorgousis, P. Zhang, S. Zhang, *Nano Lett.* **2015**, 
15, 581.

[120] Z. Huo, S.-H. Wei, W.-J. Yin, *J. Phys. D: Appl. Phys.* **2018**, 51, 474003.

[121] S. A. Filippone, Y.-Y. Sun, R. Jaramillo, *MRS Adv.* **2018**, 3, 3249.

[122] C. J. Bartel, A. W. Weimer, S. Lany, C. B. Musgrave, A. M. Holder, npj Comput. Mater. **2019**, 5, 4.

[123] S.  Kirklin, J. E.  Saal, B.  Meredig, A.  Thompson, J. W.  Doak, M. Aykol, S. Rühl, C. Wolverton, *npj Comput. Mater.* **2015**, 1, 15010.

[124] H.  Zhang, C.  Ming, K.  Yang, H.  Zeng, S.  Zhang, Y.-Y.  Sun, Chin. 

Phys. Lett. **2020**, 37, 097201.

[125] W. Meng, B. Saparov, F. Hong, J. Wang, D. B. Mitzi, Y. Yan, Chem. 

Mater. **2016**, 28, 821.

[126] M. Ong, D. M. Guzman, Q. Campbell, I. Dabo, R. A. Jishi, *J. Appl.* 
Phys. **2019**, 125, 235702.

[127] M.-G. Ju, J. Dai, L. Ma, X. C. Zeng, *Adv. Energy Mater.* **2017**, 7, 1700216.

[128] H. I. Eya, E. Ntsoenzok, N. Y. Dzade, *Materials* **2020**, 13, 978. [129] Y.-Y.  Zhang, S.  Chen, P.  Xu, H.  Xiang, X.-G.  Gong, A.  Walsh, S.-H. Wei, *Chin. Phys. Lett.* **2018**, 35, 036104.

[130] J. A.  Márquez, M.  Rusu, H.  Hempel, I. Y.  Ahmet, M.  Kölbach, I. Simsek, L. Choubrac, G. Gurieva, R. Gunder, S. Schorr, T. Unold, J. Phys. Chem. Lett. **2021**, 12, 2148.

[131] N. Vonrüti, U. Aschauer, *J. Mater. Chem. A* **2019**, 7, 15741.

[132] R. H.  Nielsen, G.  Wilfing, *Ullmann's Encyclopedia of Industrial* Chemistry, American Cancer Society, Washington, DC **2010**.

[133] J.  Werner, B.  Niesen, C.  Ballif, *Adv. Mater. Interfaces* **2018**, 5, 1700731.

[134] S. Niu, D. Sarkar, K. Williams, Y. Zhou, Y. Li, E. Bianco, H. Huyan, S. B. Cronin, M. E. McConney, R. Haiges, R. Jaramillo, D. J. Singh, W. A. Tisdale, R. Kapadia, J. Ravichandran, *Chem. Mater.* **2018**, 30, 4882.

[135] Y.  Cen, J.  Shi, M.  Zhang, M.  Wu, J.  Du, W.  Guo, S.  Liu, S.  Han, Y. Zhu, *Chem. Mater.* **2020**, 32, 2450.

[136] D.  Mitzi, Y.  Yan, *High Performance Perovskite-Based Solar Cells*, 
Duke University, Durham, NC **2020**.

[137] W.  Li, S.  Niu, B.  Zhao, R.  Haiges, Z.  Zhang, J.  Ravichandran, A. Janotti, *Phys. Rev. Mater.* **2019**, 3, 101601.

[138] D. R. Lide, *CRC Handbook of Chemistry and Physics*, 84th ed., CRC 
Press, Boca Raton, FL **2004**.

[139] S. Pors Nielsen, *Bone* **2004**, 35, 583.

[140] H. A. Schroeder, J. J. Balassa, *J. Chronic Dis.* **1966**, 19, 573.

[141] S.  Niu, J.  Milam-Guerrero, Y.  Zhou, K.  Ye, B.  Zhao, B. C.  Melot, J. Ravichandran, *J. Mater. Res.* **2018**, 33, 4135.

[142] Y. Wang, N. Sato, T. Fujino, *J. Alloys Compd.* **2001**, 327, 104.

[143] G. Y. Kim, A. Senocrate, T.-Y. Yang, G. Gregori, M. Grätzel, J. Maier, Nat. Mater. **2018**, 17, 445.

[144] H.  Zeng, Green, Stable and Earth Abundant Ionic PV Absorbers Based on Chalcogenide Perovskite, State University of New York (SUNY), Buffalo, NY **2018**.

[145] R. T. Ross, *J. Chem. Phys.* **1967**, 46, 4590. [146] M.  Krause, A.  Nikolaeva, M.  Maiberg, P.  Jackson, D.  Hariskos, W.  Witte, J. A.  Márquez, S.  Levcenko, T.  Unold, R.  Scheer, D. Abou-Ras, *Nat. Commun.* **2020**, 11, 4189.

[147] Z. Liu, L. Krückemeier, B. Krogmeier, B. Klingebiel, J. A. Márquez, S. Levcenko, S. Öz, S. Mathur, U. Rau, T. Unold, T. Kirchartz, *ACS* Energy Lett. **2019**, 4, 110.

[148] A.  Cabas-Vidani, S. G.  Haass, C.  Andres, R.  Caballero, R.  Figi, C.  Schreiner, J. A.  Márquez, C.  Hages, T.  Unold, D.  Bleiner, A. N. Tiwari, Y. E. Romanyuk, *Adv. Energy Mater.* **2018**, 8, 1801191.

[149] P.  Becker, J. A.  Márquez, J.  Just, A.  Al-Ashouri, C.  Hages, H. Hempel, M. Jošt, S. Albrecht, R. Frahm, T. Unold, Adv. Energy Mater. **2019**, 9, 1900555.

[150] S. Rühle, *Sol. Energy* **2016**, 130, 139.

[151] X. Chen, H. Lu, Y. Yang, M. C. Beard, *J. Phys. Chem. Lett.* **2018**, 9, 2595.

[152] N. Gross, Y.-Y. Sun, S. Perera, H. Hui, X. Wei, S. Zhang, H. Zeng, B. A. Weinstein, *Phys. Rev. Appl.* **2017**, 8, 044014.

[153] M.  Oumertem, D.  Maouche, S.  Berri, N.  Bouarissa, D. P.  Rai, R. Khenata, M. Ibrir, *J. Comput. Electron.* **2019**, 18, 415.

[154] Y. Peng, Q. Sun, H. Chen, W.-J. Yin, *J. Phys. Chem. Lett.* **2019**, 10, 4566.

[155] J.  Jean, T. S.  Mahony, D.  Bozyigit, M.  Sponseller, J.  Holovský, M. G. Bawendi, V. Bulović, *ACS Energy Lett.* **2017**, 2, 2616.

[156] J. Mattheis, U. Rau, J. H. Werner, *J. Appl. Phys.* **2007**, 101, 113519.

[157] J. K.  Katahara, H. W.  Hillhouse, *2016 IEEE 43rd Photovoltaic Specialists Conf. (PVSC)*, IEEE, Piscataway, NJ **2016**, pp. 3563–3566.

[158] W.  Li, S.  Niu, B.  Zhao, R.  Haiges, Z.  Zhang, J.  Ravichandran, A. Janotti, *Phys. Rev. Mater.* **2019**, 3, 101601.

[159] *ZrS2 Energy Gap: Datasheet from "PAULING FILE Multinaries Edition - 2012" in Springer Materials (Online Database)*, (Ed: P. Villars), 
Springer, Heidelberg **2012**.

[160] *ZrS3 Energy Gap: Datasheet from "PAULING FILE Multinaries Edition - 2012" in SpringerMaterials (Online Database)*, (Ed: P. Villars), 
Springer, Heidelberg **2012**.

[161] G. Giorgi, J.-I. Fujisawa, H. Segawa, K. Yamashita, *J. Phys. Chem.* 
Lett. **2013**, 4, 4213.

[162] Z.  Yu, X.  Wei, Y.  Zheng, H.  Hui, M.  Bian, S.  Dhole, J.-H.  Seo, Y.-Y. Sun, Q. Jia, S. Zhang, S. Yang, H. Zeng, *Nano Energy* **2021**, 85, 105959.

[163] M. Grossberg, J. Krustok, C. J. Hages, D. M. Bishop, O. Gunawan, R. Scheer, S. M. Lyam, H. Hempel, S. Levcenco, T. Unold, *J. Phys.* Energy **2019**, 1, 044002.

[164] L. M. Herz, *ACS Energy Lett.* **2017**, 2, 1539.

[165] R. Jaramillo, J. Ravichandran, *APL Mater.* **2019**, 7, 100902. [166] S. Filippone, B. Zhao, S. Niu, N. Z. Koocher, D. Silevitch, I. Fina, J. M.  Rondinelli, J.  Ravichandran, R.  Jaramillo, *Phys. Rev. Mater.* 2020, 4, 091601.

[167] W. van Roosbroeck, W. Shockley, *Phys. Rev.* **1954**, 94, 1558.

[168] T.  Kirchartz, J. A.  Márquez, M.  Stolterfoht, T.  Unold, Adv. Energy Mater. **2020**, 10, 1904134.

![24_image_0.png](24_image_0.png)

## 

[169] T. P.  Weiss, R.  Carron, M. H.  Wolter, J.  Löckinger, E.  Avancini, S. Siebentritt, S. Buecheler, A. N. Tiwari, *Sci. Technol. Adv. Mater.* 2019, 20, 313.

[170] T. Trupke, M. A. Green, P. Würfel, P. P. Altermatt, A. Wang, J. Zhao, R. Corkish, *J. Appl. Phys.* **2003**, 94, 4930.

[171] A. Nijamudheen, A. V. Akimov, *J. Phys. Chem. Lett.* **2018**, 9, 248.

[172] S. Kim, A. Walsh, arXiv:2003.05394 [cond-mat], 2020.

[173] W.  Chu, Q.  Zheng, O. V.  Prezhdo, J.  Zhao, W. A.  Saidi, arXiv:2004.12559 [cond-mat.mtrl-sci], 2020.

[174] J. S. Park, S. Kim, Z. Xie, A. Walsh, *Nat. Rev. Mater.* **2018**, 3, 194.

[175] R. Guo, S. Wang, *J. Phys. Chem. C* **2019**, 123, 29. [176] S.  Chen, A.  Walsh, X.-G.  Gong, S.-H.  Wei, *Adv. Mater.* **2013**, 25, 1522.

[177] X.  Wu, W.  Gao, J.  Chai, C.  Ming, M.  Chen, H.  Zeng, P.  Zhang, S. Zhang, Y.-Y. Sun, *Sci. China Mater.* **2021**, 64, 2976.

[178] J. Yan, M. Greenblatt, A. Sahiner, D. Sills, M. Croft, *J. Alloys Compd.*
1995, 229, 216.

[179] A. J. Jackson, D. Tiana, A. Walsh, *Chem. Sci.* **2016**, 7, 1082.

[180] B.-H.  Chen, W.  Wong-Ng, B. W.  Eichhorn, *J. Solid State Chem.*
1993, 103, 75.

[181] M. Ishii, M. Saeki, M. Sekita, *Mater. Res. Bull.* **1993**, 28, 493.

[182] N.  Sato, Y. R.  Wang, K.  Yamada, T.  Fujino, Synthesis of Transiton Metal Mixed Sulfides MTS3 (M = Ba, Pb, T = *Ti, Zr) Using Sulfur* Melt, Minerals, Metals & Materials Society, Warrendale, PA **2000**.

[183] Y. Wang, N. Sato, K. Yamada, T. Fujino, *J. Alloys Compd.* **2000**, 311, 214.

[184] S.  Niu, B.  Zhao, K.  Ye, E.  Bianco, J.  Zhou, M. E.  McConney, C. Settens, R. Haiges, R. Jaramillo, J. Ravichandran, *J. Mater. Res.* 2019, 34, 3819.

[185] B.  Predel, O.  Madelung, Ba-S (Barium-Sulfur): Datasheet from Landolt-Börnstein - Group IV Physical Chemistry · Volume 5B: 
"B-Ba–C-Zr" in SpringerMaterials (Online Database), SpringerVerlag, Berlin **2021**.

[186] J. J. Scragg, P. J. Dale, D. Colombara, L. M. Peter, *ChemPhysChem* 2012, 13, 3035.

[187] H. Haraldsen, A. Kjekshus, E. Røst, A. Steffensen, J. Munch-Petersen, Acta Chem. Scand. **1963**, 17, 1283.

[188] J. S.  Manser, M. I.  Saidaminov, J. A.  Christians, O. M.  Bakr, P. V. Kamat, *Acc. Chem. Res.* **2016**, 49, 330.

[189] V. K.  Ravi, S. H.  Yu, P. K.  Rajput, C.  Nayak, D.  Bhattacharyya, D. S. Chung, A. Nag, *Nanoscale* **2020**, 13, 1616.

[190] I.  Sadeghi, K.  Ye, M.  Xu, J. M.  LeBeau, R.  Jaramillo, Adv. Funct. 

Mater. **2021**, 31, 2105563.

[191] M.  Surendran, H.  Chen, B.  Zhao, A. S.  Thind, S.  Singh, T.  Orvis, H.  Zhao, J.-K.  Han, H.  Htoon, M.  Kawasaki, R.  Mishra, J. Ravichandran, *Chem. Mater.* **2021**, 33, 7457.

[192] K.  Granath, M.  Bodegård, L.  Stolt, *Sol. Energy Mater. Sol. Cells* 2000, 60, 279.

[193] A. H. Munshi, J. M. Kephart, A. Abbas, A. Danielson, G. Gē⁄linas, J.-N. Beaudry, K. L. Barth, J. M. Walls, W. S. Sampath, *Sol. Energy* Mater. Sol. Cells **2018**, 186, 259.

![25_image_0.png](25_image_0.png)

Kostiantyn V. Sopiha obtained his Ph.D. in Engineering from the Singapore University of 

![25_image_1.png](25_image_1.png) Technology and Design in 2018, after which he joined the Solar Cell Technology Division within the Department of Materials Science and Engineering at Uppsala University as a postdoc and later as a researcher. His research is focused on the first-principles modeling of chalcogenide solar absorbers, which is usually carried out in close collaboration with experimentalists. His primary research interests encompass the fundamentals of materials for solar energy harvesting and storage, photocatalysis, gas sensing, and novel 2D compounds.

Corrado Comparotto received his master's degree in electronic engineering from the University of Brescia, Italy. From 2011 to 2018 he worked for the International Solar energy Centre Konstanz, Germany, within the Department of Future Solar Cell Concepts, with focus on n-type and bifacial Si solar cells. In 2019 he joined the Department of Materials Science and Engineering at Uppsala University, Sweden, where he is currently working toward his Ph.D. degree on chalcogenide perovskites for Si-based tandem solar cells.

 

![26_image_1.png](26_image_1.png)

José A. Márquez is currently working as a postdoc researcher in the Structure and Dynamics of Energy Materials group at the Helmholtz-Zentrum Berlin (HZB). He graduated in Chemistry at the University of Sevilla and completed his Ph.D. in Physics and Electrical Engineering at Northumbria University as part of a Marie Curie Programme. His Ph.D. included research stays at HZB and at EMPA in the Laboratory for Thin Films and Photovoltaics developing earth-abundant semiconductors for photovoltaics. His current research focuses on the development of novel compound semiconductors and high-throughput and in situ characterization methods for energy materials.

Jonathan J. S. Scragg received his Ph.D. in Physical Chemistry from the University of Bath, UK, in 2010. He later joined the division of Solar Cell Technology at Uppsala University, where he is currently an associate professor in the topic thin film solar cells. His research encompasses development of robust solar absorbers for sustainable photovoltaics, using scalable synthesis techniques. The scientific focus is on the chemistry of thin-film material formation. Materials of interest are primarily chalcogenides, including kesterites and, more recently, wider gap absorbers suitable for tandem cells.

![26_image_0.png](26_image_0.png)

