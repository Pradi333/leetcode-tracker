# Last updated: 7/28/2026, 2:56:53 PM
1class Solution:
2    def fullJustify(self, words, maxWidth):
3        result = []
4        i = 0
5
6        while i < len(words):
7            # Find words that can fit in this line
8            line_length = len(words[i])
9            j = i + 1
10
11            while j < len(words):
12                if line_length + 1 + len(words[j]) > maxWidth:
13                    break
14
15                line_length += 1 + len(words[j])
16                j += 1
17
18            line_words = words[i:j]
19            total_chars = sum(len(word) for word in line_words)
20            spaces = maxWidth - total_chars
21
22            # Last line or only one word
23            if j == len(words) or len(line_words) == 1:
24                line = " ".join(line_words)
25                line += " " * (maxWidth - len(line))
26            else:
27                gaps = len(line_words) - 1
28                space_each = spaces // gaps
29                extra = spaces % gaps
30
31                line = ""
32
33                for k in range(gaps):
34                    line += line_words[k]
35                    line += " " * (space_each + (1 if k < extra else 0))
36
37                line += line_words[-1]
38
39            result.append(line)
40            i = j
41
42        return result