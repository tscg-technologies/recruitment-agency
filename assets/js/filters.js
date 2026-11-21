/**
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
