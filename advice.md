#c++
##learnt while implementing Alevin and shadowing Rob's code
1. Cmake src and lib separately
2. functional approach: following is one snippet
  * (Build + quant)
    * PE / SE 
      * 64/32
        * Quasi / SMEM
          *multithread
3. Validate at every step, specially multi-threa opration.
like in multithread environment Do everything in one variable and then
save everything to a const variable before further processing.
