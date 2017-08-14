# project-euler  

## Freq_Commands
Frequently used Command and library Syntax
#bash
Bash maintains an internal hash of previously found executables in your path. In this case, it has details that at one time there was an executable at /usr/bin/siege, and reuses that path to avoid having to search again.
You can also clear all hashed locations:  
```
hash -r
```

##gnu parallel
convert multiple sam to bam with sorting in parallel
```
parallel -j 16 "samtools view -bS {} | samtools sort - -o {\}.bam" ::: `ls *.sam`
```

##awk
remove things from one file present in another 
`https://stackoverflow.com/a/18477228/6871844`
```
awk '{if (f==1) { r[$0] } else if (! ($0 in r)) { print $0 } } ' f=1 exclude-these.txt f=2 from-this.txt
```
get 5 line after every pattern line
```
awk '/PATTERN/ {for(i=1; i<=5; i++) {getline; print}}' inputfile
```

Can be used in fastq to print every 2nd read
```
awk ' NR%8 == 1 {for(i=1; i<=4; i++) {print;getline} }'
```

compare two columns from different file and get set difference
```
awk 'NR==FNR{c[$1]++;next};c[$1] == 0' geReads.txt txReads.txt| wc -l
```

## python
dictionary argmax
```
max(stats, key=stats.get)
```
combination of 2
```
itertools.combinations(a,2)
```

## FASTA
```
from pyfasta import Fasta
if __name__ == "__main__":
    f = Fasta('file.fasta')
    for contig in fasta:
```
##ipython Notebook:
```
ssh -N -f -L localhost:7777:localhost:7777 avi@feynman
ps aux | grep ssh
kill -9 <pid>
ps aux
ipython notebook --no-browser --port=7777

import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
%matplotlib inline
```

##flux-simulator
```
./flux-simulator -t simulator -x -l -s -p ../../hg19.par
./rsem-prepare-reference --gtf ../data/bigdata/hg19/knownRef_sorted.gtf ../data/bigdata/hg19/chromFa/ ../data/bigdata/hg19/reference
```

##clear cache
```
sync && sudo purge
free && sync && sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches' && free;
```

##extract txp->gene relation from GTF
```
bioawk -c gff '$feature=="transcript" {print $group}' gencode.v26.primary_assembly.annotation.gtf | awk -F ' ' '{print substr($4,2,length($4)-3) ","  substr($2,2,length($2)-3)}' - > txp2gene.tsv
 ```
