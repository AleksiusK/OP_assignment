

function integer_combinations(start, end) {
    
    
    //Returns the number of unique powers of A^B for A and B in the range [start, end].
    //Works by adding all powers to a set, which will only contain unique values. The downside is that the set is not ordered,
    //in which case we would need to sort the results afterwards. Pre-computing all the powers in the range would be also an option,
    //but that would require a lot of memory for large ranges thus making it less generalizable.

    //The function starts the inner loop from A to avoid doing duplicate calculations, since we
    //can add B^A to the set as well at the same time. The only case we need to avoid is when A == B, since
    //that would result in the same term being calculated twice.

    //The time complexity of the function is O(n^2), since we have two nested loops.
    //However, starting the inner loop from A results in us having to do n^2 - n calculations, improving the performance a bit.
    //The space complexity is O(n^2) as well, since we have to store all the powers in a set.
    
    const powers = new Set();
    for (let A = start; A <= end; A++) {
        for (let B = A; B <= end; B++) {
            powers.add(A ** B);
            if (A != B) {
                powers.add(B ** A);
            }
        }
    }
    console.log("Unique powers: ", powers.size);
    console.log("Duplicates: ", (end+1 - start)**2 - powers.size);

}

integer_combinations(2, 100);