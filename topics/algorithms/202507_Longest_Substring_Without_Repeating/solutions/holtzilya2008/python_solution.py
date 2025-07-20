
def find_longest_substring(input: str) -> int:    
    length = len(input)
    last_index = length - 1
    
    if length == 0:
        return 0
    
    max = 1
    window_start = 0
    window_end = 0
    window_chars_to_index = {input[0]: 0}
    
    while window_end < last_index:
        window_end += 1
        next_char = input[window_end]
        
        if next_char in window_chars_to_index:
            # Starting a new substring
            previous_window_start = window_start
            window_start = window_chars_to_index[next_char] + 1
            
            # Remove all unnecessary window eleemnts from the dict
            for i in range(previous_window_start, window_start): 
                window_chars_to_index.pop(input[i])
            
        # Add "next_char" to the window chars
        window_chars_to_index[next_char] = window_end
        window_size = len(window_chars_to_index)
        
        # Update the maximum
        if window_size > max:
            max = window_size
            
    return max
