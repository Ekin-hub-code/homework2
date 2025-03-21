# Input: DNA string
s = input().strip()

# Count occurrences of 'A', 'C', 'G', and 'T'
count_A = s.count('A')
count_C = s.count('C')
count_G = s.count('G')
count_T = s.count('T')

# Output the results
print(count_A, count_C, count_G, count_T)
