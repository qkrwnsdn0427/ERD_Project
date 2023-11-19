document.querySelectorAll('.call-patient').forEach(function(button) {
    button.addEventListener('click', function() {
        var appointmentId = this.getAttribute('data-appointment-id');
        // 예약 상태를 '진행 중'으로 업데이트하는 AJAX 호출
        // 성공 시:
        //this.style.display = 'none';
        //this.nextElementSibling.style.display = 'block';
        updateAppointmentStatus(appointmentId, 'in_progress');
        // Update UI as needed
    });
});

document.querySelectorAll('.complete-appointment').forEach(function(button) {
    button.addEventListener('click', function() {
        var appointmentId = this.getAttribute('data-appointment-id');
        // 예약 상태를 '완료'로 업데이트하는 AJAX 호출
        // 성공 시:
        // this.parentElement.remove();
        updateAppointmentStatus(appointmentId, 'completed');
        // Update UI as needed
    });
});