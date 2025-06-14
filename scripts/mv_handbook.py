import os
import shutil

# Base paths
BASE_DIR = "userguide/content/en/docs"
SRC_DIR = os.path.join(BASE_DIR, "src")

# Mapping of filenames to their target handbook subfolders
target_subfolder = {
    # Complaints & Policies
    "complaints-policy.md": "compliance/complaints",
    "feedback-complaintsreviews.md": "compliance/complaints",

    # Data & Decision-Making
    "data-driven-decision-making-strategy.md": "strategy/data",
    "gdpr-acknowledgement.md": "technology/security/gdpr",
    "gdpr-breach-comm-to-data-subject.md": "technology/security/gdpr",
    "gdpr-consent-withdrawal.md": "technology/security/gdpr",
    "gdpr-dpo.md": "technology/security/gdpr",
    "gdpr-sar-more-time.md": "technology/security/gdpr",
    "gdpr-sar-provide-info.md": "technology/security/gdpr",
    "gdpr-sar-verification-verbal.md": "technology/security/gdpr",
    "gdpr-sar-verification-written.md": "technology/security/gdpr",

    # Operations & Waste Management
    "disposal-of-nonconforming-operation.md": "operations/quality",

    # E-Commerce & Marketing
    "e-commerce-plan.md": "marketing/ecommerce",
    "facebook-ads.md": "marketing/ads",
    "fundamentals-of-sustainable-marketing.md": "marketing/sustainability",

    # Electrical & Equipment Policies
    "electrical-devices-policy.md": "compliance/health-safety",
    "equipment-hire-agreement-legal-document-for-business.md": "legal/contracts",
    "equipment-policy.md": "compliance/asset-management",
    "equipment-procurement-procedure.md": "operations/procurement",
    "equipment-report-and-return-form.md": "operations/procurement",
    "equipment-security-policy.md": "technology/security",

    # Emergency & Crisis Management
    "emergency-plan-legal-document-for-business.md": "legal/templates",
    "emergency-preparedness-and-response.md": "operations/continuity",
    "ems-emergency-preparedness-and-response-plans.md": "operations/continuity",
    "fms-emergency-preparedness-plans.md": "operations/continuity",
    "fire-fighting-checklist.md": "compliance/health-safety",
    "fire-prevention.md": "compliance/health-safety",
    "first-aid-box-checklist.md": "compliance/health-safety",
    "first-aid.md": "compliance/health-safety",

    # Employee & HR Policies & Procedures
    "employee-benefits-administration-procedures-for-enrolling-employees-in-benefits-programs-handling-claims-and-managing-benefit-changes.md": "people/hr/benefits",
    "employee-code-of-conduct.md": "people/hr/policies",
    "employee-evaluation-legal-document-for-business.md": "legal/hr",
    "employee-handbooks.md": "people/hr/policies",
    "employee-onboarding-checklist.md": "people/hr/onboarding",
    "employee-onboarding-steps-for-introducing-new-hires-to-the-company-including-orientation-training-and-setup-of-necessary-tools-and-access.md": "people/hr/onboarding",
    "employee-personal-data-request-form.md": "people/hr/data-privacy",
    "employee-privacy-notice.md": "people/hr/data-privacy",
    "employee-privacy-policy.md": "people/hr/data-privacy",
    "employing-foreign-nationals.md": "people/hr/compliance",
    "employment-agreement.md": "legal/hr",
    "employment-contract-legal-document-for-business.md": "legal/hr",
    "employment-disputes.md": "people/hr/relations",
    "employment-offer-letter-legal-document-for-business.md": "legal/hr",
    "employment-termination-letter-legal-document-for-business.md": "legal/hr",

    # Energy & Environment
    "energy-objectives-and-action-plans.md": "sustainability/energy",
    "energy-performance-indicators-enpis.md": "sustainability/energy",
    "energy-policy.md": "sustainability/energy",
    "energy-review-and-baseline.md": "sustainability/energy",
    "energy-use-report.md": "sustainability/energy",
    "environment-risk-policy.md": "sustainability/environment",
    "environmental-aspects-and-impact-register.md": "sustainability/environment",
    "environmental-impact-assessment-for-digital-marketing-campaign.md": "sustainability/marketing",
    "environmental-impact-considerations.md": "sustainability/environment",
    "environmental-impact-statement.md": "sustainability/environment",
    "environmental-management-policy.md": "sustainability/environment",
    "environmental-management-system-ems-manual.md": "sustainability/environment",
    "environmental-monitoring-and-evaluation-of-compliance.md": "sustainability/environment",
    "environmental-monitoring.md": "sustainability/environment",
    "environmental-objectives-and-targets.md": "sustainability/environment",
    "environmental-policy.md": "sustainability/environment",
    "environmental-practices-for-using-companys-car.md": "sustainability/transport",
    "environmental-procedure---review-of-legal-and-other-requirements.md": "sustainability/environment",
    "environmental-procedure.md": "sustainability/environment",
    "environmental-risk-assessment-report.md": "sustainability/environment",
    "environmental-sustainability--zoho-sustainability.md": "sustainability/environment",
    "environmental-sustainability-for-virtual-offices.md": "sustainability/environment",
    "environmental-training.md": "people/training",
    "environmentally-preferable-purchasing-epp-policy.md": "sustainability/procurement",

    # Equality, Diversity & Inclusion
    "equal-opportunities-policy.md": "people/hr/inclusion",
    "equality-diversity-and-inclusion-policy.md": "people/hr/inclusion",

    # ESG & Sustainability Frameworks
    "esg-criteria-for-green-orbit-digitals-investments.md": "sustainability/esg",
    "esg-due-diligence-framework.md": "sustainability/esg",
    "esg-framework-for-digital-marketing.md": "sustainability/esg",
    "esg-policy.md": "sustainability/esg",
    "esms-audit-checklist-more-than-150-questions.md": "sustainability/ems",
    "esms-issues-register.md": "sustainability/ems",
    "esms-manual.md": "sustainability/ems",

    # Ethics & Compliance
    "ethical--decision-making.md": "compliance/ethics",
    "ethical-approach-to-ai.md": "compliance/ethics",
    "ethical-commitment.md": "compliance/ethics",
    "ethical-marketing-advertisement-and-customer-engagement-policy.md": "marketing/ethics",
    "ethical-marketing.md": "marketing/ethics",
    "ethical-partnerships-and-sponsorship-policy.md": "marketing/ethics",
    "ethical-policy.md": "compliance/ethics",
    "ethical-principles.md": "compliance/ethics",
    "ethical-screening-policy.md": "compliance/ethics",
    "ethics-and-compliance-programme.md": "compliance/ethics",
    "ethics-focused-risk-assessment.md": "compliance/ethics",

    # Event Management
    "event-accessibility-policy.md": "events/policies",
    "event-activities-planning-checklist.md": "events/planning",
    "event-inspection-checklist.md": "events/planning",
    "event-logging-and-review-policy.md": "events/policies",
    "event-loss-and-bad-work-practice-observation-report.md": "events/reports",
    "event-objectives-and-targets.md": "events/planning",
    "event-refund-policy.md": "events/policies",
    "event-terms.md": "events/policies",
    "events-code-of-conduct.md": "events/policies",

    # Legal & Contracts
    "eviction-notices-residential-legal-document-for-business.md": "legal/templates",
    "engagement-letter.md": "legal/contracts",
    "executive-support-letter.md": "legal/contracts",

    # Documentation & Review
    "evidence-of-management-review.md": "operations/quality",
    "exercise-and-testing-records.md": "operations/quality",

    # Finance & Expense
    "expense-claim-form.md": "finance/forms",
    "expense-management-procedures-for-submitting-approving-and-reimbursing-employee-expenses.md": "finance/policies",
    "expense-policy.md": "finance/policies",
    "finance--administration-strategy.md": "finance/strategy",
    "finance.md": "finance/overview",
    "financial-control-policy.md": "finance/policies",
    "financial-management-policy.md": "finance/policies",
    "financial-reporting-guidelines-for-preparing-and-reviewing-financial-statements-and-reports.md": "finance/reporting",
    "financial-statement-personal-legal-document-for-business.md": "legal/templates",

    # General Forms & Checklists
    "forms.md": "operations/forms",
    "feasibility-checklist.md": "planning/checklists",

    # Facilities & Food
    "facility-management-policy-and-strategy.md": "operations/facilities",
    "food-and-catering-policy.md": "operations/facilities",
    "food-hygiene.md": "compliance/health-safety",
    "food-labelling.md": "compliance/health-safety",

    # Fraud & Ethics
    "fraud-and-corruption--sustainable-business-alliance.md": "compliance/ethics",

    # Functional & Corporate Strategy
    "functional-strategy.md": "strategy",
}

def ensure_dir_exists(path):
    if not os.path.exists(path):
        print(f"Creating directory: {path}")
        os.makedirs(path, exist_ok=True)

def main():
    print(f"Starting processing files from: {SRC_DIR}")
    print(f"Base handbook directory: {BASE_DIR}\n")

    # List files in src directory
    files = [f for f in os.listdir(SRC_DIR) if os.path.isfile(os.path.join(SRC_DIR, f))]

    if not files:
        print("No files found in source directory.")
        return

    for filename in files:
        src_path = os.path.join(SRC_DIR, filename)

        if filename in target_subfolder:
            dest_subfolder = target_subfolder[filename]
            dest_dir = os.path.join(BASE_DIR, dest_subfolder)
            dest_path = os.path.join(dest_dir, filename)

            # Ensure destination folder exists
            ensure_dir_exists(dest_dir)

            # Move file
            print(f"Moving '{filename}' to '{dest_subfolder}/'")
            shutil.move(src_path, dest_path)
        else:
            # File not mapped: leave in src
            print(f"Skipping '{filename}': no mapping found, leaving in 'src/'")

    print("\nProcessing complete.")

if __name__ == "__main__":
    main()