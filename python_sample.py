import medford_parser

code = """
@MEDFORD Connelly 2020
@MEDFORD-Version 1.0
#Annotation by Megan Gelement 08/17/21
#Updated to 1.0 by Polina Shpilker 06/14/22

@Paper_Primary Lipopolysaccharide treatment 
stimulates Pocillopora coral 
genotype-specific immune responses but does not alter coral-associated bacteria communities
@Paper_Primary-Link https://doi.org/10.1016/j.dci.2020.103717

@Journal Developmental & Comparative Immunology 
@Journal-Volume 109
@Journal-Issue August 2020

@Date 2020-01-09
@Date-Note Received

@Date 2020-04-17
@Date-Note Revised

@Date 2020-04-17
@Date-Note Accepted

@Date 2020-04-26
@Date-Note Published Online

@Contributor M. Connelly
@Contributor-Association Department of Marine Biology and Ecology, Rosenstiel School of Marine and Atmospheric Science, University of Miami, Miami, FL, 33145, USA
@Contributor-Role First Author

# Can contributors have multiple association tags?
@Contributor C. McRae
@Contributor-Association Department of Biological Sciences, Simon Fraser University, Burnaby, British Columbia, V5A 1S6, Canada
@Contributor-Association Department of Natural Resources and Environmental Studies, National Dong Hwa University, Hualien, 974, Taiwan
@Contributor-Role Author

@Contributor P. Liu
@Contributor-Association Graduate Institute of Marine Biology, National Dong Hwa University, Pingtung, 944, Taiwan
@Contributor-Association National Museum of Marine Biology and Aquarium, Pintung, 944, Taiwan  
@Contributor-Role Author

@Contributor N. Traylor-Knowles
@Contributor-Association Department of Marine Biology and Ecology, Rosenstiel School of Marine and Atmospheric Science, University of Miami, Miami, FL, 33145, USA
@Contributor-Role Last Author

'@Contributor R. Tan
'@Contributor-Note Field Assistance and Site Environmental Data Collection

@Contributor A. Mayfield
@Contributor-Note Laboratory space

@Contributor S. Rosales
@Contributor-Note Bioinformatics Assistance

@Contributor R. Cunning
@Contributor-Note Bioinformatics Assistance

@Funding National Science Foundation East Asia and Pacific Summer Institute Program
@Funding-ID 1713962 

@Keyword Coral
@Keyword Innate immunity
@Keyword Bacteria
@Keyword Microbiome
@Keyword Lipopolysaccharide

# Can species have multiple tags of the same type, e.g. two reefs?
@Species Pocillopora damicornis
@Species-Reef Houwan
@Species-ReefCollection [..]
@Species-Reef Wanglitung
@Species-ReefCollection [..]
@Species-Cultured National Museum of Marine Biology and Aquarium (NMMBA)
@Species-CultureCollection [..]
@Species-Loc Kenting National Park, Taiwan

@Species Pocillopora acuta
@Species-Reef Houwan
@Species-ReefCollection [..]
@Species-Reef Wanglitung 
@Species-ReefCollection [..]
@Species-Cultured National Museum of Marine Biology and Aquarium (NMMBA)
@Species-CultureCollection [..]
@Species-Loc Kenting National Park, Taiwan


# Do coral lab conditions get reported as a method? (section 2.1)

@Method Qiagen RNEasy Kit
@Method-Type RNA isolation

@Method NanoDrop 2000 spectrophotometer (ThermoFisher)
@Method-Type RNA concentration and purity quantification 

@Method Illumina TruSeq RNA Library Prep Kit v2
@Method-Type cDNA creation

@Method Qubit dsDNA BR kit (ThermoFisher Q32853)
@Method-Type cDNA quantification

@Method Illumina HiSeq 2000
@Method-Type 50-bp single-end DNA sequencing
@Method-Note performed at the University of Utah's Huntsman Cancer Center

@Method Qiagen DNeasy PowerSoil kit
@Method-Type Total DNA extraction

@Method Earth Microbiome Project protocols
@Method-Type PCR amplification

@Method Qubit dsDNA BR kit
@Method-Type PCR amplicon concentration quantification

# Is there an @Method-Loc option? e.g. for methods performed by outside collaborators or at specific locations 
@Method Illumina MiSeq
@Method-Type 300-bp paired-end sequencing
@Method-Note performed at the University of Miami Center for Genome Technology 

@Code_Ref FASTQC
@Code_Ref-Type base pair quality analysis

@Code_Ref Trimmomatic
@Code_Ref-Type Quality trimming
@Code_Ref-Version 0.36

@Code_Ref STAR
@Code_Ref-Type trimmed read alignment
@Code_Ref-Version 2.5.3a
@Code_Ref-Note two-pass mode

@Code_Ref Subread
@Code_Ref-Type aligned transcript quantification
@Code_Ref-Note featureCounts command

@Code_Ref topGO
@Code_Ref-Type Gene ontology (GO) enrichment and annotation
@Code_Ref-Note using "weight01" algorithm

# Is there a better way to identify multiple plugins or packages from the same source, used for different tasks?
@Code_Ref QIIME2 pipeline
@Code_Ref-Type RNA 16S read processing, trimming; rRNA sequence taxonomic classification
@Code_Ref-Version 2020.2
@Code_Ref-Note plugin DADA2 (RNA read processing & trimming)
@Code_Ref-Note plugin q2-feature-classifier (rRNA taxonomic classification)

# Put R in 2x; specify version in each package
@Code_Ref R
@Code_Ref-Type statistical analysis
@Code_Ref-Version R v3.6.3
@Code_Ref-Note used ggplot2

@Code_Ref R
@Code_Ref-Type statistical analysis
@Code_Ref-Version R v3.5.2 

@Code_Ref DESeq2
@Code_Ref-Type R package
@Code_Ref-Note design "~ Batch + Genotype + Treatment"; "~ Batch + Treatment" for genotype-specific analysis 
@Code_Ref-Note R v3.5.2

@Code_Ref phyloseq
@Code_Ref-Type R package
@Code_Ref-Note R v3.6.3

@Code_Ref vegan
@Code_Ref-Type R package
@Code_Ref-Note R v3.6.3

@Code_Ref R package ALDeX2
@Code_Ref-Type R package
@Code_Ref-Note R v3.6.3

@Data_Ref NCBI Sequence Read Archive accession PRJNA587509
@Data_Ref-Type SRA accession
@Data_Ref-Accession PRJNA587509
@Data_Ref-URI https://www.ncbi.nlm.nih.gov/bioproject/PRJNA587509/
@Data_Ref-Filename raw_reads/

@Data_Ref EAPSI_Pocillopora_LPS
@Data_Ref-Note Scripts and data for RNASeq and 16S analysis
@Data_Ref-Type github repository
@Data_Ref-URI https://github.com/michaeltconnelly/EAPSI_Pocillopora_LPS
@Data_Ref-Filename scripts/

# If this were our own paper, these would be @Data_Copy and we would provide the file
#   alongside the MEDFORD file. We shouldn't be hard linking to the journal resources online.
@Data_Ref DESeq2 results: LPS vs. Control Volcano Plot and PCA Plot
@Data_Ref-Type JPG
@Data_Ref-URI https://ars.els-cdn.com/content/image/1-s2.0-S0145305X20300094-gr1_lrg.jpg
@Data_Ref-Filename 1-s2.0-S0145305X20300094-gr1_lrg.jpg
@Data_Ref-Size 234 KB

@Data_Ref Consensus effects of LPS on gene expression
@Data_Ref-Type JPG
@Data_Ref-URI https://ars.els-cdn.com/content/image/1-s2.0-S0145305X20300094-gr2_lrg.jpg
@Data_Ref-Filename 1-s2.0-S0145305X20300094-gr2_lrg.jpg
@Data_Ref-Size 260 KB

# I'm not sure how to handle in-paper tables. Technically, this shouldn't be a problem
#   if we wrote the paper ourselves and were writing a MEDFORD file for it, because then
#   we will be able to just make the table a csv or smth
#@Data_Ref Significantly enriched GO terms for sets of differentially expressed genes
#@Data_Ref-Type Table 
#@Data_Ref-URI None
#@Data_Ref-Note "Table 1"; see paper

@Data_Ref Bacteria Phyla Relative Abundance
@Data_Ref-Type JPG
@Data_Ref-URI https://ars.els-cdn.com/content/image/1-s2.0-S0145305X20300094-gr3_lrg.jpg
@Data_Ref-Filename 1-s2.0-S0145305X20300094-gr3_lrg.jpg
@Data_Ref-Size 432 KB

@Data_Ref Coral collection sites in Kenting National Park
@Data_Ref-Type PDF 
@Data_Ref-URI https://ars.els-cdn.com/content/image/1-s2.0-S0145305X20300094-mmc1.pdf
@Data_Ref-Filename 1-s2.0-S0145305X20300094-mmc1.pdf
@Data_Ref-Size 81 MB

@Data_Ref cDNA Library Sequencing read depth results
@Data_Ref-Type Excel
@Data_Ref-URI https://ars.els-cdn.com/content/image/1-s2.0-S0145305X20300094-mmc2.xlsx
@Data_Ref-Filename 1-s2.0-S0145305X20300094-mmc2.xlsx

@Data_Ref Identified upregulated DEG with Function Information
@Data_Ref-Type Excel
@Data_Ref-URI https://ars.els-cdn.com/content/image/1-s2.0-S0145305X20300094-mmc3.xlsx
@Data_Ref-Filename 1-s2.0-S0145305X20300094-mmc3.xlsx

@Data_Ref Indentified upregulated DEG with Gentype Specifitiy Information
@Data_Ref-Type Excel
@Data_Ref-URI https://ars.els-cdn.com/content/image/1-s2.0-S0145305X20300094-mmc4.xlsx
#@Data_Ref-Filename 1-s2.0-S0145305X20300094-mmc4.xlsx
"""

def printASTNodeInfo(rootNode):
    for child in rootNode.children:
        print(f' - Child node type: ${child.type=}\n')
        if len(child.children) > 0:
            printASTNodeInfo(child)
        else:
            if (child.text):
                print(f'    - Text content:{child.text=}\n')
                
tree = medford_parser.parse_code(code)
print(tree.root_node.sexp())
printASTNodeInfo(tree.root_node)
