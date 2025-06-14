import os

folder_structure = {
    "01_Welcome_and_Overview": [
        "Introduction_to_Green_Orbit_Digital",
        "Mission_Vision_Values",
        "Sustainability_Commitment",
        "Company_History_and_Milestones",
        "Leadership_Team_Profiles",
        "Office_Locations_and_Contact_Information",
    ],
    "02_Company_Policies_and_Guidelines": [
        "Code_of_Conduct",
        "Environmental_and_Sustainability_Policy",
        "Remote_Work_and_Hybrid_Guidelines",
        "Data_Privacy_and_Security_Policy",
        "Health_Safety_and_Wellbeing",
        "Diversity_Equity_and_Inclusion",
        "Anti_Harassment_and_Anti_Discrimination_Policy",
    ],
    "03_Employee_Resources": [
        "Onboarding_Guide",
        "Employee_Handbook",
        "Training_and_Development_Opportunities",
        "Green_Orbit_Academy",
        "Career_Progression_Pathways",
        "Feedback_and_Performance_Management",
        "Recognition_and_Rewards",
    ],
    "04_Operational_Information": [
        "Company_Structure_and_Org_Chart",
        "Department_Overviews",
        "Meeting_and_Communication_Norms",
        "Project_Management_Best_Practices",
        "Tools_and_Software_Guides/HubSpot",
        "Tools_and_Software_Guides/Notion",
        "IT_Support_and_Troubleshooting",
    ],
    "05_Marketing_and_Communications": [
        "Brand_Guidelines_and_Resources",
        "Tone_of_Voice_and_Style_Guide",
        "Approved_Templates_and_Assets",
        "Press_Kit_and_Media_Resources",
        "Social_Media_Policies",
        "Blog_and_Content_Strategy",
    ],
    "06_Sustainability_Initiatives": [
        "Space_Sustainability_Leadership_Programme",
        "Space_Integrity_Initiative",
        "Space_Impact_Forum_Details",
        "Case_Studies_on_Sustainable_Projects",
        "Environmental_Impact_Reports",
        "Partner_and_Client_Success_Stories",
    ],
    "07_Projects_and_Partnerships": [
        "Current_and_Past_Projects_Overview",
        "Client_Portfolios",
        "Partnerships_and_Collaborations",
        "Project_Management_Methodologies",
        "Reporting_and_Metrics_Tracking",
    ],
    "08_Sales_and_Business_Development": [
        "Sales_Playbook",
        "CRM_Guidelines/HubSpot",
        "Proposal_and_Pitch_Templates",
        "Competitive_Analysis",
        "Pricing_Models_and_Packages",
        "Business_Development_Strategies",
    ],
    "09_Legal_and_Compliance": [
        "Contract_Templates_and_Clauses",
        "Non_Disclosure_Agreements",
        "Intellectual_Property_Policy",
        "GDPR_and_Data_Compliance",
        "Vendor_Agreements_and_Partnerships",
    ],
    "10_Knowledge_and_Collaboration": [
        "Knowledge_Sharing_Guidelines",
        "Wiki_Contribution_Guide",
        "FAQ_Section",
        "Discussion_Boards_and_Team_Channels",
        "Feedback_and_Suggestions",
    ],
}


def create_folders(base_path, structure):
    for folder, subfolders in structure.items():
        for subfolder in subfolders:
            folder_path = os.path.join(base_path, folder, subfolder)
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created: {folder_path}")


if __name__ == "__main__":
    base_dir = input("Enter the base directory path where the folders should be created: ").strip()
    if not base_dir:
        print("Error: Base directory path cannot be empty.")
    else:
        create_folders(base_dir, folder_structure)
        print("Folder structure creation complete.")