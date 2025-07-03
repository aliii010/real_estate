function liveSearch(liveSearchInputId, dropdownBoxId) {
  const liveSearchInput = document.getElementById(liveSearchInputId);
  const dropDownBox = document.getElementById(dropdownBoxId);
  
  liveSearchInput.addEventListener("input", function() {
    const searchTerm = liveSearchInput.value.toLowerCase();
  
    const dropdownItems = dropDownBox.querySelectorAll("a");
  
    for (let region of dropdownItems) {
      const regionName = region.textContent.toLowerCase();
  
      if (regionName.includes(searchTerm)) {
        region.style.display = '';
      } else {
        region.style.display = 'none';
      }
    }
  })
}


liveSearch('purpose-live-search-input', 'purpose-dropdown-box');
liveSearch('type-live-search-input', 'type-dropdown-box');
liveSearch('city-live-search-input', 'city-dropdown-box');
liveSearch('region-live-search-input', 'region-dropdown-box');
liveSearch('project-live-search-input', 'project-dropdown-box');
