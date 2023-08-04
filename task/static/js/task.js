let form = document.getElementById('frm-task')
let task = document.getElementById('FormControlInput')
let btnAdd = document.getElementById('btnAdd')
let calendar = document.getElementById('calendar')
let linksToDelete = document.querySelectorAll('button[name="btn-delete"]')
let linksToUpdate = document.querySelectorAll('button[name="btn-update"]')
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

//Delete a task
 
    linksToDelete.forEach(link => {link.addEventListener('click', function() {
       
        const id = this.getAttribute('data-task-id');
        const description = this.getAttribute('data-task-description')
        const modalBody= document.querySelector('.modal-body')
        const frmDelete = document.getElementById('frm-delete')
        const url = `/delete/${id}/`
        frmDelete.setAttribute('action', url)
        
        modalBody.innerHTML = `
            <p id="msgAreYouSure">Are you sure you want to delete the task?</p>
            <p>${description}</p>`
      });
    });

//Update the task 
    linksToUpdate.forEach(link => {link.addEventListener('click', function(){

        const id = this.getAttribute('data-task-id')
        const description = this.getAttribute('data-task-description')
        const dueDate = this.getAttribute('data-task-due')
        const completed = this.getAttribute('data-task-completed')
        const frmUpdate = document.getElementById('frm-update')
        const urlUpdate = `/update/${id}/`

        frmUpdate.setAttribute('action', urlUpdate)
        document.getElementById('desc-update').value = description
        document.getElementById('due-update').value = dueDate
        document.getElementById('completed-update').value = completed

    })})

//Update the task completed
    flexCheckChecked.forEach(check => { check.addEventListener('click', function(){
    
        const checked = this.checked ? "True" : "False";
        const id = this.getAttribute('data-task-id');
        const url = `/updateCompleted/${id}/`
        const formUpdate = document.getElementById('frm-update-completed')
        let completed = document.createElement('input')
       
        completed.setAttribute('type', 'text')
        completed.setAttribute('name','completed')
        completed.setAttribute('value',checked)
        
        

        formUpdate.setAttribute('action', url)
        formUpdate.appendChild(completed)
        
        formUpdate.submit()

    })})


    
//Calendar
calendar.addEventListener('change', () => {
    const selectedDate= calendar.value
    console.log(selectedDate)
})