def longest_repeated_substring(s):
    """
    Identifies the longest repeated substring in a string.
    Uses a Suffix Array approach which is efficient for this purpose.
    """
    n = len(s)
    if n == 0:
        return ""
        
    # Generate suffix array (sorted list of indices)
    # This sorts indices based on the suffix starting at that index
    suffixes = sorted(range(n), key=lambda i: s[i:])
    
    max_length = 0
    longest_substr = ""
    
    # Compare adjacent suffixes in the sorted array
    for i in range(n - 1):
        # We only need to check adjacent ones because the suffixes are sorted.
        # The longest common prefix between any two suffixes must appear 
        # between some pair of adjacent suffixes in the sorted list.
        p1 = suffixes[i]
        p2 = suffixes[i+1]
        
        # Find length of common prefix
        current_length = 0
        min_len = min(n - p1, n - p2)
        
        # Optimization: fast forward common prefix check
        while current_length < min_len and s[p1 + current_length] == s[p2 + current_length]:
            current_length += 1
            
        if current_length > max_length:
            max_length = current_length
            longest_substr = s[p1:p1 + max_length]
            
    return longest_substr

def find_all_repeated_substrings(s, min_length=2):
    """
    Finds all substrings that repeat more than once with a minimum length.
    Returns a dictionary with substring as key and count as value.
    Note: identifying ALL repeated substrings can be very large.
    This limits by checking fixed lengths or using a sliding window.
    For typically short strings, a naive interaction is okay, but for optimization
    we will use a hash map counting approach for sensible lengths.
    """
    counts = {}
    n = len(s)
    
    # To optimize, we can check lengths. 
    # But a true "all repeated" list is massive for large strings.
    # We will grab all standard repeated substrings.
    
    # Optimized approach: Only keep track of substrings that actually appear.
    # We will iterate through all possible substrings.
    # Warning: O(N^3) in worst case purely by generating them.
    # Better approach for "highly optimized" request: 
    # Use LCP array derived logic or just stick to the longest one as the primary answer.
    # Here is a reasonably efficient counter for demonstration.
    
    seen = {}
    repeated = set()
    
    # Only iterate through lengths that matter? 
    # Let's simple check all substrings loop 
    for length in range(min_length, n // 2 + 1): # Max repeatable length is n/2 roughly for non-overlapping
        temp_seen = set()
        for i in range(n - length + 1):
            sub = s[i:i+length]
            if sub in temp_seen:
                repeated.add(sub)
            else:
                temp_seen.add(sub)
                
    return sorted(list(repeated), key=len, reverse=True)

if __name__ == "__main__":
    test_string = "banana"
    print(f"String: {test_string}")
    lrs = longest_repeated_substring(test_string)
    print(f"Longest Repeated Substring: '{lrs}'")

    test_string_2 = "mississippi"
    print(f"\nString: {test_string_2}")
    lrs_2 = longest_repeated_substring(test_string_2)
    print(f"Longest Repeated Substring: '{lrs_2}'")
    
    test_string_3 = "abcde"
    print(f"\nString: {test_string_3}")
    lrs_3 = longest_repeated_substring(test_string_3)
    print(f"Longest Repeated Substring: '{lrs_3}'")
