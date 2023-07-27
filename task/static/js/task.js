let form = document.getElementById('frm-task');
let task = document.getElementById('FormControlInput');
let btnAdd = document.getElementById('btnAdd')

btnAdd.addEventListener('click', function(){
    if (task.value != ""){
        document.getElementById('desc-task').value = task.value
        form.setAttribute('action', '/create/')
        form.submit()
    }else{
        alert('Please enter a task')
    }
})