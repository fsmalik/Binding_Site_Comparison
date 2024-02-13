# Binding_Site_Comparison
Contains scripts for comparing residues at the binding site in MSA. 
Malik, F., &amp; Li, Z. (2022). Non-peptide agonists and positive allosteric modulators of glucagon-like peptide-1 receptors: Alternative approaches for treatment of Type 2 diabetes. British Journal of Pharmacology, 179(4), 511–525.

1. python_sequence_reader_final.py needs to be executed with the python or python3 command
```
-i --input
-o --output
-h --help
```

2. ```./merger``` to execute the merger script
Merger will compile all alignment files (.fst or .fasta) into one file for the input in the python program.
Merger must be in the same directory as all alignment files.
Merger is originally formatted to compile only '.fasta' files in said directory -> in order to compile '.fst' files open merger with any text editor and change .fasta to .fst in line 3.

3. The ```BS_alignments``` directory contains a set of example alignment files in .fasta format and 'allBS_aligned' is the compiled file you would get if you ran the merger script in this directory.
The output file is the example output you would get if you ran python seq reader on allBS_merged.

4. The ```conservation_scripts_seqnum_adjustments``` directory contains the code adjustments required when there are more than 3 sequences aligned in a single MSA.
It is recommended to just use alignments of 3 sequences at a time since there are no instructions on how to implement this code.

5. The python_sequence_reader_final.py can accept two formats (nonsimultaneously... )
These formats can seen below -> ```.fst``` format and ```.fasta``` format
The ```python_sequence_reader_final.py``` script can only accept one argument for input and one argument for output (see usage help ```-h``` for more)

6. Squiggles i.e. '~' or gaps in the sequence are considered non-identical residues in this script.
This is a simple script, and it does not account for checking adjacent residues for conservation. maybe in the future, but not currently.
For now, you will have to check this by hand - sorry.

ACCEPTABLE FORMATS (Maestro - Multiple Sequence Viewer Export):

'.fasta' format ***THIS EXAMPLE HAS 3 COMPILED ALIGNMENTS***
```
3ODU_A, TVGLVVMKLRSMTDRDRAASRKQKKATLCPILYAL
UNIPROT, TVGLVVMKLRSMTDRDRAASRKQKKATLCPILYAL
NP_005499.1, FLGVVVLKLRSMTDLDRAASRKKKKAMVCPIIYFL

3PBL_A, ALQTTTNYRYTQSCVREKAMNIEFK
UNIPROT, ALQTTTNYRYTQSCVREKAMNIEFK
NP_000786.1, ALQTTTNYRYTYSKVKEKAMNIEFK

3RZE_A, KLTGNIDRRSVQPRRIREKAAQYNENF
UNIPROT, KLTGNIDRRSVQPRRIREKAAQYNENF
NP_001354640.1, RLNTNIDRCAVDPRVILKQVWGEEEPQ
```

2. '.fst' format ***AGAIN, THIS EXAMPLE HAS 3 COMPILED ALIGNMENTS***
```
>3PBL_A
ALQTTTNYRPYTQSCVYIYLRRKRTPLQPRPLREKKATQMAIFNIEF

>UNIPROT
ALQTTTNYRPYTQSCVYIYLRRKRTPLQPRPLREKKATQMAIFNIEF

>UNIPROT
ALQTTTNYRPYTYSKVYIYLRRKRTPAKPEQQKEKKATQMAIFNIEF


>3RZE_A
KLTVGNIDRSVPYLIHREKAAQNENF

>UNIPROT
KLTVGNIDRSVPYLIHREKAAQNENF

>P25021
RLNLTNIDRAVPYPI~REKATTNRDF


>3V2Y_A
KFHRPMYYFNFSLAIERYITMLKMHNSNRLLIACIIYLVRTRSRRLTFRKNIASSSKSLLLERAR

>UNIPROT
KFHRPMYYFNFSLAIERYITMLKMHNSNRLLIACIIYLVRTRSRRLTFRKNIASSSKSLLLERAR

>Q99500
KFHNRMYFFNCSLAIERHLTMIKMYDNRRVLIMCIIYLVKSSSRKVANHNN~~~~SRSMLLERAR

```
