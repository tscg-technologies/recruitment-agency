/**
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
