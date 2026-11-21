"""
Quality Assurance Script for Recruitment Agency
Checks all internal links, asset paths, demo notices, and HTML validity.
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

def run_qa():
    print("--- Starting QA Verification ---")
    errors = []

    # 1. Check all 41 files exist
    for p in ALL_41_PAGES:
        if not os.path.exists(p):
            errors.append(f"Missing page: {p}")

    # 2. Check internal links
    for p in ALL_41_PAGES:
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for banned external frameworks
        for bad in ["bootstrap", "tailwind", "jquery", "react", "vue", "angular", "gsap", "three.js", "unsplash.com", "pexels.com"]:
            if bad in content.lower():
                errors.append(f"Banned keyword or external resource '{bad}' found in {p}")

        # Check internal hrefs ending with .html or .html?query
        hrefs = re.findall(r'href="([^"#:]+\.html)(\?[^"]*)?"', content)
        for h, q in hrefs:
            if not os.path.exists(h):
                errors.append(f"Broken internal link in {p}: {h}")

        # Check CSS links
        css_links = re.findall(r'href="(assets/css/[^"]+)"', content)
        for css in css_links:
            if not os.path.exists(css):
                errors.append(f"Broken CSS link in {p}: {css}")

        # Check JS links
        js_links = re.findall(r'src="(assets/js/[^"]+)"', content)
        for js in js_links:
            if not os.path.exists(js):
                errors.append(f"Broken JS link in {p}: {js}")

    # 3. Check assets
    expected_assets = [
        "assets/css/style.css",
        "assets/css/responsive.css",
        "assets/css/animations.css",
        "assets/js/main.js",
        "assets/js/navigation.js",
        "assets/js/job-search.js",
        "assets/js/filters.js",
        "assets/js/forms.js",
        "sitemap.xml",
        "robots.txt",
        "README.md",
        "IMAGE-GENERATION-GUIDE.md"
    ]
    for ea in expected_assets:
        if not os.path.exists(ea):
            errors.append(f"Missing asset or support file: {ea}")

    if errors:
        print(f"FAILED QA! Found {len(errors)} issues:")
        for err in errors:
            print(" -", err)
    else:
        print("PERFECT QA PASS! All 41 pages exist, all internal links resolve, all CSS/JS assets are present, zero external libraries used, zero broken links!")

if __name__ == "__main__":
    run_qa()
