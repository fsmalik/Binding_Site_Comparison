# Binding_Site_Comparison
Contains scripts for comparing residues at the binding site in MSA. 
Malik F, Li Z. Is there a common allosteric binding site for G-protein coupled receptors? J Comput Aided Mol Des. 2022 Jun;36(6):405-413. doi: 10.1007/s10822-022-00454-5.

## Compatibility for Release 2022-2

Maestro changed the format which fasta files are exported in. Use ```process_sequences.sh``` to convert it back:

To use this script: ```./process_sequences.sh inputseq.fst outputseq.fst```

This will convert this format:
```
>NAME:6X1A.R|CHAIN:R
AT-SLWE-VQK-RE-E-LL-Y-Y-R-V-K-ALKW-ST-Q-LL-YQ-C-VF-MQ-VA-Y-W
-K-EDEGCWTRNS-W-IR-I-I-E-FA-M-RGTLRF-LF-EL-T-
>NAME:sp|P43220|GLP1R_HUMAN Glucagon-like peptide 1 receptor OS=Homo sapiens OX=9606 GN=GLP1R PE=1 SV=2|CHAIN:
AT-SLWE-VQK-RE-E-LL-Y-Y-R-V-K-ALKW-ST-Q-LL-YQ-C-VF-MQ-VA-Y-W
-K-EDEGCWTRNS-W-IR-I-I-E-FA-M-RGTLRF-LF-EL-T-
>NAME:sp|P43220|GLP1R_HUMAN Glucagon-like peptide 1 receptor OS=Homo sapiens OX=9606 GN=GLP1R PE=1 SV=2|CHAIN:
AT-SLWE-VQK-RE-E-LL-Y-Y-R-V-K-ALKW-ST-Q-LL-YQ-C-VF-MQ-VA-Y-W
-K-EDEGCWTRNS-W-IR-I-I-E-FA-M-RGTLRF-LF-EL-T-
```

To this format:

```
>NAME:6X1A.R|CHAIN:R
ATSLWEVQKREELLYYRVKALKWSTQLLYQCVFMQVAYWKEDEGCWTRNSWIRIIEFAMRGTLRFLFELT

>NAME:sp|P43220|GLP1R_HUMAN Glucagon-like peptide 1 receptor OS=Homo sapiens OX=9606 GN=GLP1R PE=1 SV=2|CHAIN:
ATSLWEVQKREELLYYRVKALKWSTQLLYQCVFMQVAYWKEDEGCWTRNSWIRIIEFAMRGTLRFLFELT

>NAME:sp|P43220|GLP1R_HUMAN Glucagon-like peptide 1 receptor OS=Homo sapiens OX=9606 GN=GLP1R PE=1 SV=2|CHAIN:
ATSLWEVQKREELLYYRVKALKWSTQLLYQCVFMQVAYWKEDEGCWTRNSWIRIIEFAMRGTLRFLFELT


```
## Running The Scripts (Maestro Release 2019)
1. python_sequence_reader_final.py needs to be executed with the python or python3 command
```
-i --input
-o --output
-h --help
```

2. ```./merger``` to execute the merger script
3. Merger will compile all alignment files (.fst or .fasta) into one file for the input in the python program.
4. Merger must be in the same directory as all alignment files.
5. Merger is originally formatted to compile only '.fasta' files in said directory -> in order to compile '.fst' files open merger with any text editor and change .fasta to .fst in line 3.

6. The ```BS_alignments``` directory contains a set of example alignment files in .fasta format and 'allBS_aligned' is the compiled file you would get if you ran the merger script in this directory.

7. The output file is the example output you would get if you ran ```python_seq_reader.py``` on ```allBS_merged```.

8. The ```conservation_scripts_seqnum_adjustments``` directory contains the code adjustments required when there are more than 3 sequences aligned in a single MSA.
It is recommended to just use alignments of 3 sequences at a time since there are no instructions on how to implement this code.

9. The python_sequence_reader_final.py can accept two formats (nonsimultaneously... )
These formats can seen below -> ```.fst``` format and ```.fasta``` format
The ```python_sequence_reader_final.py``` script can only accept one argument for input and one argument for output (see usage help ```-h``` for more)

10. Squiggles i.e. '~' or gaps in the sequence are considered non-identical residues in this script.
This is a simple script, and it does not account for checking adjacent residues for conservation.
(Alternatively, you can check this by hand.)

ACCEPTABLE FORMATS (Maestro - Multiple Sequence Viewer Export):

1. '.fasta' format ***THIS EXAMPLE HAS 3 COMPILED ALIGNMENTS***
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

11. To run the Comparison: ```python3 python_seq_reader.py -i allBS_merged -o NIRs.tsv```; ```NIRs.tsv``` will contain the results with number of non-identical residues.
