/**
 * RECRUITMENT AGENCY — Job Search & Filter System
 * Generic illustrative demonstration vacancies with live multi-attribute filtering.
 */

const DEMO_JOBS = [
  {
    id: "job-001",
    title: "Frontend Developer — Demo Vacancy",
    employer: "Confidential Technology Client",
    location: "Hyderabad, India (Hybrid)",
    industry: "Information Technology",
    category: "Software Engineering",
    type: "Full-time",
    experience: "3-5 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Seeking a modern frontend specialist skilled in semantic HTML5, modern CSS architectures, and performant Vanilla JavaScript interfaces for enterprise web portals.",
    tags: ["HTML5", "CSS3", "JavaScript", "Responsive UI", "Web Performance"]
  },
  {
    id: "job-002",
    title: "Data Analyst — Demo Vacancy",
    employer: "Corporate Financial Services Partner",
    location: "Bangalore, India (On-site)",
    industry: "Banking and Finance",
    category: "Analytics & Intelligence",
    type: "Full-time",
    experience: "2-4 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Opportunity to transform complex financial datasets into actionable intelligence dashboards, stakeholder reports, and business predictive forecasts.",
    tags: ["SQL", "Data Modeling", "Business Intelligence", "Analytics", "Reporting"]
  },
  {
    id: "job-003",
    title: "HR Executive — Demo Vacancy",
    employer: "Mid-Sized Manufacturing Enterprise",
    location: "Chennai, India (On-site)",
    industry: "Manufacturing",
    category: "Human Resources",
    type: "Full-time",
    experience: "1-3 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Responsible for onboarding coordination, employee records maintenance, statutory documentation support, and daily workplace engagement workflows.",
    tags: ["HR Operations", "Onboarding", "Statutory Compliance", "Employee Relations"]
  },
  {
    id: "job-004",
    title: "Sales Executive — Demo Vacancy",
    employer: "Growing B2B Logistics Enterprise",
    location: "Mumbai, India (Hybrid)",
    industry: "Logistics and Supply Chain",
    category: "Sales & Business Development",
    type: "Full-time",
    experience: "2-5 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Driving enterprise pipeline growth, client relationship development, commercial proposal presentations, and freight forwarding contract negotiations.",
    tags: ["B2B Sales", "Client Acquisition", "Contract Negotiation", "Supply Chain"]
  },
  {
    id: "job-005",
    title: "Accountant — Demo Vacancy",
    employer: "Established Commercial Group",
    location: "Hyderabad, India (On-site)",
    industry: "Banking and Finance",
    category: "Finance & Accounting",
    type: "Full-time",
    experience: "3-6 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Overseeing day-to-day ledger operations, tax compliance preparation, monthly financial statement reconciliation, and annual audit coordination.",
    tags: ["General Ledger", "Taxation", "Audit Coordination", "Financial Reporting"]
  },
  {
    id: "job-006",
    title: "Mechanical Engineer — Demo Vacancy",
    employer: "Heavy Industrial Engineering Facility",
    location: "Pune, India (On-site)",
    industry: "Engineering",
    category: "Engineering & Technical",
    type: "Full-time",
    experience: "4-7 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Supervising automated assembly plant machinery, preventive maintenance protocols, equipment testing cycles, and safety compliance benchmarks.",
    tags: ["Plant Machinery", "Preventive Maintenance", "CAD", "Safety Standards"]
  },
  {
    id: "job-007",
    title: "Digital Marketing Executive — Demo Vacancy",
    employer: "E-Commerce & Retail Brand",
    location: "Remote (India)",
    industry: "Sales and Marketing",
    category: "Digital Growth",
    type: "Contract",
    experience: "2-4 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Executing omni-channel acquisition campaigns across organic search channels, targeted social ad pipelines, email workflows, and conversion landing pages.",
    tags: ["SEO", "Performance Marketing", "Content Strategy", "Google Analytics"]
  },
  {
    id: "job-008",
    title: "Business Analyst — Demo Vacancy",
    employer: "Global IT Services Consultancy",
    location: "Hyderabad, India (Hybrid)",
    industry: "Information Technology",
    category: "Business Strategy",
    type: "Full-time",
    experience: "3-5 Years",
    salary: "Standard Industry Competitive",
    postedDate: "Recent Demo Listing",
    status: "Illustrative Vacancy",
    summary: "Bridging client operational stakeholders and technical engineering squads through detailed user stories, functional specification documents, and workflow diagrams.",
    tags: ["Requirement Elicitation", "User Stories", "Agile", "Process Mapping"]
  }
];

document.addEventListener('DOMContentLoaded', () => {
  const jobsListContainer = document.getElementById('jobs-list-container');
  const resultsCountEl = document.getElementById('results-count');
  const searchInput = document.getElementById('search-keyword');
  const locationSelect = document.getElementById('filter-location');
  const industrySelect = document.getElementById('filter-industry');
  const typeSelect = document.getElementById('filter-type');
  const expSelect = document.getElementById('filter-experience');
  const clearFiltersBtn = document.getElementById('clear-filters-btn');
  const searchForm = document.getElementById('jobs-search-form');

  if (!jobsListContainer) return; // Exit if not on jobs listing page

  // Parse Query Parameters from URL
  const urlParams = new URLSearchParams(window.location.search);
  const initialKeyword = urlParams.get('keyword') || '';
  const initialIndustry = urlParams.get('industry') || '';
  const initialLocation = urlParams.get('location') || '';

  if (searchInput && initialKeyword) searchInput.value = initialKeyword;
  if (industrySelect && initialIndustry) industrySelect.value = initialIndustry;
  if (locationSelect && initialLocation) locationSelect.value = initialLocation;

  const renderJobs = (jobs) => {
    if (jobs.length === 0) {
      jobsListContainer.innerHTML = `
        <div class="empty-state-card" style="text-align: center; padding: 3rem 1.5rem; background: #fff; border-radius: 12px; border: 1px solid #E1E7ED;">
          <svg style="width: 48px; height: 48px; color: #8E9BAE; margin: 0 auto 1rem;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <h3 style="font-size: 1.25rem; color: #14263D; margin-bottom: 0.5rem;">No matching demonstration vacancies found</h3>
          <p style="color: #687789; max-width: 450px; margin: 0 auto 1.5rem; font-size: 0.9375rem;">
            Try clearing or adjusting your search filters to view illustrative vacancies across other roles or industries.
          </p>
          <button type="button" class="btn btn-teal btn-sm" id="reset-empty-btn">Reset All Filters</button>
        </div>
      `;
      const resetBtn = document.getElementById('reset-empty-btn');
      if (resetBtn) resetBtn.addEventListener('click', resetFilters);
      if (resultsCountEl) resultsCountEl.textContent = "0 demonstration vacancies found";
      return;
    }

    if (resultsCountEl) {
      resultsCountEl.textContent = `Showing ${jobs.length} demonstration ${jobs.length === 1 ? 'vacancy' : 'vacancies'}`;
    }

    jobsListContainer.innerHTML = jobs.map(job => `
      <article class="job-card" data-job-id="${job.id}">
        <div class="job-card-header">
          <div>
            <div style="margin-bottom: 0.35rem;">
              <span class="badge badge-demo">DEMO VACANCY — NOT A VERIFIED LIVE JOB</span>
            </div>
            <h3 class="job-card-title">
              <a href="job-details.html?id=${job.id}">${job.title}</a>
            </h3>
            <div class="job-card-employer">
              <svg style="width: 16px; height: 16px; color: #28A69A;" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm4 0h2v2h-2V5zm-4 4h2v2H7V9zm4 0h2v2h-2V9z" clip-rule="evenodd" />
              </svg>
              <span>${job.employer}</span>
              <span style="color: #CBD5E1;">•</span>
              <span class="badge badge-teal">${job.industry}</span>
            </div>
          </div>
          <a href="job-details.html?id=${job.id}" class="btn btn-sm btn-outline-teal">View Details</a>
        </div>

        <div class="job-meta-grid">
          <div class="job-meta-item">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
            <span>${job.location}</span>
          </div>
          <div class="job-meta-item">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
            <span>${job.type}</span>
          </div>
          <div class="job-meta-item">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>Exp: ${job.experience}</span>
          </div>
          <div class="job-meta-item">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>${job.salary}</span>
          </div>
        </div>

        <p class="job-card-summary">${job.summary}</p>

        <div class="job-card-footer">
          <div class="job-tags">
            ${job.tags.map(tag => `<span class="job-tag">${tag}</span>`).join('')}
          </div>
          <div style="font-size: 0.8125rem; color: #8E9BAE;">
            Listing Type: Illustrative Preview
          </div>
        </div>
      </article>
    `).join('');
  };

  const filterJobs = () => {
    const keyword = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const loc = locationSelect ? locationSelect.value.toLowerCase() : '';
    const ind = industrySelect ? industrySelect.value.toLowerCase() : '';
    const typ = typeSelect ? typeSelect.value.toLowerCase() : '';
    const exp = expSelect ? expSelect.value.toLowerCase() : '';

    const filtered = DEMO_JOBS.filter(job => {
      const matchKeyword = !keyword || 
        job.title.toLowerCase().includes(keyword) || 
        job.summary.toLowerCase().includes(keyword) ||
        job.tags.some(t => t.toLowerCase().includes(keyword));

      const matchLocation = !loc || job.location.toLowerCase().includes(loc);
      const matchIndustry = !ind || job.industry.toLowerCase().includes(ind);
      const matchType = !typ || job.type.toLowerCase().includes(typ);
      const matchExp = !exp || job.experience.toLowerCase().includes(exp);

      return matchKeyword && matchLocation && matchIndustry && matchType && matchExp;
    });

    renderJobs(filtered);
  };

  const resetFilters = () => {
    if (searchInput) searchInput.value = '';
    if (locationSelect) locationSelect.value = '';
    if (industrySelect) industrySelect.value = '';
    if (typeSelect) typeSelect.value = '';
    if (expSelect) expSelect.value = '';
    renderJobs(DEMO_JOBS);
  };

  if (searchForm) {
    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      filterJobs();
    });
  }

  if (searchInput) searchInput.addEventListener('input', filterJobs);
  if (locationSelect) locationSelect.addEventListener('change', filterJobs);
  if (industrySelect) industrySelect.addEventListener('change', filterJobs);
  if (typeSelect) typeSelect.addEventListener('change', filterJobs);
  if (expSelect) expSelect.addEventListener('change', filterJobs);
  if (clearFiltersBtn) clearFiltersBtn.addEventListener('click', resetFilters);

  // Initial Filter Application
  filterJobs();
});
