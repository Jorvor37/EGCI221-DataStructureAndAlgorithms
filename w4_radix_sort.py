"""

radix_sort
    -> bucket_sort

sort each digit seperetly, by using any stable sort
1. sort right most digit align to each array index
2. relocate them on the array A left-right, top-bottom
3. repeat to the next digit

#notes that for floating point number do from left most digit.

If want to sort floting number like 3.14, 14.52 how do we sort by bucket sort: change to sciencetific format ( ex. 3.14 -> 0.314 * 10^1 )

If sorting in linklist the time clomplexity will change
quick sort affect
bucket sort dont affect
what if circular linked list
"""