// Wait for the document to finish loading
document.addEventListener("DOMContentLoaded", function() {
  
  // Select all elements with the class "list-edit"
  const editButtons = document.querySelectorAll(".list-edit");

  // Add event listener to each edit button
  editButtons.forEach(function(button) {
    button.addEventListener("click", function() {

      // Get the assignment details from the parent element
      const assignmentContainer = button.parentElement;
      const assignmentId = assignmentContainer.getAttribute("data-assignment-id");
      const name = assignmentContainer.querySelector(".list-name").textContent;
      const subject = assignmentContainer.querySelector(".list-subject").textContent;
      const description = assignmentContainer.querySelector(".list-description").textContent;
      const due = assignmentContainer.querySelector(".list-due").textContent;

      // Pre-populate the form fields in the popup window
      const popup = document.querySelector(".popup");
      const nameInput = popup.querySelector("#name");
      const subjectInput = popup.querySelector("#subject");
      const descriptionInput = popup.querySelector("#description");
      const dueInput = popup.querySelector("#due");

      nameInput.value = name;
      subjectInput.value = subject;
      descriptionInput.value = description;
      dueInput.value = due;

      // Show the popup window
      popup.classList.add("active");

    });
  });

  // Add event listener to the cancel button
  const cancelButton = document.querySelector(".button-cancel");
  cancelButton.addEventListener("click", function() {
    const popup = document.querySelector(".popup");
    popup.classList.remove("active");
  });

});

function getFileTypeExtension(file) {
  const fileTypes = {
    'image/jpeg': 'jpg',
    'image/png': 'png',
    'application/pdf': 'pdf',
    // add more file types here
  };

  return fileTypes[file.type] || 'unknown';
}

function showFileType(input) {
  if (input.files && input.files[0]) {
    const file = input.files[0];
    const fileType = getFileTypeExtension(file);
    const fileIcon = input.parentElement.querySelector('.file-icon');

    if (fileType !== 'unknown') {
      fileIcon.src = `static/assets/file-icons/${fileType}-icon.png`;
    } else {
      fileIcon.src = 'static/assets/folder-icon.png';
    }
  }
}
