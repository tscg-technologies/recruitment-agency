/**
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
