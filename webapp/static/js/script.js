function myFunction(){
    document.getElementById("javademo").innerHTML = "Paragraph changed"
}
    // JavaScript functions for the modal
    function openModal(content) {
        document.getElementById('modalContent').innerText = content;
        document.getElementById('myModal').style.display = 'flex';
    }

    function closeModal() {
        document.getElementById('myModal').style.display = 'none';
    }

    