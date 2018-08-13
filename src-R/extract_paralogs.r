library(biomaRt)
genes <- read.table("/mnt/scratch5/avi/alevin/data/human/gtf/genes.txt", header=FALSE)["V1"]
names <- as.vector(genes$V1)
names[1]
human = useMart("ensembl", dataset = "hsapiens_gene_ensembl")
logs <- getBM(attributes=c("ensembl_gene_id", "hsapiens_paralog_ensembl_gene"), mart = human, values=names, filter="ensembl_gene_id")
logs
dim(logs)
write.table(logs, file = "/mnt/scratch5/avi/alevin/data/human/gtf/paralogs.txt", quote = FALSE,
            col.names = FALSE, row.names = FALSE, sep = "\t")
