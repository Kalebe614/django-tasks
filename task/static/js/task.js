let form = document.getElementById('frm-task');
let task = document.getElementById('FormControlInput');
let btnAdd = document.getElementById('btnAdd')

// Create a new task
btnAdd.addEventListener('click', function(){
    if (task.value != ""){
        document.getElementById('desc-task').value = task.value
        form.setAttribute('action', '/create/')
        form.submit()
    }else{
        alert('Please enter a task')
    }
})

    let linksToDelete = document.querySelectorAll('button[name="btn-delete"]')
   
    linksToDelete.forEach(link => {
      link.addEventListener('click', function() {
       
        const id = this.getAttribute('data-task-id');
        const description = this.getAttribute('data-task-description')
        const modalBody= document.querySelector('.modal-body')
        const frmDelete = document.getElementById('frm-delete')
        const url = `/delete/${id}/`;
        frmDelete.setAttribute('action', url);
        
        modalBody.innerHTML = `
            <p id="msgAreYouSure">Are you sure you want to delete the task?</p>
            <p>${description}</p>`

        
      });
    });
