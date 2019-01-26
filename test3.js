function createDir(){
    var newdirname = prompt("Please input a directory name: ");
    if(!newdirname) return;
    $('#createdir').val(newdirname);
    $('#createdirForm').submit();
}

createDir();