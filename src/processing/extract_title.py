

def extract_title(markdown: str):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line[2:].strip()
	raise ValueError("No H1 header found in markdown")