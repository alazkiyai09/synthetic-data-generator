# Synthetic Data Generator

Synthetic data generation utilities for ML model testing and privacy-safe fraud detection experiments.

## Overview

This repository provides utilities for generating synthetic data that can be used for:

- **Machine Learning Model Testing**: Test ML pipelines without using real user data
- **Privacy-Safe Development**: Build systems without exposing sensitive information
- **OCR System Testing**: Generate document images for testing computer vision systems
- **Fraud Detection Research**: Create realistic transaction patterns for experimentation

## Why Use Synthetic Data?

### Privacy & Compliance

Real data often contains sensitive information that requires protection under:
- **GDPR** (EU General Data Protection Regulation)
- **PCI-DSS** (Payment Card Industry Data Security Standard)
- **CCPA** (California Consumer Privacy Act)

Synthetic data eliminates privacy concerns while maintaining statistical properties.

### Development Benefits

1. **No Data Access Delays**: Start development immediately
2. **Controlled Scenarios**: Generate specific edge cases
3. **Unlimited Supply**: Create as much data as needed
4. **Known Ground Truth**: Perfect labels for testing

## Modules

### 1. Document Image Generation (`generators/document_generator.py`)

**Purpose**: Generate synthetic document images for OCR system testing

**Features**:
- Indonesian ID card (eKTP) template-based generation
- Configurable personal information fields
- Image processing for realistic appearance

**Use Cases**:
- OCR accuracy testing
- Document verification pipeline development
- Computer vision model training

**Note**: This generates **clearly fake** documents for testing purposes only. Not for creating fraudulent documents.

### 2. License Plate Generator (`generators/plate_generator.py`)

**Purpose**: Generate synthetic Indonesian license plate images

**Features**:
- Region code prefixes (Indonesian provinces)
- Random number and letter combinations
- Batch image generation (150,000+ plates)
- Async processing for performance

**Generated Data**:
- CSV file with plate metadata
- JPG images of each license plate

**Use Cases**:
- ANPR (Automatic Number Plate Recognition) testing
- Traffic analysis system development
- Computer vision model training

## Installation

```bash
# Clone the repository
git clone https://github.com/alazkiyai09/synthetic-data-generator.git
cd synthetic-data-generator

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Requirements

```
Pillow>=8.0.0
pandas>=1.3.0
numpy>=1.21.0
```

## Usage

### Generating Document Images

```python
from generators.document_generator import generate_card

# Requires template images and fonts
# See docs/setup.md for template preparation
card = generate_card(fontNIK, fontHeader, fontIdentity, templateName)
card.save('output.jpg')
```

### Generating License Plates

```python
from generators.plate_generator import GeneratePlate
import asyncio

generator = GeneratePlate()
asyncio.run(generator.main())
```

This will:
1. Generate random plate combinations
2. Create `Dataset Number Plate.csv` with metadata
3. Save plate images to `Plate Image/` directory

## Data Privacy & Ethics

### Important Notes

1. **Testing Only**: These tools are for testing OCR and ML systems
2. **No Real Data**: All generated data is synthetic
3. **Clear Indicators**: Generated documents should be clearly identifiable as synthetic
4. **Compliance**: Ensure usage complies with local laws and regulations

### Responsible Use

- Use for internal testing and development only
- Never attempt to pass synthetic data as real
- Clearly label all synthetic datasets
- Follow organizational data governance policies

## Fraud Detection Applications

Synthetic transaction data is valuable for:

1. **Baseline Model Development**: Train initial models before accessing real data
2. **Edge Case Testing**: Generate rare fraud patterns
3. **Stress Testing**: Create high-volume synthetic transaction streams
4. **Compliance Development**: Build systems without touching real user data

## Dataset Structure

### License Plate Dataset

The generated CSV contains:

| Column | Description |
|--------|-------------|
| Prefix | Region code (e.g., 'B' for Jakarta) |
| Suffix | Letter combination (e.g., 'ABC') |
| Number | Numeric sequence (e.g., '1234') |
| Date | Expiry date (synthetic) |

### Indonesian Region Codes

| Prefix | Region |
|--------|--------|
| A | DKI Jakarta |
| B | Jakarta (plates) |
| D | Bandung |
| E | Cirebon |
| ... | ... |

## Configuration

### Templates Setup

1. Place document templates in appropriate directories
2. Configure font paths in generator scripts
3. Adjust output directories as needed

See `docs/setup.md` for detailed setup instructions.

## Performance

The license plate generator uses async processing:

- **Throughput**: 150,000+ plates generated efficiently
- **Optimization**: Async I/O for image operations
- **Batch Processing**: Generates entire datasets at once

## Examples

### Generate Sample Plates

```python
import asyncio
import pandas as pd
from generators.plate_generator import GeneratePlate

# Generate first 100 plates only
generator = GeneratePlate()
await generator.genrateRandomData()

dataset = pd.read_csv('Dataset Number Plate.csv')
sample = dataset.head(100)
print(sample)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

This is a utility repository. Feel free to open issues or PRs for additional generators.

## Author

**Ahmad Whafa Azka Al Azkiyai**
- GitHub: [alazkiyai09](https://github.com/alazkiyai09)
- Email: [azka.alazkiyai@outlook.com](mailto:azka.alazkiyai@outlook.com)
- Specialization: Fraud Detection & AI Security

## References

- [GDPR Compliance](https://gdpr.eu/)
- [Synthetic Data for ML](https://arxiv.org/abs/2011.05331)
- [Privacy-Preserving ML](https://arxiv.org/abs/1905.09682)
