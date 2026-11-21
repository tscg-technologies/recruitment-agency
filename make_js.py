"""
JavaScript Generator for Recruitment Agency Website
"""
import os

def create_js():
    main_js = """/**
 * RECRUITMENT AGENCY — Core JavaScript
 * Handles sticky navigation, back-to-top button, accordions, and modals.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Navigation Bar
  const siteHeader = document.querySelector('.site-header');
  if (siteHeader) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        siteHeader.classList.add('scrolled');
      } else {
        siteHeader.classList.remove('scrolled');
      }
    });
  }

  // 2. Back-to-Top Button
  const backToTopBtn = document.querySelector('.btn-back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // 3. FAQ Accordion Component
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (questionBtn) {
      questionBtn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Optional: Close sibling accordion items if inside a single accordion group
        const parentAccordion = item.closest('.faq-accordion');
        if (parentAccordion && !parentAccordion.hasAttribute('data-multi-expand')) {
          parentAccordion.querySelectorAll('.faq-item').forEach(sibling => {
            sibling.classList.remove('active');
            const siblingBtn = sibling.querySelector('.faq-question');
            if (siblingBtn) siblingBtn.setAttribute('aria-expanded', 'false');
          });
        }

        if (!isActive) {
          item.classList.add('active');
          questionBtn.setAttribute('aria-expanded', 'true');
        } else {
          item.classList.remove('active');
          questionBtn.setAttribute('aria-expanded', 'false');
        }
      });
    }
  });

  // 4. Accessible Modal Close Handlers
  document.querySelectorAll('.modal-backdrop').forEach(modal => {
    // Close on backdrop click
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('open');
      }
    });

    // Close buttons inside modal
    const closeButtons = modal.querySelectorAll('[data-close-modal]');
    closeButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        modal.classList.remove('open');
      });
    });
  });

  // Close modals on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-backdrop.open').forEach(modal => {
        modal.classList.remove('open');
      });
    }
  });
});
"""

    navigation_js = """/**
 * RECRUITMENT AGENCY — Navigation JavaScript
 * Mobile drawer navigation, accessibility keyboard focus, and active states.
 */

document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');
  const overlay = document.querySelector('.mobile-nav-overlay');
  const closeBtn = document.querySelector('.mobile-drawer-close');

  if (toggleBtn && drawer && overlay) {
    const openMenu = () => {
      drawer.classList.add('open');
      overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
      toggleBtn.setAttribute('aria-expanded', 'true');
      if (closeBtn) closeBtn.focus();
    };

    const closeMenu = () => {
      drawer.classList.remove('open');
      overlay.classList.remove('open');
      document.body.style.overflow = '';
      toggleBtn.setAttribute('aria-expanded', 'false');
      toggleBtn.focus();
    };

    toggleBtn.addEventListener('click', openMenu);
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    overlay.addEventListener('click', closeMenu);

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer.classList.contains('open')) {
        closeMenu();
      }
    });
  }

  // Highlight Current Page in Navigation
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link, .nav-dropdown a, .mobile-nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
});
"""

    job_search_js = """/**
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
"""

    filters_js = """/**
 * RECRUITMENT AGENCY — Category & Resource Filter System
 * Filtering for Insights, Resources, Career Advice, and Case Studies.
 */

document.addEventListener('DOMContentLoaded', () => {
  const filterButtons = document.querySelectorAll('.filter-tab-btn');
  const filterableItems = document.querySelectorAll('.filterable-card');
  const searchInput = document.querySelector('.filter-search-input');

  if (filterButtons.length > 0 && filterableItems.length > 0) {
    let currentCategory = 'all';

    const applyFilter = () => {
      const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

      filterableItems.forEach(card => {
        const itemCategory = card.getAttribute('data-category') || '';
        const itemTitle = card.querySelector('h3, h4')?.textContent.toLowerCase() || '';
        const itemText = card.textContent.toLowerCase();

        const matchCat = (currentCategory === 'all' || itemCategory === currentCategory);
        const matchQuery = (!query || itemTitle.includes(query) || itemText.includes(query));

        if (matchCat && matchQuery) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    };

    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-category') || 'all';
        applyFilter();
      });
    });

    if (searchInput) {
      searchInput.addEventListener('input', applyFilter);
    }
  }
});
"""

    forms_js = """/**
 * RECRUITMENT AGENCY — Forms & Resume Upload Demonstration UI
 * Provides frontend validation, file preview (PDF/DOC/DOCX), and demo submission alerts.
 * Strictly front-end only: NO data or files are stored or transmitted.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Resume Upload Demonstration Component
  const fileInput = document.getElementById('resume-file-input');
  const dropzone = document.getElementById('file-dropzone');
  const filePreview = document.getElementById('file-preview-card');
  const fileNameDisplay = document.getElementById('file-name-display');
  const fileSizeDisplay = document.getElementById('file-size-display');
  const clearFileBtn = document.getElementById('clear-file-btn');
  const fileError = document.getElementById('file-error-msg');

  const ALLOWED_EXTENSIONS = ['pdf', 'doc', 'docx'];
  const MAX_SIZE_MB = 5;

  const handleSelectedFile = (file) => {
    if (!file) return;

    const extension = file.name.split('.').pop().toLowerCase();
    const sizeInMB = file.size / (1024 * 1024);

    if (fileError) fileError.textContent = '';

    // Validate Extension
    if (!ALLOWED_EXTENSIONS.includes(extension)) {
      if (fileError) {
        fileError.textContent = 'Invalid file format. Please upload a PDF, DOC, or DOCX document.';
        fileError.style.display = 'block';
      }
      clearFileSelection();
      return;
    }

    // Validate File Size
    if (sizeInMB > MAX_SIZE_MB) {
      if (fileError) {
        fileError.textContent = `File exceeds ${MAX_SIZE_MB}MB limit (selected file: ${sizeInMB.toFixed(1)}MB).`;
        fileError.style.display = 'block';
      }
      clearFileSelection();
      return;
    }

    // Update Preview
    if (fileNameDisplay) fileNameDisplay.textContent = file.name;
    if (fileSizeDisplay) fileSizeDisplay.textContent = `${(file.size / 1024).toFixed(0)} KB`;
    if (filePreview) filePreview.classList.add('visible');
    if (dropzone) dropzone.style.display = 'none';
  };

  const clearFileSelection = () => {
    if (fileInput) fileInput.value = '';
    if (filePreview) filePreview.classList.remove('visible');
    if (dropzone) dropzone.style.display = 'block';
    if (fileNameDisplay) fileNameDisplay.textContent = '';
    if (fileSizeDisplay) fileSizeDisplay.textContent = '';
  };

  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      handleSelectedFile(file);
    });
  }

  if (clearFileBtn) {
    clearFileBtn.addEventListener('click', (e) => {
      e.preventDefault();
      clearFileSelection();
    });
  }

  // Drag and Drop Effects
  if (dropzone) {
    ['dragenter', 'dragover'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.add('dragover');
      });
    });

    ['dragleave', 'drop'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.remove('dragover');
      });
    });

    dropzone.addEventListener('drop', (e) => {
      const dt = e.dataTransfer;
      const file = dt.files[0];
      if (fileInput) fileInput.files = dt.files;
      handleSelectedFile(file);
    });
  }

  // 2. Candidate Registration Form Handler
  const candidateForm = document.getElementById('candidate-registration-form');
  const demoSuccessModal = document.getElementById('demo-success-modal');

  if (candidateForm) {
    candidateForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Check required fields
      let isValid = true;
      const requiredInputs = candidateForm.querySelectorAll('[required]');
      
      requiredInputs.forEach(input => {
        if (!input.value.trim()) {
          input.classList.add('invalid');
          isValid = false;
        } else {
          input.classList.remove('invalid');
        }
      });

      if (!isValid) {
        alert('Please complete all required fields before proceeding.');
        return;
      }

      // Show Demo Modal Confirmation
      const modalTitle = document.getElementById('modal-confirmation-title');
      const modalMessage = document.getElementById('modal-confirmation-msg');
      
      if (modalTitle) modalTitle.textContent = "Candidate Registration Demo Complete";
      if (modalMessage) {
        modalMessage.innerHTML = `
          <strong>Demonstration Notice:</strong> Your information and selected resume have been validated successfully in this prototype. 
          <br><br>
          <em>Please note:</em> As this is a frontend demonstration, no personal data or resume files have been saved, transmitted, or emailed to any server.
        `;
      }

      if (demoSuccessModal) {
        demoSuccessModal.classList.add('open');
      }

      candidateForm.reset();
      clearFileSelection();
    });
  }

  // 3. Employer Hiring Enquiry Form Handler
  const employerForm = document.getElementById('employer-hiring-form');
  if (employerForm) {
    employerForm.addEventListener('submit', (e) => {
      e.preventDefault();

      let isValid = true;
      const requiredInputs = employerForm.querySelectorAll('[required]');
      
      requiredInputs.forEach(input => {
        if (!input.value.trim()) {
          input.classList.add('invalid');
          isValid = false;
        } else {
          input.classList.remove('invalid');
        }
      });

      if (!isValid) {
        alert('Please complete all required employer requirement fields.');
        return;
      }

      const modalTitle = document.getElementById('modal-confirmation-title');
      const modalMessage = document.getElementById('modal-confirmation-msg');
      
      if (modalTitle) modalTitle.textContent = "Hiring Requirement Enquiry Submitted (Demo)";
      if (modalMessage) {
        modalMessage.innerHTML = `
          <strong>Demonstration Notice:</strong> Your hiring requirements have been structured and validated.
          <br><br>
          <em>Please note:</em> This is a static frontend prototype. In a live enterprise implementation, this submission would route directly to a designated recruitment account director. No commercial data was transmitted or recorded.
        `;
      }

      if (demoSuccessModal) {
        demoSuccessModal.classList.add('open');
      }

      employerForm.reset();
    });
  }

  // 4. General Contact Form Handler
  const contactForm = document.getElementById('general-contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const modalTitle = document.getElementById('modal-confirmation-title');
      const modalMessage = document.getElementById('modal-confirmation-msg');
      
      if (modalTitle) modalTitle.textContent = "Message Received (Demo Mode)";
      if (modalMessage) {
        modalMessage.innerHTML = `
          Thank you for reaching out to the generic <strong>RECRUITMENT AGENCY</strong> demonstration portal.
          <br><br>
          Your enquiry form passed frontend validation. No information was stored or dispatched to live mail servers.
        `;
      }

      if (demoSuccessModal) {
        demoSuccessModal.classList.add('open');
      }

      contactForm.reset();
    });
  }

  // 5. Internal Agency Careers Application Form Handler
  const internalCareerForm = document.getElementById('agency-career-form');
  if (internalCareerForm) {
    internalCareerForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const modalTitle = document.getElementById('modal-confirmation-title');
      const modalMessage = document.getElementById('modal-confirmation-msg');
      
      if (modalTitle) modalTitle.textContent = "Application Submitted (Demo)";
      if (modalMessage) {
        modalMessage.innerHTML = `
          Thank you for expressing interest in working at our recruitment agency.
          <br><br>
          This is an illustrative agency careers demonstration. No application data was saved or sent.
        `;
      }

      if (demoSuccessModal) {
        demoSuccessModal.classList.add('open');
      }

      internalCareerForm.reset();
    });
  }
});
"""

    with open(os.path.join("assets", "js", "main.js"), "w", encoding="utf-8") as f:
        f.write(main_js)
    with open(os.path.join("assets", "js", "navigation.js"), "w", encoding="utf-8") as f:
        f.write(navigation_js)
    with open(os.path.join("assets", "js", "job-search.js"), "w", encoding="utf-8") as f:
        f.write(job_search_js)
    with open(os.path.join("assets", "js", "filters.js"), "w", encoding="utf-8") as f:
        f.write(filters_js)
    with open(os.path.join("assets", "js", "forms.js"), "w", encoding="utf-8") as f:
        f.write(forms_js)
    print("JavaScript files created successfully.")

if __name__ == "__main__":
    create_js()
