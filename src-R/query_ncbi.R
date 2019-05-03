% query ncbi for read length
read_lens <- c()

for (i in srrs$V1) { 
    sql <- paste0("SELECT DISTINCT bases,spots FROM sra WHERE run_accession IN ('", toString(i), "')", collapse = "");
    x <- dbGetQuery(sra_con,  sql);
    read_len <- x$bases/x$spots
    
    read_lens <- c(read_lens, floor(read_len/2))
}
