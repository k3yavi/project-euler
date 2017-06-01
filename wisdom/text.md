# c++ 
## learnt while implementing Alevin and shadowing Rob's code
1. Cmake src and lib separately
2. functional approach: following is one snippet
  * (Build + quant)
  * PE / SE
  * 64/32
  * Quasi / SMEM *multithread
3. Validate at every step, specially multi-thread opration. like in multithread environment Do everything in one variable and then save everything to a const variable before further processing.

# frequently used data-structure in our lab (No particular order):
1. Equivalence Class
2. Suffix Array
3. Rand and select
4. de-bruijn graph (colored and compact)
5. Bloom filter (Normal and Quotient)
6. Graphical Models (This is lil more generic)

# Things Rob do different than me:
1. Project Ideas are very well formulated with the tineast detail possible with every corner case.
2. Think like Bayesian !!!!
3. He think on multiple projects parallely while I can concentrate on only one at a time. (idk which is better though). [UPDATE] Working on multiple projects helps connect the insights from one another.
4. Think about the tineast detail why it could have happen. Imagination is the key!!!
5. Be cautious of pre-mature conclusion, this biases your analysis, towards the already set conclusion (can be wrong). 