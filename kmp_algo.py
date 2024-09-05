def ComputeLSP(pattern: str, size: int, lps: list):
  longest_pref_size = 0
  lps.append(0)
  i = 1

  while i < size:
    if pattern[i] == pattern[longest_pref_size]:
      longest_pref_size += 1
      lps.append(longest_pref_size)
      i += 1
    else:
      if longest_pref_size != 0:
        longest_pref_size = lps[longest_pref_size-1]
      else:
        lps.append(0)
        i += 1

def KMPSearch(text: str, pattern: str):
  findings = []

  n = len(text)
  m = len(pattern)

  lps = [0] * m
  j = 0

  ComputeLSP(pattern, m, lps)

  i = 0
  while i < n:
    if pattern[j] == text[i]:
      i += 1
      j += 1

    if j == m:
      start_index = i - j
      end_index = i - 1
      print("Pattern found at indexes:", start_index, "-", end_index)
      findings.append((start_index, end_index))
      j = lps[j-1]
    elif i < n and pattern[j] != text[i]:
      if j != 0:
        j = lps[j-1]
      else:
        i += 1

  return findings