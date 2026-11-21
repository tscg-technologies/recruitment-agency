"""
HTML Site Generator for Recruitment Agency
Generates all 41 complete, semantic, accessible HTML pages.
Clean 4-dropdown header architecture: For Candidates | For Employers | Industries | About Agency
"""
import os
import json

# Abstract Logo SVG
LOGO_SVG = """<svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect width="40" height="40" rx="8" fill="url(#logo_grad)" />
  <circle cx="14" cy="14" r="4" fill="#28A69A" />
  <circle cx="26" cy="14" r="4" fill="#5ED9CB" />
  <circle cx="20" cy="27" r="5" fill="#FFFFFF" />
  <path d="M14 18L18 24M26 18L22 24" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
  <defs>
    <linearGradient id="logo_grad" x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
      <stop stop-color="#0C192A" />
      <stop offset="1" stop-color="#1E3E61" />
    </linearGradient>
  </defs>
</svg>"""

IMAGE_INVENTORY = []

ALT_TEXT_MAP = {
    "hero-recruitment-agency.webp": "Recruitment agency partners consulting with enterprise clients in modern glass office",
    "candidate-interview-session.webp": "Professional one-on-one candidate interview and career advisory discussion",
    "employer-consultation-meeting.webp": "Executive talent acquisition consultation with corporate hiring directors",
    "about-recruitment-agency-team.webp": "Recruitment agency talent acquisition advisory team collaborating in modern office",
    "team-recruitment-consultant.webp": "Senior Recruitment Consultant — Permanent Recruitment Practice",
    "team-talent-acquisition-lead.webp": "Talent Acquisition Lead — Strategic Workforce Solutions",
    "team-it-recruitment-specialist.webp": "IT Recruitment Specialist — Technology Practice",
    "team-healthcare-staffing-coordinator.webp": "Healthcare Staffing Coordinator — Clinical Practice",
    "team-executive-search-partner.webp": "Executive Search Partner — Leadership Appointments",
    "team-staffing-operations-specialist.webp": "Staffing Operations Specialist — Project Workforce",
    "team-candidate-engagement-advisor.webp": "Candidate Engagement Advisor — Talent Relations",
    "team-employer-relations-director.webp": "Employer Relations Director — Corporate Partnerships",
    "recruitment-methodology-framework.webp": "Strategic 5-stage recruitment methodology and talent evaluation framework",
    "recruitment-process-workflow-review.webp": "Candidate and employer recruitment process comparison review",
    "pricing-commercial-models.webp": "Recruitment partnership and commercial engagement models consultation",
    "contact-consultation-hub.webp": "Recruitment agency consultation reception and advisory hub",
    "services-overview-banner.webp": "Comprehensive recruitment and staffing solutions presentation",
    "permanent-recruitment-process.webp": "Permanent recruitment process and long-term talent acquisition interview",
    "contract-staffing-workforce.webp": "Specialized project contractor team collaborating on technical deliverables",
    "temporary-staffing-operations.webp": "Temporary operational workforce coordination and scheduling",
    "executive-search-leadership.webp": "Executive search leadership talent mapping and discrete recruitment",
    "rpo-workforce-solutions.webp": "Enterprise recruitment process outsourcing team managing hiring metrics",
    "bulk-hiring-drive-event.webp": "Structured high-volume bulk recruitment drive and assessment stations",
    "campus-recruitment-graduates.webp": "Campus recruitment workshop and early-career graduate talent engagement",
    "talent-acquisition-strategy-session.webp": "Workforce demand planning and talent acquisition strategy session",
    "industries-overview-banner.webp": "Sector-specific recruitment practice leads in executive strategy meeting",
    "it-recruitment-tech-professionals.webp": "Software engineering and cloud architecture professionals in tech workspace",
    "healthcare-recruitment-medical-staff.webp": "Clinical healthcare practitioners in modern hospital facility",
    "finance-recruitment-analysts.webp": "Financial analysts and audit professionals reviewing financial models",
    "engineering-recruitment-facility.webp": "Civil and mechanical engineers reviewing site blueprints at industrial facility",
    "manufacturing-workforce-operations.webp": "Plant manager and production supervisor reviewing assembly line efficiency",
    "sales-marketing-recruitment-team.webp": "Commercial sales executives and digital marketing specialists strategizing",
    "logistics-recruitment-warehouse.webp": "Supply chain analysts and warehouse operations lead in distribution hub",
    "job-detail-workplace-preview.webp": "Contemporary corporate office workspace and collaborative meeting area",
    "candidate-career-growth-path.webp": "Career transition advisory session between candidate and talent consultant",
    "candidate-cv-registration-hero.webp": "Professional candidate reviewing resume credentials for profile registration",
    "career-advice-resource-center.webp": "Interactive resume optimization and interview preparation masterclass",
    "resources-library-banner.webp": "Recruitment checklists, interview scorecards, and hiring templates desk",
    "careers-agency-culture.webp": "Internal recruitment agency team collaborating in open modern office",
    "employer-talent-solutions-banner.webp": "Corporate HR leaders in strategic workforce roadmap consultation",
    "hire-talent-enquiry-meeting.webp": "Recruitment consultant scoping hiring requisition with client business director",
    "employer-hiring-stages-consulting.webp": "Eight-stage employer recruitment process review and timeline roadmap",
    "case-studies-portfolio-banner.webp": "Recruitment consultant presenting talent acquisition case review analytics",
    "case-study-detail-overview.webp": "Recruitment advisory team conducting post-placement methodology review",
    "insights-editorial-banner.webp": "Editorial recruitment strategy research and labor market trends review",
    "article-detail-recruitment-process.webp": "Talent strategist analyzing structured recruitment workflows and rubrics"
}

def record_image(filename, page, section, description, aspect_ratio, resolution, orientation, prompt, composition, camera_angle, lighting, background, visual_style, color_palette, subject_details, negative_space):
    image_num = f"IMG-{len(IMAGE_INVENTORY) + 1:03d}"
    entry = {
        "num": image_num,
        "filename": filename,
        "page": page,
        "section": section,
        "description": description,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
        "orientation": orientation,
        "prompt": prompt,
        "composition": composition,
        "camera_angle": camera_angle,
        "lighting": lighting,
        "background": background,
        "visual_style": visual_style,
        "color_palette": color_palette,
        "subject_details": subject_details,
        "negative_space": negative_space
    }
    IMAGE_INVENTORY.append(entry)
    return filename

def get_actual_image_file(placeholder_filename):
    """Finds the matching image file in assets/images or images/"""
    base = os.path.splitext(placeholder_filename)[0]
    search_dirs = [os.path.join('assets', 'images'), 'images']
    
    for sdir in search_dirs:
        if not os.path.exists(sdir):
            continue
        files = os.listdir(sdir)
        for ext in ['.jpeg', '.jpg', '.webp.jpg', '.webp', '.png']:
            candidate = base + ext
            if candidate in files:
                return f"assets/images/{candidate}"
        if placeholder_filename in files:
            return f"assets/images/{placeholder_filename}"
    return None

def render_placeholder(filename, aspect_ratio="16/9", meta="1600 × 900 • Landscape"):
    actual_path = get_actual_image_file(filename)
    
    # If the real image file exists, render it beautifully
    if actual_path and os.path.exists(actual_path):
        alt_text = ALT_TEXT_MAP.get(filename, "Recruitment Agency talent acquisition and staffing operations")
        
        # Check if team square portrait
        if aspect_ratio == "1/1":
            return f"""
    <div class="team-img-frame" style="aspect-ratio: 1/1;" data-filename="{filename}">
      <img src="{actual_path}" alt="{alt_text}" width="600" height="600" loading="lazy" decoding="async">
    </div>
    """
        else:
            is_hero = ("hero" in filename and "subpage" not in filename)
            loading_attr = 'loading="eager" fetchpriority="high"' if is_hero else 'loading="lazy"'
            
            # Dimensions based on aspect ratio
            if "1920" in meta or is_hero:
                w, h = 1920, 1080
            elif "4/3" in aspect_ratio or "1200x900" in meta or "1200 × 900" in meta:
                w, h = 1200, 900
            elif "1200x675" in meta or "1200 × 675" in meta:
                w, h = 1200, 675
            else:
                w, h = 1600, 900
                
            return f"""
    <div class="img-frame" style="aspect-ratio: {aspect_ratio};" data-filename="{filename}">
      <img src="{actual_path}" alt="{alt_text}" width="{w}" height="{h}" {loading_attr} decoding="async">
    </div>
    """

    # Fallback to placeholder if file not found
    return f"""
    <div class="img-placeholder" style="aspect-ratio: {aspect_ratio};" data-filename="{filename}">
      <div class="placeholder-inner">
        <svg class="placeholder-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
        <span class="placeholder-badge">IMAGE PLACEHOLDER</span>
        <code class="placeholder-filename">{filename}</code>
        <span class="placeholder-meta">{meta}</span>
      </div>
    </div>
    """

def get_header(active_page=""):
    return f"""
  <!-- Demo Top Bar -->
  <aside class="top-notice-bar" aria-label="Demonstration Notice">
    <div class="container top-notice-inner">
      <div>
        <span class="top-notice-badge">Demonstration Website</span>
        <span>Generic recruitment &amp; talent acquisition prototype. No live ATS or database connection.</span>
      </div>
      <div class="top-notice-contact">
        <a href="tel:0000000000">
          <svg style="width:14px;height:14px;" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 4V3z"/></svg>
          0000000000
        </a>
        <a href="mailto:demo@example.com">
          <svg style="width:14px;height:14px;" fill="currentColor" viewBox="0 0 20 20"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/></svg>
          demo@example.com
        </a>
      </div>
    </div>
  </aside>

  <!-- Site Header -->
  <header class="site-header" role="banner">
    <div class="header-container">
      <a href="index.html" class="site-logo" aria-label="Recruitment Agency Homepage">
        <div class="logo-symbol">
          {LOGO_SVG}
        </div>
        <div class="logo-text-group">
          <span class="logo-text-main">RECRUITMENT AGENCY</span>
          <span class="logo-text-sub">Talent &amp; Staffing Solutions</span>
        </div>
      </a>

      <!-- Primary Desktop Nav: Clean 4-Dropdown Architecture -->
      <nav class="main-nav" aria-label="Primary Navigation">
        <ul class="nav-list">
          <!-- 1. For Candidates Dropdown -->
          <li class="nav-item">
            <a href="candidates.html" class="nav-link {'active' if active_page in ['jobs', 'job-details', 'candidates', 'register-cv', 'career-advice', 'recruitment-process', 'resources'] else ''}">
              For Candidates
              <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </a>
            <div class="nav-dropdown">
              <a href="jobs.html">Search Job Opportunities</a>
              <a href="register-cv.html">Register Your CV Profile</a>
              <a href="candidates.html">Candidate Advisory Hub</a>
              <a href="career-advice.html">Career Advice &amp; Guides</a>
              <a href="recruitment-process.html">Candidate Process Roadmap</a>
              <a href="resources.html">Resume &amp; Interview Templates</a>
              <a href="faq.html">Candidate FAQs</a>
            </div>
          </li>

          <!-- 2. For Employers Dropdown -->
          <li class="nav-item">
            <a href="employers.html" class="nav-link {'active' if active_page in ['employers', 'hire-talent', 'services', 'permanent-recruitment', 'contract-staffing', 'temporary-staffing', 'executive-search', 'recruitment-process-outsourcing', 'bulk-hiring', 'campus-recruitment', 'talent-acquisition', 'employer-process', 'methodology', 'pricing', 'case-studies', 'case-study-details'] else ''}">
              For Employers
              <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </a>
            <div class="nav-dropdown">
              <a href="hire-talent.html">Submit Hiring Requisition</a>
              <a href="employers.html">Employer Hub &amp; Overview</a>
              <a href="services.html">All Recruitment Services</a>
              <a href="employer-process.html">Employer Hiring Process</a>
              <a href="methodology.html">5-Stage Methodology</a>
              <a href="case-studies.html">Case Studies Portfolio</a>
              <a href="pricing.html">Commercial Pricing Models</a>
              <a href="faq.html">Employer FAQs</a>
            </div>
          </li>

          <!-- 3. Industries Dropdown -->
          <li class="nav-item">
            <a href="industries.html" class="nav-link {'active' if active_page in ['industries', 'it-recruitment', 'healthcare-recruitment', 'finance-recruitment', 'engineering-recruitment', 'manufacturing-recruitment', 'sales-marketing-recruitment', 'logistics-recruitment'] else ''}">
              Industries
              <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </a>
            <div class="nav-dropdown">
              <a href="industries.html">All 14 Industry Practices</a>
              <a href="it-recruitment.html">Information Technology</a>
              <a href="healthcare-recruitment.html">Healthcare &amp; Life Sciences</a>
              <a href="finance-recruitment.html">Banking &amp; Financial Services</a>
              <a href="engineering-recruitment.html">Engineering &amp; Infrastructure</a>
              <a href="manufacturing-recruitment.html">Manufacturing &amp; Operations</a>
              <a href="sales-marketing-recruitment.html">Sales &amp; Marketing</a>
              <a href="logistics-recruitment.html">Logistics &amp; Supply Chain</a>
            </div>
          </li>

          <!-- 4. About Agency Dropdown -->
          <li class="nav-item">
            <a href="about.html" class="nav-link {'active' if active_page in ['about', 'team', 'insights', 'article-details', 'careers', 'faq', 'contact'] else ''}">
              About Agency
              <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </a>
            <div class="nav-dropdown">
              <a href="about.html">About the Agency</a>
              <a href="team.html">Our Functional Team</a>
              <a href="insights.html">Insights &amp; Articles</a>
              <a href="resources.html">Resource &amp; Template Library</a>
              <a href="careers.html">Work With Us (Internal)</a>
              <a href="faq.html">Frequently Asked Questions</a>
              <a href="contact.html">Contact Us</a>
            </div>
          </li>
        </ul>
      </nav>

      <!-- Two-Audience Header CTAs -->
      <div class="header-actions">
        <a href="jobs.html" class="btn-candidate-action" aria-label="Search Job Opportunities">
          <svg style="width:16px;height:16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          Find Jobs
        </a>
        <a href="hire-talent.html" class="btn-employer-action" aria-label="Hire Talent for Employers">
          <svg style="width:16px;height:16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
          Hire Talent
        </a>
      </div>

      <!-- Mobile Hamburger Button -->
      <button type="button" class="mobile-nav-toggle" aria-label="Open Navigation Menu" aria-expanded="false">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </header>

  <!-- Mobile Drawer -->
  <div class="mobile-nav-overlay" aria-hidden="true"></div>
  <div class="mobile-nav-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation Drawer">
    <div class="mobile-drawer-header">
      <div class="site-logo">
        <div class="logo-symbol" style="width:32px;height:32px;">
          {LOGO_SVG}
        </div>
        <span class="logo-text-main" style="font-size:0.95rem;">RECRUITMENT AGENCY</span>
      </div>
      <button type="button" class="mobile-drawer-close" aria-label="Close Navigation Menu">&times;</button>
    </div>

    <!-- Candidate Mobile Actions -->
    <div class="mobile-audience-block">
      <div class="mobile-audience-title">For Candidates &amp; Job Seekers</div>
      <a href="jobs.html" class="btn btn-teal btn-sm" style="width:100%;margin-bottom:0.5rem;">Search Job Opportunities</a>
      <a href="register-cv.html" class="btn btn-outline-teal btn-sm" style="width:100%;">Register Your CV</a>
    </div>

    <!-- Employer Mobile Actions -->
    <div class="mobile-audience-block" style="background-color:#EBF1F7;">
      <div class="mobile-audience-title" style="color:var(--color-navy);">For Employers &amp; Hiring Teams</div>
      <a href="hire-talent.html" class="btn btn-primary btn-sm" style="width:100%;margin-bottom:0.5rem;">Submit Hiring Need</a>
      <a href="services.html" class="btn btn-outline-navy btn-sm" style="width:100%;">Browse Services</a>
    </div>

    <nav class="mobile-nav-links" aria-label="Mobile Menu Links">
      <div class="mobile-audience-title" style="margin-top:0.75rem;margin-bottom:0.25rem;">Candidate Section</div>
      <a href="jobs.html">Search Jobs</a>
      <a href="register-cv.html">Register Your CV</a>
      <a href="candidates.html">Candidate Hub</a>
      <a href="career-advice.html">Career Advice &amp; Guides</a>
      <a href="recruitment-process.html">Candidate Journey</a>

      <div class="mobile-audience-title" style="margin-top:1.25rem;margin-bottom:0.25rem;">Employer Section</div>
      <a href="hire-talent.html">Submit Hiring Requisition</a>
      <a href="employers.html">Employer Hub &amp; Overview</a>
      <a href="services.html">All Recruitment Services</a>
      <a href="employer-process.html">Employer Hiring Process</a>
      <a href="methodology.html">5-Stage Methodology</a>
      <a href="pricing.html">Pricing Models</a>
      <a href="case-studies.html">Case Studies</a>

      <div class="mobile-audience-title" style="margin-top:1.25rem;margin-bottom:0.25rem;">Industries &amp; Specializations</div>
      <a href="industries.html">All 14 Industry Practices</a>
      <a href="it-recruitment.html">Information Technology</a>
      <a href="healthcare-recruitment.html">Healthcare</a>
      <a href="finance-recruitment.html">Banking &amp; Finance</a>
      <a href="engineering-recruitment.html">Engineering</a>

      <div class="mobile-audience-title" style="margin-top:1.25rem;margin-bottom:0.25rem;">About &amp; Contact</div>
      <a href="about.html">About the Agency</a>
      <a href="team.html">Our Functional Team</a>
      <a href="insights.html">Insights &amp; Articles</a>
      <a href="resources.html">Resources &amp; Templates</a>
      <a href="careers.html">Work With Us (Careers)</a>
      <a href="faq.html">Frequently Asked Questions</a>
      <a href="contact.html">Contact Us</a>
    </nav>
  </div>
"""

def get_footer():
    return f"""
  <!-- Site Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-top-grid">
        <!-- Col 1: Identity -->
        <div class="footer-col">
          <div class="site-logo" style="margin-bottom:1.25rem;">
            <div class="logo-symbol">
              {LOGO_SVG}
            </div>
            <div class="logo-text-group">
              <span class="logo-text-main" style="color:#FFFFFF;">RECRUITMENT AGENCY</span>
              <span class="logo-text-sub" style="color:#5ED9CB;">Talent &amp; Staffing Solutions</span>
            </div>
          </div>
          <p style="color:#94A3B8;font-size:0.875rem;line-height:1.6;margin-bottom:1.5rem;">
            Connecting ambitious businesses with talented professionals through strategic recruitment, contract staffing, executive search, and workforce solutions.
          </p>
          <div style="font-size:0.75rem;color:#64748B;line-height:1.5;background:rgba(255,255,255,0.04);padding:0.75rem;border-radius:6px;border:1px solid rgba(255,255,255,0.08);">
            Demonstration Website &bull; Generic recruitment prototype for portfolio and presentation purposes.
          </div>
        </div>

        <!-- Col 2: Services -->
        <div class="footer-col">
          <h4>Recruitment Services</h4>
          <ul class="footer-links">
            <li><a href="permanent-recruitment.html">Permanent Recruitment</a></li>
            <li><a href="contract-staffing.html">Contract Staffing</a></li>
            <li><a href="temporary-staffing.html">Temporary Staffing</a></li>
            <li><a href="executive-search.html">Executive Search</a></li>
            <li><a href="bulk-hiring.html">Bulk Hiring Solutions</a></li>
            <li><a href="talent-acquisition.html">Talent Acquisition</a></li>
            <li><a href="campus-recruitment.html">Campus Recruitment</a></li>
            <li><a href="recruitment-process-outsourcing.html">Recruitment Process Outsourcing</a></li>
          </ul>
        </div>

        <!-- Col 3: Candidates -->
        <div class="footer-col">
          <h4>For Candidates</h4>
          <ul class="footer-links">
            <li><a href="jobs.html">Search Job Opportunities</a></li>
            <li><a href="register-cv.html">Register Your CV</a></li>
            <li><a href="career-advice.html">Career Advice &amp; Guides</a></li>
            <li><a href="recruitment-process.html">Candidate Process</a></li>
            <li><a href="resources.html">Resume &amp; Interview Templates</a></li>
            <li><a href="faq.html">Candidate FAQs</a></li>
            <li><a href="careers.html">Internal Agency Careers</a></li>
          </ul>
        </div>

        <!-- Col 4: Employers -->
        <div class="footer-col">
          <h4>For Employers</h4>
          <ul class="footer-links">
            <li><a href="hire-talent.html">Submit a Hiring Requirement</a></li>
            <li><a href="services.html">Explore Solutions</a></li>
            <li><a href="industries.html">Industry Specializations</a></li>
            <li><a href="employer-process.html">Employer Hiring Process</a></li>
            <li><a href="methodology.html">Our 5-Stage Methodology</a></li>
            <li><a href="case-studies.html">Illustrative Case Studies</a></li>
            <li><a href="pricing.html">Pricing Models</a></li>
            <li><a href="faq.html">Employer FAQs</a></li>
          </ul>
        </div>

        <!-- Col 5: Contact -->
        <div class="footer-col">
          <h4>Contact &amp; Location</h4>
          <div class="footer-contact-item">
            <svg fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 4V3z"/></svg>
            <div>
              <a href="tel:0000000000">0000000000</a><br>
              <a href="tel:0000000000">0000000000 (Alternative)</a>
            </div>
          </div>
          <div class="footer-contact-item">
            <svg fill="currentColor" viewBox="0 0 20 20"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"/><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"/></svg>
            <a href="mailto:demo@example.com">demo@example.com</a>
          </div>
          <div class="footer-contact-item">
            <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg>
            <span>Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000</span>
          </div>
          <div class="footer-contact-item">
            <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/></svg>
            <span>Monday–Saturday: 9:00 AM–6:00 PM</span>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom-bar">
        <div>
          &copy; 2026 RECRUITMENT AGENCY. Generic demonstration website. All rights reserved.
        </div>
        <div class="footer-legal-links">
          <a href="about.html">About</a>
          <a href="team.html">Functional Team</a>
          <a href="insights.html">Insights</a>
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-and-conditions.html">Terms &amp; Conditions</a>
          <a href="contact.html">Contact</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Back to Top Button -->
  <button type="button" class="btn-back-to-top" aria-label="Scroll back to top of page">
    <svg style="width:20px;height:20px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/></svg>
  </button>

  <!-- Demo Confirmation Modal Component -->
  <div class="modal-backdrop" id="demo-success-modal" role="dialog" aria-modal="true" aria-labelledby="modal-confirmation-title">
    <div class="modal-dialog">
      <div class="modal-icon success">
        <svg style="width:32px;height:32px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
      </div>
      <h3 class="modal-title" id="modal-confirmation-title">Submission Confirmed (Demo)</h3>
      <div class="modal-body" id="modal-confirmation-msg">
        Thank you for exploring our recruitment agency demonstration. Your input has been validated successfully.
      </div>
      <button type="button" class="btn btn-teal" data-close-modal>Close Window</button>
    </div>
  </div>

  <!-- Reusable Scripts -->
  <script src="assets/js/main.js"></script>
  <script src="assets/js/navigation.js"></script>
  <script src="assets/js/forms.js"></script>
  <script src="assets/js/filters.js"></script>
  <script src="assets/js/job-search.js"></script>
</body>
</html>
"""

def wrap_page(title, meta_desc, active_page, body_content, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | RECRUITMENT AGENCY</title>
  <meta name="description" content="{meta_desc}">
  <meta name="robots" content="index, follow">
  
  <!-- Open Graph -->
  <meta property="og:title" content="{title} | RECRUITMENT AGENCY">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="website">
  
  <!-- CSS Stylesheets -->
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
  <link rel="stylesheet" href="assets/css/animations.css">
  {extra_head}
</head>
<body>
{get_header(active_page)}
<main id="main-content">
{body_content}
</main>
{get_footer()}
"""

print("Base generator framework configured with 4-dropdown header.")
