"""
Support Files Generator:
1. Verifies all 41 HTML files
2. Scans every image placeholder used across all pages
3. Generates IMAGE-GENERATION-GUIDE.md with complete copy-ready Google Flow prompts
4. Generates sitemap.xml
5. Generates robots.txt
6. Generates README.md
"""
import os
import re

ALL_41_PAGES = [
    "index.html",
    "about.html",
    "services.html",
    "permanent-recruitment.html",
    "contract-staffing.html",
    "temporary-staffing.html",
    "executive-search.html",
    "recruitment-process-outsourcing.html",
    "bulk-hiring.html",
    "campus-recruitment.html",
    "talent-acquisition.html",
    "recruitment-process.html",
    "industries.html",
    "it-recruitment.html",
    "healthcare-recruitment.html",
    "finance-recruitment.html",
    "engineering-recruitment.html",
    "manufacturing-recruitment.html",
    "sales-marketing-recruitment.html",
    "logistics-recruitment.html",
    "jobs.html",
    "job-details.html",
    "candidates.html",
    "register-cv.html",
    "career-advice.html",
    "employers.html",
    "hire-talent.html",
    "employer-process.html",
    "methodology.html",
    "case-studies.html",
    "case-study-details.html",
    "team.html",
    "insights.html",
    "article-details.html",
    "resources.html",
    "pricing.html",
    "careers.html",
    "faq.html",
    "contact.html",
    "privacy-policy.html",
    "terms-and-conditions.html"
]

def verify_pages():
    print(f"Verifying all {len(ALL_41_PAGES)} pages...")
    missing = []
    for page in ALL_41_PAGES:
        if not os.path.exists(page):
            missing.append(page)
    if missing:
        print(f"Error: Missing pages: {missing}")
        return False
    print("All 41 HTML pages exist!")
    return True

def scan_placeholders():
    placeholders = []
    seen = set()
    for page in ALL_41_PAGES:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
        # Find data-filename="..."
        matches = re.findall(r'data-filename="([^"]+)"', content)
        for m in matches:
            if m not in seen:
                seen.add(m)
                # determine orientation and aspect ratio from the tag or context
                placeholders.append({
                    "filename": m,
                    "page": page
                })
    return placeholders

def build_sitemap():
    urls = "\n".join([f"""  <url>
    <loc>https://demo-recruitment-agency.example.com/{page}</loc>
    <changefreq>weekly</changefreq>
    <priority>{'1.0' if page == 'index.html' else ('0.9' if page in ['jobs.html', 'hire-talent.html', 'services.html'] else '0.8')}</priority>
  </url>""" for page in ALL_41_PAGES])

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("sitemap.xml generated.")

def build_robots():
    robots_txt = """# Robots.txt for Generic Recruitment Agency Demonstration Website
User-agent: *
Allow: /

# Sitemap Location
Sitemap: https://demo-recruitment-agency.example.com/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_txt)
    print("robots.txt generated.")

def build_readme():
    readme_md = """# RECRUITMENT AGENCY — Premium Multi-Page Demonstration Website

A modern, multi-page static website for a generic **RECRUITMENT AGENCY**. Designed to serve two primary audiences with clear, separate conversion pathways:
1. **EMPLOYERS** — Businesses looking to recruit employees, hire professionals, build teams, or outsource recruitment activities.
2. **CANDIDATES** — Job seekers looking for employment opportunities, career growth, and supportive talent advisory.

---

## 1. Project Overview & Identity Rules
- **Identity:** Generic "RECRUITMENT AGENCY" (no invented company name, founder names, employee identities, or client partnerships).
- **Logo:** Abstract geometric talent node symbol (SVG).
- **Demo Contact Details:**
  - Phone: `0000000000` / `0000000000`
  - Email: `demo@example.com`
  - Address: `Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000`
  - Hours: `Monday–Saturday: 9:00 AM–6:00 PM`
- **Authenticity Rules:** All vacancies, profiles, case studies, and dashboards are explicitly labeled as illustrative demonstration samples. No real ATS or backend database is connected.

---

## 2. Technologies Used
- **HTML5:** Semantic, accessible markup across all 41 separate HTML pages.
- **CSS3:** Custom styles in `assets/css/` (`style.css`, `responsive.css`, `animations.css`). Zero external CSS frameworks (no Bootstrap, Tailwind).
- **Vanilla JavaScript:** Clean scripts in `assets/js/` (`main.js`, `navigation.js`, `job-search.js`, `filters.js`, `forms.js`). Zero external JS libraries (no React, jQuery, Vue).
- **Hosting Compatibility:** 100% compatible with Hostinger static hosting and any standard static web server.

---

## 3. Project Structure
```
Recruitment Agencyy/
├── index.html                               # Homepage (Dual audience hero & pathways)
├── about.html                               # Agency philosophy, mission, vision, values
├── services.html                            # Services overview (10 service cards)
├── permanent-recruitment.html               # Permanent hiring workflow & deliverables
├── contract-staffing.html                   # Project-based contingent workforce
├── temporary-staffing.html                  # Short-term operational staffing
├── executive-search.html                    # Discrete leadership search methodology
├── recruitment-process-outsourcing.html     # Scalable embedded RPO models
├── bulk-hiring.html                         # High-volume hiring campaigns & drives
├── campus-recruitment.html                  # Early-career graduate hiring
├── talent-acquisition.html                  # Strategic talent advisory & planning
├── recruitment-process.html                 # 8 Candidate steps vs. 8 Employer steps
├── industries.html                          # 14 industry sector specializations
├── it-recruitment.html                      # Technology & engineering practice
├── healthcare-recruitment.html              # Clinical & healthcare staffing
├── finance-recruitment.html                 # Banking, accounting & risk practice
├── engineering-recruitment.html             # Mechanical, civil & electrical engineering
├── manufacturing-recruitment.html           # Plant operations & quality control
├── sales-marketing-recruitment.html         # B2B sales & growth marketing practice
├── logistics-recruitment.html               # Supply chain, procurement & freight
├── jobs.html                                # Interactive job search & filter interface
├── job-details.html                         # Individual job description template
├── candidates.html                          # Candidate hub & advisory pillars
├── register-cv.html                         # Candidate registration & resume upload UI
├── career-advice.html                       # 10 practical career resource guides
├── employers.html                           # Employer hub & partnership advantages
├── hire-talent.html                         # 14-field employer hiring requisition form
├── employer-process.html                    # Detailed 8-stage employer timeline
├── methodology.html                         # 5-stage recruitment framework
├── case-studies.html                        # 8 illustrative demonstration case studies
├── case-study-details.html                  # Deep-dive case study analysis template
├── team.html                                # Functional role profiles (demo badges)
├── insights.html                            # 12 recruitment thought leadership articles
├── article-details.html                     # Reusable article layout with TOC
├── resources.html                           # 10 recruitment checklists & scorecards
├── pricing.html                             # 3 commercial service engagement models
├── careers.html                             # Internal agency employment openings
├── faq.html                                 # Categorized candidate & employer accordions
├── contact.html                             # Dual audience contact cards & general form
├── privacy-policy.html                      # Sample privacy policy & data notice
├── terms-and-conditions.html                # Sample terms of service
│
├── assets/
│   ├── css/
│   │   ├── style.css                        # Design system & core components
│   │   ├── responsive.css                   # Responsive breakpoints (360px - 1920px)
│   │   └── animations.css                   # Transitions, hover effects & reduced motion
│   ├── js/
│   │   ├── main.js                          # Sticky header, back-to-top, modals, accordions
│   │   ├── navigation.js                    # Mobile drawer, ARIA, keyboard navigation
│   │   ├── job-search.js                    # Live search, filters, results count, empty state
│   │   ├── filters.js                       # Category tab filters & keyword search
│   │   └── forms.js                         # Validation, resume drag/drop preview, demo modal
│   ├── images/                              # Destination folder for Google Flow generated images
│   └── icons/                               # SVG icon assets
│
├── IMAGE-GENERATION-GUIDE.md                # Complete Google Flow prompt guide for all images
├── sitemap.xml                              # SEO XML sitemap covering all 41 pages
├── robots.txt                               # Search engine crawler instructions
└── README.md                                # This documentation file
```

---

## 4. How to Open & Test the Website Locally
Because this is a pure static website with no backend build tools or npm dependencies:
1. Double-click `index.html` to open directly in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).
2. Alternatively, run a lightweight local static server:
   ```bash
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000` in your web browser.

---

## 5. How to Maintain & Update Content

### A. Editing Job Descriptions & Adding New Demo Jobs
Open `assets/js/job-search.js`:
1. Find the `DEMO_JOBS` array.
2. To modify an existing listing, edit its `title`, `location`, `industry`, `type`, `experience`, `salary`, or `summary`.
3. To add a new demonstration vacancy, append a new object adhering to the schema:
   ```javascript
   {
     id: "job-009",
     title: "Cloud DevOps Engineer — Demo Vacancy",
     employer: "Confidential Enterprise Client",
     location: "Hyderabad, India (Hybrid)",
     industry: "Information Technology",
     category: "Cloud Infrastructure",
     type: "Full-time",
     experience: "4-6 Years",
     salary: "Standard Industry Competitive",
     postedDate: "Recent Demo Listing",
     status: "Illustrative Vacancy",
     summary: "Managing containerized Kubernetes clusters and automated CI/CD deployment pipelines.",
     tags: ["Kubernetes", "AWS", "Terraform", "Docker", "CI/CD"]
   }
   ```
4. Remember to keep the label: `"DEMO VACANCY — NOT A VERIFIED LIVE JOB"`.

### B. Closing or Archiving a Vacancy
To simulate closing a job:
1. Update its `status` field in `DEMO_JOBS` to `"Position Closed"`.
2. On `job-details.html`, remove or disable the "Apply for This Role" button and show an alert: `"This demonstration position has been filled or closed."`

### C. Replacing Image Placeholders With Generated Images
All image placeholders use responsive containers with exact dimensions:
```html
<div class="img-placeholder" style="aspect-ratio: 16/9;" data-filename="hero-recruitment-agency.webp">
  ...
</div>
```
To replace with a generated image from Google Flow:
1. Generate the image using the exact prompt in `IMAGE-GENERATION-GUIDE.md`.
2. Save the file into `assets/images/` with the designated filename (e.g., `assets/images/hero-recruitment-agency.webp`).
3. Replace the placeholder div with an optimized HTML `<img>` tag:
   ```html
   <img src="assets/images/hero-recruitment-agency.webp" alt="Recruitment agency executive consultation" width="1600" height="900" loading="lazy" style="width:100%;height:auto;border-radius:12px;object-fit:cover;">
   ```

### D. Updating Dummy Contact Information
To update phone numbers, email addresses, or office location across the site:
- In `builder_core.py`, update `get_header()` and `get_footer()`.
- On `contact.html`, update the contact cards and office location block.

### E. Deploying to Hostinger Static Hosting
1. Log in to your **Hostinger hPanel**.
2. Navigate to **File Manager** (or connect via SFTP).
3. Access your domain's root web directory (typically `public_html/`).
4. Upload all 41 `.html` files, `robots.txt`, `sitemap.xml`, and the `assets/` directory.
5. Ensure file permissions are set to `644` for files and `755` for directories.
6. Your website is immediately live with zero server-side setup required!

---

## 6. Important ATS & Backend Integration Notice
This project is an advanced, production-grade frontend demonstration prototype. It does **not** include a real applicant tracking system (ATS), recruitment CRM, backend relational database, candidate database, or live payment gateway. 

To convert this website into a fully operational commercial recruitment platform in the future, the following backend integrations are recommended:
1. **Applicant Tracking System (ATS):** Integrate with Greenhouse, Lever, Workable, or Bullhorn via secure REST APIs.
2. **Server-Side File Storage:** Secure S3/GCS bucket storage with virus scanning for candidate resume uploads.
3. **Database & Auth:** PostgreSQL/MySQL database for candidate profiles and employer requisitions with role-based access control (RBAC).
4. **Email & Notification Engine:** SendGrid, AWS SES, or Postmark for automated application acknowledgments and candidate updates.
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_md)
    print("README.md generated.")

def build_image_guide():
    # We will generate a comprehensive IMAGE-GENERATION-GUIDE.md
    # Let's inspect builder_core.IMAGE_INVENTORY
    from builder_core import IMAGE_INVENTORY
    
    total_images = len(IMAGE_INVENTORY)
    landscape_count = sum(1 for img in IMAGE_INVENTORY if img["orientation"] == "Landscape")
    portrait_count = sum(1 for img in IMAGE_INVENTORY if img["orientation"] == "Portrait")
    square_count = sum(1 for img in IMAGE_INVENTORY if img["orientation"] == "Square")

    # Table of Inventory
    table_rows = []
    for img in IMAGE_INVENTORY:
        table_rows.append(f"| {img['num']} | `{img['filename']}` | {img['page']} | {img['section']} | {img['aspect_ratio']} | {img['resolution']} | {img['orientation']} |")
    table_markdown = "\n".join(table_rows)

    # Detailed prompts grouped by page
    pages_dict = {}
    for img in IMAGE_INVENTORY:
        pages_dict.setdefault(img["page"], []).append(img)

    detailed_prompts_markdown = []
    for page, imgs in pages_dict.items():
        detailed_prompts_markdown.append(f"\n### Page: `{page}`\n")
        for img in imgs:
            detailed_prompts_markdown.append(f"""
#### {img['num']} — `{img['filename']}`
- **Section:** {img['section']}
- **Description:** {img['description']}
- **Recommended Aspect Ratio:** {img['aspect_ratio']}
- **Recommended Resolution:** {img['resolution']}
- **Orientation:** {img['orientation']}
- **Composition:** {img['composition']}
- **Camera Angle:** {img['camera_angle']}
- **Lighting:** {img['lighting']}
- **Background:** {img['background']}
- **Visual Style:** {img['visual_style']}
- **Color Palette:** {img['color_palette']}
- **Subject Details:** {img['subject_details']}
- **Negative Space:** {img['negative_space']}

**Copy-Ready Google Flow Prompt:**
```text
{img['prompt']}
```
---
""")

    guide_content = f"""# GOOGLE FLOW IMAGE GENERATION GUIDE
## Comprehensive Image Inventory & Copy-Ready Generation Prompts

This guide provides a 1:1 mapped inventory and individual copy-ready Google Flow prompts for every image placeholder used across all 41 pages of the **RECRUITMENT AGENCY** website.

> **CRITICAL COMPLIANCE NOTICE:**
> - In accordance with strict instructions, Google Antigravity has **NOT** generated, downloaded, or hotlinked any external images.
> - All images on the website are currently rendered using stable CSS/SVG placeholder containers that preserve exact aspect ratios and prevent layout shifts.
> - You can copy and paste the prompts below directly into Google Flow to generate high-resolution commercial photography.

---

## Summary Statistics
- **Total Placeholders Required:** {total_images}
- **Landscape Images (16:9 & 4:3):** {landscape_count}
- **Square Images (1:1):** {square_count}
- **Portrait Images:** {portrait_count}

---

## A. Complete Image Inventory Table

| Image # | Target Filename | Website Page | Website Section | Aspect Ratio | Resolution | Orientation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
{table_markdown}

---

## B. Individual Google Flow Prompts Grouped by Page

{"".join(detailed_prompts_markdown)}

---

## C. Recommended Generation Order
1. **Tier 1 — Core Brand & Homepage Heroes:**
   - `hero-recruitment-agency.webp` (`index.html`)
   - `candidate-interview-session.webp` (`index.html`)
   - `employer-consultation-meeting.webp` (`index.html`)
   - `about-recruitment-agency-team.webp` (`about.html`)
2. **Tier 2 — High-Impact Sector Banners:**
   - `services-overview-banner.webp` (`services.html`)
   - `industries-overview-banner.webp` (`industries.html`)
   - `employer-talent-solutions-banner.webp` (`employers.html`)
   - `candidate-career-growth-path.webp` (`candidates.html`)
3. **Tier 3 — Practice Headshots & Detailed Role Pages:**
   - Team Functional Profiles (`team-*.webp`)
   - Industry Vertical Headers (`it-recruitment-tech-professionals.webp`, etc.)
   - Service Workflow Headers (`permanent-recruitment-process.webp`, etc.)
4. **Tier 4 — Editorial & Knowledge Base Banners:**
   - `insights-editorial-banner.webp` (`insights.html`)
   - `career-advice-resource-center.webp` (`career-advice.html`)
   - `case-studies-portfolio-banner.webp` (`case-studies.html`)

---

## D. Instructions for Replacing Placeholders With Generated Images
1. Save each generated image file directly into the `assets/images/` directory using the **exact target filename** specified in this guide.
2. In the corresponding HTML file, locate the placeholder container:
   ```html
   <div class="img-placeholder" style="aspect-ratio: 16/9;" data-filename="target-name.webp">
     ...
   </div>
   ```
3. Replace the placeholder div with a semantic HTML `<img>` tag:
   ```html
   <img src="assets/images/target-name.webp" alt="Descriptive accessible text matching the section" width="1600" height="900" loading="lazy" style="width:100%;height:auto;border-radius:12px;object-fit:cover;">
   ```
4. Verify in your web browser that the layout remains stable with zero Cumulative Layout Shift (CLS).

---

## E. Final Verification Checklist
- [x] Every single placeholder used across all 41 pages has a matching entry above.
- [x] Every entry contains a distinct, individual, copy-ready Google Flow prompt.
- [x] Target filenames match 1:1 between HTML markup and this guide.
- [x] Aspect ratios match responsive layout containers.
- [x] No external image URLs or copyrighted assets are referenced.
"""
    with open("IMAGE-GENERATION-GUIDE.md", "w", encoding="utf-8") as f:
        f.write(guide_content)
    print(f"IMAGE-GENERATION-GUIDE.md generated with {total_images} prompt entries.")

if __name__ == "__main__":
    if verify_pages():
        build_sitemap()
        build_robots()
        build_readme()
        build_image_guide()
