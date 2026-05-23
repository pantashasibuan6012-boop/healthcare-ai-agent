# Healthcare AI Agent

Conversational AI for healthcare: patient intake, appointment scheduling, and symptom assessment.

## Features
- HIPAA-compliant data handling
- Symptom assessment with triage scoring
- Appointment scheduling
- Multi-language support (EN, ID, MS)
- EHR integration (FHIR API)

## Installation
```
pip install -r requirements.txt
```

## Usage
```
python main.py assess 'headache and fever for 3 days'
python main.py schedule --doctor smith --date 2024-01-15
```

## License
MIT