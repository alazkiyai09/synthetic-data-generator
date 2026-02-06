# Synthetic Data Generator - Setup Guide

## Prerequisites

1. Python 3.7 or higher
2. pip package manager
3. (Optional) Virtual environment

## Installation

```bash
# Clone the repository
git clone https://github.com/alazkiyai09/synthetic-data-generator.git
cd synthetic-data-generator

# Install dependencies
pip install -r requirements.txt
```

## Template Setup

### Document Generator Setup

The document generator requires:

1. **Template Image**: `Template eKTP.jpg` - Indonesian ID card template
2. **Photo**: `1.jpg` - Portrait photo for the card
3. **Signature**: `sign.jpg` - Signature image
4. **Fonts**:
   - `OCR-A Regular.ttf` - For NIK (ID number)
   - `ArialUnicodeMS.ttf` - For identity information
   - `ArialCEBold.ttf` - For headers

### License Plate Generator Setup

The plate generator requires:

1. **Template Directory**: `Template/` folder containing:
   - `Plat Nomor.jpg` - License plate template
   - `PlatNomor.ttf` - License plate font

## Directory Structure

```
synthetic-data-generator/
├── generators/
│   ├── document_generator.py
│   └── plate_generator.py
├── docs/
│   └── setup.md
├── requirements.txt
└── README.md

# Runtime created directories:
├── Plate Image/           # Generated license plates
└── Dataset Number Plate.csv  # Plate metadata
```

## Usage Examples

### Generate License Plates

```python
import asyncio
from generators.plate_generator import GeneratePlate

# Create generator instance
generator = GeneratePlate()

# Run generation (creates CSV and images)
asyncio.run(generator.main())
```

**Output**:
- `Dataset Number Plate.csv` - Metadata for all generated plates
- `Plate Image/` - Directory containing JPG images of each plate

### Generate Document Images

```python
from PIL import ImageFont
from generators.document_generator import generate_card

# Load fonts
fontNIK = ImageFont.truetype("OCR-A Regular.ttf", size=70)
fontIdentity = ImageFont.truetype("ArialUnicodeMS.ttf", size=46)
fontHeader = ImageFont.truetype("ArialCEBold.ttf", size=65)

# Generate card
templateName = "Template eKTP.jpg"
card = generate_card(fontNIK, fontHeader, fontIdentity, templateName)
card.save('Result.jpg')
```

## Customization

### Changing Plate Region Codes

Edit the `prefixes` list in `plate_generator.py`:

```python
prefixes = ['A', 'B', 'D', 'E', 'G', 'H', 'K',
            'L', 'M', 'N', 'P', 'R', 'AA', 'AB',
            # ... add more region codes
           ]
```

### Adjusting Generation Count

Modify the slice in `plate_generator.py`:

```python
# Generate all
dataset = pd.read_csv('Dataset Number Plate.csv')

# Or limit to specific number
dataset = pd.read_csv('Dataset Number Plate.csv')[:100]
```

## Output Formats

### License Plate CSV

| Column | Type | Description |
|--------|------|-------------|
| Prefix | string | Region code (1-2 characters) |
| Suffix | string | Letter suffix (3 characters or blank) |
| Number | string | Numeric sequence (1-5 digits) |
| Date | string | Synthetic expiry date (HH:MM format) |

### Image Specifications

- **Format**: JPEG
- **Quality**: High contrast enhancement applied
- **Naming**: `{Prefix}{Number}{Suffix}.jpg`

## Troubleshooting

### Font Errors

If you get font loading errors:
1. Ensure font files are in the correct location
2. Or update font paths in the generator code
3. Or use system fonts by changing the path

### Template Not Found

Ensure template images are in the working directory or update paths:
```python
templateName = "/path/to/your/Template eKTP.jpg"
```

### Async Warnings

The plate generator uses `asyncio`. If you see warnings:
```python
# Python 3.7+
asyncio.run(generator.main())

# Python 3.6
loop = asyncio.get_event_loop()
loop.run_until_complete(generator.main())
```

## Notes

- Generated documents are for **testing purposes only**
- Templates should be clearly marked as synthetic
- Always comply with local laws and regulations
- Never use generated data for fraudulent purposes
