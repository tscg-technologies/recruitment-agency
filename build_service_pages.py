"""
Generates Service Pages (11-19):
11. services.html
12. permanent-recruitment.html
13. contract-staffing.html
14. temporary-staffing.html
15. executive-search.html
16. recruitment-process-outsourcing.html
17. bulk-hiring.html
18. campus-recruitment.html
19. talent-acquisition.html
"""
import os
from builder_core import wrap_page, render_placeholder, record_image

def build_services():
    # 11. services.html
    img_services_hero = record_image(
        filename="services-overview-banner.webp",
        page="services.html",
        section="Services Hero Banner",
        description="A dynamic corporate meeting room where recruitment consultants present multi-tiered talent acquisition solutions to client leadership.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A modern talent acquisition consulting briefing. Agency specialists presenting staffing framework solutions on digital screens to a corporate hiring committee in an architectural conference room. Deep navy, teal, warm ambient light, 35mm lens, sharp natural focus, authentic business atmosphere.",
        composition="Wide balanced corporate meeting scene.",
        camera_angle="Eye-level three-quarter view.",
        lighting="Natural ambient daylight with warm fill.",
        background="Modern glass conference room.",
        visual_style="Clean executive corporate photography.",
        color_palette="Navy (#14263D), teal (#28A69A), white, charcoal.",
        subject_details="Professional consultants and corporate hiring committee.",
        negative_space="Upper area with subtle depth."
    )

    services_overview_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Services</span>
        </nav>
        <h1>Recruitment and Staffing Solutions for Every Hiring Need</h1>
        <p class="lead">
          Strategic, flexible, and structured talent acquisition models designed to address permanent, contract, executive, and volume workforce requirements.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Enterprise Capabilities</span>
            <h2 class="section-title">End-to-End Talent Acquisition</h2>
            <p>
              Whether your organization is seeking a single C-suite executive, ramping up specialized engineering contractors, or establishing an outsourced hiring funnel, our recruitment solutions provide predictability, technical rigor, and dedicated consultant partnership.
            </p>
            <p>
              Each service model is backed by thorough role profiling, active candidate qualification, and structured coordination through offer acceptance and onboarding.
            </p>
          </div>
          <div>
            {render_placeholder(img_services_hero, "16/9", "1600 × 900 • Services Overview Banner")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Service Notice:</strong> All recruitment solutions are delivered through agreed service agreements. This prototype demonstrates capabilities and typical workflows without asserting active commercial client relationships.
          </p>
        </div>

        <!-- 10 Service Cards Grid -->
        <div class="service-grid" style="margin-top:3rem;">
          <!-- 1. Permanent Recruitment -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
              </div>
              <h3>Permanent Recruitment</h3>
              <p>Identify and secure full-time professionals who align with your organizational culture, technical benchmarks, and long-term goals.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Long-term capacity expansion</li>
                  <li>Core departmental leadership</li>
                  <li>Deep cultural alignment</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="permanent-recruitment.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 2. Contract Staffing -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              </div>
              <h3>Contract Staffing</h3>
              <p>Flexible contractor talent deployment for fixed-duration initiatives, seasonal surges, or specialized technical mandates.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Project-specific technical capabilities</li>
                  <li>Budget and headcount flexibility</li>
                  <li>Rapid resource deployment</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="contract-staffing.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 3. Temporary Staffing -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
              </div>
              <h3>Temporary Staffing</h3>
              <p>Short-term personnel solutions ensuring continuous operations during leaves, seasonal peak loads, or sudden operational shifts.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Immediate interim coverage</li>
                  <li>Peak season operations support</li>
                  <li>Continuity in critical operations</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="temporary-staffing.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 4. Executive Search -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
              </div>
              <h3>Executive Search</h3>
              <p>Discreet, confidential search engagements targeting board directors, C-level officers, and high-impact functional heads.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Mission-critical leadership appointments</li>
                  <li>Strict non-disclosure confidentiality</li>
                  <li>Executive competency mapping</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="executive-search.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 5. Recruitment Process Outsourcing (RPO) -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
              </div>
              <h3>Recruitment Process Outsourcing</h3>
              <p>Transfer of all or part of your recruitment operations to our specialized team to streamline hiring funnels and optimize costs.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Standardized hiring governance</li>
                  <li>Reduced cost-per-hire metrics</li>
                  <li>Scalable recruiter capacity</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="recruitment-process-outsourcing.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 6. Bulk Hiring -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
              </div>
              <h3>Bulk Hiring Solutions</h3>
              <p>High-volume recruitment campaigns and multi-city hiring drives structured for facility launches, expansions, and call centers.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Large headcount quotas on tight timelines</li>
                  <li>Batched screening and interview drives</li>
                  <li>Unified candidate assessment funnels</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="bulk-hiring.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 7. Campus Recruitment -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 14l9-5-9-5-9 5 9 5z"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"/></svg>
              </div>
              <h3>Campus Recruitment</h3>
              <p>Structured graduate acquisition programs connecting growing enterprises with promising early-career talent and academic institutions.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Fresh graduate talent pipelines</li>
                  <li>Standardized entry-level assessment</li>
                  <li>Campus interview drive logistics</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="campus-recruitment.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 8. Talent Acquisition -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
              </div>
              <h3>Talent Acquisition Strategy</h3>
              <p>Strategic workforce planning, employer branding guidance, talent pipeline design, and recruitment analytics consulting.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Future talent demand modeling</li>
                  <li>Employer value proposition (EVP)</li>
                  <li>Sourcing analytics &amp; KPI audits</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="talent-acquisition.html" class="btn btn-outline-navy btn-sm">Learn More &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 9. Specialist Recruitment -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
              </div>
              <h3>Specialist Domain Recruitment</h3>
              <p>Deep-domain talent sourcing for certified professions in clinical healthcare, advanced engineering, and compliance banking.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Rare technical skill set sourcing</li>
                  <li>Regulatory qualification checks</li>
                  <li>Peer-level candidate discussions</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="industries.html" class="btn btn-outline-navy btn-sm">Explore Industries &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>

          <!-- 10. Recruitment Process Consulting -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>
              </div>
              <h3>Recruitment Process Consulting</h3>
              <p>Auditing and upgrading internal hiring workflows, interview rubric design, and candidate experience optimization.</p>
              <div class="service-deliverables">
                <h5>Employer Needs Addressed</h5>
                <ul>
                  <li>Interview rubric standardization</li>
                  <li>Candidate drop-off diagnosis</li>
                  <li>Time-to-offer optimization</li>
                </ul>
              </div>
            </div>
            <div style="display:flex;gap:0.5rem;flex-direction:column;">
              <a href="methodology.html" class="btn btn-outline-navy btn-sm">View Methodology &rarr;</a>
              <a href="hire-talent.html" class="btn btn-primary btn-sm">Submit Hiring Requirement</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    with open("services.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Recruitment Services | Permanent, Contract & Executive Solutions",
            meta_desc="Explore our 10 recruitment and staffing solutions: permanent hiring, contract staffing, executive search, bulk recruitment, and RPO.",
            active_page="services",
            body_content=services_overview_html
        ))

    # Helper function for individual service pages
    def generate_service_subpage(filename, title, eyebrow, subtitle, img_name, img_desc, prompt, deliverables_list, workflow_steps, disclaimer_text):
        img_id = record_image(
            filename=img_name,
            page=filename,
            section=f"{title} Hero Banner",
            description=img_desc,
            aspect_ratio="16/9",
            resolution="1600x900",
            orientation="Landscape",
            prompt=prompt,
            composition="Wide commercial corporate scene.",
            camera_angle="Eye-level three-quarter view.",
            lighting="Natural daylight with soft interior lighting.",
            background="Modern corporate office interior.",
            visual_style="Clean executive commercial photography.",
            color_palette="Navy, teal, white, slate.",
            subject_details="Professional corporate team members.",
            negative_space="Upper section clear."
        )

        steps_rendered = "".join([f"""
          <div style="background:#FFF;border:1px solid var(--color-border);padding:1.5rem;border-radius:8px;box-shadow:var(--shadow-sm);">
            <div style="width:32px;height:32px;background:var(--color-teal-light);color:var(--color-teal);font-weight:700;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:0.75rem;">{i+1}</div>
            <h4 style="font-size:1.1rem;margin-bottom:0.35rem;color:var(--color-navy);">{s[0]}</h4>
            <p style="font-size:0.875rem;color:var(--color-text-secondary);line-height:1.5;margin:0;">{s[1]}</p>
          </div>
        """ for i, s in enumerate(workflow_steps)])

        deliverables_rendered = "".join([f"<li style='margin-bottom:0.5rem;'>✓ {d}</li>" for d in deliverables_list])

        body_html = f"""
        <section class="subpage-hero" aria-label="Page Title">
          <div class="container">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
              <a href="index.html">Home</a>
              <span class="separator">/</span>
              <a href="services.html">Services</a>
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
                <span class="section-eyebrow">{eyebrow}</span>
                <h2 class="section-title">Strategic Sourcing for Critical Enterprise Needs</h2>
                <p style="font-size:1rem;line-height:1.7;color:var(--color-text-main);margin-bottom:1.25rem;">
                  Building teams requires precision and rigor. We partner with hiring authorities to dissect functional prerequisites, evaluate behavioral suitability, and streamline candidate movement through interview rounds.
                </p>
                <div style="background:var(--color-surface-light);padding:1.5rem;border-radius:8px;border:1px solid var(--color-border);margin-bottom:1.5rem;">
                  <h4 style="font-size:1rem;color:var(--color-navy);margin-bottom:0.75rem;">Deliverables &amp; Value Proposition</h4>
                  <ul style="font-size:0.9375rem;color:var(--color-text-secondary);list-style:none;padding:0;margin:0;">
                    {deliverables_rendered}
                  </ul>
                </div>
                <a href="hire-talent.html" class="btn btn-primary">Submit a Hiring Requirement</a>
              </div>
              <div>
                {render_placeholder(img_id, "16/9", "1600 × 900 • Service Overview")}
              </div>
            </div>

            <div class="demo-alert-banner">
              <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
              <p>
                <strong>Important Notice:</strong> {disclaimer_text}
              </p>
            </div>

            <!-- Workflow Steps -->
            <div style="margin-top:4rem;">
              <div class="section-header text-center">
                <span class="section-eyebrow">Structured Execution</span>
                <h2 class="section-title">The Delivery Workflow</h2>
              </div>
              <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:1.5rem;">
                {steps_rendered}
              </div>
            </div>

            <div style="margin-top:4.5rem;background:var(--color-navy);color:#FFF;padding:3rem;border-radius:12px;text-align:center;">
              <h3 style="color:#FFF;font-size:2rem;margin-bottom:1rem;">Ready to Discuss Your Organization's Hiring Goals?</h3>
              <p style="color:#CBD5E1;max-width:650px;margin:0 auto 2rem;font-size:1.05rem;line-height:1.6;">
                Our recruitment specialists are prepared to review your job specifications and prepare an objective talent sourcing roadmap.
              </p>
              <div style="display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;">
                <a href="hire-talent.html" class="btn btn-teal btn-lg">Submit Requirement</a>
                <a href="contact.html" class="btn btn-outline-white btn-lg">Schedule Consultation</a>
              </div>
            </div>
          </div>
        </section>
        """

        with open(filename, "w", encoding="utf-8") as f:
            f.write(wrap_page(
                title=f"{title} | Recruitment Agency",
                meta_desc=subtitle,
                active_page="services",
                body_content=body_html
            ))

    # 12. permanent-recruitment.html
    generate_service_subpage(
        filename="permanent-recruitment.html",
        title="Permanent Recruitment",
        eyebrow="Long-Term Talent Acquisition",
        subtitle="Find the Right People for Long-Term Roles.",
        img_name="permanent-recruitment-process.webp",
        img_desc="Recruitment consultant conducting a thorough candidate interview for a permanent engineering role in a modern corporate office.",
        prompt="Corporate photography: A recruitment consultant and candidate in an executive interview discussion. High-end modern office, notebook and tablet on the table, candid professional interaction, 50mm lens, natural daylight, sophisticated navy and warm gray tones.",
        deliverables_list=[
            "Role profiling & job description optimization",
            "Multi-channel active & passive candidate sourcing",
            "Technical screening & preliminary competency evaluation",
            "Interview coordination & candidate debriefing",
            "Offer alignment & joining notice follow-up"
        ],
        workflow_steps=[
            ("1. Role Profiling", "Reviewing job specifications, organizational hierarchy, salary benchmarks, and cultural expectations with hiring managers."),
            ("2. Talent Sourcing", "Engaging targeted industry talent pools, active job board networks, and discrete referral pipelines."),
            ("3. Screening & Vetting", "Conducting structured preliminary interviews evaluating technical credentials and career stability."),
            ("4. Shortlist Presentation", "Submitting curated candidate dossiers with detailed recruiter assessment notes and salary expectations."),
            ("5. Offer & Joining", "Supporting compensation negotiations, formal offer letter issuance, and notice period check-ins.")
        ],
        disclaimer_text="Permanent hiring terms, placement warranties, and candidate guarantee windows depend entirely on the commercial terms negotiated in the final client agreement."
    )

    # 13. contract-staffing.html
    generate_service_subpage(
        filename="contract-staffing.html",
        title="Contract Staffing",
        eyebrow="Flexible Project Workforce",
        subtitle="Agile workforce solutions for project-based demands and specialized skills.",
        img_name="contract-staffing-workforce.webp",
        img_desc="Specialized contractors collaborating around a high-tech project workstation with multiple monitors and architectural blueprints.",
        prompt="Commercial corporate photography: A team of specialized IT and engineering contractors collaborating around modern dual-screen computer workstations in an agile project office. Authentic teamwork, natural expressions, high detail, 35mm lens.",
        deliverables_list=[
            "Fixed-term contractor sourcing & matching",
            "Project workforce capacity planning",
            "Rapid onboarding logistics coordination",
            "Contract extension and transition planning"
        ],
        workflow_steps=[
            ("1. Requirement Scoping", "Defining project duration, required technical stack, deliverables, and billing rate thresholds."),
            ("2. Fast-Track Sourcing", "Targeting pre-qualified contractor networks available for immediate or short-notice deployment."),
            ("3. Technical Evaluation", "Verifying practical project capabilities through hands-on technical problem review."),
            ("4. Onboarding Support", "Coordinating access logistics, equipment readiness, and non-disclosure documentation.")
        ],
        disclaimer_text="Employment arrangements, payroll responsibilities, statutory obligations, and contractual responsibilities depend on the agreed service model and applicable local labor laws."
    )

    # 14. temporary-staffing.html
    generate_service_subpage(
        filename="temporary-staffing.html",
        title="Temporary Staffing",
        eyebrow="Contingent Workforce Coordination",
        subtitle="Short-term staffing solutions to maintain continuous operations during peak periods.",
        img_name="temporary-staffing-operations.webp",
        img_desc="Operations supervisor coordinating short-term assignment schedules with staff in a modern corporate facility.",
        prompt="Corporate photography: Operational staffing coordinator reviewing roster schedules with team members in an organized modern logistics and corporate workplace. Clean lighting, professional, crisp focus, 50mm lens.",
        deliverables_list=[
            "Short-term operational workforce scheduling",
            "Immediate backup personnel coordination",
            "Shift coverage and attendance reporting",
            "Flexible scaling based on operational demand"
        ],
        workflow_steps=[
            ("1. Demand Forecasting", "Analyzing seasonal volume surges, leave coverage requirements, and peak period shifts."),
            ("2. Availability Matching", "Identifying available pre-screened talent ready for rapid deployment."),
            ("3. Shift Scheduling", "Coordinating shift rotations, reporting instructions, and onsite point of contact."),
            ("4. Operational Review", "Ongoing monitoring of attendance, productivity benchmarks, and duration adjustments.")
        ],
        disclaimer_text="Temporary personnel availability fluctuates based on regional market dynamics. Candidate availability and staffing timelines cannot be guaranteed prior to formal requisition confirmation."
    )

    # 15. executive-search.html
    generate_service_subpage(
        filename="executive-search.html",
        title="Executive Search",
        eyebrow="Leadership Appointments",
        subtitle="Identify Leadership Talent for Critical Roles.",
        img_name="executive-search-leadership.webp",
        img_desc="Executive search partners reviewing senior talent market maps in an executive private office.",
        prompt="Executive corporate photography: Two senior executive search partners reviewing organizational talent mapping dossiers in an upscale, tasteful private consultation office. Subtle gold and navy tones, warm ambient lighting, elegant, non-cliché, 85mm lens, f/2.8, shallow depth of field.",
        deliverables_list=[
            "Executive leadership competency profiling",
            "Comprehensive market talent mapping",
            "Confidential non-disclosure candidate outreach",
            "Leadership behavioral evaluation",
            "Executive compensation structuring support"
        ],
        workflow_steps=[
            ("1. Board & Stakeholder Brief", "Deep alignment on strategic corporate vision, governance priorities, and required leadership capabilities."),
            ("2. Talent Mapping", "Exhaustive confidential mapping of industry leaders and peer competitors across regional markets."),
            ("3. Discreet Outreach", "Direct partner-led discussions conducted under strict non-disclosure safeguards."),
            ("4. Comprehensive Evaluation", "Rigorous evaluation of leadership track records, crisis management capability, and cultural fit."),
            ("5. Offer & Transition", "Facilitating confidential package structuring, board presentation, and executive integration.")
        ],
        disclaimer_text="Executive search processes adhere to strict confidentiality protocols. We do not invent confidential client mandates, executive candidate identities, or placement outcomes in this demonstration."
    )

    # 16. recruitment-process-outsourcing.html
    generate_service_subpage(
        filename="recruitment-process-outsourcing.html",
        title="Recruitment Process Outsourcing (RPO)",
        eyebrow="Outsourced Talent Operations",
        subtitle="End-to-end recruitment process management embedded within your organizational structure.",
        img_name="rpo-workforce-solutions.webp",
        img_desc="An integrated recruitment process outsourcing team managing candidate pipelines and hiring metrics on interactive analytics monitors.",
        prompt="Corporate photography: An enterprise recruitment operations center. Dedicated talent acquisition specialists monitoring hiring pipelines and SLA metrics across multiple displays in a sleek glass corporate environment. Natural light, professional focus, 35mm lens.",
        deliverables_list=[
            "Recruitment workflow assessment & standardization",
            "Job requisition intake & management",
            "Dedicated sourcing & screening infrastructure",
            "Interview logistics and feedback governance",
            "Comprehensive hiring analytics & SLA reporting"
        ],
        workflow_steps=[
            ("1. Process Assessment", "Evaluating current hiring bottlenecks, cost per hire, candidate drop-off, and cycle times."),
            ("2. SLA & Workflow Design", "Establishing service level benchmarks, role requisition protocols, and evaluation rubrics."),
            ("3. Team Deployment", "Deploying a dedicated recruitment pod aligned with your corporate talent acquisition requirements."),
            ("4. Continuous Optimization", "Ongoing reporting, hiring manager satisfaction tracking, and process enhancements.")
        ],
        disclaimer_text="Recruitment process outsourcing requires formal contractual integration and SLA governance. This static prototype illustrates RPO operational workflows and is distinct from a live software ATS integration."
    )

    # 17. bulk-hiring.html
    generate_service_subpage(
        filename="bulk-hiring.html",
        title="Bulk Hiring Solutions",
        eyebrow="High-Volume Talent Delivery",
        subtitle="Build Teams at Scale With Structured Hiring.",
        img_name="bulk-hiring-drive-event.webp",
        img_desc="Coordinated high-volume hiring event with structured candidate registration and multi-stage interview pods in a convention hall.",
        prompt="Corporate commercial photography: A well-organized high-volume hiring event in a modern conference center. Recruitment coordinators guiding candidates through organized assessment stations and interview pods. Bright, professional, orderly atmosphere, 35mm lens.",
        deliverables_list=[
            "High-volume recruitment campaign architecture",
            "Multi-channel mass candidate generation",
            "Multi-stage structured assessment drives",
            "Interview drive event logistics management",
            "Batch onboarding & documentation coordination"
        ],
        workflow_steps=[
            ("1. Volume Scoping", "Analyzing target numbers, role standardization, hiring timelines, and regional venue logistics."),
            ("2. Campaign Launch", "Deploying omni-channel candidate generation across targeted digital networks and local recruitment pipelines."),
            ("3. Assessment Drives", "Managing batched screening, written/technical testing stations, and panel interviews."),
            ("4. Batch Onboarding", "Streamlining document collection, background verification briefing, and cohort orientation.")
        ],
        disclaimer_text="Volume hiring numbers, cycle times, and batch completion rates vary by role requirements and regional candidate pools. We do not invent arbitrary placement statistics or guaranteed headcount volumes."
    )

    # 18. campus-recruitment.html
    generate_service_subpage(
        filename="campus-recruitment.html",
        title="Campus Recruitment",
        eyebrow="Early-Career Talent",
        subtitle="Connecting organizations with fresh academic graduates and early-career talent.",
        img_name="campus-recruitment-graduates.webp",
        img_desc="Recruitment specialists conducting an early-career graduate recruitment workshop in a modern university lecture auditorium.",
        prompt="Corporate photography: Campus recruitment workshop in an airy contemporary university hall. Corporate talent advisors engaging with ambitious, professional university students reviewing career pathways. Diverse subjects, bright natural lighting, authentic, 50mm lens.",
        deliverables_list=[
            "Campus engagement & hiring calendar planning",
            "Early-career competency framework design",
            "Standardized campus screening & assessment tests",
            "On-campus interview drive logistics",
            "Graduate cohort onboarding coordination"
        ],
        workflow_steps=[
            ("1. Campus Strategy", "Selecting academic disciplines, graduation timelines, and entry-level role competencies."),
            ("2. Engagement Workshops", "Conducting career awareness sessions, organizational presentations, and Q&A forums."),
            ("3. Standardized Testing", "Administering objective cognitive, aptitude, and fundamental technical assessments."),
            ("4. Selection & Placement", "Conducting panel interviews, extending conditional offers, and tracking campus-to-corporate transitions.")
        ],
        disclaimer_text="Campus hiring initiatives require direct institutional approvals and academic calendar alignment. We do not fabricate specific university partnerships or historical student placement volumes."
    )

    # 19. talent-acquisition.html
    generate_service_subpage(
        filename="talent-acquisition.html",
        title="Talent Acquisition Strategy",
        eyebrow="Strategic Advisory",
        subtitle="Build a Talent Strategy Around Your Business Goals.",
        img_name="talent-acquisition-strategy-session.webp",
        img_desc="Talent acquisition strategist and HR directors collaborating over an interactive workforce projection roadmap in a modern boardroom.",
        prompt="Executive corporate photography: Talent acquisition strategists collaborating with corporate HR executives around a sleek conference table with roadmap diagrams and workforce models. Confident, focused business atmosphere, natural daylight, 50mm lens, sharp details.",
        deliverables_list=[
            "Workforce demand forecasting & capacity modeling",
            "Talent pipeline architecture & nurturing models",
            "Employer value proposition (EVP) alignment",
            "Candidate experience audit & journey mapping",
            "Recruitment metrics & KPI dashboard consulting"
        ],
        workflow_steps=[
            ("1. Strategic Alignment", "Connecting upcoming commercial roadmap milestones with required human capital capabilities."),
            ("2. Sourcing Channel Audit", "Evaluating channel effectiveness, referral program yields, and agency spend efficiency."),
            ("3. Candidate Experience Redesign", "Eliminating friction across application, interview, and offer communication touchpoints."),
            ("4. Governance & Metrics", "Implementing structured metrics including quality of hire, offer acceptance ratios, and sourcing velocity.")
        ],
        disclaimer_text="Talent strategy recommendations are tailored to individual organizational maturity and hiring objectives. Our illustrative frameworks provide advisory guidance without replacing internal management decision-making."
    )

    print("Service pages (11-19) generated successfully.")

if __name__ == "__main__":
    build_services()
