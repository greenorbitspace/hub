import os
import shutil
from pathlib import Path

# Root directory where files are currently located
SOURCE_DIR = Path.cwd()
TARGET_DIR = SOURCE_DIR / "Employee_Handbook"

# Map of filename to folder path (relative to TARGET_DIR)
file_map = {
    # 01 - Values & Conduct
    "employee-code-of-conduct.md": "01-values-conduct",
    "dignity-and-respect-at-work-policy.md": "01-values-conduct",
    "standards-of-conduct.md": "01-values-conduct",
    "harassment-and-bullying-at-work.md": "01-values-conduct",
    "trust.md": "01-values-conduct",
    "transgender-guidance.md": "01-values-conduct",
    "understanding-unconscious-bias.md": "08-inclusion-culture",

    # 02 - Employment Policies
    "consultant-privacy-policy.md": "02-employment-policies/contracts",
    "consultant-resource-guide.md": "02-employment-policies/contracts",
    "contractor-privacy-notice.md": "02-employment-policies/contracts",
    "temporary-and-agency-workers.md": "02-employment-policies/contracts",

    "recruitment-and-selection-policy.md": "02-employment-policies/onboarding-offboarding",
    "safer-recruitment-policy.md": "02-employment-policies/onboarding-offboarding",
    "screening-policy-pre-employment-checks.md": "02-employment-policies/onboarding-offboarding",
    "termination-of-employment.md": "02-employment-policies/onboarding-offboarding",
    "termination-process-steps-for-handling-resignations-terminations-and-exit-interviews.md": "02-employment-policies/onboarding-offboarding",
    "responsibilities-after-termination-or-change-of-employment.md": "02-employment-policies/onboarding-offboarding",
    "retire-and-return.md": "02-employment-policies/onboarding-offboarding",
    "retirement-and-retirement-gift-policy.md": "02-employment-policies/onboarding-offboarding",
    "redundancy.md": "02-employment-policies/onboarding-offboarding",

    # 03 - Time & Attendance
    # Leave
    "annual-leave-policy.md": "03-time-attendance/leave",
    "vacation-policy.md": "03-time-attendance/leave",
    "other-leave-policy.md": "03-time-attendance/leave",
    "maternity-paternity-adoption-and-parental-leave-policy.md": "03-time-attendance/leave",
    "pregnancy-and-maternity-leave-and-pay.md": "03-time-attendance/leave",
    "paternity-leave-and-pay.md": "03-time-attendance/leave",
    "compassionate-leave.md": "03-time-attendance/leave",
    "holidays-and-pay.md": "03-time-attendance/leave",
    "time-off-in-lieu-policy.md": "03-time-attendance/leave",
    "time-off-work.md": "03-time-attendance/leave",
    "morale-events-policy.md": "03-time-attendance/leave",

    # Work Arrangements
    "attendance-policy.md": "03-time-attendance/work-arrangements",
    "attendance-management-policy.md": "03-time-attendance/work-arrangements",
    "timekeeping-policies-and-procedures.md": "03-time-attendance/work-arrangements",
    "overtime-policy.md": "03-time-attendance/work-arrangements",
    "working-from-home-policy.md": "03-time-attendance/work-arrangements",
    "remote-working-and-homeworking-policy.md": "03-time-attendance/work-arrangements",
    "remote-and-agile-working.md": "03-time-attendance/work-arrangements",
    "remote-work--byod-policy.md": "03-time-attendance/work-arrangements",
    "wfh-guidance.md": "03-time-attendance/work-arrangements",
    "mobile-and-remote-access-policy.md": "03-time-attendance/work-arrangements",
    "mobile-device-and-teleworking-policy.md": "03-time-attendance/work-arrangements",
    "remote-access-policy.md": "03-time-attendance/work-arrangements",
    "sustainable-working-home-and-working.md": "03-time-attendance/work-arrangements",
    "workplace-transport.md": "03-time-attendance/work-arrangements",

    # 04 - Health & Wellbeing
    "mental-health-policy.md": "04-health-wellbeing",
    "stress-at-work.md": "04-health-wellbeing",
    "homesickness-and-culture-shock.md": "04-health-wellbeing",
    "tiredness-and-fatigue.md": "04-health-wellbeing",
    "sickness-and-return-to-work.md": "04-health-wellbeing",
    "sickness-and-sick-pay.md": "04-health-wellbeing",
    "workplace-violence.md": "04-health-wellbeing",

    # 05 - Performance & Development
    "annual-performance-self-review.md": "05-performance-development/performance",
    "performance--reports-kpi-dashboard.md": "05-performance-development/performance",
    "performance-management-guidelines-for-setting-objectives-conducting-performance-reviews-and-managing-employee-development.md": "05-performance-development/performance",
    "performance-reviews.md": "05-performance-development/performance",
    "underperformance.md": "05-performance-development/performance",

    "competency-framework.md": "05-performance-development/learning",
    "competence-development-questionnaire.md": "05-performance-development/learning",
    "competence-report.md": "05-performance-development/learning",
    "skill-requirements.md": "05-performance-development/learning",
    "career_progression_pathways.md": "05-performance-development/learning",
    "talent-acquisition-and-retention-strategy.md": "05-performance-development/learning",
    "talent-assessment.md": "05-performance-development/learning",
    "workshop-feedback.md": "05-performance-development/learning",
    "workshops.md": "05-performance-development/learning",

    # 06 - Pay & Benefits
    "pay-advances.md": "06-pay-benefits",
    "pay-and-performance-policy.md": "06-pay-benefits",
    "benefits-presentation.md": "06-pay-benefits",
    "childcare.md": "06-pay-benefits",
    "relocation-assistance-policy.md": "06-pay-benefits",

    # 07 - Policies & Procedures
    "system-acceptable-use-policy.md": "07-policies-procedures/security",
    "staff-data-protection-training-policy.md": "07-policies-procedures/security",
    "disciplinary-process-policy-information-security-breaches.md": "07-policies-procedures/security",

    "grievance-policy--procedure.md": "07-policies-procedures/legal",
    "disciplinary-procedures.md": "07-policies-procedures/legal",
    "whistleblowing-policy.md": "07-policies-procedures/legal",
    "employee-handbooks.md": "07-policies-procedures/legal",
    "compliance.md": "07-policies-procedures/legal",

    # 08 - Inclusion & Culture
    "inclusion.md": "08-inclusion-culture",
    "underrepresentative-stategy.md": "08-inclusion-culture",
}

def organise_files():
    for filename, subfolder in file_map.items():
        src = SOURCE_DIR / filename
        dest_folder = TARGET_DIR / subfolder
        dest_folder.mkdir(parents=True, exist_ok=True)
        dest = dest_folder / filename

        if src.exists():
            shutil.move(str(src), str(dest))
            print(f"✅ Moved: {filename} → {subfolder}")
        else:
            print(f"⚠️  Missing: {filename}")

if __name__ == "__main__":
    organise_files()