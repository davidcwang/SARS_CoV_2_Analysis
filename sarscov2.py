#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Bio.Seq import Seq
from Bio import SeqIO


# In[5]:


sc1g = SeqIO.read('data/sars_cov_1_genome.fasta', 'fasta')
sc2g = SeqIO.read('data/sars_cov_2_genome.fasta', 'fasta')

print('Length of Sars-Cov-1 Genome: {}'.format(len(sc1g)))
print('Length of Sars-Cov-2 Genome: {}'.format(len(sc1g)))


# In[238]:


import os
from Bio import pairwise2
from Bio import SeqIO
from Bio.Align import substitution_matrices

def similarity_score(ref, seq):
    similar = 0

    for i in range(len(ref)):
        if ref[i] == seq[i]:
            similar += 1

    return similar / len(ref)

def seqsim(alignfile):
    blosum62 = substitution_matrices.load("BLOSUM62")

    # basedir = '/Users/davidwang/projects/sarscov2/data'
    # seq1 = SeqIO.read('{}/sars_cov_2_e_prot.fasta'.format(basedir), 'fasta')
    # seq2 = SeqIO.read('{}/mers_cov_e_prot.fasta'.format(basedir), 'fasta')
    # aligns = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5)

    # Read in Sequences Aligned by MAFFT
    aligndata = open(alignfile).read()
    seqs = aligndata.split('>')
    seq1 = ''.join(seqs[1].split('\n')[1:])
    seq2 = ''.join(seqs[2].split('\n')[1:])

    return {
        'seq1': seq1,
        'seq2': seq2,
        'similarity': similarity_score(seq1, seq2),
    }


# In[239]:


proteins = ['e', 'm', 'n', 's']

basedir = '/Users/davidwang/projects/sarscov2/data'
for p in proteins:
    alignfile = '{}/sars_cov_2_mers_cov_{}_prot.ali'.format(basedir, p)
    result = seqsim(alignfile)

    basename = os.path.basename(alignfile)
    print('{} Protein Length: {}'.format(basename, len(result['seq1'])))
    print('{} Protein Length: {}'.format(basename, len(result['seq2'])))
    print('{} Protein Sequence Similarity: {:.1f}%'.format(basename, result['similarity']*100))

for p in proteins:
    alignfile = '{}/sars_cov_2_sars_cov_1_{}_prot.ali'.format(basedir, p)
    result = seqsim(alignfile)

    basename = os.path.basename(alignfile)
    print('{} Protein Length: {}'.format(basename, len(result['seq1'])))
    print('{} Protein Length: {}'.format(basename, len(result['seq2'])))
    print('{} Protein Sequence Similarity: {:.1f}%'.format(basename, result['similarity']*100))


# In[233]:


def cdna_to_rna(dna):
    return str(dna).replace('T', 'U')



# In[131]:


#rna = cdna_to_rna(cnuc.seq)
#
#
## In[1]:
#
#
#seq_ids = [
# 'YP_005352862.1',
# 'AMN91620.1',
# 'YP_002308478.1',
# 'P0C6Y5.1',
# 'APD51497.1',
# 'AVA26872.1',
# 'AKJ21970.1',
# 'YP_001718610.1',
# 'AHB63507.1',
# 'AAS00078.1',
# 'ACV87277.1',
# 'YP_009555238.1',
# 'YP_209229.2',
# 'ARB07596.1',
# 'ATG84853.1',
# 'ABN10847.1',
# 'AAP33696.1',
# 'AVP25405.1',
#]
#
#
## In[2]:
#
#
#from Bio import Entrez
#from Bio import SeqIO
#Entrez.email = 'something@something.com'
#
#seqs = {}
#for s_id in seq_ids:
#    handle = Entrez.efetch(db='protein', id=s_id, rettype='gb', retmode='text')
#    seq = SeqIO.read(handle, 'genbank')
#    seqs[s_id] = seq
#
#
## In[4]:
#
#
#
#
#
## In[155]:
#
#
#SeqIO.write(seqs, 'all.faa', 'fasta')
#
#
## In[181]:
#
#
#with open('clustalo.clustal_num') as f:
#    data = f.readlines()
#
#
## In[186]:
#
#
#"""
#Got the following error when using consurf:
#
#"The uploaded MSA file, which appears to be in clustalw format, contains non-standard characters: "J".
#To fix the format please replace all non-standard characters with standard characters
#(gaps : "-" Amino Acids : "A" , "C" , "D" .. "Y") and resubmit your query."
#
#This is because we have a 'J' amino acid in on line 998 in our clustalo.clustal_num multi alignment file
#
#'ATG84853.1          GTPNEKLVTTSTAPDFVAFNVFQGIETAVGHYVHARLKGGJILKFDSGTVSKTSDWKCKV	1788'
#
#Apparently a 'J' is supposed to indicate either 'I' or 'L'.
#We will replace with an 'L' in this case because ABN10847.1 and AVP25405.1 have 'L's in that position
#which is the majority.
#"""
#
## Replace ambiguous amino acids with the majority e.g. J -> L because J can be either I or L.
## def replace_ambiguous_aa(rows):
##     for i, r in enumerate(rows):
##         cols = r.split()
##         align = cols[1] if len(cols) > 2 else ''
##         if 'J' in align:
##             row = cols[1].replace('J', 'L')
#
## replace_ambiguous_aa(data)
## open('clustalo_unique_aa.clustal_num', 'w').write(''.join(data))
#
#
## In[37]:
#
#
#'''
#Get Accession IDs for Sars-Cov-2 Genomes https://www.pnas.org/content/117/17/9241?cct=2302
#Paper: Phylogenetic network analysis of SARS-CoV-2 genomes
#'''
#
#import csv
#
#ids = []
#with open('forster_data/2b Cluster assignments-Table 1.csv') as file:
#    reader = csv.reader(file)
#
#    for i, row in enumerate(reader):
#        if i > 3:
#            ids.append(row[3])
#
#print(ids)
#
#
## In[29]:
#
#
#seqs = SeqIO.[('gisaid/msa_0727/msa_0727.fasta', 'fasta')

