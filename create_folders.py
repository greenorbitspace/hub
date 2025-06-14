import os

base_dir = "userguide/content/en/docs/legal-hub"

structure = {
    "contracts": {
        "employment": [
            "employment-agreement.md",
            "nda.md",
            "consultant-contract.md",
            "termination-letter.md"
        ],
        "client-agreements": [
            "service-agreement.md",
            "master-services-agreement.md",
            "statement-of-work.md"
        ],
        "supplier-contracts": [
            "equipment-hire-agreement.md",
            "procurement-contract.md"
        ],
        "partnership-agreements": [
            "collaboration-agreement.md"
        ],
        "templates": [
            "contract-template.md",
            "nda-template.md"
        ],
    },
    "compliance": {
        "data-protection": [
            "gdpr-policy.md",
            "data-processing-agreement.md",
            "privacy-notice.md"
        ],
        "health-and-safety": [
            "health-safety-policy.md",
            "incident-reporting.md"
        ],
        "environmental": [
            "sustainability-compliance.md",
            "environmental-risk-assessment.md"
        ],
        "ethics": [
            "code-of-conduct.md",
            "whistleblowing-policy.md"
        ]
    },
    "governance": {
        "board-meetings": [
            "meeting-minutes.md",
            "resolutions.md"
        ],
        "policies": [
            "company-policies.md",
            "conflict-of-interest.md"
        ],
        "regulatory": [
            "licences.md",
            "registrations.md"
        ]
    },
    "intellectual-property": [
        "patents.md",
        "trademarks.md",
        "copyrights.md",
        "ip-policy.md"
    ],
    "dispute-resolution": [
        "mediation.md",
        "arbitration.md",
        "legal-notices.md"
    ],
    "templates": {
        "letter-templates": [
            "offer-letter.md",
            "termination-letter.md",
            "demand-letter.md"
        ],
        "form-templates": [
            "consent-form.md",
            "incident-report-form.md"
        ]
    },
    "README.md": None
}


def create_structure(base_path, structure):
    if isinstance(structure, dict):
        for key, value in structure.items():
            path = os.path.join(base_path, key)
            if value is None:
                # Create a file (like README.md)
                with open(path, 'w') as f:
                    pass  # empty file
                print(f"Created file: {path}")
            else:
                # Create folder and recurse
                os.makedirs(path, exist_ok=True)
                print(f"Created directory: {path}")
                create_structure(path, value)
    elif isinstance(structure, list):
        for filename in structure:
            file_path = os.path.join(base_path, filename)
            with open(file_path, 'w') as f:
                pass  # empty file
            print(f"Created file: {file_path}")


if __name__ == "__main__":
    create_structure(base_dir, structure)
    print("Legal hub folder structure created successfully.")