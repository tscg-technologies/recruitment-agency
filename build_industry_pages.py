"""
Generates Industry Pages (20-27):
20. industries.html
21. it-recruitment.html
22. healthcare-recruitment.html
23. finance-recruitment.html
24. engineering-recruitment.html
25. manufacturing-recruitment.html
26. sales-marketing-recruitment.html
27. logistics-recruitment.html
"""
import os
from builder_core import wrap_page, render_placeholder, record_image

def build_industries():
    # 20. industries.html
    img_ind_overview = record_image(
        filename="industries-overview-banner.webp",
        page="industries.html",
        section="Industries Overview Hero",
        description="Recruitment consultants collaborating with diverse sector specialists in an executive corporate setting.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A panoramic corporate conference table with industry talent acquisition practice leads reviewing sector trend dossiers. Modern glass boardroom overlooking cityscape, natural daylight, sophisticated business attire, authentic non-stock interaction, 35mm lens, sharp focus.",
        composition="Wide balanced corporate meeting scene.",
        camera_angle="Eye-level three-quarter view.",
        lighting="Natural ambient daylight with warm fill.",
        background="Modern glass conference room.",
        visual_style="Clean executive corporate photography.",
        color_palette="Navy, teal, charcoal, white.",
        subject_details="Diverse corporate talent specialists.",
        negative_space="Upper quadrant open."
    )

    all_14_industries = [
        ("Information Technology", "it-recruitment.html", "Software Engineering, Cloud, Cyber, Data Science &amp; IT Ops", "Fast-evolving technical stacks, intense competition for senior engineers, and rigorous technical vetting requirements."),
        ("Healthcare &amp; Life Sciences", "healthcare-recruitment.html", "Doctors, Nurses, Allied Health, Clinical Technologists &amp; Hospital Ops", "Strict statutory credential verification, clinical compliance, and immediate coverage imperatives."),
        ("Banking &amp; Financial Services", "finance-recruitment.html", "Chartered Accountants, Analysts, Risk Officers, Auditors &amp; Controllers", "Stringent regulatory compliance, fiduciary integrity, and deep financial modeling capabilities."),
        ("Engineering &amp; Infrastructure", "engineering-recruitment.html", "Mechanical, Civil, Electrical, Design, Project &amp; Site Engineers", "Complex project lifecycles, site mobility requirements, and specialized CAD/BIM proficiencies."),
        ("Manufacturing &amp; Heavy Industry", "manufacturing-recruitment.html", "Plant Managers, Production Supervisors, QC, Safety &amp; Technicians", "Shift operations management, plant safety standards, and multi-tier floor supervision."),
        ("Sales &amp; Commercial Marketing", "sales-marketing-recruitment.html", "Enterprise B2B Sales, BDMs, Digital Marketers, SEO &amp; Growth Leads", "Demonstrated revenue generation track records, CRM mastery, and pipeline velocity."),
        ("Logistics &amp; Supply Chain", "logistics-recruitment.html", "Supply Chain Planners, Warehouse Leads, Procurement &amp; Transport", "High-efficiency fulfillment benchmarks, multimodal freight logistics, and inventory control."),
        ("Education &amp; Academic Training", "contact.html?subject=Education+Inquiry", "Academic Faculty, Lecturers, Deans, Curriculum Leads &amp; Trainers", "Accredited pedagogical qualifications, research track records, and student engagement acumen."),
        ("Real Estate &amp; Urban Development", "contact.html?subject=Real+Estate+Inquiry", "Project Directors, Real Estate Valuers, Leasing Managers &amp; Site Leads", "Complex land acquisition, regulatory zoning approvals, and commercial leasing acumen."),
        ("Retail &amp; Modern E-Commerce", "contact.html?subject=Retail+Inquiry", "Store Operations Managers, Merchandisers, E-Com Leads &amp; Fulfillment", "Omni-channel customer experience, dynamic inventory turns, and seasonal workforce scale."),
        ("Hospitality &amp; Guest Experience", "contact.html?subject=Hospitality+Inquiry", "Hotel General Managers, Executive Chefs, F&amp;B Leads &amp; Operations", "Exceptional service standards, rapid guest resolution, and multi-shift facility management."),
        ("Construction &amp; Civil Works", "contact.html?subject=Construction+Inquiry", "Contract Managers, Quantity Surveyors, Structural Leads &amp; Inspectors", "Stringent safety regulations, contractor oversight, and milestone deadline adherence."),
        ("Telecommunications &amp; Networks", "contact.html?subject=Telecom+Inquiry", "RF Engineers, Network Architects, Fiber Ops &amp; Telecom PMs", "Rapid 5G / fiber rollout schedules, network uptime SLAs, and specialized infrastructure skills."),
        ("Professional &amp; Advisory Services", "contact.html?subject=ProfServices+Inquiry", "Management Consultants, Legal Advisors, Corporate Strategists &amp; Tax", "High intellectual rigor, client advisory pedigree, and commercial problem solving.")
    ]

    ind_cards_html = ""
    for title, link, roles, challenge in all_14_industries:
        ind_cards_html += f"""
        <div class="industry-card">
          <div class="industry-card-body">
            <div>
              <span class="badge badge-teal" style="margin-bottom:0.75rem;">Industry Practice</span>
              <h3 style="color:var(--color-navy);">{title}</h3>
              <p style="font-size:0.875rem;color:var(--color-text-secondary);margin-bottom:0.75rem;">
                <strong>Typical Roles:</strong> {roles}
              </p>
              <p style="font-size:0.8125rem;color:var(--color-text-muted);margin-bottom:1.25rem;">
                <strong>Key Hiring Challenges:</strong> {challenge}
              </p>
            </div>
            <div>
              <a href="{link}" class="btn btn-sm btn-outline-navy" style="width:100%;">Explore Practice &rarr;</a>
            </div>
          </div>
        </div>
        """

    industries_overview_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Industries</span>
        </nav>
        <h1>Sector-Focused Recruitment Specializations</h1>
        <p class="lead">
          Understanding the technical nuances, market talent benchmarks, and operational pressures distinct to each industry vertical.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Industry Expertise</span>
            <h2 class="section-title">Specialized Practices for Focused Results</h2>
            <p>
              Recruiting in healthcare requires fundamentally different verification protocols than sourcing cloud software engineers or manufacturing plant managers.
            </p>
            <p>
              Our functional practice groups focus on specific industry verticals, allowing our consultants to speak the language of hiring managers and assess candidates with technical insight.
            </p>
          </div>
          <div>
            {render_placeholder(img_ind_overview, "16/9", "1600 × 900 • Industry Specializations")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> Industry sector sections showcase standard functional domains. We do not claim actual commercial client partnerships, specialized statutory certifications, or proprietary candidate databases in this demonstration.
          </p>
        </div>

        <!-- 14 Industry Cards Grid -->
        <div class="industry-grid" style="margin-top:3rem;">
          {ind_cards_html}
        </div>
      </div>
    </section>
    """

    with open("industries.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Industries We Recruit For | Recruitment Agency",
            meta_desc="Explore our specialized recruitment practices across 14 major industries including IT, Healthcare, Finance, Engineering, and Manufacturing.",
            active_page="industries",
            body_content=industries_overview_html
        ))

    # Helper for detailed industry subpages
    def generate_industry_subpage(filename, title, subtitle, img_name, img_desc, prompt, role_categories, assessment_points, disclaimer_text):
        img_id = record_image(
            filename=img_name,
            page=filename,
            section=f"{title} Practice Header",
            description=img_desc,
            aspect_ratio="16/9",
            resolution="1600x900",
            orientation="Landscape",
            prompt=prompt,
            composition="Wide commercial corporate scene.",
            camera_angle="Eye level.",
            lighting="Natural daylight.",
            background="Professional modern workplace environment.",
            visual_style="Clean executive commercial photography.",
            color_palette="Navy, teal, neutral gray, white.",
            subject_details="Industry-specific professionals in authentic workplace.",
            negative_space="Upper quadrant open."
        )

        roles_rendered = "".join([f"""
          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:8px;padding:1.5rem;box-shadow:var(--shadow-sm);">
            <h4 style="font-size:1.15rem;color:var(--color-navy);margin-bottom:0.5rem;">{cat[0]}</h4>
            <p style="font-size:0.875rem;color:var(--color-text-secondary);line-height:1.5;margin-bottom:0.75rem;">{cat[1]}</p>
            <div style="font-size:0.8125rem;color:var(--color-teal);font-weight:600;">Roles: {cat[2]}</div>
          </div>
        """ for cat in role_categories])

        points_rendered = "".join([f"<li style='margin-bottom:0.75rem;display:flex;align-items:flex-start;gap:0.5rem;'><span style='color:var(--color-teal);font-weight:bold;'>✓</span><span>{pt}</span></li>" for pt in assessment_points])

        body_html = f"""
        <section class="subpage-hero" aria-label="Page Title">
          <div class="container">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
              <a href="index.html">Home</a>
              <span class="separator">/</span>
              <a href="industries.html">Industries</a>
              <span class="separator">/</span>
              <span>{title}</span>
            </nav>
            <h1>{title}</h1>
            <p class="lead">{subtitle}</p>
          </div>
        </section>

        <section class="section bg-white">
          <div class="container">
            <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
              <div>
                <span class="section-eyebrow">Industry Practice</span>
                <h2 class="section-title">Targeted Sourcing &amp; Competency Vetting</h2>
                <p style="line-height:1.7;color:var(--color-text-main);margin-bottom:1.5rem;">
                  Our dedicated practice consultants focus exclusively on the specific talent demands, certification standards, and organizational cultures of this sector.
                </p>
                <div style="display:flex;gap:1rem;flex-wrap:wrap;">
                  <a href="hire-talent.html" class="btn btn-primary">Hire in This Sector</a>
                  <a href="jobs.html?industry={title.replace(' ', '+')}" class="btn btn-outline-teal">View Related Jobs</a>
                </div>
              </div>
              <div>
                {render_placeholder(img_id, "16/9", "1600 × 900 • Practice Header")}
              </div>
            </div>

            <div class="demo-alert-banner">
              <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
              <p>
                <strong>Industry Notice:</strong> {disclaimer_text}
              </p>
            </div>

            <!-- Role Categories -->
            <div style="margin-top:4rem;">
              <div class="section-header">
                <span class="section-eyebrow">Specialized Coverage</span>
                <h2 class="section-title">Sector Roles We Regularly Recruit</h2>
              </div>
              <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1.5rem;">
                {roles_rendered}
              </div>
            </div>

            <!-- Evaluation Criteria -->
            <div style="margin-top:4.5rem;background:var(--color-surface-light);padding:2.5rem;border-radius:12px;border:1px solid var(--color-border);">
              <h3 style="font-size:1.4rem;color:var(--color-navy);margin-bottom:1.25rem;">Candidate Skill Assessment &amp; Vetting Framework</h3>
              <ul style="list-style:none;padding:0;margin:0;">
                {points_rendered}
              </ul>
            </div>

            <!-- CTA Box -->
            <div style="margin-top:4.5rem;background:var(--color-navy);color:#FFF;padding:3rem;border-radius:12px;text-align:center;">
              <h3 style="color:#FFF;font-size:2rem;margin-bottom:1rem;">Need Capable Talent in {title}?</h3>
              <p style="color:#CBD5E1;max-width:650px;margin:0 auto 2rem;font-size:1.05rem;line-height:1.6;">
                Submit your hiring requirement or connect directly with our sector practice lead to discuss candidate market availability.
              </p>
              <div style="display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;">
                <a href="hire-talent.html" class="btn btn-teal btn-lg">Submit Requirement</a>
                <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Us</a>
              </div>
            </div>
          </div>
        </section>
        """

        with open(filename, "w", encoding="utf-8") as f:
            f.write(wrap_page(
                title=f"{title} | Recruitment Agency",
                meta_desc=subtitle,
                active_page="industries",
                body_content=body_html
            ))

    # 21. it-recruitment.html
    generate_industry_subpage(
        filename="it-recruitment.html",
        title="Information Technology Recruitment",
        subtitle="Connecting technology enterprises with software engineers, cloud architects, and data specialists.",
        img_name="it-recruitment-tech-professionals.webp",
        img_desc="Software engineering squad reviewing application code architectures and cloud microservices on dual displays in a tech hub.",
        prompt="Commercial corporate photography: A team of software developers and cloud architects collaborating in a modern tech office. Open workspace, clean dual-monitor desks displaying code syntax and infrastructure dashboards, natural light, diverse engineers, 35mm lens, authentic workplace atmosphere.",
        role_categories=[
            ("Software Engineering", "Full stack, frontend, and backend application development.", "Frontend Developers, Backend Developers, Full Stack Developers"),
            ("Data Science & Analytics", "Turning big data into strategic business intelligence.", "Data Analysts, Data Engineers, Data Scientists, BI Developers"),
            ("Cloud & DevOps Infrastructure", "Scalable cloud architectures, CI/CD pipelines, and uptime.", "Cloud Engineers, DevOps Engineers, Site Reliability Engineers (SRE)"),
            ("Cybersecurity & QA", "Protecting digital perimeters and ensuring code excellence.", "Cybersecurity Analysts, Information Security Officers, QA Engineers"),
            ("Product & IT Delivery", "Guiding Agile sprints and technical roadmaps.", "Business Analysts, Technical Project Managers, IT Support Specialists")
        ],
        assessment_points=[
            "Practical architecture review: Evaluating clean code practices, modular scalability, and modern framework competency.",
            "Live problem-solving assessment: Coordinating technical screening discussions around real-world coding problems.",
            "Cloud & infrastructure verification: Reviewing production experience with AWS, Azure, GCP, Docker, and Kubernetes.",
            "Cultural & team communication fit: Assessing adaptability within agile cross-functional teams and sprint cadences."
        ],
        disclaimer_text="We do not claim proprietary verified candidate databases or guaranteed technical placement records in this demonstration."
    )

    # 22. healthcare-recruitment.html
    generate_industry_subpage(
        filename="healthcare-recruitment.html",
        title="Healthcare Recruitment",
        subtitle="Staffing solutions for hospitals, clinical networks, diagnostics centers, and healthcare administration.",
        img_name="healthcare-recruitment-medical-staff.webp",
        img_desc="Clinical healthcare professionals in scrubs and lab coats collaborating in a bright modern medical facility.",
        prompt="Professional corporate medical photography: A clinical consultation in a modern hospital setting. A medical director and lead nurse reviewing patient care workflows on a medical tablet in a clean, state-of-the-art facility. Natural lighting, professional, respectful medical environment, 50mm lens.",
        role_categories=[
            ("Medical Practitioners", "Specialized clinical physicians and general practitioners.", "Consultant Doctors, General Physicians, Medical Officers"),
            ("Nursing & Patient Care", "Registered nursing staff across acute and outpatient settings.", "ICU Nurses, Ward Nurses, Nurse Supervisors, Clinical Coordinators"),
            ("Diagnostics & Laboratory", "Precision clinical pathology and medical imaging.", "Medical Technologists, Lab Technicians, Radiologists, Pharmacists"),
            ("Hospital Administration", "Managing healthcare facilities and operational compliance.", "Healthcare Administrators, Hospital Operations Managers, Quality Leads")
        ],
        assessment_points=[
            "Academic qualification review: Reviewing verified medical degrees, accredited diplomas, and residency completions.",
            "Clinical licensing coordination: Verifying active state or national medical council registration statuses.",
            "Specialized department experience: Assessing critical care, emergency, operating theatre, or pediatric unit tenure.",
            "Patient safety compliance: Verifying background records, patient confidentiality protocols, and statutory standards."
        ],
        disclaimer_text="Professional licensing, state council registrations, and clinical qualifications must be independently verified by the hiring healthcare organization prior to patient-facing duties."
    )

    # 23. finance-recruitment.html
    generate_industry_subpage(
        filename="finance-recruitment.html",
        title="Banking and Finance Recruitment",
        subtitle="Connecting financial institutions and corporate enterprises with accounting, audit, and risk specialists.",
        img_name="finance-recruitment-analysts.webp",
        img_desc="Financial analysts analyzing financial statements and risk forecasting models on multiple monitors in a financial tower.",
        prompt="Corporate photography: Financial analysts and audit specialists reviewing fiscal balance sheets and financial models in a glass high-rise office. Clean financial workspace, laptops and spreadsheets, natural sunlight, sharp focus, 50mm lens.",
        role_categories=[
            ("Accounting & Controllership", "Day-to-day general ledgers, reconciliation, and reporting.", "Accountants, Accounts Executives, Finance Managers, Controllers"),
            ("Financial Planning & Analysis", "Budgeting, commercial forecasting, and variance analytics.", "Financial Analysts, FP&A Managers, Strategic Finance Directors"),
            ("Audit & Taxation", "Statutory compliance, direct/indirect tax, and internal controls.", "Auditors, Tax Professionals, Transfer Pricing Specialists, Payroll Leads"),
            ("Banking & Risk Management", "Commercial lending, credit underwriting, and risk frameworks.", "Banking Professionals, Credit Analysts, Risk Officers, Compliance Leads")
        ],
        assessment_points=[
            "Chartered & professional credentials: Confirming verified CA, CPA, CMA, ACCA, or CFA progress and certifications.",
            "Financial modeling rigor: Evaluating proficiency in complex three-statement financial modeling and forecasting.",
            "Statutory tax compliance: Reviewing deep familiarity with GST, corporate taxation laws, and international audit standards.",
            "Integrity & fiduciary track record: Rigorous reference verification regarding fiscal diligence and ethical conduct."
        ],
        disclaimer_text="Professional credentials and financial certifications must be verified against official issuing registries before final commercial appointment."
    )

    # 24. engineering-recruitment.html
    generate_industry_subpage(
        filename="engineering-recruitment.html",
        title="Engineering Recruitment",
        subtitle="Staffing mechanical, civil, electrical, design, and site engineering professionals for infrastructure projects.",
        img_name="engineering-recruitment-facility.webp",
        img_desc="Civil and mechanical engineers reviewing site blueprints and structural 3D models at an industrial project facility.",
        prompt="Industrial corporate photography: Civil and mechanical engineers in high-visibility vests and protective gear reviewing construction drawings and tablet models at a modern infrastructure facility. Professional, sharp detail, natural ambient light, 35mm lens.",
        role_categories=[
            ("Mechanical & Production", "Machinery design, thermal systems, and automation.", "Mechanical Engineers, Production Engineers, Maintenance Engineers"),
            ("Civil & Structural Infrastructure", "Commercial buildings, highways, and structural engineering.", "Civil Engineers, Structural Engineers, Site Engineers, Quantity Surveyors"),
            ("Electrical & Electronics", "Power distribution, circuit design, and instrumentation.", "Electrical Engineers, Electronics Engineers, Instrumentation Specialists"),
            ("Project & Quality Engineering", "Safety compliance, project timelines, and quality benchmarks.", "Project Engineers, Quality Engineers, Safety & Compliance Officers")
        ],
        assessment_points=[
            "Technical design software proficiency: Verifying hands-on expertise in AutoCAD, SolidWorks, Revit, or STAAD.Pro.",
            "Site execution & project management: Evaluating project delivery milestones, contractor supervision, and safety records.",
            "Codes & standards compliance: Assessing familiarity with relevant national and international engineering codes (IS, ASME, ASTM).",
            "Site mobility and shift readiness: Confirming availability for site deployments, plant operations, and project travel."
        ],
        disclaimer_text="Engineering certifications and site safety authorisations must be independently validated by the hiring employer."
    )

    # 25. manufacturing-recruitment.html
    generate_industry_subpage(
        filename="manufacturing-recruitment.html",
        title="Manufacturing Recruitment",
        subtitle="Workforce solutions for production plants, assembly facilities, quality control, and safety teams.",
        img_name="manufacturing-workforce-operations.webp",
        img_desc="Plant manager and quality supervisors reviewing production metrics on a digital factory dashboard.",
        prompt="Industrial commercial photography: A manufacturing plant manager and floor supervisor reviewing assembly line efficiency metrics on a digital plant monitor. Clean, modern automated factory floor in background, safety eyewear, authentic workplace scene, 50mm lens.",
        role_categories=[
            ("Plant Leadership & Operations", "Overall factory management, P&L, and lean manufacturing.", "Plant Managers, Production Managers, Operations Directors"),
            ("Shop Floor Supervision", "Shift scheduling, operator management, and output tracking.", "Production Supervisors, Line Supervisors, Shift Coordinators"),
            ("Quality Assurance & Testing", "ISO compliance, defect reduction, and calibration.", "Quality Control Professionals, QA Inspectors, Metrology Technicians"),
            ("Plant Maintenance & EHS", "Preventive upkeep, automated tooling, and worker safety.", "Maintenance Technicians, Machine Operators, Safety & EHS Officers")
        ],
        assessment_points=[
            "Lean manufacturing principles: Evaluating practical application of 5S, Kaizen, Six Sigma, and Total Productive Maintenance (TPM).",
            "Plant safety & EHS compliance: Reviewing safety track records, incident reporting protocols, and statutory factory acts.",
            "Shift operation resilience: Assessing capability to lead rotating shifts and handle high-throughput production targets.",
            "Equipment troubleshooting proficiency: Evaluating mechanical, hydraulic, and electrical machinery maintenance capabilities."
        ],
        disclaimer_text="Workforce planning and manufacturing staffing numbers are structured in coordination with individual plant operating guidelines."
    )

    # 26. sales-marketing-recruitment.html
    generate_industry_subpage(
        filename="sales-marketing-recruitment.html",
        title="Sales and Marketing Recruitment",
        subtitle="Connecting commercial enterprises with revenue drivers, growth marketers, and customer relationship leaders.",
        img_name="sales-marketing-recruitment-team.webp",
        img_desc="Sales and digital marketing leads strategizing around customer acquisition funnels in a creative corporate space.",
        prompt="Corporate photography: A commercial sales and digital marketing strategy session. Dynamic professionals analyzing customer journey charts and conversion metrics on a whiteboard in a stylish modern office. Candid, energetic professional discussion, natural lighting, 35mm lens.",
        role_categories=[
            ("B2B Enterprise Sales", "Direct client acquisition, contract negotiations, and quotas.", "Sales Executives, Business Development Managers (BDM), Sales Managers"),
            ("Digital Growth & Acquisition", "Omni-channel campaigns, paid search, SEO, and funnels.", "Digital Marketing Executives, SEO Specialists, Performance Marketers"),
            ("Brand, Content & PR", "Storytelling, corporate communications, and social reach.", "Marketing Managers, Social Media Managers, Content Writers"),
            ("Customer Success & Retention", "Account management, renewals, and client satisfaction.", "Customer Relationship Professionals, Account Managers, Client Success Leads")
        ],
        assessment_points=[
            "Verified sales performance: Evaluating historical quota attainment, average contract sizes, and deal cycle velocity.",
            "Digital attribution & analytics: Reviewing hands-on proficiency in Google Analytics, HubSpot, Salesforce, and SEMrush.",
            "Strategic presentation skills: Assessing commercial pitch acumen, objection handling, and executive communication.",
            "Market segment familiarity: Confirming proven relationships within target enterprise, SMB, or retail customer segments."
        ],
        disclaimer_text="Commercial achievements and sales targets must be validated through authorized professional references."
    )

    # 27. logistics-recruitment.html
    generate_industry_subpage(
        filename="logistics-recruitment.html",
        title="Logistics and Supply Chain Recruitment",
        subtitle="Staffing warehouse managers, procurement specialists, inventory analysts, and freight coordinators.",
        img_name="logistics-recruitment-warehouse.webp",
        img_desc="Supply chain operations director reviewing distribution logistics workflows on a tablet in an organized logistics hub.",
        prompt="Commercial industrial photography: Supply chain analyst and warehouse operations supervisor reviewing shipment tracking diagrams on a tablet inside a clean modern distribution facility. High ceilings, organized inventory racks in soft focus, bright natural lighting, 35mm lens.",
        role_categories=[
            ("Supply Chain Planning", "Demand forecasting, material requirements, and S&OP.", "Supply Chain Analysts, Supply Chain Planners, Demand Forecasters"),
            ("Warehouse Operations", "Facility layout, inventory accuracy, and team leadership.", "Warehouse Managers, Inventory Managers, Warehouse Supervisors"),
            ("Procurement & Sourcing", "Vendor negotiations, contracts, and strategic purchasing.", "Procurement Specialists, Strategic Sourcing Leads, Vendor Coordinators"),
            ("Transport & Fleet Logistics", "Freight routing, multimodal dispatch, and tracking.", "Transport Coordinators, Distribution Managers, Logistics Coordinators")
        ],
        assessment_points=[
            "WMS and ERP expertise: Evaluating operational proficiency in SAP SCM, Oracle NetSuite, Manhattan WMS, or Blue Yonder.",
            "Inventory turnover & accuracy: Reviewing track records in cycle counts, shrink reduction, and order fulfillment SLAs.",
            "Vendor relationship governance: Assessing negotiation skills, vendor scorecards, and cost reduction achievements.",
            "Multimodal transport compliance: Verifying familiarity with domestic road freight, maritime customs, and express logistics."
        ],
        disclaimer_text="Supply chain operational workflows and logistics staffing requirements are structured according to specific distribution SLAs."
    )

    print("Industry pages (20-27) generated successfully.")

if __name__ == "__main__":
    build_industries()
