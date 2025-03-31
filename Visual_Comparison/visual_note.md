1. Entropy Analysis:
	•	Entropy measures the randomness or unpredictability of passwords.
	•	A higher entropy score suggests that the honeywords are more difficult to guess.
	•	A lower entropy might indicate more predictable passwords, making them weaker.
Comparisons & Insights:
	•	The entropy graphs compare honeywords generated for 000webhost vs. myspace.
	•	Different temperature settings (t=0.1, 0.5, 1) indicate how randomness is controlled during generation.
		o	Lower temperature (t=0.1) → More structured, less diverse passwords.
		o	Higher temperature (t=1) → More randomness but potentially less realistic passwords.
	•	If myspace consistently has higher entropy than 000webhost, its honeywords may be stronger.
2. Length Distribution:
	•	This shows the distribution of password lengths across datasets.
	•	Helps identify trends like whether a dataset generates more short or long passwords.
Comparisons & Insights:
	•	If one dataset consistently generates shorter passwords, it may be using simpler words.
	•	If another generates longer passwords, it may be using more complex phrases or patterns.
	•	A dataset with a more even length distribution might have better diversity.
3. Levenshtein Distance
	•	Levenshtein distance measures how different two words are based on character edits (insertions, deletions, substitutions).
	•	This metric helps compare honeywords between 000webhost and myspace.
Comparisons & Insights:
	•	If the average Levenshtein distance is low, the two datasets generate similar honeywords.
	•	If it's high, the datasets produce significantly different honeywords.
	•	A heatmap representation can show clusters where honeywords are highly similar or distinct.
4. Cosine Similarity 
	•	Uses TF-IDF (text-based similarity) to compare datasets.
	•	Ranges from 0 (completely different) to 1 (identical honeywords).
	•	The heatmap visualizes the degree of similarity.
Comparisons & Insights:
	•	If 000webhost and myspace show high similarity, they might be generating honeywords using similar patterns.
	•	If similarity is low, the datasets are producing more unique results.
	•	Variations across temperature settings can indicate how randomness affects honeyword structure.

