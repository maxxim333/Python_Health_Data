#Exercise 1.1. Consider the nucleotide chain:
#CATAGCGACAAGCTCGTAGGACATGAGACCACTTGAGCTTCACGCGCCATCCCCAGTGTAAGTCCCCTTACCCCGC
#1. Indicate the position (index) of the ?TTGAGC? substring.
chain= "CATAGCGACAAGCTCGTAGGACATGAGACCACTTGAGCTTCACGCGCCATCCCCAGTGTAAGTCCCCTTACCCCGC"
chain.find('TTGAGC')
#2. Indicate the position (index) of the ?ATG? substring.
a.find('ATG')

#3. Indicate the position (index) of the ?TAA? substring.
a.index('TAA')
#4. Indicate the number of nucleotides that are between ?ATG? and ?TAA? (both not
#inclusive).
import re

m = re.search(r'ATG[ACTG]{,}TAA',chain)
if m:
     c=m.group()
     print(len(c)-6)
 

#Note: consider that the first position or index in the string is 0.
#The nucleotide chain can be found in:
#https://gist.github.com/anonymous/a0b1d331ccaba7a413c9b85ecb307b4a
#Exercise 1.2. Consider the nucleotide chain of the previous exercise. Indicate the frequency of
#occurrence (in %) of nucleotides A, C, G and T.




def freq1(dna):
         """
         Frequencies in DNA.
         """
         freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
         for nucl in dna:
             freq[nucl] += 1
         for nucl in freq:
             freq[nucl] *= 100.0/len(dna)
         return freq
chain = "CATAGCGACAAGCTCGTAGGACATGAGACCACTTGAGCTTCACGCGCCATCCCCAGTGTAAGTCCCCTTACCCCGC"
freq1(chain)
