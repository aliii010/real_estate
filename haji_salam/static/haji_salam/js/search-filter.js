function filteringActions(dropdownItemClass, dropdownToggleClass, fieldClass, dropdownItemAttrName) {
  const dropDownItem = document.querySelectorAll('.' + dropdownItemClass);

  dropDownItem.forEach(element => {
    element.addEventListener("click", (e) => {
      e.preventDefault();

      // removing the selected class for all the dropdown-items
      dropDownItem.forEach(element2 => {
        element2.classList.remove('selected');
      });
  
      // and then add the selected class to the clicked dropdown-item
      element.classList.add('selected');
  
      document.querySelector('.' + dropdownToggleClass).innerHTML = element.innerHTML;
      document.querySelector('.' + fieldClass).value = element.getAttribute(dropdownItemAttrName);
      
      // Disable the project dropdown when the region field value attr is not empty.
      // And remove the disability of the project dropdown when the region field is empty.
      if (document.querySelector('.region-field').getAttribute('value') != "") {
        document.querySelector('.project-toggle').classList.add('disabled');
      } else {
        document.querySelector('.project-toggle').classList.remove('disabled');
      } 

      // Disable the region dropdown when the project field value attr is not empty.
      // And remove the disability of the region dropdown when the project field is empty.
      if (document.querySelector('.project-field').getAttribute('value') != "") {
        document.querySelector('.region-toggle').classList.add('disabled');
      } else {
        document.querySelector('.region-toggle').classList.remove('disabled');
      }

    });
  });
};



filteringActions('city-dropdown-item', 'city-toggle', 'city-field', 'cityValue');
filteringActions('region-dropdown-item', 'region-toggle', 'region-field', 'regionValue');
filteringActions('project-dropdown-item', 'project-toggle', 'project-field', 'projectValue');
filteringActions('purpose-dropdown-item', 'purpose-toggle', 'purpose-field', 'purposeValue');
filteringActions('type-dropdown-item', 'type-toggle', 'type-field', 'typeValue');