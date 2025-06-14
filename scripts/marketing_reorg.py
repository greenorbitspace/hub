import os
import shutil

BASE_DIR = "marketing-communications"

# Define folder structure
folders = [
    "brand/branding",
    "brand/messaging",
    "brand/assets",
    "brand/ethics",
    "brand/compliance",

    "campaigns/ads",
    "campaigns/campaigns",
    "campaigns/email",
    "campaigns/newsletter",
    "campaigns/social",
    "campaigns/podcasts",
    "campaigns/events",
    "campaigns/ecommerce",
    "campaigns/pitches",

    "content/content",
    "content/guides",
    "content/research",
    "content/press",

    "planning/audit",
    "planning/programmes",
    "planning/plans",
    "planning/strategy",
    "planning/sustainability",

    "engagement/client-engagement",
    "engagement/customer-experience",
    "engagement/crm",

    "operations/technology",
    "operations/sops",
    "operations/procedures",

    "seo",
]

# Keywords to folder mapping for moving files
keyword_map = {
    # brand
    "branding": "brand/branding",
    "messaging": "brand/messaging",
    "asset": "brand/assets",
    "assets": "brand/assets",
    "ethics": "brand/ethics",
    "compliance": "brand/compliance",

    # campaigns
    "ads": "campaigns/ads",
    "campaign": "campaigns/campaigns",
    "email": "campaigns/email",
    "newsletter": "campaigns/newsletter",
    "social": "campaigns/social",
    "podcast": "campaigns/podcasts",
    "event": "campaigns/events",
    "ecommerce": "campaigns/ecommerce",
    "pitch": "campaigns/pitches",

    # content
    "guide": "content/guides",
    "research": "content/research",
    "press": "content/press",
    "content": "content/content",

    # planning
    "audit": "planning/audit",
    "programme": "planning/programmes",
    "plan": "planning/plans",
    "strategy": "planning/strategy",
    "sustainability": "planning/sustainability",

    # engagement
    "client-engagement": "engagement/client-engagement",
    "customer-experience": "engagement/customer-experience",
    "crm": "engagement/crm",

    # operations
    "technology": "operations/technology",
    "sop": "operations/sops",
    "procedure": "operations/procedures",

    # seo
    "seo": "seo",
}

def ensure_directories():
    for folder in folders:
        path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created folder: {path}")

def move_files():
    # List only files at top level of BASE_DIR
    items = [f for f in os.listdir(BASE_DIR) if os.path.isfile(os.path.join(BASE_DIR, f))]
    
    for filename in items:
        # Skip hidden or system files
        if filename.startswith('.'):
            continue
        
        src_path = os.path.join(BASE_DIR, filename)
        dest_folder = None
        
        # Find folder based on keyword matching in filename (case-insensitive)
        for keyword, folder in keyword_map.items():
            if keyword.lower() in filename.lower():
                dest_folder = folder
                break
        
        # Default fallback: move to content/content if no keyword matched
        if not dest_folder:
            dest_folder = "content/content"
        
        dest_path = os.path.join(BASE_DIR, dest_folder, filename)
        
        print(f"Moving '{filename}' to '{dest_folder}/'")
        shutil.move(src_path, dest_path)

def main():
    ensure_directories()
    move_files()
    print("\nReorganization complete.")

if __name__ == "__main__":
    main()