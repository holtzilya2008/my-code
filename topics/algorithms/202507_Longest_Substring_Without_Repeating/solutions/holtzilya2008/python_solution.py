
def find_longest_substring_length(input: str) -> int:
    """
    finds the length of the longest substring within a given string that doesn't have 
    any repeating characters.
    
    A **substring** is a continuous sequence of characters within the original string.
    
    **Repeating characters** means the same character appears more than once.
    
    The substring must be continuous (unlike a subsequence which can skip characters).
    """
    if not isinstance(input, str):
        raise TypeError("The 'input' argument is expected to be a string.")
    
    length = len(input)
    if length == 0:
        return 0
    
    max = 1
    window_start = 0
    window_end = 0
    window_chars_to_index = {input[0]: 0}
    
    while window_end < length - 1:
        window_end += 1
        next_char = input[window_end]
        
        if next_char in window_chars_to_index:
            # Starting a new substring, Moving the window start point
            window_start = window_chars_to_index[next_char] + 1

            # Initialize a new window 
            # The length of this operation will be the longest substring so far. Not longer than 
            # The length of the given alphabet, therefore will take constant time.
            window_chars_to_index = {}
            for i in range(window_start, window_end): 
                window_chars_to_index[input[i]] = i
            
        # Add "next_char" to the window chars
        window_chars_to_index[next_char] = window_end
        window_size = len(window_chars_to_index)
        
        # Update the maximum
        if window_size > max:
            max = window_size
            
    return max
