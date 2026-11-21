"""
Generates core general pages:
1. index.html
2. about.html
3. team.html
4. methodology.html
5. recruitment-process.html
6. pricing.html
7. faq.html
8. contact.html
9. privacy-policy.html
10. terms-and-conditions.html
"""
import os
from builder_core import wrap_page, render_placeholder, record_image

def build_core():
    # 1. index.html
    img_hero = record_image(
        filename="hero-recruitment-agency.webp",
        page="index.html",
        section="Hero Section",
        description="A bright, modern executive board room or high-end office meeting where professional recruiters and corporate clients engage in a collaborative talent acquisition consultation.",
        aspect_ratio="16/9",
        resolution="1920x1080",
        orientation="Landscape",
        prompt="Professional high-end commercial corporate photography: An international recruitment consultancy meeting room in a modern glass office. Two corporate talent acquisition consultants, dressed in tailored navy and charcoal business attire, engage in a productive, smiling discussion with two client hiring directors over candidate profile dossiers and a laptop. Warm architectural lighting, sleek interior with soft bokeh view of city skyline, neutral tones with navy and subtle teal accents. Candid, authentic expressions, non-posed, 85mm lens, f/2.8, hyper-detailed, clean natural light.",
        composition="Wide environmental shot with subjects positioned slightly to the right to leave gentle negative space on the left.",
        camera_angle="Eye-level, shallow depth of field.",
        lighting="Soft natural daytime light with warm interior architectural accents.",
        background="Contemporary corporate glass conference room with subtle skyline view.",
        visual_style="Editorial corporate executive photography, crisp and sophisticated.",
        color_palette="Deep navy (#14263D), slate gray, subtle warm gold accents, soft ambient white.",
        subject_details="Four diverse corporate professionals (two women, two men), neatly groomed, natural expressions.",
        negative_space="Left side open for hero typography overlay if needed."
    )

    img_candidate_entry = record_image(
        filename="candidate-interview-session.webp",
        page="index.html",
        section="Candidate Journey Preview",
        description="A supportive one-on-one professional recruiter and candidate interview dialogue in a contemporary office setting.",
        aspect_ratio="4/3",
        resolution="1200x900",
        orientation="Landscape",
        prompt="Commercial corporate photography: A positive, professional one-on-one interview between an experienced talent advisor and a job candidate across a wooden conference table in a modern airy office. Recruiter is reviewing a clean portfolio notebook, candidate is engaged and speaking confidently. Natural smiles, genuine eye contact, modern office greenery in soft background. 50mm lens, f/2.0, soft diffused lighting, no watermarks, realistic human interaction.",
        composition="Medium close-up showing both individuals in dynamic balance.",
        camera_angle="Slight three-quarter perspective at eye level.",
        lighting="Diffused window illumination with subtle fill light.",
        background="Bright open-plan office interior with tasteful minimalist decor.",
        visual_style="Modern, trustworthy, human-centered talent consulting.",
        color_palette="Teal accents (#28A69A), warm wood tones, crisp white, deep navy.",
        subject_details="Professional female recruiter and professional male candidate.",
        negative_space="Balanced framing with natural depth."
    )

    img_employer_entry = record_image(
        filename="employer-consultation-meeting.webp",
        page="index.html",
        section="Employer Hiring Journey Preview",
        description="Senior recruitment partners consulting with corporate hiring executives around a conference table with workforce roadmap charts.",
        aspect_ratio="4/3",
        resolution="1200x900",
        orientation="Landscape",
        prompt="Premium corporate photography: An executive talent acquisition briefing meeting. Senior recruitment partner pointing to a tablet displaying workforce roadmap diagrams, discussing organizational hiring plans with a corporate CEO and HR director. Focused, professional atmosphere, elegant boardroom table, laptops and architectural coffee cups, shallow depth of field, 70mm lens, professional executive atmosphere, authentic non-stock aesthetic.",
        composition="Group medium shot focused on the strategic consultation discussion.",
        camera_angle="Slightly elevated three-quarter boardroom angle.",
        lighting="Warm interior recessed lighting combined with clean daylight.",
        background="Executive boardroom with frosted glass walls and understated artwork.",
        visual_style="Sophisticated international staffing consultancy imagery.",
        color_palette="Navy blue, charcoal, brushed steel, warm wood tones.",
        subject_details="Three corporate executives in smart business attire.",
        negative_space="Top portion gently out of focus."
    )

    index_html = f"""
    <!-- Hero Section -->
    <section class="hero-section" aria-label="Welcome and Overview">
      <div class="container">
        <div class="hero-grid">
          <div>
            <div class="hero-badge-tag">
              <svg style="width:16px;height:16px;" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              <span>Strategic Talent &amp; Workforce Solutions</span>
            </div>
            <h1 class="hero-title">THE RIGHT PEOPLE MAKE ALL THE DIFFERENCE.</h1>
            <p class="hero-subtitle">
              Connecting ambitious businesses with talented professionals through thoughtful recruitment, contract staffing, executive search, and workforce solutions.
            </p>
            <div class="hero-actions">
              <a href="jobs.html" class="btn btn-teal btn-lg">Explore Job Opportunities</a>
              <a href="hire-talent.html" class="btn btn-outline-white btn-lg">Hire Talent</a>
            </div>
            <div class="hero-trust-bar">
              <div class="hero-trust-item">
                <svg style="width:18px;height:18px;color:#5ED9CB;" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                <span>Permanent &amp; Contract Staffing</span>
              </div>
              <div class="hero-trust-item">
                <svg style="width:18px;height:18px;color:#5ED9CB;" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                <span>Executive Search &amp; Leadership</span>
              </div>
              <div class="hero-trust-item">
                <svg style="width:18px;height:18px;color:#5ED9CB;" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                <span>Cross-Industry Specialization</span>
              </div>
            </div>
          </div>
          <div>
            {render_placeholder(img_hero, "16/9", "1920 × 1080 • Landscape Hero")}
          </div>
        </div>
      </div>
    </section>

    <!-- Prominent Two Audience Cards -->
    <section class="section-sm" style="padding-top:0;" aria-label="Audience Portals">
      <div class="container">
        <div class="audience-cards-container">
          <!-- CARD 1: For Candidates -->
          <div class="audience-card audience-card-candidate">
            <div>
              <div class="audience-icon">
                <svg style="width:28px;height:28px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
              </div>
              <span class="badge badge-teal" style="margin-bottom:0.75rem;">For Job Seekers &amp; Professionals</span>
              <h3>Find Your Next Opportunity</h3>
              <p>
                Explore job opportunities, discover career possibilities, and take your next professional step with our supportive recruitment advisory.
              </p>
            </div>
            <div>
              <div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
                <a href="jobs.html" class="btn btn-teal">Search Jobs</a>
                <a href="register-cv.html" class="btn btn-outline-teal">Register Your CV</a>
              </div>
            </div>
          </div>

          <!-- CARD 2: For Employers -->
          <div class="audience-card audience-card-employer">
            <div>
              <div class="audience-icon">
                <svg style="width:28px;height:28px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
              </div>
              <span class="badge badge-navy" style="margin-bottom:0.75rem;">For Organizations &amp; Hiring Teams</span>
              <h3>Find the Talent You Need</h3>
              <p>
                Build stronger teams with recruitment and staffing solutions aligned with your business requirements, operational goals, and growth roadmap.
              </p>
            </div>
            <div>
              <div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
                <a href="hire-talent.html" class="btn btn-primary">Submit a Hiring Requirement</a>
                <a href="services.html" class="btn btn-outline-navy">Explore Services</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick Job Search Bar -->
    <section class="section-sm bg-warm" aria-label="Job Search Widget">
      <div class="container">
        <div class="job-search-box">
          <div style="margin-bottom:1.25rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
            <div>
              <h3 style="font-size:1.25rem;margin-bottom:0.25rem;">Search Illustrative Job Opportunities</h3>
              <p style="color:var(--color-text-secondary);font-size:0.875rem;margin:0;">Filter sample vacancies across industries, locations, and employment arrangements.</p>
            </div>
            <span class="badge badge-demo">DEMO VACANCY — NOT A VERIFIED LIVE JOB</span>
          </div>

          <form action="jobs.html" method="GET" class="search-form-grid">
            <div class="form-group" style="margin-bottom:0;">
              <label for="home-search-keyword">Role or Keyword</label>
              <input type="text" id="home-search-keyword" name="keyword" class="form-control" placeholder="e.g. Developer, Analyst, Manager">
            </div>
            <div class="form-group" style="margin-bottom:0;">
              <label for="home-filter-industry">Industry</label>
              <select id="home-filter-industry" name="industry" class="form-select">
                <option value="">All Industries</option>
                <option value="Information Technology">Information Technology</option>
                <option value="Banking and Finance">Banking and Finance</option>
                <option value="Healthcare">Healthcare</option>
                <option value="Engineering">Engineering</option>
                <option value="Manufacturing">Manufacturing</option>
                <option value="Sales and Marketing">Sales &amp; Marketing</option>
                <option value="Logistics and Supply Chain">Logistics &amp; Supply Chain</option>
              </select>
            </div>
            <div class="form-group" style="margin-bottom:0;">
              <label for="home-filter-location">Location</label>
              <select id="home-filter-location" name="location" class="form-select">
                <option value="">All Locations</option>
                <option value="Hyderabad">Hyderabad</option>
                <option value="Bangalore">Bangalore</option>
                <option value="Mumbai">Mumbai</option>
                <option value="Chennai">Chennai</option>
                <option value="Pune">Pune</option>
                <option value="Remote">Remote</option>
              </select>
            </div>
            <button type="submit" class="btn btn-teal" style="height:45px;">
              <svg style="width:16px;height:16px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
              Search
            </button>
          </form>
        </div>
      </div>
    </section>

    <!-- Featured Demo Vacancies Section -->
    <section class="section bg-white" aria-label="Featured Demo Opportunities">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-eyebrow">Explore Roles</span>
          <h2 class="section-title">Featured Demonstration Vacancies</h2>
          <p class="section-subtitle">
            Illustrative sample job listings showcasing the structure, transparency, and detail our recruitment platform provides for professional candidates.
          </p>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> The jobs displayed below are generic illustrative vacancies designed to test and showcase search, filtering, and role overview interfaces. These are not active commercial job offers.
          </p>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:2.5rem;">
          <!-- Sample Job 1 -->
          <article class="job-card">
            <div class="job-card-header">
              <div>
                <span class="badge badge-demo">DEMO VACANCY — NOT A VERIFIED LIVE JOB</span>
                <h3 class="job-card-title" style="margin-top:0.4rem;">
                  <a href="job-details.html?id=job-001">Frontend Developer — Demo Vacancy</a>
                </h3>
                <div class="job-card-employer">
                  <span>Confidential Technology Client</span> &bull; <span class="badge badge-teal">Information Technology</span>
                </div>
              </div>
              <a href="job-details.html?id=job-001" class="btn btn-sm btn-outline-teal">Details</a>
            </div>
            <div class="job-meta-grid">
              <span class="job-meta-item">📍 Hyderabad, India (Hybrid)</span>
              <span class="job-meta-item">💼 Full-time</span>
              <span class="job-meta-item">⏳ 3-5 Years</span>
            </div>
            <p class="job-card-summary">Modern frontend specialist skilled in semantic HTML5, modern CSS, and Vanilla JavaScript interfaces.</p>
          </article>

          <!-- Sample Job 2 -->
          <article class="job-card">
            <div class="job-card-header">
              <div>
                <span class="badge badge-demo">DEMO VACANCY — NOT A VERIFIED LIVE JOB</span>
                <h3 class="job-card-title" style="margin-top:0.4rem;">
                  <a href="job-details.html?id=job-002">Data Analyst — Demo Vacancy</a>
                </h3>
                <div class="job-card-employer">
                  <span>Corporate Financial Services Partner</span> &bull; <span class="badge badge-teal">Banking &amp; Finance</span>
                </div>
              </div>
              <a href="job-details.html?id=job-002" class="btn btn-sm btn-outline-teal">Details</a>
            </div>
            <div class="job-meta-grid">
              <span class="job-meta-item">📍 Bangalore, India (On-site)</span>
              <span class="job-meta-item">💼 Full-time</span>
              <span class="job-meta-item">⏳ 2-4 Years</span>
            </div>
            <p class="job-card-summary">Transforming complex financial datasets into actionable intelligence dashboards and executive reports.</p>
          </article>
        </div>

        <div class="text-center">
          <a href="jobs.html" class="btn btn-primary">Browse All 8 Demonstration Vacancies</a>
        </div>
      </div>
    </section>

    <!-- Recruitment Services Overview -->
    <section class="section bg-light" aria-label="Recruitment Services">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-eyebrow">Workforce Solutions</span>
          <h2 class="section-title">Comprehensive Staffing &amp; Talent Solutions</h2>
          <p class="section-subtitle">
            From single critical hires to end-to-end recruitment process outsourcing, our structured service models adapt to your organizational hiring scale.
          </p>
        </div>

        <div class="service-grid">
          <!-- Service 1 -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
              </div>
              <h3>Permanent Recruitment</h3>
              <p>Identify, evaluate, and secure verified talent for permanent, full-time roles across diverse departmental disciplines.</p>
              <div class="service-deliverables">
                <h5>Key Deliverables</h5>
                <ul>
                  <li>Role profiling &amp; benchmark analysis</li>
                  <li>Multi-channel talent sourcing</li>
                  <li>Technical screening &amp; shortlisting</li>
                </ul>
              </div>
            </div>
            <div>
              <a href="permanent-recruitment.html" class="btn btn-outline-navy btn-sm" style="width:100%;">Learn More &rarr;</a>
            </div>
          </div>

          <!-- Service 2 -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              </div>
              <h3>Contract Staffing</h3>
              <p>Agile, project-based professional staffing solutions designed to address short-term capability needs and surges.</p>
              <div class="service-deliverables">
                <h5>Key Deliverables</h5>
                <ul>
                  <li>Project duration planning</li>
                  <li>Rapid specialized skill placement</li>
                  <li>Onboarding coordination</li>
                </ul>
              </div>
            </div>
            <div>
              <a href="contract-staffing.html" class="btn btn-outline-navy btn-sm" style="width:100%;">Learn More &rarr;</a>
            </div>
          </div>

          <!-- Service 3 -->
          <div class="service-card">
            <div>
              <div class="service-card-icon">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
              </div>
              <h3>Executive Search</h3>
              <p>Confidential, discrete recruitment consulting focused exclusively on C-suite, board-level, and mission-critical leadership appointments.</p>
              <div class="service-deliverables">
                <h5>Key Deliverables</h5>
                <ul>
                  <li>Leadership competency mapping</li>
                  <li>Discrete talent outreach</li>
                  <li>Executive assessment coordination</li>
                </ul>
              </div>
            </div>
            <div>
              <a href="executive-search.html" class="btn btn-outline-navy btn-sm" style="width:100%;">Learn More &rarr;</a>
            </div>
          </div>
        </div>

        <div class="text-center" style="margin-top:2.5rem;">
          <a href="services.html" class="btn btn-teal">View All 10 Recruitment Services</a>
        </div>
      </div>
    </section>

    <!-- Two Journeys Walkthrough -->
    <section class="section bg-white" aria-label="Two Journeys">
      <div class="container">
        <!-- Candidate Journey Preview -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;align-items:center;margin-bottom:5rem;">
          <div>
            <span class="section-eyebrow">The Candidate Path</span>
            <h2 class="section-title">Supportive, Transparent Career Engagement</h2>
            <p style="color:var(--color-text-secondary);line-height:1.7;margin-bottom:1.5rem;">
              We believe candidate care is the bedrock of credible recruitment. We keep professionals informed at every stage of the evaluation journey, from initial profile discovery through interview prep and offer negotiation.
            </p>
            <div style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2rem;">
              <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                <div style="width:28px;height:28px;background:var(--color-teal-light);color:var(--color-teal);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;">1</div>
                <div>
                  <h4 style="font-size:1rem;margin-bottom:0.2rem;">Discovery &amp; Profile Alignment</h4>
                  <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Explore verified job profiles matching your career trajectory and skills.</p>
                </div>
              </div>
              <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                <div style="width:28px;height:28px;background:var(--color-teal-light);color:var(--color-teal);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;">2</div>
                <div>
                  <h4 style="font-size:1rem;margin-bottom:0.2rem;">Recruiter Consultation &amp; Prep</h4>
                  <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Discuss organizational culture, role expectations, and interview readiness.</p>
                </div>
              </div>
              <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                <div style="width:28px;height:28px;background:var(--color-teal-light);color:var(--color-teal);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;">3</div>
                <div>
                  <h4 style="font-size:1rem;margin-bottom:0.2rem;">Offer Negotiation &amp; Onboarding</h4>
                  <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Receive objective support during terms finalization and joining coordination.</p>
                </div>
              </div>
            </div>
            <a href="candidates.html" class="btn btn-teal">Explore Candidate Hub</a>
          </div>
          <div>
            {render_placeholder(img_candidate_entry, "4/3", "1200 × 900 • Candidate Journey")}
          </div>
        </div>

        <!-- Employer Journey Preview -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;align-items:center;">
          <div>
            {render_placeholder(img_employer_entry, "4/3", "1200 × 900 • Employer Journey")}
          </div>
          <div>
            <span class="section-eyebrow">The Employer Partnership</span>
            <h2 class="section-title">Rigorous, Aligned Talent Acquisition</h2>
            <p style="color:var(--color-text-secondary);line-height:1.7;margin-bottom:1.5rem;">
              Hiring decisions shape enterprise performance. Our 5-stage recruitment methodology ensures we understand your team dynamics, evaluate candidates against technical benchmarks, and coordinate smooth onboarding.
            </p>
            <div style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2rem;">
              <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                <div style="width:28px;height:28px;background:#EBF1F7;color:var(--color-navy);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;">✓</div>
                <div>
                  <h4 style="font-size:1rem;margin-bottom:0.2rem;">In-Depth Role Profiling</h4>
                  <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Clarifying exact hard skills, team culture fit, and commercial deliverables.</p>
                </div>
              </div>
              <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                <div style="width:28px;height:28px;background:#EBF1F7;color:var(--color-navy);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;">✓</div>
                <div>
                  <h4 style="font-size:1rem;margin-bottom:0.2rem;">Targeted Talent Sourcing &amp; Screening</h4>
                  <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Rigorous pre-qualification reducing hiring manager interview load.</p>
                </div>
              </div>
              <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                <div style="width:28px;height:28px;background:#EBF1F7;color:var(--color-navy);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0;">✓</div>
                <div>
                  <h4 style="font-size:1rem;margin-bottom:0.2rem;">Transparent Process Coordination</h4>
                  <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Consistent feedback loops and offer acceptance management.</p>
                </div>
              </div>
            </div>
            <a href="employers.html" class="btn btn-primary">Explore Employer Solutions</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Illustrative Dashboard Mockup Section -->
    <section class="section bg-light" aria-label="Illustrative Pipeline Mockup">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-eyebrow">Structured Visibility</span>
          <h2 class="section-title">Transparent Talent Pipeline Management</h2>
          <p class="section-subtitle">
            An illustrative preview of how structured stage tracking ensures candidates and hiring managers maintain clear communication throughout the recruitment lifecycle.
          </p>
        </div>

        <div class="dashboard-mockup">
          <div class="dashboard-header-bar">
            <div style="display:flex;align-items:center;gap:0.5rem;">
              <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#28A69A;"></span>
              <strong>Illustrative Recruitment Pipeline Demonstration</strong>
            </div>
            <span class="badge badge-demo">Illustrative Demo Data — Not Actual Recruitment Records</span>
          </div>
          <div class="dashboard-content-body">
            <div class="dashboard-stats-row">
              <div class="dashboard-stat-card">
                <div class="dashboard-stat-val">24</div>
                <div class="dashboard-stat-label">Profiles Screened</div>
              </div>
              <div class="dashboard-stat-card">
                <div class="dashboard-stat-val">8</div>
                <div class="dashboard-stat-label">Interviews Coordinated</div>
              </div>
              <div class="dashboard-stat-card">
                <div class="dashboard-stat-val">3</div>
                <div class="dashboard-stat-label">Final Shortlist</div>
              </div>
              <div class="dashboard-stat-card">
                <div class="dashboard-stat-val">1</div>
                <div class="dashboard-stat-label">Offer Stage</div>
              </div>
            </div>

            <div class="pipeline-stage-bar">
              <div class="pipeline-pill">1. Requirement</div>
              <div class="pipeline-pill">2. Sourcing</div>
              <div class="pipeline-pill">3. Screening</div>
              <div class="pipeline-pill active">4. Shortlisting</div>
              <div class="pipeline-pill">5. Interview</div>
              <div class="pipeline-pill">6. Joining</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Dual Conversion CTAs -->
    <section class="section bg-navy" aria-label="Action Calls">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;">
          <div style="border-right:1px solid rgba(255,255,255,0.15);padding-right:2rem;">
            <span class="badge badge-teal" style="margin-bottom:1rem;">Ready for Your Next Step?</span>
            <h3 style="color:#FFF;font-size:2rem;margin-bottom:1rem;">Looking for Employment Opportunities?</h3>
            <p style="color:#CCD6E0;line-height:1.6;margin-bottom:1.75rem;">
              Browse our demonstration job board or submit your resume for consideration across upcoming client mandates.
            </p>
            <div style="display:flex;gap:1rem;flex-wrap:wrap;">
              <a href="jobs.html" class="btn btn-teal">Search Opportunities</a>
              <a href="register-cv.html" class="btn btn-outline-white">Register Your CV</a>
            </div>
          </div>

          <div>
            <span class="badge badge-gold" style="margin-bottom:1rem;">Building Your Team?</span>
            <h3 style="color:#FFF;font-size:2rem;margin-bottom:1rem;">Need Specialized Talent for Your Organization?</h3>
            <p style="color:#CCD6E0;line-height:1.6;margin-bottom:1.75rem;">
              Submit your hiring requisition details. Our recruitment advisory team will review your requirements and outline a tailored recruitment strategy.
            </p>
            <div style="display:flex;gap:1rem;flex-wrap:wrap;">
              <a href="hire-talent.html" class="btn btn-gold">Submit a Hiring Requirement</a>
              <a href="contact.html" class="btn btn-outline-white">Contact Agency</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Recruitment Agency | Strategic Talent & Staffing Solutions",
            meta_desc="Connecting ambitious businesses with talented professionals through strategic recruitment, permanent hiring, contract staffing, and talent acquisition.",
            active_page="index",
            body_content=index_html
        ))

    # 2. about.html
    img_about = record_image(
        filename="about-recruitment-agency-team.webp",
        page="about.html",
        section="Agency Overview",
        description="Recruitment advisory team working collaboratively in a modern consultancy workspace with laptops and organizational charts.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A collaborative recruitment consultancy office. Professional talent advisors reviewing organizational charts and candidate profiles on digital displays and laptops in an elegant, well-lit modern agency workspace. Navy, teal, and warm wood accents, natural daytime light, sincere professional engagement, 35mm lens, sharp focus, authentic workplace atmosphere.",
        composition="Wide establishing shot of a modern talent agency workspace.",
        camera_angle="Eye-level, architectural perspective.",
        lighting="Abundant natural sunlight through large industrial-style windows.",
        background="Open collaborative office with whiteboards and tasteful indoor plants.",
        visual_style="Clean, minimalist corporate documentary photography.",
        color_palette="Deep navy, warm wood, slate, light teal.",
        subject_details="Professional recruitment team members in smart casual business dress.",
        negative_space="Natural open space in upper quadrant."
    )

    about_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>About Us</span>
        </nav>
        <h1>Bringing People and Opportunities Together</h1>
        <p class="lead">
          We operate as a strategic bridge between organizations seeking capable talent and professionals seeking meaningful career growth.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Our Identity &amp; Purpose</span>
            <h2 class="section-title">About the Recruitment Agency</h2>
            <p>
              As an independent recruitment and talent acquisition consultancy, our focus is grounded in understanding the real operational requirements of hiring managers and the authentic capabilities of job seekers.
            </p>
            <p>
              Recruitment is not merely matching keywords on a resume with phrases in a job description. Sustainable hiring requires an appreciation of organizational culture, team communication, technical proficiency, and long-term career motivation.
            </p>
            <p>
              We provide structured recruitment, contract staffing, and workforce solutions across multiple established industries, ensuring both employers and candidates experience a respectful, transparent, and rigorous hiring process.
            </p>
          </div>
          <div>
            {render_placeholder(img_about, "16/9", "1600 × 900 • Agency Overview")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> This profile represents a generic recruitment agency demonstration website. In accordance with strict demonstration rules, we do not fabricate founding years, founder biographies, employee headcounts, specific client relationships, or historical placement statistics.
          </p>
        </div>

        <!-- Mission & Vision Cards -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:3rem;">
          <div style="background:var(--color-surface-light);padding:2.5rem;border-radius:12px;border:1px solid var(--color-border);">
            <div style="width:48px;height:48px;background:var(--color-teal-light);color:var(--color-teal);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
            </div>
            <h3 style="font-size:1.4rem;margin-bottom:0.75rem;">Our Mission</h3>
            <p style="color:var(--color-text-secondary);line-height:1.6;margin:0;">
              To empower organizational performance through precise, ethical recruitment and to champion professional careers through honest, constructive talent advisory.
            </p>
          </div>

          <div style="background:var(--color-surface-light);padding:2.5rem;border-radius:12px;border:1px solid var(--color-border);">
            <div style="width:48px;height:48px;background:#EBF1F7;color:var(--color-navy);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
            </div>
            <h3 style="font-size:1.4rem;margin-bottom:0.75rem;">Our Vision</h3>
            <p style="color:var(--color-text-secondary);line-height:1.6;margin:0;">
              To be recognized as a premier talent acquisition partner where recruitment is conducted with integrity, meticulous technical assessment, and lasting professional value.
            </p>
          </div>
        </div>

        <!-- Principles Grid -->
        <div style="margin-top:5rem;">
          <div class="section-header text-center">
            <span class="section-eyebrow">Guiding Values</span>
            <h2 class="section-title">Core Principles of Our Practice</h2>
          </div>

          <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:1.5rem;">
            <div style="border:1px solid var(--color-border);padding:1.75rem;border-radius:8px;background:#FFF;">
              <h4 style="font-size:1.15rem;margin-bottom:0.5rem;color:var(--color-navy);">1. Candidate-Centered Respect</h4>
              <p style="color:var(--color-text-secondary);font-size:0.9rem;line-height:1.5;margin:0;">Every applicant deserves prompt feedback, clear status visibility, and thoughtful interview preparation.</p>
            </div>
            <div style="border:1px solid var(--color-border);padding:1.75rem;border-radius:8px;background:#FFF;">
              <h4 style="font-size:1.15rem;margin-bottom:0.5rem;color:var(--color-navy);">2. Objective Evaluation</h4>
              <p style="color:var(--color-text-secondary);font-size:0.9rem;line-height:1.5;margin:0;">We assess candidates strictly against job-relevant competencies, verified experience, and validated capabilities.</p>
            </div>
            <div style="border:1px solid var(--color-border);padding:1.75rem;border-radius:8px;background:#FFF;">
              <h4 style="font-size:1.15rem;margin-bottom:0.5rem;color:var(--color-navy);">3. Confidentiality &amp; Trust</h4>
              <p style="color:var(--color-text-secondary);font-size:0.9rem;line-height:1.5;margin:0;">Client strategic hiring plans and candidate career inquiries are handled with discrete, professional confidentiality.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    with open("about.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="About Us | Recruitment Agency",
            meta_desc="Learn about our recruitment philosophy, mission, vision, and principles connecting businesses with great professionals.",
            active_page="about",
            body_content=about_html
        ))

    # 3. team.html
    team_profiles = [
        ("team-recruitment-consultant.webp", "Senior Recruitment Consultant", "Permanent Recruitment Practice", "Focuses on candidate talent mapping, job profiling, and technical assessment coordination across commercial domains."),
        ("team-talent-acquisition-lead.webp", "Talent Acquisition Lead", "Workforce Solutions", "Guides strategic hiring roadmaps, multi-channel sourcing methodologies, and employer talent acquisition frameworks."),
        ("team-it-recruitment-specialist.webp", "IT Recruitment Specialist", "Technology & Engineering Practice", "Specializes in software engineering, cloud infrastructure, and data analytics role evaluation and sourcing."),
        ("team-healthcare-staffing-coordinator.webp", "Healthcare Staffing Coordinator", "Healthcare & Life Sciences", "Oversees clinical workforce planning, qualifications verification coordination, and specialized hospital staffing."),
        ("team-executive-search-partner.webp", "Executive Search Partner", "Leadership Practice", "Conducts discrete talent mapping and confidential outreach for board-level and executive leadership mandates."),
        ("team-staffing-operations-specialist.webp", "Staffing Operations Specialist", "Contract & Bulk Staffing", "Manages project-based workforce scheduling, candidate onboarding logistics, and compliance documentation support."),
        ("team-candidate-engagement-advisor.webp", "Candidate Engagement Advisor", "Talent Relations", "Provides interview preparation guidance, feedback communication, and candidate career transition support."),
        ("team-employer-relations-director.webp", "Employer Relations Director", "Corporate Partnerships", "Coordinates client requirement scoping, SLA compliance, and cross-functional recruitment project governance.")
    ]

    team_cards_html = ""
    for filename, role_title, practice, bio in team_profiles:
        record_image(
            filename=filename,
            page="team.html",
            section="Team Functional Profiles",
            description=f"Professional corporate portrait placeholder representing the functional role of {role_title}.",
            aspect_ratio="1/1",
            resolution="600x600",
            orientation="Square",
            prompt=f"Professional corporate studio portrait: Abstract, modern executive portrait placeholder for a {role_title}. Neutral corporate background, soft Rembrandt lighting, sharp focus on subject dressed in professional business attire, authentic confident expression, 85mm portrait lens, f/2.8, clean, sophisticated color palette featuring deep navy and subtle warm gray tones.",
            composition="Square head-and-shoulders corporate portrait.",
            camera_angle="Eye-level portrait.",
            lighting="Diffused studio portrait lighting.",
            background="Neutral textured corporate studio background.",
            visual_style="Premium executive headshot, natural and authentic.",
            color_palette="Charcoal, navy, crisp white, neutral gray.",
            subject_details=f"Corporate professional embodying the role of {role_title}.",
            negative_space="Minimal negative space, centered subject."
        )

        team_cards_html += f"""
        <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;overflow:hidden;box-shadow:var(--shadow-card);">
          {render_placeholder(filename, "1/1", "600 × 600 • Square Portrait")}
          <div style="padding:1.5rem;">
            <div style="margin-bottom:0.35rem;">
              <span class="badge badge-demo">Demo Profile</span>
            </div>
            <h3 style="font-size:1.15rem;margin-bottom:0.25rem;color:var(--color-navy);">{role_title}</h3>
            <div style="color:var(--color-teal);font-size:0.8125rem;font-weight:600;margin-bottom:0.75rem;text-transform:uppercase;letter-spacing:0.04em;">{practice}</div>
            <p style="font-size:0.875rem;color:var(--color-text-secondary);line-height:1.5;margin:0;">{bio}</p>
          </div>
        </div>
        """

    team_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Our Team</span>
        </nav>
        <h1>Functional Recruitment &amp; Advisory Team</h1>
        <p class="lead">
          Our functional structure encompasses specialized consultants dedicated to distinct recruitment practices, workforce disciplines, and talent coordination workflows.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> The profiles below represent functional recruitment roles within an agency hierarchy. In accordance with demonstration guidelines, we do not invent individual employee names, personal biographies, educational pedigrees, or placement records. All cards are generic demo role profiles.
          </p>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(260px, 1fr));gap:2rem;">
          {team_cards_html}
        </div>
      </div>
    </section>
    """

    with open("team.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Our Team | Recruitment Agency",
            meta_desc="Explore the functional recruitment practices and specialized talent advisory roles comprising our agency structure.",
            active_page="about",
            body_content=team_html
        ))

    # 4. methodology.html
    img_method = record_image(
        filename="recruitment-methodology-framework.webp",
        page="methodology.html",
        section="Methodology Framework",
        description="Recruitment strategists mapping out candidate evaluation milestones and organizational job matrices on a strategic visual board.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate editorial photography: Talent acquisition consultants analyzing a multi-stage recruitment workflow diagram on an interactive smart board. High-end modern consulting office, warm architectural lighting, focus on collaborative problem solving, clean corporate aesthetic, 50mm lens, authentic business discussion, no artificial stock poses.",
        composition="Medium wide composition focusing on the workflow discussion.",
        camera_angle="Eye-level three-quarter view.",
        lighting="Natural office illumination with soft backlight.",
        background="Minimalist conference room with smart board display.",
        visual_style="Professional corporate advisory aesthetic.",
        color_palette="Navy, teal, soft amber, crisp white.",
        subject_details="Two talent acquisition consultants engaged in strategy planning.",
        negative_space="Right side with subtle depth."
    )

    methodology_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Methodology</span>
        </nav>
        <h1>Recruitment Built Around People, Roles, and Business Requirements</h1>
        <p class="lead">
          A disciplined 5-stage recruitment framework providing structure, rigorous qualification, and measurable accountability across every placement.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Our Guiding Framework</span>
            <h2 class="section-title">The 5-Stage Recruitment Methodology</h2>
            <p>
              Predictable hiring outcomes require systematic execution. Rather than relying on superficial keyword matching, our methodology investigates the operational context of every role to identify candidates who will genuinely succeed and remain.
            </p>
            <p>
              Each phase includes documented checkpoints, employer feedback loops, and candidate touchpoints that minimize misunderstandings and accelerate time-to-productivity.
            </p>
          </div>
          <div>
            {render_placeholder(img_method, "16/9", "1600 × 900 • Methodology Framework")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> This framework illustrates standard recruitment industry best practices. It is not presented as proprietary software or a guaranteed formula for hiring success.
          </p>
        </div>

        <!-- 5 Stages Grid -->
        <div style="display:flex;flex-direction:column;gap:1.75rem;margin-top:3rem;">
          <div style="background:#FFF;border:1px solid var(--color-border);border-left:5px solid var(--color-navy);padding:2rem;border-radius:8px;box-shadow:var(--shadow-sm);">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin:0;">Stage 1 — Understand</h3>
              <span class="badge badge-navy">Discovery &amp; Scoping</span>
            </div>
            <p style="color:var(--color-text-secondary);margin:0;line-height:1.6;">
              We conduct in-depth briefings with hiring managers to understand team structure, business objectives, project deliverables, internal culture, and non-negotiable technical requirements.
            </p>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-left:5px solid var(--color-teal);padding:2rem;border-radius:8px;box-shadow:var(--shadow-sm);">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin:0;">Stage 2 — Define</h3>
              <span class="badge badge-teal">Competency Benchmarking</span>
            </div>
            <p style="color:var(--color-text-secondary);margin:0;line-height:1.6;">
              We translate business needs into comprehensive candidate success profiles, establishing core evaluation criteria, salary market benchmarks, and relevant assessment rubrics.
            </p>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-left:5px solid var(--color-blue);padding:2rem;border-radius:8px;box-shadow:var(--shadow-sm);">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin:0;">Stage 3 — Source</h3>
              <span class="badge badge-navy">Targeted Talent Outreach</span>
            </div>
            <p style="color:var(--color-text-secondary);margin:0;line-height:1.6;">
              Leveraging multi-channel sourcing, professional networks, direct headhunting, and specialized industry talent pools to uncover both active and passive candidates.
            </p>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-left:5px solid var(--color-gold);padding:2rem;border-radius:8px;box-shadow:var(--shadow-sm);">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin:0;">Stage 4 — Evaluate</h3>
              <span class="badge badge-gold">Screening &amp; Assessment</span>
            </div>
            <p style="color:var(--color-text-secondary);margin:0;line-height:1.6;">
              Detailed preliminary interviews, verification of career milestones, practical competency reviews, and cultural alignment checks before submitting shortlists.
            </p>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-left:5px solid var(--color-navy);padding:2rem;border-radius:8px;box-shadow:var(--shadow-sm);">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin:0;">Stage 5 — Coordinate</h3>
              <span class="badge badge-navy">Offer &amp; Onboarding</span>
            </div>
            <p style="color:var(--color-text-secondary);margin:0;line-height:1.6;">
              Facilitating client interviews, consolidating stakeholder feedback, managing offer negotiations, and maintaining contact through notice periods to ensure successful joining.
            </p>
          </div>
        </div>

        <div class="text-center" style="margin-top:4rem;">
          <a href="hire-talent.html" class="btn btn-primary btn-lg">Plan Your Hiring With Our Team</a>
        </div>
      </div>
    </section>
    """

    with open("methodology.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Recruitment Methodology | 5-Stage Framework",
            meta_desc="Explore our 5-stage recruitment methodology: Understand, Define, Source, Evaluate, and Coordinate for consistent hiring results.",
            active_page="employers",
            body_content=methodology_html
        ))

    # 5. recruitment-process.html
    img_process = record_image(
        filename="recruitment-process-workflow-review.webp",
        page="recruitment-process.html",
        section="Process Comparison Overview",
        description="Visual presentation of side-by-side candidate and employer recruitment pathways in a modern advisory setting.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: Talent acquisition consultants reviewing a two-column candidate and employer recruitment journey map in a modern bright conference room. Balanced composition, clean corporate dress, natural sunlight, sharp details, 35mm lens, authentic collaboration.",
        composition="Wide balanced corporate meeting scene.",
        camera_angle="Eye-level.",
        lighting="Natural ambient daylight with warm fill.",
        background="Glass partitioned contemporary office.",
        visual_style="Professional corporate documentary.",
        color_palette="Navy, teal, white, light slate.",
        subject_details="Two talent specialists examining hiring stages.",
        negative_space="Upper area suitable for header elements."
    )

    process_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Recruitment Process</span>
        </nav>
        <h1>A Transparent Recruitment Journey for Both Audiences</h1>
        <p class="lead">
          Understanding the end-to-end recruitment process from both the candidate experience and employer partnership perspectives.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Clear Expectations</span>
            <h2 class="section-title">Two Separate Journeys, One Shared Goal</h2>
            <p>
              Successful recruitment happens when both candidates and hiring organizations have absolute clarity on what occurs at every milestone.
            </p>
            <p>
              Below is the complete 8-stage breakdown showing the synchronized progression between job seekers and hiring teams.
            </p>
          </div>
          <div>
            {render_placeholder(img_process, "16/9", "1600 × 900 • Process Overview")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> Recruitment timelines, specific evaluation rounds, and offer approvals vary based on employer organizational policies and statutory regulations. We do not guarantee placement outcomes or fixed hiring durations.
          </p>
        </div>

        <!-- Side by Side Journeys -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;margin-top:3rem;">
          <!-- Column 1: Candidate Journey -->
          <div style="background:var(--color-surface-light);padding:2rem;border-radius:12px;border:1px solid var(--color-border);border-top:4px solid var(--color-teal);">
            <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.5rem;">
              <span class="badge badge-teal">Candidate Journey</span>
              <h3 style="font-size:1.35rem;margin:0;">The 8 Candidate Steps</h3>
            </div>
            
            <ol style="display:flex;flex-direction:column;gap:1.25rem;">
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>1. Job Discovery:</strong> Identify openings matching your skills through our job board or consultant outreach.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>2. Application / CV Submission:</strong> Submit resume details and career preferences for initial evaluation.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>3. Initial Screening:</strong> Brief discussion reviewing work history, role expectations, and availability.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>4. Recruiter Discussion:</strong> In-depth dialogue on technical strengths, project portfolio, and compensation.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>5. Interview Coordination:</strong> Scheduling briefings and sharing context about employer interview formats.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>6. Employer Interview:</strong> Formal interview rounds with hiring managers and technical panelists.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>7. Selection Process:</strong> Reviewing mutual fit, feedback debrief, and compensation alignment.
              </li>
              <li>
                <strong>8. Offer &amp; Joining:</strong> Formal offer letter acceptance, notice period support, and Day 1 onboarding.
              </li>
            </ol>
            <div style="margin-top:2rem;">
              <a href="register-cv.html" class="btn btn-teal" style="width:100%;">Register Your Profile</a>
            </div>
          </div>

          <!-- Column 2: Employer Journey -->
          <div style="background:var(--color-surface-light);padding:2rem;border-radius:12px;border:1px solid var(--color-border);border-top:4px solid var(--color-navy);">
            <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.5rem;">
              <span class="badge badge-navy">Employer Journey</span>
              <h3 style="font-size:1.35rem;margin:0;">The 8 Employer Steps</h3>
            </div>
            
            <ol style="display:flex;flex-direction:column;gap:1.25rem;">
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>1. Hiring Requirement:</strong> Share headcount specifications, role responsibilities, and target start dates.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>2. Role Definition:</strong> Refine job description, mandatory competencies, and salary positioning.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>3. Recruitment Strategy:</strong> Determine sourcing channels, candidate target pools, and outreach timelines.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>4. Candidate Sourcing:</strong> Active candidate identification across passive databases and direct networks.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>5. Shortlisting:</strong> Review verified candidate profiles with detailed recruiter assessment notes.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>6. Interview Coordination:</strong> Seamless calendar management and feedback consolidation.
              </li>
              <li style="padding-bottom:1rem;border-bottom:1px solid var(--color-border);">
                <strong>7. Selection Support:</strong> Assisting with reference checks and salary negotiation alignment.
              </li>
              <li>
                <strong>8. Joining Coordination:</strong> Continuous engagement through candidate notice periods to ensure arrival.
              </li>
            </ol>
            <div style="margin-top:2rem;">
              <a href="hire-talent.html" class="btn btn-primary" style="width:100%;">Submit Hiring Requisition</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    with open("recruitment-process.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Recruitment Process | Candidate & Employer Pathways",
            meta_desc="Detailed 8-stage breakdown of both the candidate application journey and the employer hiring lifecycle.",
            active_page="candidates",
            body_content=process_html
        ))

    # 6. pricing.html
    img_pricing = record_image(
        filename="pricing-commercial-models.webp",
        page="pricing.html",
        section="Commercial Models Header",
        description="Corporate finance and talent acquisition partners reviewing commercial contract frameworks in an executive boardroom.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: An executive boardroom meeting discussing recruitment partnership terms. Professional hiring director and agency account partner reviewing proposal documentation on a sleek desk. Crisp business attire, elegant office interior, natural sunlight, shallow depth of field, 50mm lens, authentic professional demeanor.",
        composition="Medium shot of corporate consultation.",
        camera_angle="Eye level.",
        lighting="Soft natural window lighting.",
        background="Executive glass office interior.",
        visual_style="Clean corporate commercial photography.",
        color_palette="Navy, charcoal, gold, white.",
        subject_details="Two corporate executives in serious discussion.",
        negative_space="Top portion clear."
    )

    pricing_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Pricing Models</span>
        </nav>
        <h1>Flexible Commercial Recruitment Models</h1>
        <p class="lead">
          Structured recruitment engagement scopes tailored to organizational volume, role specialization, and hiring frequency.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Engagement Options</span>
            <h2 class="section-title">Transparent Service Scopes</h2>
            <p>
              Recruitment requirements differ widely between single specialized placements, rapid project team expansion, and ongoing enterprise hiring. We structure our engagement models to align with your organizational scale.
            </p>
            <p>
              Every model includes dedicated consultant oversight, verified candidate screening, and structured joining support.
            </p>
          </div>
          <div>
            {render_placeholder(img_pricing, "16/9", "1600 × 900 • Commercial Models")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Pricing Notice:</strong> Final recruitment fees and commercial terms depend on the role, hiring volume, service scope, employment arrangement, and agreed engagement terms. We do not publish generic fixed prices without assessing specific organizational requirements.
          </p>
        </div>

        <!-- 3 Service Models Cards -->
        <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:2rem;margin-top:3rem;">
          <!-- Model 1 -->
          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2.25rem;box-shadow:var(--shadow-card);display:flex;flex-direction:column;justify-content:space-between;">
            <div>
              <span class="badge badge-teal" style="margin-bottom:1rem;">Model 01</span>
              <h3 style="font-size:1.4rem;margin-bottom:0.75rem;">Standard Recruitment</h3>
              <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.5rem;">
                Ideal for individual permanent hires, mid-level professional openings, and periodic team expansion.
              </p>
              <ul style="font-size:0.875rem;color:var(--color-text-main);display:flex;flex-direction:column;gap:0.65rem;margin-bottom:2rem;">
                <li>✓ Role profiling &amp; benchmark analysis</li>
                <li>✓ Multi-channel active sourcing</li>
                <li>✓ Candidate qualification &amp; screening</li>
                <li>✓ Interview scheduling coordination</li>
                <li>✓ Offer acceptance support</li>
              </ul>
            </div>
            <div>
              <a href="hire-talent.html" class="btn btn-outline-teal" style="width:100%;">Request Proposal</a>
            </div>
          </div>

          <!-- Model 2 -->
          <div style="background:#FFF;border:2px solid var(--color-teal);border-radius:12px;padding:2.25rem;box-shadow:var(--shadow-md);display:flex;flex-direction:column;justify-content:space-between;position:relative;">
            <div style="position:absolute;top:-12px;right:20px;background:var(--color-teal);color:#FFF;font-size:0.75rem;font-weight:700;padding:0.2rem 0.6rem;border-radius:4px;text-transform:uppercase;">Popular Choice</div>
            <div>
              <span class="badge badge-teal" style="margin-bottom:1rem;">Model 02</span>
              <h3 style="font-size:1.4rem;margin-bottom:0.75rem;">Specialized Talent Acquisition</h3>
              <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.5rem;">
                Designed for high-demand technical roles, niche certifications, or urgent project team ramp-ups.
              </p>
              <ul style="font-size:0.875rem;color:var(--color-text-main);display:flex;flex-direction:column;gap:0.65rem;margin-bottom:2rem;">
                <li>✓ Everything in Standard Recruitment</li>
                <li>✓ Dedicated domain recruitment consultant</li>
                <li>✓ Passive talent headhunting</li>
                <li>✓ Deep technical competency vetting</li>
                <li>✓ SLA-driven candidate shortlist delivery</li>
              </ul>
            </div>
            <div>
              <a href="hire-talent.html" class="btn btn-teal" style="width:100%;">Request Proposal</a>
            </div>
          </div>

          <!-- Model 3 -->
          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2.25rem;box-shadow:var(--shadow-card);display:flex;flex-direction:column;justify-content:space-between;">
            <div>
              <span class="badge badge-navy" style="margin-bottom:1rem;">Model 03</span>
              <h3 style="font-size:1.4rem;margin-bottom:0.75rem;">Custom Partnership</h3>
              <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.5rem;">
                Tailored enterprise partnerships for high-volume recruitment, campus hiring, or managed RPO.
              </p>
              <ul style="font-size:0.875rem;color:var(--color-text-main);display:flex;flex-direction:column;gap:0.65rem;margin-bottom:2rem;">
                <li>✓ Fully embedded or hybrid account team</li>
                <li>✓ Custom workflow &amp; reporting cadence</li>
                <li>✓ High-volume screening coordination</li>
                <li>✓ Candidate onboarding lifecycle support</li>
                <li>✓ Volume-adjusted commercial structure</li>
              </ul>
            </div>
            <div>
              <a href="hire-talent.html" class="btn btn-outline-navy" style="width:100%;">Request Proposal</a>
            </div>
          </div>
        </div>

        <!-- Scope Comparison Table -->
        <div style="margin-top:4rem;">
          <h3 style="font-size:1.4rem;margin-bottom:1.5rem;">Engagement Scope Comparison</h3>
          <div class="table-responsive">
            <table class="comparison-table">
              <thead>
                <tr>
                  <th>Service Feature</th>
                  <th>Standard Recruitment</th>
                  <th>Specialized Acquisition</th>
                  <th>Custom Partnership</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Job Requirement Assessment</strong></td>
                  <td>Included</td>
                  <td>Deep Technical Scoping</td>
                  <td>Comprehensive Workforce Audit</td>
                </tr>
                <tr>
                  <td><strong>Candidate Sourcing Channels</strong></td>
                  <td>Active Databases &amp; Network</td>
                  <td>Active + Passive Headhunting</td>
                  <td>Omni-channel + Campus + RPO</td>
                </tr>
                <tr>
                  <td><strong>Screening Coordination</strong></td>
                  <td>Standard Preliminary</td>
                  <td>Technical Benchmark Review</td>
                  <td>Multi-tiered Custom Rubric</td>
                </tr>
                <tr>
                  <td><strong>Interview Coordination</strong></td>
                  <td>Included</td>
                  <td>Priority Coordination</td>
                  <td>Dedicated Event / Batch Coordination</td>
                </tr>
                <tr>
                  <td><strong>Joining Support</strong></td>
                  <td>Notice Period Follow-up</td>
                  <td>Active Engagement Calls</td>
                  <td>Structured Onboarding Check-in</td>
                </tr>
                <tr>
                  <td><strong>Reporting</strong></td>
                  <td>Weekly Shortlist Updates</td>
                  <td>Bi-weekly Talent Dashboard</td>
                  <td>Custom Analytics &amp; Pipeline Review</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
    """

    with open("pricing.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Pricing Models | Recruitment Agency",
            meta_desc="Explore illustrative commercial recruitment models: Standard Recruitment, Specialized Talent Acquisition, and Custom Partnership.",
            active_page="employers",
            body_content=pricing_html
        ))

    # 7. faq.html
    faq_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Frequently Asked Questions</span>
        </nav>
        <h1>Frequently Asked Questions</h1>
        <p class="lead">
          Find answers regarding our recruitment processes, candidate support, employer hiring options, and engagement models.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container-narrow">
        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> These FAQs provide illustrative insights into standard recruitment agency operations. Individual commercial contracts and specific employer recruitment mandates govern live service terms.
          </p>
        </div>

        <!-- Section 1: For Candidates -->
        <div style="margin-bottom:3.5rem;">
          <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:1.5rem;">
            <span class="badge badge-teal">Job Seekers</span>
            <h2 style="font-size:1.6rem;color:var(--color-navy);margin:0;">Candidate Questions</h2>
          </div>

          <div class="faq-accordion">
            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>How can I search for jobs?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>You can search our opportunities on the Jobs page by role title, industry, employment arrangement (full-time, contract, remote), or geographic location. In this demonstration, all listed vacancies are illustrative samples.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>How can I submit my resume?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Candidates can navigate to the "Register CV" page to enter their contact details, career preferences, and select a resume document (PDF, DOC, DOCX). In this demonstration, files are validated on the front-end only and are not uploaded or stored.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Can I apply for multiple jobs simultaneously?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Yes. Our recruitment consultants evaluate registered profiles against all current active client mandates that match your demonstrated skill set and preferences.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>How does the recruitment process work for candidates?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Our process involves initial profile discovery, preliminary recruiter screening, client shortlist presentation, interview coordination, offer negotiation support, and joining follow-up.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Will I receive application updates?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>In genuine recruitment engagements, consultants provide candid feedback after client screening and interview rounds. We emphasize transparent communication throughout each recruitment stage.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Does candidate registration guarantee a job?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>No. Registration does not guarantee interview scheduling or employment placement. Selection decisions are made solely by hiring organizations based on their role requirements.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Can fresh graduates register their CVs?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Yes. We support early-career professionals and graduates seeking entry-level corporate positions and graduate trainee programs.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Section 2: For Employers -->
        <div style="margin-bottom:3.5rem;">
          <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:1.5rem;">
            <span class="badge badge-navy">Hiring Teams</span>
            <h2 style="font-size:1.6rem;color:var(--color-navy);margin:0;">Employer Questions</h2>
          </div>

          <div class="faq-accordion">
            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>How can I submit a hiring requirement?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>You can submit requisition details via our "Hire Talent" page. In this demonstration, form validation illustrates requirement capture without sending data to a live database.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>What recruitment services do you offer?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>We provide permanent recruitment, contract staffing, temporary workforce solutions, executive search, bulk hiring campaigns, campus recruitment, and talent acquisition consulting.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Can you support bulk hiring campaigns?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Yes. Our bulk hiring solutions include structured screening funnels, interview drive coordination, assessment day management, and batch onboarding coordination.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Do you provide contract staffing solutions?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Yes. We coordinate specialized contractor talent for short-term projects and peak operational periods. Contractual and payroll structures depend on applicable local laws and agreed service models.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>How does the recruitment process work for employers?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>It starts with understanding your role requirements, defining benchmark profiles, sourcing and screening talent, presenting curated shortlists, managing interview logistics, and supporting offer closure.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>How are recruitment fees calculated?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Commercial terms depend on hiring volume, role seniority, level of specialization, and engagement model (contingent, retained, or project-based). Custom proposals are provided after role scoping.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Can you recruit for specialized or confidential roles?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Yes. Our executive search and specialized practices operate under strict non-disclosure procedures for confidential leadership appointments and competitive market hires.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Section 3: General -->
        <div>
          <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:1.5rem;">
            <span class="badge badge-gold">General</span>
            <h2 style="font-size:1.6rem;color:var(--color-navy);margin:0;">General Agency Questions</h2>
          </div>

          <div class="faq-accordion">
            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Which industries do you cover?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>We recruit across Information Technology, Healthcare, Banking &amp; Finance, Engineering, Manufacturing, Sales &amp; Marketing, Logistics &amp; Supply Chain, and related corporate services.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Can I request confidential recruitment support?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Yes. Confidential mandates are insulated through discrete candidate outreach, anonymized role profiles, and secure interview scheduling.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>Do you provide recruitment process outsourcing (RPO)?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>Yes. In full or hybrid RPO arrangements, we manage all or defined parts of an organization's permanent recruitment lifecycle to optimize time-to-hire and talent quality.</p>
              </div>
            </div>

            <div class="faq-item">
              <button class="faq-question" type="button" aria-expanded="false">
                <span>How can I contact the agency?</span>
                <svg class="faq-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="faq-answer">
                <p>You can reach our team via our Contact page, by phone at 0000000000, or via email at demo@example.com during our standard demonstration operating hours.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    with open("faq.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Frequently Asked Questions | Recruitment Agency",
            meta_desc="Categorized answers for candidates and employers about our recruitment services, job search, hiring workflows, and pricing.",
            active_page="candidates",
            body_content=faq_html
        ))

    # 8. contact.html
    img_contact = record_image(
        filename="contact-consultation-hub.webp",
        page="contact.html",
        section="Contact Header",
        description="Recruitment consultants in a welcoming corporate reception setting ready to consult with incoming clients and candidates.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A modern corporate recruitment agency consultation reception. Friendly, impeccably dressed talent coordinator welcoming a business client in an airy contemporary reception lounge with architectural lighting, warm wood accents, and comfortable leather seating. Professional, hospitable, 35mm lens, natural daylight, crisp focus.",
        composition="Wide establishing shot of a modern office reception.",
        camera_angle="Eye level.",
        lighting="Natural ambient daylight with warm architectural accents.",
        background="Contemporary corporate reception with greenery and glass accents.",
        visual_style="Clean, welcoming executive corporate photography.",
        color_palette="Navy, teal, soft wood tones, white.",
        subject_details="Two corporate professionals in professional business attire.",
        negative_space="Ample open space in upper framing."
    )

    contact_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Contact</span>
        </nav>
        <h1>Let's Connect Employers With the Right Talent</h1>
        <p class="lead">
          Get in touch with our recruitment advisory team to discuss hiring mandates, candidate inquiries, or partnership opportunities.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Separate Audience Direct Cards -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:4rem;">
          <div style="background:var(--color-surface-light);border:1px solid var(--color-border);border-top:4px solid var(--color-navy);border-radius:12px;padding:2rem;">
            <span class="badge badge-navy" style="margin-bottom:0.75rem;">Hiring Organizations</span>
            <h3 style="font-size:1.35rem;margin-bottom:0.5rem;">Looking to Hire Talent?</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.5rem;">
              Share your role specifications, skill requirements, and headcount targets. Our recruitment consultants will coordinate a prompt consultation.
            </p>
            <a href="hire-talent.html" class="btn btn-primary">Submit Hiring Requirement</a>
          </div>

          <div style="background:var(--color-surface-light);border:1px solid var(--color-border);border-top:4px solid var(--color-teal);border-radius:12px;padding:2rem;">
            <span class="badge badge-teal" style="margin-bottom:0.75rem;">Job Seekers &amp; Candidates</span>
            <h3 style="font-size:1.35rem;margin-bottom:0.5rem;">Looking for Your Next Opportunity?</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.5rem;">
              Browse our demonstration job listings or submit your resume details for consideration across current and future client openings.
            </p>
            <a href="jobs.html" class="btn btn-teal">Explore Opportunities</a>
          </div>
        </div>

        <div style="display:grid;grid-template-columns:1.2fr 0.8fr;gap:3.5rem;">
          <!-- General Contact Form -->
          <div>
            <h2 style="font-size:1.75rem;margin-bottom:0.5rem;color:var(--color-navy);">Send Us a Message</h2>
            <p style="color:var(--color-text-secondary);margin-bottom:1.75rem;">
              Please complete the inquiry form below. In this static demonstration, entries are validated on the front-end only.
            </p>

            <form id="general-contact-form" novalidate>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;">
                <div class="form-group">
                  <label for="contact-name">Full Name *</label>
                  <input type="text" id="contact-name" class="form-control" placeholder="Your full name" required>
                </div>
                <div class="form-group">
                  <label for="contact-email">Email Address *</label>
                  <input type="email" id="contact-email" class="form-control" placeholder="name@company.com" required>
                </div>
              </div>

              <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;">
                <div class="form-group">
                  <label for="contact-phone">Phone Number</label>
                  <input type="tel" id="contact-phone" class="form-control" placeholder="0000000000">
                </div>
                <div class="form-group">
                  <label for="contact-type">I am an *</label>
                  <select id="contact-type" class="form-select" required>
                    <option value="">Select identity...</option>
                    <option value="Employer">Employer / Hiring Manager</option>
                    <option value="Candidate">Candidate / Job Seeker</option>
                    <option value="Other">Other / General Inquirer</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label for="contact-subject">Subject *</label>
                <input type="text" id="contact-subject" class="form-control" placeholder="Inquiry subject" required>
              </div>

              <div class="form-group">
                <label for="contact-message">Message *</label>
                <textarea id="contact-message" class="form-control" rows="5" placeholder="Share your inquiry or requirement..." required></textarea>
              </div>

              <div style="background:#FFFBEB;border:1px solid #FDE68A;padding:0.75rem 1rem;border-radius:6px;margin-bottom:1.5rem;font-size:0.8125rem;color:#92400E;">
                <strong>Demo Form Only:</strong> Information entered into this prototype is not stored or transmitted to any server.
              </div>

              <button type="submit" class="btn btn-primary btn-lg">Send Message (Demo)</button>
            </form>
          </div>

          <!-- Contact Information Card -->
          <div>
            <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);margin-bottom:2rem;">
              <h3 style="font-size:1.35rem;margin-bottom:1.25rem;color:var(--color-navy);">Demonstration Contact Details</h3>
              
              <div style="display:flex;flex-direction:column;gap:1.25rem;font-size:0.9375rem;">
                <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                  <div style="color:var(--color-teal);margin-top:2px;">📞</div>
                  <div>
                    <strong>Phone Numbers</strong><br>
                    <a href="tel:0000000000" style="color:var(--color-navy);">0000000000</a><br>
                    <a href="tel:0000000000" style="color:var(--color-text-secondary);font-size:0.875rem;">0000000000 (Alternative)</a>
                  </div>
                </div>

                <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                  <div style="color:var(--color-teal);margin-top:2px;">✉️</div>
                  <div>
                    <strong>Email Address</strong><br>
                    <a href="mailto:demo@example.com" style="color:var(--color-navy);">demo@example.com</a>
                  </div>
                </div>

                <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                  <div style="color:var(--color-teal);margin-top:2px;">📍</div>
                  <div>
                    <strong>Office Location</strong><br>
                    <span style="color:var(--color-text-secondary);line-height:1.5;">
                      Plot No. 000, Demo Road, Sample Area,<br>
                      Hyderabad, Telangana – 000000
                    </span>
                  </div>
                </div>

                <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                  <div style="color:var(--color-teal);margin-top:2px;">⏰</div>
                  <div>
                    <strong>Operating Hours</strong><br>
                    <span style="color:var(--color-text-secondary);">
                      Monday–Saturday: 9:00 AM–6:00 PM<br>
                      Sunday: Closed
                    </span>
                  </div>
                </div>
              </div>

              <div style="margin-top:1.5rem;padding-top:1.25rem;border-top:1px solid var(--color-border-light);font-size:0.8125rem;color:var(--color-text-muted);">
                All phone numbers, emails, and address lines above are demonstration placeholders.
              </div>
            </div>

            {render_placeholder(img_contact, "16/9", "1600 × 900 • Reception Hub")}
          </div>
        </div>
      </div>
    </section>
    """

    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Contact Us | Recruitment Agency",
            meta_desc="Connect with our recruitment agency team in Hyderabad, Telangana. Submit hiring needs or explore candidate advisory.",
            active_page="contact",
            body_content=contact_html
        ))

    # 9. privacy-policy.html
    privacy_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Privacy Policy</span>
        </nav>
        <h1>Sample Privacy Policy &amp; Data Notice</h1>
        <p class="lead">
          Demonstration data protection principles and recruitment confidentiality disclosure.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container-narrow">
        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <div>
            <h4 style="font-size:0.95rem;margin-bottom:0.25rem;color:#92400E;">STATIC DEMONSTRATION NOTICE — PLEASE READ</h4>
            <p style="margin:0;">
              This website is a static demonstration prototype. It does NOT collect, transmit, store, or process any real personal data, candidate resumes, or employer hiring details. In a live enterprise implementation, a recruitment agency must establish legally approved privacy notices, statutory compliance mechanisms, and data access policies compliant with GDPR, Indian DPDP Act, and applicable privacy regulations.
            </p>
          </div>
        </div>

        <article style="line-height:1.7;color:var(--color-text-main);">
          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">1. Overview &amp; Scope</h2>
          <p>
            This sample privacy policy outlines the standard framework for handling candidate curriculum vitae (CVs), employer hiring specifications, and website visitor communications within a recruitment and talent acquisition consultancy.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">2. Candidate Information &amp; Resume Handling</h2>
          <p>
            In a genuine operating agency, candidate data collected includes contact details, employment history, academic qualifications, verified certifications, compensation expectations, and references. This information is utilized exclusively for evaluating suitability against relevant client job vacancies with the explicit consent of the candidate.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">3. Employer Inquiries &amp; Requisition Details</h2>
          <p>
            Employer data collected comprises corporate contact names, business email addresses, telephone numbers, organizational headcount requirements, and hiring challenge specifications. Such details are treated confidentially and accessed strictly by designated recruitment account teams.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">4. Demonstration Form Functionality</h2>
          <p>
            All forms present on this prototype (including the Candidate CV Registration form, Employer Hiring Requisition form, and General Contact form) execute purely on the client side via Vanilla JavaScript. No data is dispatched across networks or saved to any database.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">5. Data Retention &amp; Security Principles</h2>
          <p>
            Operational recruitment agencies must implement rigorous technical and organizational safeguards, role-based access permissions, encryption in transit and at rest, and defined document retention schedules ensuring records are purged when no longer lawfully required.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">6. Inquiries &amp; Demonstration Contact</h2>
          <p>
            For questions regarding this demonstration framework, please contact:<br>
            <strong>RECRUITMENT AGENCY (Demo Portal)</strong><br>
            Email: <a href="mailto:demo@example.com">demo@example.com</a><br>
            Phone: 0000000000<br>
            Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000
          </p>
        </article>
      </div>
    </section>
    """

    with open("privacy-policy.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Privacy Policy | Recruitment Agency",
            meta_desc="Sample privacy policy and candidate data notice for the generic recruitment agency demonstration website.",
            active_page="",
            body_content=privacy_html
        ))

    # 10. terms-and-conditions.html
    terms_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Terms and Conditions</span>
        </nav>
        <h1>Sample Terms and Conditions</h1>
        <p class="lead">
          Illustrative terms governing website usage, candidate registration, and recruitment engagement scope.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container-narrow">
        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <div>
            <h4 style="font-size:0.95rem;margin-bottom:0.25rem;color:#92400E;">SAMPLE TERMS — DEMONSTRATION MATERIAL</h4>
            <p style="margin:0;">
              This document contains sample terms created for demonstration purposes. These terms must be reviewed and customized by qualified legal counsel prior to any commercial recruitment deployment.
            </p>
          </div>
        </div>

        <article style="line-height:1.7;color:var(--color-text-main);">
          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">1. Acceptance of Terms</h2>
          <p>
            By accessing or browsing this website, users acknowledge that they are interacting with a generic recruitment agency demonstration portal designed to showcase UI/UX workflows, candidate search systems, and workforce solutions.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">2. Nature of Vacancy Listings</h2>
          <p>
            All job vacancies showcased on this website are designated as "DEMO VACANCY — NOT A VERIFIED LIVE JOB". They are created exclusively for testing search filters, layout responsiveness, and role description presentation. They do not constitute actual offers of employment.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">3. Candidate Registration Conditions</h2>
          <p>
            Submitting information via candidate forms does not establish an employment contract or guarantee interview opportunities, recruiter representation, or job placement. Hiring decisions rest entirely with potential employer organizations.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">4. Employer Requisition Conditions</h2>
          <p>
            Submitting hiring requirements creates no commercial obligation or contractual liability until a separate, formal Master Services Agreement (MSA) or Statement of Work (SOW) is mutually executed between the agency and the hiring organization.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">5. Limitation of Liability</h2>
          <p>
            Under no circumstances shall the creators or owners of this demonstration platform be liable for any direct, indirect, incidental, or consequential damages resulting from the use or inability to use the illustrative features or content presented herein.
          </p>

          <h2 style="font-size:1.5rem;margin-top:2rem;margin-bottom:1rem;">6. Contact Details</h2>
          <p>
            For legal or administrative questions regarding this demonstration:<br>
            <strong>RECRUITMENT AGENCY</strong><br>
            Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000<br>
            Email: <a href="mailto:demo@example.com">demo@example.com</a> &bull; Phone: 0000000000
          </p>
        </article>
      </div>
    </section>
    """

    with open("terms-and-conditions.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Terms & Conditions | Recruitment Agency",
            meta_desc="Sample terms and conditions governing website usage and recruitment engagement scope.",
            active_page="",
            body_content=terms_html
        ))

    print("Core pages (1-10) generated successfully.")

if __name__ == "__main__":
    build_core()
