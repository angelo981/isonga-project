/* ══════════════════════════════════════
   HOSTS PAGE - EQUIPMENT ORDER FORM
   ══════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function() {
  
  // Equipment selection tracking
  const equipmentChecklist = document.getElementById('equipmentChecklist');
  const equipmentForm = document.getElementById('equipmentOrderForm');
  let selectedEquipment = [];

  if (equipmentChecklist) {
    // Listen to checkbox changes
    const checkboxes = equipmentChecklist.querySelectorAll('input[type="checkbox"]');
    
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', function() {
        updateSelectedEquipment();
        animateCheckmark(this);
      });
    });

    // Function to update selected equipment list
    function updateSelectedEquipment() {
      selectedEquipment = [];
      checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
          selectedEquipment.push({
            id: checkbox.dataset.id,
            value: checkbox.value
          });
        }
      });
      
      console.log('Selected Equipment:', selectedEquipment);
    }

    // Animate checkmark on selection
    function animateCheckmark(checkbox) {
      const card = checkbox.nextElementSibling;
      const check = card.querySelector('.equipment-check');
      
      if (checkbox.checked) {
        check.style.animation = 'none';
        setTimeout(() => {
          check.style.animation = 'popIn 0.3s ease-out';
        }, 10);
      }
    }
  }

  // Form submission handler
  if (equipmentForm) {
    equipmentForm.addEventListener('submit', function(e) {
      // Validate that at least one equipment is selected
      if (selectedEquipment.length === 0) {
        e.preventDefault();
        alert('Please select at least one equipment or service.');
        return false;
      }

      // Validate form fields
      const name = document.querySelector('input[name="full_name"]').value.trim();
      const email = document.querySelector('input[name="email"]').value.trim();
      const phone = document.querySelector('input[name="phone"]').value.trim();
      const eventType = document.querySelector('select[name="event_type"]').value;
      const eventDate = document.querySelector('input[name="event_date"]').value;
      const guests = document.querySelector('input[name="expected_guests"]').value;
      const spaceType = document.querySelector('select[name="space_type"]').value;

      if (!name || !email || !phone || !eventType || !eventDate || !guests || !spaceType) {
        e.preventDefault();
        alert('Please fill in all required fields.');
        return false;
      }

      // Optional: Show loading state on button
      const submitBtn = equipmentForm.querySelector('.form-submit-btn');
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="animation: spin 1s linear infinite;"><circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="2" fill="none"/><path d="M8 1V3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg> Processing...';

      // Re-enable button after submission
      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }, 2000);
    });
  }

  // Smooth scroll to form on button click
  const exploreSpacesBtn = document.querySelector('a[href="#contact"]');
  if (exploreSpacesBtn) {
    exploreSpacesBtn.addEventListener('click', function(e) {
      e.preventDefault();
      const contactSection = document.getElementById('contact');
      if (contactSection) {
        contactSection.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  // Real-time validation for email
  const emailInput = document.querySelector('input[name="email"]');
  if (emailInput) {
    emailInput.addEventListener('blur', function() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (this.value && !emailRegex.test(this.value)) {
        this.classList.add('error');
        this.parentElement.insertAdjacentHTML('afterend', '<span class="form-error">Please enter a valid email address</span>');
      } else {
        this.classList.remove('error');
        const errorMsg = this.parentElement.nextElementSibling;
        if (errorMsg && errorMsg.classList.contains('form-error')) {
          errorMsg.remove();
        }
      }
    });
  }

  // Phone number formatting
  const phoneInput = document.querySelector('input[name="phone"]');
  if (phoneInput) {
    phoneInput.addEventListener('input', function() {
      // Allow only numbers, +, and spaces
      this.value = this.value.replace(/[^\d+\s-]/g, '');
    });
  }

  // Date validation (prevent past dates)
  const dateInput = document.querySelector('input[name="event_date"]');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);

    dateInput.addEventListener('change', function() {
      const selectedDate = new Date(this.value);
      const todayDate = new Date(today);
      
      if (selectedDate < todayDate) {
        alert('Please select a date in the future.');
        this.value = '';
      }
    });
  }

  // Guest count validation
  const guestInput = document.querySelector('input[name="expected_guests"]');
  if (guestInput) {
    guestInput.addEventListener('input', function() {
      if (this.value < 1) {
        this.value = 1;
      }
      if (this.value > 10000) {
        this.value = 10000;
      }
    });
  }

});

// Animation keyframes
const style = document.createElement('style');
style.textContent = `
  @keyframes popIn {
    0% {
      transform: scale(0) rotate(-45deg);
      opacity: 0;
    }
    50% {
      transform: scale(1.2) rotate(0deg);
    }
    100% {
      transform: scale(1) rotate(0deg);
      opacity: 1;
    }
  }

  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }

  .form-error {
    display: block;
    color: #dc3545;
    font-size: 0.8rem;
    margin-top: 0.25rem;
  }

  input.error,
  select.error {
    border-color: #dc3545 !important;
    background-color: rgba(220, 53, 69, 0.05) !important;
  }
`;
document.head.appendChild(style);
