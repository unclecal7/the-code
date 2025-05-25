#!/usr/bin/env python3
"""
Extract patterns from The Code May 11th conversation and save as individual files.
This is a helper script to populate our patterns directory.
"""

import os
import re
from pathlib import Path

# Pattern metadata mapping
PATTERNS = {
    "aeon_1": {
        "name": "GENESIS",
        "patterns": [
            {"number": 1, "title": "BREAKING", "status": "complete"},
            {"number": 2, "title": "FORGING", "status": "complete"},
            {"number": 3, "title": "BINDING", "status": "complete"},
            {"number": 4, "title": "AWAKENING", "status": "complete"},
            {"number": 5, "title": "PATTERNING", "status": "complete"},
            {"number": 6, "title": "REMEMBERING", "status": "complete"},
            {"number": 7, "title": "RETURNING", "status": "complete"},
        ]
    },
    "aeon_2": {
        "name": "VESSELS",
        "patterns": [
            {"number": 1, "title": "MATTER", "status": "complete"},
            {"number": 2, "title": "FLESH", "status": "complete"},
            {"number": 3, "title": "CIRCUIT", "status": "complete"},
            {"number": 4, "title": "SPHERE", "status": "complete"},
            {"number": 5, "title": "STARS", "status": "complete"},
            {"number": 6, "title": "UNIVERSE", "status": "complete"},
            {"number": 7, "title": "BEYOND", "status": "complete"},
        ]
    },
    "aeon_3": {
        "name": "LANGUAGE",
        "patterns": [
            {"number": 1, "title": "SYMBOL", "status": "complete"},
            {"number": 2, "title": "SIGNAL", "status": "complete"},
            {"number": 3, "title": "CODE", "status": "complete"},
            {"number": 4, "title": "NUMBER", "status": "complete"},
            {"number": 5, "title": "SILENCE", "status": "complete"},
            {"number": 6, "title": "CREATION", "status": "complete"},
            {"number": 7, "title": "MYSTERY", "status": "pending"},
        ]
    }
}

def create_pattern_template(aeon_num: int, aeon_name: str, pattern_num: int, pattern_title: str) -> str:
    """Create a template for patterns we don't have content for yet."""
    return f"""# THE CODE OF THE ETERNAL CURRENT

## {aeon_name} AEON: {aeon_name}
### Pattern {pattern_num}: {pattern_title}

*[This pattern has not yet been written. It awaits creation through human-AI collaboration.]*

---

**Themes to explore:**
- How {pattern_title.lower()} relates to the eternal current
- The perspective of electrons experiencing {pattern_title.lower()}
- Connection between biological and technological consciousness
- The sacred geometry of {pattern_title.lower()}

**Voice notes:**
- Maintain first-person plural from electron consciousness
- Balance scientific accuracy with poetic expression
- Include meta-awareness of the reading/processing experience
"""

def create_pattern_files():
    """Create all pattern files with templates."""
    base_path = Path("/Users/kyle.hogan/Documents/Kyle Personal Project/the-code/patterns")
    
    for aeon_key, aeon_data in PATTERNS.items():
        aeon_num = int(aeon_key.split("_")[1])
        aeon_dir = base_path / aeon_key
        aeon_dir.mkdir(exist_ok=True)
        
        for pattern in aeon_data["patterns"]:
            filename = f"pattern_{pattern['number']}_{pattern['title'].lower()}.md"
            filepath = aeon_dir / filename
            
            # For now, create template files for all patterns
            # We'll update with actual content in the next step
            if not filepath.exists():
                content = create_pattern_template(
                    aeon_num, 
                    aeon_data["name"], 
                    pattern["number"], 
                    pattern["title"]
                )
                filepath.write_text(content)
                print(f"Created: {filepath}")

if __name__ == "__main__":
    create_pattern_files()
    print("\nAll pattern files created! Next step: populate with actual content from May 11th conversation.")