let form = document.getElementById('frm-task')
let task = document.getElementById('FormControlInput')
let btnAdd = document.getElementById('btnAdd')
let calendar = document.getElementById('calendar')
let flexCheckChecked = document.querySelectorAll('#flexCheckChecked')


// Create a new task
btnAdd.addEventListener('click', function(){
    if (task.value != ""){
        document.getElementById('desc-task').value = task.value
        document.getElementById('due-date').value = calendar.value

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

    //Update the task completed
    flexCheckChecked.forEach(check => { check.addEventListener('click', function(){
    
       
        let checked = this.checked ? "True" : "False";

        const id = this.getAttribute('data-task-id');
        const url = `/update/${id}/`
        const formUpdate = document.getElementById('frm-update')
        let completed = document.createElement('input')
        completed.setAttribute('type', 'text')
        completed.setAttribute('name','completed')
        completed.setAttribute('value',checked)
        formUpdate.setAttribute('action', url)
        formUpdate.appendChild(completed)
        formUpdate.submit()

    })})

calendar.addEventListener('change', () => {
    const selectedDate= calendar.value
    console.log(selectedDate)
})  