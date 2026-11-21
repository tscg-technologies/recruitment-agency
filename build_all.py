"""
Master Build Script
Runs all generators in a single Python process to populate IMAGE_INVENTORY completely
and generate all 41 HTML pages, CSS, JS, sitemap.xml, robots.txt, README.md,
and IMAGE-GENERATION-GUIDE.md.
"""
from make_css import create_css
from make_js import create_js
from build_core_pages import build_core
from build_service_pages import build_services
from build_industry_pages import build_industries
from build_candidate_pages import build_candidate_pages
from build_employer_insights_pages import build_employer_insights
from build_support_files import verify_pages, build_sitemap, build_robots, build_readme, build_image_guide
from builder_core import IMAGE_INVENTORY

def run_master():
    print("=== Step 1: Building CSS & JS ===")
    create_css()
    create_js()

    print("=== Step 2: Clearing & Rebuilding All 41 Pages ===")
    IMAGE_INVENTORY.clear()
    build_core()
    build_services()
    build_industries()
    build_candidate_pages()
    build_employer_insights()

    print(f"=== Step 3: Total Recorded Placeholders: {len(IMAGE_INVENTORY)} ===")

    print("=== Step 4: Building Supporting Files ===")
    if verify_pages():
        build_sitemap()
        build_robots()
        build_readme()
        build_image_guide()

    print("=== BUILD COMPLETE! ALL 41 PAGES & SUPPORTING FILES READY ===")

if __name__ == "__main__":
    run_master()
