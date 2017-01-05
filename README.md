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
parallel -j 16 "samtools view -bS {} | samtools sort -" ::: `ls *.sam`
```

##awk
get 5 line after every pattern line
```
awk '/PATTERN/ {for(i=1; i<=5; i++) {getline; print}}' inputfile
```

Can be used in fastq to print every 2nd read
```
awk ' NR%8 == 1 {for(i=1; i<=4; i++) {print;getline} }'
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

##STAR
```
./bin/Linux_x86_64/STAR --runThreadN 20 --runMode genomeGenerate --genomeDir ./index/ --genomeFastaFiles ../data/bigdata/hg19/reference.transcripts.fa --limitGenomeGenerateRAM 57993269973 --genomeChrBinNbits 12
/usr/bin/time ./src/rapmap pseudomap -i ./pseudoindex/ -1 ../../data/25M/1.fastq -2 ../../data/25M/2.fastq -t 20 -o pseudoout.sam
```

##build bowtie index:  313M
```
./bowtie2-build ./data/ref.fa ./index/
```

##bowtie align:
```
./bowtie2 -k 200 -x ./index/ -1 ./data/one.fq -2 ./data/two.fq -S ./out/out --no-mixed -p 20
```

##Build ilwa index: 3.6G
```
./src/ilwa index -t ../data/bigdata/hg19/reference.transcripts.fa -i ./index/
```

##ilwa align
```
../ilwa align -i ../index/ -1 ../data/one.fq -2 ../data/two.fq -o ./out/
```

##rapmap index       3.1G
```
./src/rapmap index -t ../data/bigdata/hg19/reference.transcripts.fa -i ./index/ -k 20
```

##rapmap SA index    3.2G
```
./src/rapmap saindex -t ../data/bigdata/hg19/reference.transcripts.fa -i ./saindex/
```
