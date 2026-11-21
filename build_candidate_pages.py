"""
Generates Candidate Pages (28-34):
28. jobs.html
29. job-details.html
30. candidates.html
31. register-cv.html
32. career-advice.html
33. resources.html
34. careers.html
"""
import os
from builder_core import wrap_page, render_placeholder, record_image

def build_candidate_pages():
    # 28. jobs.html
    jobs_html = """
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Find Jobs</span>
        </nav>
        <h1>Find Opportunities That Match Your Skills</h1>
        <p class="lead">
          Explore curated demonstration vacancies across diverse industries, employment models, and technical disciplines.
        </p>
      </div>
    </section>

    <section class="section bg-warm">
      <div class="container">
        <!-- Prominent Demo Disclaimer -->
        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
          <div>
            <h4 style="font-size:0.95rem;margin-bottom:0.25rem;color:#92400E;">IMPORTANT DEMONSTRATION NOTICE — NOT VERIFIED LIVE JOBS</h4>
            <p style="margin:0;">
              All vacancies listed below are illustrative demonstration samples created exclusively to test and showcase search, filter, and role overview interfaces. In accordance with strict authenticity rules, we do not invent active vacancies, real employer names, contact details, or salary commitments.
            </p>
          </div>
        </div>

        <!-- Filter Controls Box -->
        <div class="job-search-box">
          <form id="jobs-search-form">
            <div style="display:grid;grid-template-columns:2fr 1.2fr 1.2fr 1.2fr 1fr;gap:1rem;align-items:flex-end;">
              <div class="form-group" style="margin-bottom:0;">
                <label for="search-keyword">Role Keyword / Skill</label>
                <input type="text" id="search-keyword" class="form-control" placeholder="e.g. Developer, Analyst, HR, Sales">
              </div>

              <div class="form-group" style="margin-bottom:0;">
                <label for="filter-location">Location</label>
                <select id="filter-location" class="form-select">
                  <option value="">All Locations</option>
                  <option value="Hyderabad">Hyderabad</option>
                  <option value="Bangalore">Bangalore</option>
                  <option value="Mumbai">Mumbai</option>
                  <option value="Chennai">Chennai</option>
                  <option value="Pune">Pune</option>
                  <option value="Remote">Remote</option>
                </select>
              </div>

              <div class="form-group" style="margin-bottom:0;">
                <label for="filter-industry">Industry</label>
                <select id="filter-industry" class="form-select">
                  <option value="">All Industries</option>
                  <option value="Information Technology">Information Technology</option>
                  <option value="Banking and Finance">Banking &amp; Finance</option>
                  <option value="Manufacturing">Manufacturing</option>
                  <option value="Engineering">Engineering</option>
                  <option value="Logistics and Supply Chain">Logistics &amp; Supply Chain</option>
                  <option value="Sales and Marketing">Sales &amp; Marketing</option>
                </select>
              </div>

              <div class="form-group" style="margin-bottom:0;">
                <label for="filter-type">Employment Type</label>
                <select id="filter-type" class="form-select">
                  <option value="">All Types</option>
                  <option value="Full-time">Full-time</option>
                  <option value="Contract">Contract</option>
                </select>
              </div>

              <div class="form-group" style="margin-bottom:0;">
                <label for="filter-experience">Experience</label>
                <select id="filter-experience" class="form-select">
                  <option value="">Any Experience</option>
                  <option value="1-3">1-3 Years</option>
                  <option value="2-4">2-4 Years</option>
                  <option value="3-5">3-5 Years</option>
                  <option value="4-7">4-7 Years</option>
                </select>
              </div>
            </div>

            <div style="display:flex;justify-content:space-between;align-items:center;margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--color-border-light);flex-wrap:wrap;gap:1rem;">
              <div id="results-count" style="font-size:0.9375rem;font-weight:600;color:var(--color-navy);">
                Showing 8 demonstration vacancies
              </div>
              <div style="display:flex;gap:0.75rem;">
                <button type="button" id="clear-filters-btn" class="btn btn-sm btn-outline-navy">Clear All Filters</button>
                <button type="submit" class="btn btn-sm btn-teal">Apply Filters</button>
              </div>
            </div>
          </form>
        </div>

        <!-- Job Cards Container (Populated via assets/js/job-search.js) -->
        <div id="jobs-list-container" style="min-height:400px;">
          <!-- Fallback or dynamic content rendered via JavaScript -->
        </div>

        <div style="margin-top:3.5rem;text-align:center;background:#FFF;padding:2.5rem;border-radius:12px;border:1px solid var(--color-border);">
          <h3 style="font-size:1.35rem;margin-bottom:0.5rem;color:var(--color-navy);">Don't See a Matching Opportunity?</h3>
          <p style="color:var(--color-text-secondary);max-width:550px;margin:0 auto 1.5rem;font-size:0.9375rem;">
            Submit your resume details to our general talent pool. In genuine recruitment operations, consultants reach out directly when matching client openings emerge.
          </p>
          <a href="register-cv.html" class="btn btn-teal">Register Your CV Profile</a>
        </div>
      </div>
    </section>
    """

    with open("jobs.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Search Job Opportunities | Recruitment Agency",
            meta_desc="Explore illustrative demonstration job opportunities. Filter vacancies by keyword, location, industry, and experience level.",
            active_page="jobs",
            body_content=jobs_html
        ))

    # 29. job-details.html
    img_job_detail = record_image(
        filename="job-detail-workplace-preview.webp",
        page="job-details.html",
        section="Job Details Preview",
        description="Clean, modern collaborative office workplace showing contemporary desk setup and meeting space.",
        aspect_ratio="16/9",
        resolution="1200x675",
        orientation="Landscape",
        prompt="Corporate photography: A modern, collaborative corporate office environment. Contemporary wood and white desks, ergonomic chairs, subtle natural daylight, warm potted plants, 35mm lens, sharp focus, authentic workspace aesthetic.",
        composition="Wide environmental corporate setting.",
        camera_angle="Eye level.",
        lighting="Soft natural ambient light.",
        background="Contemporary open office with tasteful architectural details.",
        visual_style="Clean corporate interior photography.",
        color_palette="Warm wood, navy, white, soft green.",
        subject_details="Modern workplace setting.",
        negative_space="Upper section clear."
    )

    job_details_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <a href="jobs.html">Jobs</a>
          <span class="separator">/</span>
          <span id="detail-breadcrumb-title">Job Details</span>
        </nav>
        <div style="margin-bottom:0.75rem;">
          <span class="badge badge-demo">DEMO VACANCY — NOT A VERIFIED LIVE JOB</span>
        </div>
        <h1 id="detail-job-title">Frontend Developer — Demo Vacancy</h1>
        <p class="lead" id="detail-job-employer">
          Confidential Technology Client &bull; Information Technology Practice
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <!-- Main Job Details Grid -->
        <div style="display:grid;grid-template-columns:1.35fr 0.65fr;gap:3.5rem;">
          <!-- Left Column: Job Description & Details -->
          <div>
            <div class="demo-alert-banner">
              <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
              <div>
                <h4 style="font-size:0.95rem;margin-bottom:0.25rem;color:#92400E;">ILLUSTRATIVE SAMPLE VACANCY</h4>
                <p style="margin:0;">
                  This is a sample vacancy layout. In genuine recruitment deployments, this page renders verified job specifications, actual employer identity (or confidential mandate disclosure), and valid expiry schedules. JobPosting structured data is omitted per SEO integrity rules.
                </p>
              </div>
            </div>

            <!-- Job Summary -->
            <div style="margin-bottom:2.5rem;">
              <h2 style="font-size:1.5rem;color:var(--color-navy);margin-bottom:1rem;">Role Summary</h2>
              <p style="line-height:1.7;color:var(--color-text-secondary);font-size:1rem;">
                This illustrative role represents a mid-level frontend engineering position responsible for developing responsive web portals, optimizing user interface performance, and collaborating closely with design and backend API squads.
              </p>
            </div>

            <!-- Key Responsibilities -->
            <div style="margin-bottom:2.5rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin-bottom:1rem;">Key Responsibilities</h3>
              <ul style="display:flex;flex-direction:column;gap:0.75rem;font-size:0.95rem;color:var(--color-text-secondary);line-height:1.6;">
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Develop high-performance, accessible, and responsive client-side web interfaces.</li>
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Collaborate with UX designers and product managers to translate wireframes into interactive prototypes.</li>
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Ensure cross-browser compatibility, web accessibility (WCAG), and search engine optimization.</li>
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Participate in peer code reviews, continuous integration workflows, and unit testing.</li>
              </ul>
            </div>

            <!-- Required Qualifications & Skills -->
            <div style="margin-bottom:2.5rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin-bottom:1rem;">Required Qualifications &amp; Skills</h3>
              <ul style="display:flex;flex-direction:column;gap:0.75rem;font-size:0.95rem;color:var(--color-text-secondary);line-height:1.6;">
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> 3 to 5 years of demonstrated commercial experience in modern web frontend engineering.</li>
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Mastery of semantic HTML5, modern CSS3 architectures (Flexbox, Grid), and Vanilla JavaScript (ES6+).</li>
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Working knowledge of RESTful API consumption and asynchronous data handling.</li>
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Proficiency with Git version control and collaborative branching methodologies.</li>
              </ul>
            </div>

            <!-- Preferred Skills -->
            <div style="margin-bottom:2.5rem;">
              <h3 style="font-size:1.35rem;color:var(--color-navy);margin-bottom:1rem;">Preferred Skills</h3>
              <ul style="display:flex;flex-direction:column;gap:0.75rem;font-size:0.95rem;color:var(--color-text-secondary);line-height:1.6;">
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Experience optimizing web vitals, page load speeds, and client-side caching.</li>
                <li style="display:flex;gap:0.5rem;"><span style="color:var(--color-teal);font-weight:bold;">•</span> Familiarity with containerization tools (Docker) and build tooling.</li>
              </ul>
            </div>

            <!-- Job Expiry Strategy Notice -->
            <div style="background:var(--color-surface-light);padding:1.5rem;border-radius:8px;border:1px solid var(--color-border);font-size:0.875rem;color:var(--color-text-secondary);line-height:1.6;">
              <strong>Vacancy Lifecycle &amp; Expiry Notice:</strong> Genuine recruitment listings on our platform feature active closing dates. Once an employer concludes recruitment or accepts an offer, the listing is automatically unlisted or archived to prevent obsolete candidate submissions.
            </div>
          </div>

          <!-- Right Column: Role Overview Card & Actions -->
          <div>
            <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);position:sticky;top:100px;">
              <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:1.25rem;">Opportunity Overview</h3>

              <div style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2rem;font-size:0.9375rem;">
                <div>
                  <span style="color:var(--color-text-muted);font-size:0.8125rem;display:block;">Location</span>
                  <strong>Hyderabad, India (Hybrid)</strong>
                </div>
                <div>
                  <span style="color:var(--color-text-muted);font-size:0.8125rem;display:block;">Employment Arrangement</span>
                  <strong>Full-time Permanent</strong>
                </div>
                <div>
                  <span style="color:var(--color-text-muted);font-size:0.8125rem;display:block;">Experience Required</span>
                  <strong>3-5 Years</strong>
                </div>
                <div>
                  <span style="color:var(--color-text-muted);font-size:0.8125rem;display:block;">Compensation</span>
                  <strong>Standard Industry Competitive</strong>
                </div>
                <div>
                  <span style="color:var(--color-text-muted);font-size:0.8125rem;display:block;">Listing Status</span>
                  <span class="badge badge-demo">Illustrative Demo</span>
                </div>
              </div>

              <div style="display:flex;flex-direction:column;gap:0.75rem;">
                <a href="register-cv.html" class="btn btn-teal btn-lg" style="width:100%;">Apply for This Role (Demo)</a>
                <a href="jobs.html" class="btn btn-outline-navy btn-sm" style="width:100%;">Back to All Jobs</a>
              </div>

              <div style="margin-top:1.5rem;padding-top:1.25rem;border-top:1px solid var(--color-border-light);font-size:0.8125rem;color:var(--color-text-muted);text-align:center;">
                Submissions in demo mode are validated on the front-end only without data storage.
              </div>
            </div>

            <div style="margin-top:2rem;">
              {render_placeholder(img_job_detail, "16/9", "1200 × 675 • Workplace Preview")}
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    with open("job-details.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Job Details | Recruitment Agency",
            meta_desc="Individual demonstration job vacancy specifications, responsibilities, qualification requirements, and application procedures.",
            active_page="jobs",
            body_content=job_details_html
        ))

    # 30. candidates.html
    img_candidate_hub = record_image(
        filename="candidate-career-growth-path.webp",
        page="candidates.html",
        section="Candidates Hub Hero",
        description="A talent consultant having a positive career transition advisory session with an ambitious professional.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A career development consultation in a bright architectural office. An experienced talent advisor reviewing career pathways and interview readiness strategies with a job candidate. Natural smiling engagement, modern office aesthetic, 50mm lens, authentic interaction.",
        composition="Wide balanced corporate consultation scene.",
        camera_angle="Eye level.",
        lighting="Natural ambient daylight with warm fill.",
        background="Contemporary office consultation room.",
        visual_style="Clean executive corporate photography.",
        color_palette="Teal, navy, warm wood, white.",
        subject_details="Two corporate professionals in career advisory discussion.",
        negative_space="Upper area open."
    )

    candidates_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Candidates</span>
        </nav>
        <h1>Your Next Career Move Starts Here</h1>
        <p class="lead">
          Guiding professionals through job discovery, interview preparation, and transparent career opportunities across premier organizations.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Candidate Care</span>
            <h2 class="section-title">Supportive, Respectful Recruitment Representation</h2>
            <p>
              Navigating job changes is among the most pivotal decisions in professional life. We treat candidates as long-term partners, providing honest feedback, market compensation guidance, and preparation before every employer interview.
            </p>
            <p>
              Whether you are an experienced software architect, certified accountant, healthcare professional, or entry-level graduate, our candidate services are designed to present your capabilities accurately and respectfully.
            </p>
            <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:2rem;">
              <a href="jobs.html" class="btn btn-teal btn-lg">Browse Opportunities</a>
              <a href="register-cv.html" class="btn btn-outline-teal btn-lg">Submit Your CV</a>
            </div>
          </div>
          <div>
            {render_placeholder(img_candidate_hub, "16/9", "1600 × 900 • Candidate Hub")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Candidate Notice:</strong> Registration and advisory services provided by our agency are free of charge for job seekers. We never promise guaranteed job placement, interview selection, or specific compensation offers.
          </p>
        </div>

        <!-- 6 Candidate Resource Pillars -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:2rem;margin-top:4rem;">
          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);">
            <div style="width:48px;height:48px;background:var(--color-teal-light);color:var(--color-teal);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">1. Search Opportunities</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.25rem;">
              Explore illustrative vacancies across sectors, filtering by location, technical skill, and employment arrangement.
            </p>
            <a href="jobs.html" style="font-weight:600;font-size:0.875rem;color:var(--color-teal);">Search Jobs &rarr;</a>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);">
            <div style="width:48px;height:48px;background:var(--color-teal-light);color:var(--color-teal);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">2. Register Your CV</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.25rem;">
              Submit your curriculum vitae and career preferences for consideration across current and upcoming client hiring mandates.
            </p>
            <a href="register-cv.html" style="font-weight:600;font-size:0.875rem;color:var(--color-teal);">Register CV &rarr;</a>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);">
            <div style="width:48px;height:48px;background:var(--color-teal-light);color:var(--color-teal);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">3. Career Advice &amp; Guides</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.25rem;">
              Explore practical guides covering resume optimization, behavioral interview answers, and salary negotiation tactics.
            </p>
            <a href="career-advice.html" style="font-weight:600;font-size:0.875rem;color:var(--color-teal);">Read Advice &rarr;</a>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);">
            <div style="width:48px;height:48px;background:var(--color-teal-light);color:var(--color-teal);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">4. Candidate Journey</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.25rem;">
              Review the detailed 8-stage candidate lifecycle from discovery and screening to employer interviews and Day 1 onboarding.
            </p>
            <a href="recruitment-process.html" style="font-weight:600;font-size:0.875rem;color:var(--color-teal);">View Journey &rarr;</a>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);">
            <div style="width:48px;height:48px;background:var(--color-teal-light);color:var(--color-teal);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">5. Templates &amp; Checklists</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.25rem;">
              Access candidate preparation templates, interview evaluation rubrics, and resume formatting checklists.
            </p>
            <a href="resources.html" style="font-weight:600;font-size:0.875rem;color:var(--color-teal);">View Templates &rarr;</a>
          </div>

          <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);">
            <div style="width:48px;height:48px;background:var(--color-teal-light);color:var(--color-teal);border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;">
              <svg style="width:24px;height:24px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">6. Candidate FAQs</h3>
            <p style="color:var(--color-text-secondary);font-size:0.9375rem;line-height:1.6;margin-bottom:1.25rem;">
              Common inquiries regarding data privacy, multiple applications, fresh graduate eligibility, and feedback timelines.
            </p>
            <a href="faq.html" style="font-weight:600;font-size:0.875rem;color:var(--color-teal);">Read FAQs &rarr;</a>
          </div>
        </div>
      </div>
    </section>
    """

    with open("candidates.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Candidate Hub | Recruitment Agency",
            meta_desc="Candidate services, job search discovery, CV registration, career advice, and interview preparation resources.",
            active_page="candidates",
            body_content=candidates_html
        ))

    # 31. register-cv.html
    img_reg_cv = record_image(
        filename="candidate-cv-registration-hero.webp",
        page="register-cv.html",
        section="CV Registration Header",
        description="A professional candidate preparing resume credentials and portfolio documentation for recruitment agency submission.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A young professional at a clean wooden desk with a laptop and organized resume papers, thoughtfully reviewing career credentials in a well-lit modern home office or coworking hub. Soft ambient light, 50mm lens, sharp focus, authentic concentration.",
        composition="Medium shot of focused professional at desk.",
        camera_angle="Eye level.",
        lighting="Natural window light.",
        background="Minimalist contemporary workspace.",
        visual_style="Clean corporate commercial photography.",
        color_palette="Warm wood, navy, white, soft amber.",
        subject_details="Focused professional reviewing career credentials.",
        negative_space="Upper section clear."
    )

    register_cv_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <a href="candidates.html">Candidates</a>
          <span class="separator">/</span>
          <span>Register CV</span>
        </nav>
        <h1>Candidate Profile Registration</h1>
        <p class="lead">
          Share your professional background, preferred job roles, and resume document for consideration across client hiring mandates.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.2fr 0.8fr;gap:3.5rem;">
          <!-- Registration Form -->
          <div>
            <div class="demo-alert-banner">
              <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
              <div>
                <h4 style="font-size:0.95rem;margin-bottom:0.25rem;color:#92400E;">DEMONSTRATION FORM ONLY — NO DATA TRANSMITTED</h4>
                <p style="margin:0;">
                  This is a frontend demonstration. Your entered information and selected resume file are validated in your local browser and are <strong>never uploaded, transmitted, emailed, or stored</strong>.
                </p>
              </div>
            </div>

            <form id="candidate-registration-form" novalidate>
              <!-- Personal Details -->
              <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:1rem;">1. Personal &amp; Contact Information</h3>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-bottom:1.5rem;">
                <div class="form-group">
                  <label for="cand-name">Full Name *</label>
                  <input type="text" id="cand-name" class="form-control" placeholder="Jane Doe" required>
                </div>
                <div class="form-group">
                  <label for="cand-email">Email Address *</label>
                  <input type="email" id="cand-email" class="form-control" placeholder="jane.doe@example.com" required>
                </div>
              </div>

              <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-bottom:2rem;">
                <div class="form-group">
                  <label for="cand-phone">Phone Number *</label>
                  <input type="tel" id="cand-phone" class="form-control" placeholder="0000000000" required>
                </div>
                <div class="form-group">
                  <label for="cand-location">Current Location *</label>
                  <input type="text" id="cand-location" class="form-control" placeholder="e.g. Hyderabad, India" required>
                </div>
              </div>

              <!-- Career Preferences -->
              <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:1rem;">2. Career Preferences &amp; Experience</h3>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-bottom:1.5rem;">
                <div class="form-group">
                  <label for="cand-role">Preferred Job Role *</label>
                  <input type="text" id="cand-role" class="form-control" placeholder="e.g. Frontend Developer" required>
                </div>
                <div class="form-group">
                  <label for="cand-industry">Industry *</label>
                  <select id="cand-industry" class="form-select" required>
                    <option value="">Select industry...</option>
                    <option value="Information Technology">Information Technology</option>
                    <option value="Healthcare">Healthcare</option>
                    <option value="Banking and Finance">Banking and Finance</option>
                    <option value="Engineering">Engineering</option>
                    <option value="Manufacturing">Manufacturing</option>
                    <option value="Sales and Marketing">Sales and Marketing</option>
                    <option value="Logistics and Supply Chain">Logistics and Supply Chain</option>
                  </select>
                </div>
              </div>

              <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1rem;margin-bottom:1.5rem;">
                <div class="form-group">
                  <label for="cand-exp">Experience Level *</label>
                  <select id="cand-exp" class="form-select" required>
                    <option value="">Select...</option>
                    <option value="Fresher">Fresher / Graduate</option>
                    <option value="1-3">1-3 Years</option>
                    <option value="3-5">3-5 Years</option>
                    <option value="5-8">5-8 Years</option>
                    <option value="8+">8+ Years</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="cand-status">Employment Status *</label>
                  <select id="cand-status" class="form-select" required>
                    <option value="">Select...</option>
                    <option value="Employed">Currently Employed</option>
                    <option value="Notice">Serving Notice Period</option>
                    <option value="Available">Immediately Available</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="cand-type">Preferred Type *</label>
                  <select id="cand-type" class="form-select" required>
                    <option value="">Select...</option>
                    <option value="Full-time">Full-time</option>
                    <option value="Contract">Contract</option>
                    <option value="Any">Flexible / Any</option>
                  </select>
                </div>
              </div>

              <div class="form-group" style="margin-bottom:2rem;">
                <label for="cand-skills">Key Technical or Functional Skills *</label>
                <input type="text" id="cand-skills" class="form-control" placeholder="e.g. JavaScript, HTML5, CSS3, REST APIs, Git" required>
                <div style="font-size:0.8125rem;color:var(--color-text-muted);margin-top:0.25rem;">Separate multiple skills with commas.</div>
              </div>

              <!-- Resume Upload UI -->
              <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:1rem;">3. Resume / CV Document</h3>
              <div class="file-dropzone" id="file-dropzone">
                <input type="file" id="resume-file-input" accept=".pdf,.doc,.docx" aria-label="Upload Resume File">
                <svg style="width:36px;height:36px;color:var(--color-teal);margin:0 auto 0.75rem;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg>
                <div style="font-weight:600;color:var(--color-navy);margin-bottom:0.25rem;">Drag &amp; drop your resume file here, or click to browse</div>
                <div style="font-size:0.8125rem;color:var(--color-text-muted);">Accepted formats: PDF, DOC, DOCX &bull; Maximum file size: 5MB</div>
              </div>

              <!-- File Preview Card -->
              <div class="file-preview-card" id="file-preview-card">
                <div class="file-preview-info">
                  <svg style="width:28px;height:28px;color:var(--color-teal);" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                  <div>
                    <strong id="file-name-display" style="font-size:0.9375rem;color:var(--color-navy);">resume.pdf</strong>
                    <div id="file-size-display" style="font-size:0.75rem;color:var(--color-text-muted);">142 KB</div>
                  </div>
                </div>
                <button type="button" class="btn-file-clear" id="clear-file-btn">Remove File</button>
              </div>

              <div id="file-error-msg" class="form-feedback error" style="display:none;margin-top:0.5rem;"></div>

              <div style="margin-top:2rem;margin-bottom:1.5rem;font-size:0.8125rem;color:var(--color-text-secondary);line-height:1.5;">
                By clicking "Submit Registration (Demo)", you acknowledge that this is a simulated frontend prototype. Read our <a href="privacy-policy.html">Candidate Privacy Notice</a> for details on operational data security.
              </div>

              <button type="submit" class="btn btn-teal btn-lg">Submit Registration (Demo)</button>
            </form>
          </div>

          <!-- Right Column: Registration Guidance -->
          <div>
            <div style="background:var(--color-surface-light);border:1px solid var(--color-border);border-radius:12px;padding:2rem;margin-bottom:2rem;">
              <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:1rem;">Candidate Registration Guidance</h3>
              <ul style="display:flex;flex-direction:column;gap:1rem;font-size:0.9rem;color:var(--color-text-secondary);line-height:1.5;">
                <li>
                  <strong>Accurate Role Preferences:</strong> Specifying targeted titles ensures relevant recruiter alignment without mismatched inquiries.
                </li>
                <li>
                  <strong>Highlight Key Technologies:</strong> Mentioning exact frameworks, tools, or regulatory licenses speeds up technical qualification.
                </li>
                <li>
                  <strong>Notice Period Transparency:</strong> Stating immediate availability or official notice timelines helps match client start dates.
                </li>
              </ul>
            </div>

            {render_placeholder(img_reg_cv, "16/9", "1600 × 900 • Registration Overview")}
          </div>
        </div>
      </div>
    </section>
    """

    with open("register-cv.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Register Your CV | Recruitment Agency",
            meta_desc="Candidate registration demonstration form. Validate resume uploads (PDF/DOC/DOCX) and career preferences.",
            active_page="candidates",
            body_content=register_cv_html
        ))

    # 32. career-advice.html
    img_advice = record_image(
        filename="career-advice-resource-center.webp",
        page="career-advice.html",
        section="Career Advice Hub Banner",
        description="A group of ambitious candidates attending an interactive resume and interview masterclass led by an experienced recruitment advisor.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A modern career coaching seminar in a stylish open-plan workspace. A professional recruitment mentor guiding job seekers through interview strategy slides and resume feedback. Engaging, natural daylight, diverse participants, 35mm lens, sharp focus.",
        composition="Wide balanced corporate seminar scene.",
        camera_angle="Eye level.",
        lighting="Natural ambient daylight.",
        background="Modern learning hub with presentation display.",
        visual_style="Clean executive corporate photography.",
        color_palette="Teal, navy, white, soft gold.",
        subject_details="Professional mentor and engaged candidates.",
        negative_space="Upper quadrant open."
    )

    career_topics = [
        ("Resume Writing & ATS Optimization", "resume", "How to structure technical resumes, quantify career impact, and avoid common applicant tracking formatting pitfalls."),
        ("Behavioral Interview Preparation", "interview", "Mastering the STAR framework to articulate situational leadership, conflict resolution, and technical problem solving."),
        ("Strategic Job Search Architecture", "strategy", "Structuring a disciplined daily job search routine, targeting niche industry boards, and building recruiter relationships."),
        ("Optimizing Your LinkedIn Profile", "branding", "Transforming your LinkedIn presence into a magnetic passive sourcing profile with clear headline positioning."),
        ("Long-Term Career Path Planning", "career", "Evaluating promotion tracks, lateral domain transitions, and when to pursue specialized certifications."),
        ("Essential Soft Skills in High Demand", "skills", "Developing cross-functional communication, asynchronous teamwork, and proactive executive presence."),
        ("Salary Negotiation Preparation", "negotiation", "Benchmarking market compensation, understanding total rewards packages, and timing offer discussions."),
        ("Fresh Graduate Job Search Guide", "graduates", "Translating academic projects, internships, and coursework into compelling entry-level candidate profiles."),
        ("Navigating a Career Change", "transition", "Identifying transferable core competencies and crafting persuasive narratives for cross-industry shifts."),
        ("Workplace Readiness & Day 1 Success", "readiness", "Establishing professional credibility, understanding organizational dynamics, and mastering onboarding milestones.")
    ]

    advice_cards_html = ""
    for title, cat, summary in career_topics:
        advice_cards_html += f"""
        <div class="filterable-card" data-category="{cat}" style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);display:flex;flex-direction:column;justify-content:space-between;">
          <div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
              <span class="badge badge-teal">{cat.upper()}</span>
              <span style="font-size:0.75rem;color:var(--color-text-muted);">Demo Material</span>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">{title}</h3>
            <p style="font-size:0.9375rem;color:var(--color-text-secondary);line-height:1.6;margin-bottom:1.5rem;">{summary}</p>
          </div>
          <div>
            <a href="article-details.html" class="btn btn-sm btn-outline-teal" style="width:100%;">Read Detailed Guide &rarr;</a>
          </div>
        </div>
        """

    career_advice_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <a href="candidates.html">Candidates</a>
          <span class="separator">/</span>
          <span>Career Advice</span>
        </nav>
        <h1>Candidate Career Resource Center</h1>
        <p class="lead">
          Actionable guidance on resume crafting, technical interview performance, compensation benchmarking, and career trajectory management.
        </p>
      </div>
    </section>

    <section class="section bg-warm">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Practical Career Insights</span>
            <h2 class="section-title">Knowledge to Accelerate Your Career</h2>
            <p>
              Navigating competitive hiring markets requires more than sending generic applications. Our career guides distill recruiter observations from thousands of candidate screening sessions into practical, actionable steps.
            </p>
          </div>
          <div>
            {render_placeholder(img_advice, "16/9", "1600 × 900 • Career Advice Hub")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> Articles and resource guides featured in this resource center are demonstration materials created for educational presentation.
          </p>
        </div>

        <!-- Filter Controls -->
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2rem;flex-wrap:wrap;gap:1rem;">
          <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
            <button type="button" class="btn btn-sm btn-outline-navy filter-tab-btn active" data-category="all">All Topics</button>
            <button type="button" class="btn btn-sm btn-outline-navy filter-tab-btn" data-category="resume">Resume</button>
            <button type="button" class="btn btn-sm btn-outline-navy filter-tab-btn" data-category="interview">Interview</button>
            <button type="button" class="btn btn-sm btn-outline-navy filter-tab-btn" data-category="strategy">Strategy</button>
            <button type="button" class="btn btn-sm btn-outline-navy filter-tab-btn" data-category="negotiation">Negotiation</button>
          </div>
          <div style="max-width:280px;width:100%;">
            <input type="text" class="form-control filter-search-input" placeholder="Search guides...">
          </div>
        </div>

        <!-- 10 Advice Cards Grid -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:2rem;">
          {advice_cards_html}
        </div>
      </div>
    </section>
    """

    with open("career-advice.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Career Advice & Guides | Recruitment Agency",
            meta_desc="10 actionable career guides on resume writing, behavioral interview prep, salary negotiation, and career planning.",
            active_page="candidates",
            body_content=career_advice_html
        ))

    # 33. resources.html
    img_resources = record_image(
        filename="resources-library-banner.webp",
        page="resources.html",
        section="Resources Library Header",
        description="Recruitment library workspace with neatly categorized hiring templates, interview evaluation forms, and workforce planning checklists.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A corporate talent resources desk with neatly bound checklists, interview evaluation matrices, and digital tablets in a bright corporate library or executive training suite. Professional, orderly, 50mm lens, natural daylight.",
        composition="Wide establishing shot of corporate workspace.",
        camera_angle="Eye level.",
        lighting="Natural ambient daylight with warm fill.",
        background="Modern corporate library or training center.",
        visual_style="Clean executive corporate photography.",
        color_palette="Navy, teal, crisp white, slate.",
        subject_details="Corporate talent resources setup.",
        negative_space="Upper section clear."
    )

    resource_items = [
        ("Resume Preparation Checklist", "Candidate", "A 15-point audit covering contact clarity, bullet structure, ATS formatting, and technical skill categorizations."),
        ("Interview Preparation Guide", "Candidate", "Structured question breakdown, STAR technique examples, and essential questions to ask hiring authorities."),
        ("Job Description Template", "Employer", "Standardized job requisition template establishing clear deliverables, role hierarchy, and essential qualifications."),
        ("Recruitment Planning Checklist", "Employer", "Pre-search alignment framework detailing timeline milestones, hiring committee roles, and SLA agreements."),
        ("Candidate Screening Template", "Shared", "Objective telephone/video preliminary screening scorecard evaluating communication, technical scope, and expectations."),
        ("Interview Evaluation Form", "Employer", "Structured candidate scoring rubric for hiring managers to rate competency, problem solving, and cultural alignment."),
        ("Employer Hiring Requirement Form", "Employer", "Standardized intake document for corporate departmental heads requesting new headcount or replacements."),
        ("Candidate Onboarding Checklist", "Employer", "Day 1 to Day 90 integration roadmap covering equipment setup, documentation, buddy assignments, and check-ins."),
        ("Workforce Planning Worksheet", "Employer", "Strategic headcount forecast template calculating ramp-up timelines, skill turnover, and budget allocations."),
        ("Recruitment Process Template", "Shared", "Visual end-to-end flowchart template mapping interview stages, candidate touchpoints, and feedback deadlines.")
    ]

    res_cards_html = ""
    for title, audience, summary in resource_items:
        badge_class = "badge-teal" if audience == "Candidate" else ("badge-navy" if audience == "Employer" else "badge-gold")
        res_cards_html += f"""
        <div style="background:#FFF;border:1px solid var(--color-border);border-radius:12px;padding:2rem;box-shadow:var(--shadow-card);display:flex;flex-direction:column;justify-content:space-between;">
          <div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
              <span class="badge {badge_class}">{audience} Resource</span>
              <span style="font-size:0.75rem;color:var(--color-text-muted);">Demonstration Preview</span>
            </div>
            <h3 style="font-size:1.25rem;color:var(--color-navy);margin-bottom:0.75rem;">{title}</h3>
            <p style="font-size:0.9375rem;color:var(--color-text-secondary);line-height:1.6;margin-bottom:1.5rem;">{summary}</p>
          </div>
          <div>
            <button type="button" class="btn btn-sm btn-outline-navy" style="width:100%;" onclick="alert('Demonstration Notice: This is an illustrative resource template. Downloadable files are disabled in this prototype.')">
              View Resource Preview &rarr;
            </button>
          </div>
        </div>
        """

    resources_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Resources</span>
        </nav>
        <h1>Recruitment Resource &amp; Template Library</h1>
        <p class="lead">
          Illustrative checklists, job description templates, interview scorecards, and onboarding frameworks for candidates and employers.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Standardized Tools</span>
            <h2 class="section-title">Practical Tools for Structured Hiring</h2>
            <p>
              Standardized documents reduce hiring bias, align interview panels, and help candidates present their credentials with confidence.
            </p>
            <p>
              Explore our collection of 10 illustrative recruitment templates and operational checklists below.
            </p>
          </div>
          <div>
            {render_placeholder(img_resources, "16/9", "1600 × 900 • Resource Library")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> The templates displayed below represent preview frameworks. In this static prototype, downloadable files are provided as visual summaries rather than live file downloads.
          </p>
        </div>

        <!-- 10 Resource Cards Grid -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:2rem;margin-top:3rem;">
          {res_cards_html}
        </div>
      </div>
    </section>
    """

    with open("resources.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Recruitment Resources & Templates | Recruitment Agency",
            meta_desc="Access 10 illustrative recruitment templates, interview evaluation forms, resume checklists, and workforce worksheets.",
            active_page="candidates",
            body_content=resources_html
        ))

    # 34. careers.html (Internal Agency Careers)
    img_careers = record_image(
        filename="careers-agency-culture.webp",
        page="careers.html",
        section="Internal Agency Culture",
        description="A collaborative and welcoming recruitment agency team meeting celebrating a milestone in an airy office space.",
        aspect_ratio="16/9",
        resolution="1600x900",
        orientation="Landscape",
        prompt="Corporate photography: A collaborative recruitment agency team meeting in an open contemporary office. Dedicated talent consultants in smart business casual attire smiling and discussing strategy around a whiteboard. Natural lighting, warm camaraderie, 35mm lens, authentic workplace atmosphere.",
        composition="Wide group shot of modern office team.",
        camera_angle="Eye level.",
        lighting="Natural ambient daylight with warm fill.",
        background="Contemporary open office with greenery and glass boards.",
        visual_style="Clean executive corporate photography.",
        color_palette="Navy, teal, warm wood, white.",
        subject_details="Diverse professional recruitment team members.",
        negative_space="Upper quadrant open."
    )

    careers_html = f"""
    <section class="subpage-hero" aria-label="Page Title">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="separator">/</span>
          <span>Work With Us (Internal)</span>
        </nav>
        <h1>Build Your Career at Our Recruitment Agency</h1>
        <p class="lead">
          Join our internal team of recruitment consultants, talent acquisition leads, and workforce operations specialists.
        </p>
      </div>
    </section>

    <section class="section bg-white">
      <div class="container">
        <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:3.5rem;align-items:center;margin-bottom:4rem;">
          <div>
            <span class="section-eyebrow">Internal Opportunities</span>
            <h2 class="section-title">Work With Us at the Agency</h2>
            <p>
              This page showcases career opportunities within our own recruitment firm. (If you are seeking job opportunities with client organizations, please visit our external <a href="jobs.html">Job Search Portal</a>).
            </p>
            <p>
              We value curiosity, rigorous technical evaluation, empathy for job seekers, and disciplined client service delivery.
            </p>
          </div>
          <div>
            {render_placeholder(img_careers, "16/9", "1600 × 900 • Internal Agency Culture")}
          </div>
        </div>

        <div class="demo-alert-banner">
          <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
          <p>
            <strong>Demonstration Notice:</strong> Internal agency openings listed below are illustrative roles for demonstration purposes. We do not assert active internal hiring quotas or commercial salary commitments.
          </p>
        </div>

        <!-- Illustrative Internal Roles -->
        <div style="margin-top:3rem;">
          <h3 style="font-size:1.4rem;color:var(--color-navy);margin-bottom:1.5rem;">Sample Internal Agency Roles</h3>
          
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:4rem;">
            <div style="background:#FFF;border:1px solid var(--color-border);padding:1.75rem;border-radius:8px;">
              <span class="badge badge-demo">Illustrative Internal Role</span>
              <h4 style="font-size:1.15rem;margin-top:0.35rem;margin-bottom:0.25rem;">Recruitment Consultant — IT Practice</h4>
              <div style="font-size:0.8125rem;color:var(--color-teal);font-weight:600;margin-bottom:0.5rem;">Hyderabad &bull; Full-time</div>
              <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Managing full-lifecycle sourcing, technical screening, and client interview coordination for software engineering roles.</p>
            </div>

            <div style="background:#FFF;border:1px solid var(--color-border);padding:1.75rem;border-radius:8px;">
              <span class="badge badge-demo">Illustrative Internal Role</span>
              <h4 style="font-size:1.15rem;margin-top:0.35rem;margin-bottom:0.25rem;">Talent Acquisition Associate — Healthcare</h4>
              <div style="font-size:0.8125rem;color:var(--color-teal);font-weight:600;margin-bottom:0.5rem;">Hyderabad &bull; Full-time</div>
              <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Assisting clinical practice leads with credential checks, candidate screening calls, and interview drive logistics.</p>
            </div>

            <div style="background:#FFF;border:1px solid var(--color-border);padding:1.75rem;border-radius:8px;">
              <span class="badge badge-demo">Illustrative Internal Role</span>
              <h4 style="font-size:1.15rem;margin-top:0.35rem;margin-bottom:0.25rem;">Business Development Manager</h4>
              <div style="font-size:0.8125rem;color:var(--color-teal);font-weight:600;margin-bottom:0.5rem;">Hyderabad &bull; Full-time</div>
              <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Forging corporate relationships with hiring authorities and structuring staffing proposals across regional enterprise accounts.</p>
            </div>

            <div style="background:#FFF;border:1px solid var(--color-border);padding:1.75rem;border-radius:8px;">
              <span class="badge badge-demo">Illustrative Internal Role</span>
              <h4 style="font-size:1.15rem;margin-top:0.35rem;margin-bottom:0.25rem;">Recruitment Operations Intern</h4>
              <div style="font-size:0.8125rem;color:var(--color-teal);font-weight:600;margin-bottom:0.5rem;">Hyderabad &bull; Internship (6 Months)</div>
              <p style="font-size:0.875rem;color:var(--color-text-secondary);margin:0;">Learning fundamental talent mapping, ATS workflow management, and candidate communication governance.</p>
            </div>
          </div>
        </div>

        <!-- Internal Application Form (Frontend-only) -->
        <div style="background:var(--color-surface-light);border:1px solid var(--color-border);padding:2.5rem;border-radius:12px;max-width:800px;margin:0 auto;">
          <h3 style="font-size:1.4rem;color:var(--color-navy);margin-bottom:0.5rem;text-align:center;">Express Interest in Agency Careers</h3>
          <p style="text-align:center;color:var(--color-text-secondary);font-size:0.9375rem;margin-bottom:2rem;">
            Submit your details for internal consideration. In this demonstration, submissions are validated locally on the client side only.
          </p>

          <form id="agency-career-form" novalidate>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-bottom:1.25rem;">
              <div class="form-group">
                <label for="career-name">Full Name *</label>
                <input type="text" id="career-name" class="form-control" placeholder="Your name" required>
              </div>
              <div class="form-group">
                <label for="career-email">Email Address *</label>
                <input type="email" id="career-email" class="form-control" placeholder="name@example.com" required>
              </div>
            </div>

            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-bottom:1.25rem;">
              <div class="form-group">
                <label for="career-phone">Phone Number *</label>
                <input type="tel" id="career-phone" class="form-control" placeholder="0000000000" required>
              </div>
              <div class="form-group">
                <label for="career-role">Role of Interest *</label>
                <select id="career-role" class="form-select" required>
                  <option value="">Select role...</option>
                  <option value="Recruitment Consultant">Recruitment Consultant</option>
                  <option value="Talent Acquisition Associate">Talent Acquisition Associate</option>
                  <option value="Business Development">Business Development</option>
                  <option value="Recruitment Operations Intern">Recruitment Operations Intern</option>
                </select>
              </div>
            </div>

            <div class="form-group" style="margin-bottom:1.75rem;">
              <label for="career-notes">Brief Overview of Recruitment Experience</label>
              <textarea id="career-notes" class="form-control" rows="4" placeholder="Share your experience or motivation..."></textarea>
            </div>

            <button type="submit" class="btn btn-primary btn-lg" style="width:100%;">Submit Internal Application (Demo)</button>
          </form>
        </div>
      </div>
    </section>
    """

    with open("careers.html", "w", encoding="utf-8") as f:
        f.write(wrap_page(
            title="Internal Careers | Recruitment Agency",
            meta_desc="Explore opportunities to work internally as a recruitment consultant, talent acquisition lead, or operations specialist at our agency.",
            active_page="about",
            body_content=careers_html
        ))

    print("Candidate pages (28-34) generated successfully.")

if __name__ == "__main__":
    build_candidate_pages()
